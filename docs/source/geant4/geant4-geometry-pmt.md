# PMTを作りたい（`BuildPmtWindow`）

PMT（光電子増倍管）は、PMT全体を作る必要はありません。
光子を検出するのは**感光面**だけなので、入射窓と感光面だけを作り、感光面をSensitiveDetectorにするのが一般的な方法です。
附属サンプルでも、この方法が使われています（下の「参考にした附属サンプル」の表を参照）。

実装は次の流れで進めます。

1. **入射窓（PMT）を作る**: 論理ボリューム。`BuildPmtWindow`で作り、1回だけ作ります。
2. **感光面を作る**: 論理ボリューム。`BuildPmtPhotocathode`で作り、光学表面（`EFFICIENCY`）を付けます。
3. **感光面を入射窓の中に置く**: 物理ボリューム。`SetupPmt`で、入射窓の中に感光面を配置します。
4. **PMTを並べる**: 物理ボリューム（コピー番号つき）。`SetupPmtArray`で、`SetupPmt`を並べた数だけ呼びます。
5. **SensitiveDetectorを作って感光面に登録する**: `PmtSD`を作り、`ConstructSDandField()`で登録します。
6. **光学物理で検出を通知する**: `SetBoundaryInvokeSD(true)`を設定します。

## 入射窓を作りたい（`BuildPmtWindow`）

```cpp
G4LogicalVolume* BuildPmtWindow(
    const G4String& logicalName = "PMTWindow",
    const G4String& materialName = "G4_PLEXIGLASS",
    G4double radius = 3.81 * cm,  // 3in.管
    G4double thickness = 1.0 * mm)
{
    // 形状を定義（PMTの入射窓を、平たい円柱で作成）
    G4double rMin = 0. * cm;          // 内径
    G4double rMax = radius;           // 外径
    G4double halfZ = 0.5 * thickness; // 高さ（厚み）の半分
    G4double sPhi = 0. * deg;         // 開始角度
    G4double dPhi = 360. * deg;       // 回転角
    auto solid = new G4Tubs(
        logicalName + "Solid",  // solid 名
        rMin,
        rMax,
        halfZ,
        sPhi,
        dPhi
    );

    // 材料を定義（入射窓はプレキシガラス（アクリル））
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial(materialName);

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,         // G4VSolid
        material,      // G4Material
        logicalName,   // 名前
        nullptr,       // G4FieldManager（未使用）
        nullptr,       // G4VSensitiveDetector（未使用）
        nullptr        // G4UserLimits（未使用）
    );

    return logical;
}
```

PMTの入射窓の論理ボリュームを作ります。
名前・素材・半径・厚みは引数で変えられます。既定値は3インチ管の入射窓です。
この関数は、`Construct()`の中で**1回だけ**呼びます。PMTを並べるときは、この論理ボリュームを何回も使い回します。

## 感光面を作りたい（`BuildPmtPhotocathode`）

```cpp
G4LogicalVolume* BuildPmtPhotocathode(
    const G4String& logicalName = "Photocathode",
    const G4String& materialName = "G4_Al",
    G4double radius = 3.81 * cm,
    G4double thickness = 0.01 * mm)
{
    // 形状を定義（入射窓と同じ半径の薄い円板）
    auto solid = new G4Tubs(
        logicalName + "Solid",  // solid 名
        0. * cm,                // 内径
        radius,                 // 外径
        0.5 * thickness,        // 高さの半分
        0. * deg,               // 開始角度
        360. * deg              // 回転角
    );

    // 材料を定義
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial(materialName);

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,         // G4VSolid
        material,      // G4Material
        logicalName,   // 名前
        nullptr,       // G4FieldManager（未使用）
        nullptr,       // G4VSensitiveDetector（未使用）
        nullptr        // G4UserLimits（未使用）
    );

    // 光学表面を定義（検出効率 EFFICIENCY を与える）
    std::vector<G4double> photonEnergies{2.0 * eV, 3.5 * eV};
    std::vector<G4double> efficiency{1.0, 1.0};  // 吸収された光子は検出される
    std::vector<G4double> realIndex{1.92, 1.92};       // 金属の複素屈折率（LXeの例）
    std::vector<G4double> imagIndex{1.69, 1.69};

    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("EFFICIENCY", photonEnergies, efficiency);
    mpt->AddProperty("REALRINDEX", photonEnergies, realIndex);
    mpt->AddProperty("IMAGINARYRINDEX", photonEnergies, imagIndex);

    auto surface = new G4OpticalSurface("PhotocathodeSurface", glisur, polished, dielectric_metal);
    surface->SetMaterialPropertiesTable(mpt);

    // 論理ボリュームに光学表面を貼る
    new G4LogicalSkinSurface("PhotocathodeSurface", logical, surface);

    return logical;
}
```

