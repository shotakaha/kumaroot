# PMTを作りたい（`BuildPmtWindow`）

光電子増倍管（PMT）を使って光子検出するGeant4アプリを作るケースは多いと思います。
附属サンプルを参考にすると、PMT全体を作るのではなく、入射窓（PmtWindow）と光電面（PmtPhotocathode）の2つの論理ボリュームを作るのが簡単なようです。

次の6ステップでPMTを実装できます。

1. **光電面（PmtPhotocathode）** を論理ボリュームとして作る（`BuildPmtPhotocathode`）
2. **入射窓（PmtWindow）** を論理ボリュームとして作り、その中に光電面を置く（`BuildPmtWindow`）
3. **PMT** を親ボリュームに物理ボリュームとして配置する（`SetupPmt`）
4. **複数のPMT** をコピー番号つきで並べる（`SetupPmtArray`）
5. **光電面** をSensitiveDetectorとして登録する（`ConstructSDandField()`）
6. **光学物理（G4OpticalPhysics）** で光子検出を通知する（`SetBoundaryInvokeSD(true)`）

## 光電面を作りたい（`BuildPmtPhotocathode`）

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
    std::vector<G4double> efficiency{1.0, 1.0};        // 吸収された光子は検出される
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

`BuildPmtPhotocathode`は、PMTの光電面の論理ボリュームを1つ作成する関数です。
光電面は入射窓と同じ半径の薄い円板としています。

光電面に光が当たったときの光子検出のふるまいは、`G4MaterialPropertiesTable`を使ってユーザーが設定する必要があります。
光子のエネルギー（`photonEnergies`）に対する検出効率（`EFFICIENCY`）と複素屈折率（`REALRINDEX` / `IMAGINARYRINDEX`）などの指定が必要です。

これらの値は、光電面の材質のデータシートの値を参考にしてアプリ開発をはじめることが多いです。
シミュレーションの精度をあげる必要が生じた場合には、別途測定し、実測値を使う場合もあります。

:::{caution}

上記のサンプルコードは、附属サンプル（`LXe`や`DMX`）を参考にした設定例です。
光電面の表面（`G4OpticalSurface`）を金属（`dielectric_metal`）とし、光子を吸収する簡易的なモデルにしています。
実際の光電面は、入射窓の内側に付いた薄い半透明の膜です。光はこの膜を通って、光電子を放出します。
この膜の透過を正確に扱うには、表面の設定を`dielectric_dielectric`に変える必要があります。

:::

:::{seealso}

- [](./geant4-qe.md)
- [](./geant4-material-propertiestable.md)

:::

## 入射窓を組み立てたい（`BuildPmtWindow`）

```cpp
G4LogicalVolume* BuildPmtWindow(
    const G4String& logicalName = "PMTWindow",
    const G4String& materialName = "G4_PLEXIGLASS",
    G4double radius = 3.81 * cm,  // 3in.管
    G4double thickness = 1.0 * mm)
{
    // 形状を定義（入射窓は平たい円柱）
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

    // 光学特性を設定する（屈折率と吸収長）
    std::vector<G4double> photonEnergies{2.0 * eV, 3.5 * eV};
    std::vector<G4double> rIndex{1.49, 1.49};          // アクリルの屈折率（約1.49）
    std::vector<G4double> absLength{1. * m, 1. * m};   // 窓の中での吸収長

    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("RINDEX", photonEnergies, rIndex);
    mpt->AddProperty("ABSLENGTH", photonEnergies, absLength);
    material->SetMaterialPropertiesTable(mpt);

    // 入射窓の論理ボリュームを定義
    auto window = new G4LogicalVolume(
        solid,         // G4VSolid
        material,      // G4Material
        logicalName,   // 名前
        nullptr,       // G4FieldManager（未使用）
        nullptr,       // G4VSensitiveDetector（未使用）
        nullptr        // G4UserLimits（未使用）
    );

    // 光電面を窓の裏側（-z側）に配置する
    auto photocathode = BuildPmtPhotocathode(radius);
    auto photoSolid = static_cast<G4Tubs*>(photocathode->GetSolid());
    G4double photoHalfZ = photoSolid->GetZHalfLength();
    G4ThreeVector backPosition{0., 0., -(halfZ - photoHalfZ)};

    new G4PVPlacement(
        nullptr,        // 回転なし
        backPosition,   // 窓の中の位置
        photocathode,   // 配置する論理ボリューム
        "Photocathode", // 物理ボリュームの名前
        window,         // 親（窓の論理ボリューム）
        false,          // pMany（未使用）
        0,              // コピー番号
        true            // 重なりチェック
    );

    return window;
}
```

`BuildPmtWindow`は、PMTの入射窓の論理ボリュームを1つ作成する関数です。
名前・素材・半径・厚みは引数で変えられます。
デフォルトは3インチ管の入射窓です。

最初に光電面を作るのは、窓の中に配置するためです。
光電面の厚みは、論理ボリュームの形状から取得するので、窓と光電面の大きさは常に一致します。

入射窓は光子を透過させる必要があるため、`G4MaterialPropertiesTable`を使ってユーザーが設定を追加する必要があります。
光子のエネルギー（`photonEnergies`）に対する屈折率（`RINDEX`）と吸収長（`ABSLENGTH`）の指定が必要です。

:::{hint}

このサンプルコードでは、入射窓の材質にアクリル（`G4_PLEXIGLASS`）を使い、屈折率を1.49、吸収長を1mに設定しています。
実際の入射窓の材質のデータシートを参考に屈折率と吸収長を設定してください。
とくに`RINDEX`を設定しないと、入射した光子は入射窓の境界で消えてしまいます。

:::

