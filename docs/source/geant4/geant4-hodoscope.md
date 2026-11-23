# ホドスコープを作りたい（`BuildHodoscope`）

```cpp
// Construct() の中
auto world = SetupWorld();
SetupHodoscope(world);  // 実験室の中に短冊を15本並べる
```

ホドスコープは、短冊状のシンチレーターを並べて、粒子が通過した場所を知る飛跡検出器です。
付属サンプル[B5](https://github.com/Geant4/geant4/tree/master/examples/basic/B5)のホドスコープを参考に、KumaROOT向けに組み直しました。

関数は次の4つに分けています。

1. **短冊を作る**（`BuildHodoscopeStrip`）：1本のシンチレーターの論理ボリュームを返す
2. **短冊を並べる**（`BuildHodoscope`）：短冊を一列に並べた外形の論理ボリュームを返す
3. **配置する**（`SetupHodoscope`）：外形を親ボリュームに物理ボリュームとして配置する
4. **有感領域を設定する**（`ConstructSDandField`）：短冊をSensitiveDetectorとして登録する

## 短冊を作りたい（`BuildHodoscopeStrip`）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4VisAttributes.hh"

G4LogicalVolume* BuildHodoscopeStrip(
    const G4String& logicalName = "HodoscopeStrip",
    const G4String& materialName = "G4_PLASTIC_SC_VINYLTOLUENE",
    G4double lengthX = 10. * cm,
    G4double lengthY = 40. * cm,
    G4double lengthZ = 1. * cm)
{
    // 形状を定義（G4Box は半分の長さで指定する）
    auto solid = new G4Box(
        logicalName + "Solid",  // solid 名
        0.5 * lengthX,
        0.5 * lengthY,
        0.5 * lengthZ
    );

    // 材料を定義（プラスチックシンチレーター）
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

    // （オプション）赤色で表示する
    auto color = new G4VisAttributes(G4Colour::Red());
    logical->SetVisAttributes(color);

    return logical;
}
```

`BuildHodoscopeStrip`は、1本の短冊を表す論理ボリュームを返します。
大きさは幅10 cm、長さ40 cm、厚さ1 cmの直方体です。
素材は`G4_PLASTIC_SC_VINYLTOLUENE`（プラスチックシンチレーター）を既定値にしています。

:::{note}

短冊の論理ボリューム名（`HodoscopeStrip`）は、後で`ConstructSDandField()`が名前で探すときに使います。
名前を変えるときは、そちらの名前も合わせてください。

:::

## 短冊を並べたい（`BuildHodoscope`）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

G4LogicalVolume* BuildHodoscope(
    const G4String& logicalName = "Hodoscope",
    G4int nStrips = 15)
{
    // 短冊の論理ボリュームと、その大きさを取得する
    auto strip = BuildHodoscopeStrip();
    auto stripBox = static_cast<G4Box*>(strip->GetSolid());

    // 短冊は隙間なく並べるので、ピッチは短冊の幅になる
    G4double pitch = 2. * stripBox->GetXHalfLength();

    // 短冊を並べる外形（空気の箱）を作る
    G4double halfX = 0.5 * nStrips * pitch;
    G4double halfY = stripBox->GetYHalfLength();
    G4double halfZ = stripBox->GetZHalfLength();
    auto envelopeSolid = new G4Box(logicalName + "Solid", halfX, halfY, halfZ);
    auto envelope = new G4LogicalVolume(
        envelopeSolid,                                   // G4VSolid
        G4NistManager::Instance()->FindOrBuildMaterial("G4_AIR"),  // G4Material
        logicalName,                                     // 名前
        nullptr,  // G4FieldManager（未使用）
        nullptr,  // G4VSensitiveDetector（未使用）
        nullptr   // G4UserLimits（未使用）
    );

    // 短冊を一列に並べる（中心が原点に来るように）
    for (G4int i = 0; i < nStrips; i++) {
        G4double x = (i - 0.5 * (nStrips - 1)) * pitch;
        new G4PVPlacement(
            nullptr,                      // 回転なし
            G4ThreeVector(x, 0., 0.),     // 位置
            strip,                        // 配置する論理ボリューム
            logicalName + "Strip",        // 物理ボリュームの名前
            envelope,                     // 親（外形の論理ボリューム）
            false,                        // pMany（未使用）
            i,                            // コピー番号（短冊の番号）
            true                          // 重なりチェック
        );
    }

    return envelope;
}
```

`BuildHodoscope`は、短冊を一列に並べた外形の論理ボリュームを1つ返します。
外形は空気（`G4_AIR`）の箱で、その中に`nStrips`本の短冊を置いています。

短冊の数は引数`nStrips`で指定します。
既定値は15本です。

x方向の位置は`(i - 0.5 * (nStrips - 1)) * pitch`で決めています。
奇数本でも偶数本でも、列の中心が原点に来ます。

コピー番号には短冊の番号`i`を使っています。
ヒットから何番目の短冊かを知るときに使います。

## ホドスコープを配置したい（`SetupHodoscope`）

```cpp
G4VPhysicalVolume* SetupHodoscope(
    G4VPhysicalVolume* parent,
    const G4ThreeVector& position = G4ThreeVector(0., 0., -1.5 * m),
    const G4String& physicalName = "Hodoscope")
{
    // 回転なしで配置する
    G4RotationMatrix rotation;

    // 外形の論理ボリュームを作る
    auto hodoscope = BuildHodoscope();

    return new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        hodoscope,                          // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        0,                                  // コピー番号
        true                                // 重なりチェック
    );
}
```

`SetupHodoscope`は、`BuildHodoscope`で作った外形を親ボリューム（`parent`）の中に配置します。
既定では、実験室の中心から z = -1.5 m の位置に置きます。
位置は引数`position`で変えられます。

## 有感領域を設定したい（`ConstructSDandField`）

```cpp
#include "G4LogicalVolumeStore.hh"
#include "G4SDManager.hh"
#include "HodoscopeSD.hh"  // G4VSensitiveDetector を継承した自作クラス

void Geometry::ConstructSDandField()
{
    // 短冊の論理ボリュームを名前で取得する
    auto strip = G4LogicalVolumeStore::GetInstance()->GetVolume("HodoscopeStrip");

    // SensitiveDetector を作って SDManager に登録し、短冊に設定する
    auto sd = new HodoscopeSD("HodoscopeSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(sd);
    strip->SetSensitiveDetector(sd);
}
```

`ConstructSDandField`は、短冊の論理ボリュームに`HodoscopeSD`を設定します。
短冊の中をステップが通るたびに、`HodoscopeSD::ProcessHits()`が呼ばれます。

`ProcessHits()`の中では、`aStep->GetPreStepPoint()->GetTouchableHandle()->GetCopyNumber()`で、ヒットした短冊の番号を取得できます。
`HodoscopeSD`の作り方は[SensitiveDetector](geant4-sensor-sensitivedetector)と[ヒットの判断](geant4-sensor-processhits)を参照してください。

## Constructで組み立てたい

```cpp
G4VPhysicalVolume* Construct()
{
    // 実験室（World）を配置する
    auto world = SetupWorld();

    // ホドスコープを実験室の中に配置する
    SetupHodoscope(world);

    return world;
}
```

`Construct()`では、`SetupWorld()`で実験室を配置し、その物理ボリュームを親として`SetupHodoscope()`を呼び出します。
`ConstructSDandField()`は、`Construct()`の後に呼ばれます。
組み立ての流れは[ジオメトリを構築したい](geant4-geometry-construct)にまとめています。

## B5との違い

| 項目 | B5 | このページ |
| --- | --- | --- |
| 短冊の論理ボリューム | メンバー変数`fHodoscopeLogical` | `BuildHodoscopeStrip()`の戻り値（名前で取得） |
| 短冊の数 | `Constants.hh`の`kNofHodoscopes` | `BuildHodoscope()`の引数`nStrips`（既定値15） |
| 配置先 | 親ボリュームに直接配置 | 短冊を空気の外形に並べ、外形を配置 |
| x方向の位置 | `(i - kNofHodoscopes/2) * 10 cm` | `(i - 0.5 * (nStrips - 1)) * pitch` |
| 可視化 | 赤色を設定 | 赤色を既定で設定（`BuildHodoscopeStrip`内） |

:::{seealso}

- [](./geant4-geometry-world.md)
- [](./geant4-geometry-tank.md)
- [](./geant4-geometry-mppc.md)
- [](./geant4-geometry-construct.md)
- [](./geant4-geometry-constructsdandfield.md)
- [](./geant4-sensor-sensitivedetector.md)
- [](./geant4-sensor-processhits.md)

:::

## リファレンス

- [G4Box](https://geant4.kek.jp/Reference/11.2.0/classG4Box.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4LogicalVolumeStore](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolumeStore.html)
- [G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)
- [G4SDManager](https://geant4.kek.jp/Reference/11.2.0/classG4SDManager.html)
- [G4VisAttributes](https://geant4.kek.jp/Reference/11.2.0/classG4VisAttributes.html)