感光面は、入射窓と同じ半径の薄い円板です。
光が当たったときに、光子を検出するかどうかを`EFFICIENCY`で決めます。
ここでは検出効率を1.0にしていますが、実際のPMTの量子効率（QE）は波長によって変わります。
波長ごとの値は[量子効率](geant4-qe)を参照してください。

## 感光面を入射窓に配置したい（`SetupPmt`）

```cpp
G4VPhysicalVolume* SetupPmt(
    G4VPhysicalVolume* parent,
    G4LogicalVolume* window,        // BuildPmtWindow()の戻り値
    G4LogicalVolume* photocathode,  // BuildPmtPhotocathode()の戻り値
    G4int copyNo,
    const G4ThreeVector& position = G4ThreeVector(),
    const G4String& physicalName = "PMT")
{
    // 回転なしで配置する
    G4RotationMatrix rotation;

    // 入射窓（PMT）を親ボリュームに配置する
    auto pmt = new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        window,                             // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        copyNo,                             // コピー番号
        true                                // 重なりチェック
    );

    // 感光面を入射窓の裏側（-z側）に配置する
    // 厚みは BuildPmtWindow / BuildPmtPhotocathode の既定値と同じにしている
    G4double windowHalfZ = 0.5 * 1.0 * mm;
    G4double photoHalfZ = 0.5 * 0.01 * mm;
    G4ThreeVector backPosition{0., 0., -(windowHalfZ - photoHalfZ)};
    new G4PVPlacement(
        nullptr,        // 回転なし
        backPosition,   // 入射窓の中の位置
        photocathode,   // 配置する論理ボリューム
        "Photocathode", // 物理ボリュームの名前
        window,         // 親（入射窓の論理ボリューム）
        false,          // pMany（未使用）
        0,              // コピー番号
        true            // 重なりチェック
    );

    return pmt;
}
```

`SetupPmt`は、入射窓を親ボリュームに置き、その中に感光面を置きます。
感光面は入射窓の論理ボリュームの子になるので、光子は入射窓を通ってから感光面に届きます。

## PMTを並べたい（`SetupPmtArray`）

```cpp
G4VPhysicalVolume* SetupPmtArray(
    G4VPhysicalVolume* parent,
    G4LogicalVolume* window,        // BuildPmtWindow()の戻り値
    G4LogicalVolume* photocathode,  // BuildPmtPhotocathode()の戻り値
    G4int firstCopyNo = 101,
    G4int count = 5,
    G4double spacing = 10. * cm)
{
    // PMTを横一列に、中心をそろえて並べる
    for (G4int i = 0; i < count; ++i) {
        G4int copyNo = firstCopyNo + i;
        G4double x = (i - 0.5 * (count - 1)) * spacing;
        G4ThreeVector position{x, 0., 0.};
        SetupPmt(parent, window, photocathode, copyNo, position);
    }

    // 親ボリュームを返す（Setup系の戻り値は物理ボリューム）
    return parent;
}
```

```cpp
G4VPhysicalVolume* Construct()
{
    // 実験室（World）を配置する
    auto world = SetupWorld();

    // 論理ボリュームは1回だけ作る
    auto window = BuildPmtWindow();
    auto photocathode = BuildPmtPhotocathode();

    // PMTを5本並べる
    return SetupPmtArray(world, window, photocathode);
}
```

`SetupPmtArray`は、同じ論理ボリュームを使って、`SetupPmt`を`count`回呼びます。
コピー番号は`firstCopyNo`から連番になり、どのPMTかを区別できます。
既定値では、10cm間隔で5本を横一列に並べます。

## 光子を数えたい（`PmtSD`）

SensitiveDetectorは、`G4VSensitiveDetector`を継承して作ります。
`ProcessHits()`は、感光面で光子が検出されたときに呼ばれます。