この関数を`Construct()`の中で **1回だけ** 呼ぶようにします。
複数のPMTを並べる場合は、この論理ボリュームを使い回します。

## PMTを配置したい（`SetupPmt`）

```cpp
G4VPhysicalVolume* SetupPmt(
    G4VPhysicalVolume* parent,
    G4LogicalVolume* pmt,  // BuildPmtWindow()の戻り値
    G4int copyNo,
    const G4ThreeVector& position = G4ThreeVector(),
    const G4String& physicalName = "PMT")
{
    // 回転なしで配置する
    G4RotationMatrix rotation;

    return new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        pmt,                                // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        copyNo,                             // コピー番号
        true                                // 重なりチェック
    );
}
```

`SetupPmt`は、`BuildPmtWindow`が返したPMTを親ボリュームに置きます。
光電面は窓の子になっているので、一緒に配置されます。

## PMTを並べたい（`SetupPmtArray`）

```cpp
G4VPhysicalVolume* SetupPmtArray(
    G4VPhysicalVolume* parent,
    G4LogicalVolume* pmt,  // BuildPmtWindow()の戻り値
    G4int firstCopyNo = 101,
    G4int count = 5,
    G4double spacing = 10. * cm)
{
    // PMTを横一列に、中心をそろえて並べる
    for (G4int i = 0; i < count; ++i) {
        G4int copyNo = firstCopyNo + i;
        G4double x = (i - 0.5 * (count - 1)) * spacing;
        G4ThreeVector position{x, 0., 0.};
        SetupPmt(parent, pmt, copyNo, position);
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
    auto pmt = BuildPmtWindow();

    // PMTを5本並べる
    return SetupPmtArray(world, pmt);
}
```

`SetupPmtArray`は、同じ論理ボリュームを使って、`SetupPmt`を`count`回呼びます。
コピー番号は`firstCopyNo`から連番になり、どのPMTかを区別できます。
既定値では、10cm間隔で5本を横一列に並べます。

## 光子を数えたい（`PmtSD`）

SensitiveDetectorは、`G4VSensitiveDetector`を継承して作ります。
`ProcessHits()`は、光電面で光子が検出されたときに呼ばれます。

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
    // 光電面で検出された光子を1つ数える
    fNumPhotons++;
    return true;
}
```

`ProcessHits()`には、光電面で検出された光子だけが届きます。
光子の判定やトラックの停止は、光学物理（境界プロセス）が行うので、このクラスでは書きません。

## 検出を通知する設定（`G4OpticalParameters`）

光電面での検出を`ProcessHits()`に通知するには、光学物理の設定で`SetBoundaryInvokeSD(true)`を指定します。
`main()`の中で、物理リストを登録する前に設定します。

```cpp
// main() の中
auto opticalParams = G4OpticalParameters::Instance();
opticalParams->SetBoundaryInvokeSD(true);
```

光子が光電面で検出されると、境界プロセスが`Detection`の状態を返し、光電面のSensitiveDetectorを呼び出します。
光子は光電面で吸収されるので、トラックを止める処理は不要です。
光学物理の詳細は[光学物理したい](geant4-physics-opticalphysics)を参照してください。

## SensitiveDetectorを登録したい（`ConstructSDandField`）

SensitiveDetectorの登録は、`DetectorConstruction::ConstructSDandField()`で行います。

```cpp
void DetectorConstruction::ConstructSDandField()
{
    auto pmtSD = new PmtSD("PmtSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(pmtSD);

    // 光電面の論理ボリュームに登録する（名前は BuildPmtPhotocathode の既定値）
    SetSensitiveDetector("Photocathode", pmtSD);
}
```

`Construct()`ではなく`ConstructSDandField()`に書く理由は、マルチスレッドのGeant4では、各ワーカースレッドごとにSensitiveDetectorが必要だからです。
`Construct()`は、ジオメトリを作るときに1回だけ呼ばれます。
一方、`ConstructSDandField()`は、ワーカースレッドごとに呼ばれます。

## 参考にした附属サンプル

| サンプル | 光電面の作り方 | SensitiveDetector | 検出の通知 |
|---|---|---|---|
| `extended/optical/LXe` | 薄い円板（`photocath_log`）を`pmt_log`の子に配置。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | `SteppingAction`で`ProcessHits_boundary`を手動で呼び出し |
| `extended/optical/wls` | 薄い検出面（`PhotonDet_LV`）。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | `SetBoundaryInvokeSD(true)`で自動通知 |
| `advanced/underground_physics`（DMX） | 薄い殻（`phcath_log`）を`pmt_log`の子に配置。`EFFICIENCY`の光学表面 | `ConstructSDandField()`で登録 | — |
| `advanced/air_shower` | 窓（`PMT_log`）そのものをSensitiveDetectorにする（光電面は作らない） | `ConstructSDandField()`で登録 | `ProcessHits()`で光子を数え、トラックを停止 |

光電面を別に作る方法（LXe、wls、DMX）が、検出効率（`EFFICIENCY`）を使う標準的な方法です。
窓をそのままSensitiveDetectorにする方法（air_shower）は、より簡単な方法です。

:::{note}

光電面の論理ボリュームは、`G4LogicalVolumeStore`で名前から探すこともできます。
ただし、名前が重複すると`SetSensitiveDetector`がエラーになるので、名前は一意にしてください。

:::

:::{note}

大量のPMTを配置する場合（スーパーカミオカンデ規模で約1万本）は、`SetupPmtArray`のループよりも
`G4PVParameterised`のような仕組みを使うと、メモリの使用量を減らせます。
PMTの種類が複数ある場合は、半径や厚みを構造体にまとめておくと見通しがよくなります。

:::