```cpp
// PmtSD.hh
#pragma once

#include "G4VSensitiveDetector.hh"

class PmtSD : public G4VSensitiveDetector
{
    public:
        explicit PmtSD(const G4String& name);
        void Initialize(G4HCofThisEvent*) override { fNumPhotons = 0; }
        G4bool ProcessHits(G4Step* step, G4TouchableHistory*) override;
        G4int GetNumPhotons() const { return fNumPhotons; }

    private:
        G4int fNumPhotons = 0;
};
```

```cpp
// PmtSD.cc
#include "PmtSD.hh"

#include "G4Step.hh"

PmtSD::PmtSD(const G4String& name)
    : G4VSensitiveDetector(name)
{
}

G4bool PmtSD::ProcessHits(G4Step*, G4TouchableHistory*)
{
    // 感光面で検出された光子を1つ数える
    fNumPhotons++;
    return true;
}
```

`ProcessHits()`には、感光面で検出された光子だけが届きます。
光子の判定やトラックの停止は、光学物理（境界プロセス）が行うので、このクラスでは書きません。

## 検出を通知する設定（`G4OpticalParameters`）

感光面での検出を`ProcessHits()`に通知するには、光学物理の設定で`SetBoundaryInvokeSD(true)`を指定します。
`main()`の中で、物理リストを登録する前に設定します。

```cpp
// main() の中
auto opticalParams = G4OpticalParameters::Instance();
opticalParams->SetBoundaryInvokeSD(true);
```

光子が感光面で検出されると、境界プロセスが`Detection`の状態を返し、感光面のSensitiveDetectorを呼び出します。
光子は感光面で吸収されるので、トラックを止める処理は不要です。
光学物理の詳細は[光学物理したい](geant4-physics-opticalphysics)を参照してください。

## SensitiveDetectorを登録したい（`ConstructSDandField`）

SensitiveDetectorの登録は、`DetectorConstruction::ConstructSDandField()`で行います。

```cpp
void DetectorConstruction::ConstructSDandField()
{
    auto pmtSD = new PmtSD("PmtSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(pmtSD);

    // 感光面の論理ボリュームに登録する（名前は BuildPmtPhotocathode の既定値）
    SetSensitiveDetector("Photocathode", pmtSD);
}
```

`Construct()`ではなく`ConstructSDandField()`に書く理由は、マルチスレッドのGeant4では、各ワーカースレッドごとにSensitiveDetectorが必要だからです。
`Construct()`は、ジオメトリを作るときに1回だけ呼ばれます。
一方、`ConstructSDandField()`は、ワーカースレッドごとに呼ばれます。

## 参考にした附属サンプル

| サンプル | 感光面の作り方 | SensitiveDetector | 検出の通知 |
|---|---|---|---|
| `extended/optical/LXe` | 薄い円板（`photocath_log`）を`pmt_log`の子に配置。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | `SteppingAction`で`ProcessHits_boundary`を手動で呼び出し |
| `extended/optical/wls` | 薄い検出面（`PhotonDet_LV`）。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | `SetBoundaryInvokeSD(true)`で自動通知 |
| `advanced/underground_physics`（DMX） | 薄い殻（`phcath_log`）を`pmt_log`の子に配置。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | — |
| `advanced/air_shower` | 窓（`PMT_log`）そのものをSensitiveDetectorにする（感光面は作らない） | `ConstructSDandField()`で登録 | `ProcessHits()`で光子を数え、トラックを停止 |

感光面を別に作る方法（LXe、wls、DMX）が、検出効率（`EFFICIENCY`）を使う標準的な方法です。
窓をそのままSensitiveDetectorにする方法（air_shower）は、より簡単な方法です。

:::{note}

感光面の論理ボリュームは、`G4LogicalVolumeStore`で名前から探すこともできます。
ただし、名前が重複すると`SetSensitiveDetector`がエラーになるので、名前は一意にしてください。

:::

:::{note}

大量のPMTを配置する場合（スーパーカミオカンデ規模で約1万本）は、`SetupPmtArray`のループよりも
`G4PVParameterised`のような仕組みを使うと、メモリの使用量を減らせます。
PMTの種類が複数ある場合は、半径や厚みを構造体にまとめておくと見通しがよくなります。

:::
