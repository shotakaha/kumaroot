# 電磁カロリメーターを作りたい（`BuildCalorimeter`）

```cpp
// Construct() の中
auto world = SetupWorld();
SetupCalorimeter(world);  // 実験室の中に20 × 4本のセルを並べる
```

カロリメーターは、密度の高い結晶シンチレーターを並べて設置し、通過する粒子が落としたエネルギーを光に変換して測定する検出器です。
付属サンプル[B5](https://github.com/Geant4/geant4/tree/master/examples/basic/B5)の電磁カロリメーターを参考に、KumaROOT向けに組み直しました。

関数は次の4つに分けています。

1. **結晶を作る**（`BuildCalorimeterCell`）：1本の結晶の論理ボリュームを返す
2. **結晶を並べる**（`BuildCalorimeter`）：結晶を格子状に並べた外形の論理ボリュームを返す
3. **配置する**（`SetupCalorimeter`）：外形を親ボリュームに物理ボリュームとして配置する
4. **有感領域を設定する**（`ConstructSDandField`）：結晶をSensitiveDetectorとして登録する

## 結晶を作りたい（`BuildCalorimeterCell`）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4VisAttributes.hh"

G4LogicalVolume* BuildCalorimeterCell(
    const G4String& logicalName = "CalorimeterCell",
    const G4String& materialName = "G4_CESIUM_IODIDE",
    G4double lengthX = 15. * cm,
    G4double lengthY = 15. * cm,
    G4double lengthZ = 30. * cm)
{
    // 形状を定義（G4Box は半分の長さで指定する）
    auto solid = new G4Box(
        logicalName + "Solid",  // solid 名
        0.5 * lengthX,
        0.5 * lengthY,
        0.5 * lengthZ
    );

    // 材料を定義（ヨウ化セシウム CsI）
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

    // （オプション）黄色で表示する
    auto color = new G4VisAttributes(G4Colour::Yellow());
    logical->SetVisAttributes(color);

    return logical;
}
```

`BuildCalorimeterCell`は、結晶1本の論理ボリュームを返します。
大きさは幅15 cm、高さ15 cm、長さ30 cmの直方体で、材料はCsIです。

:::{note}

結晶の論理ボリューム名（`CalorimeterCell`）は、後で`ConstructSDandField()`が名前で探すときに使います。
名前を変えるときは、そちらの名前も合わせてください。

:::

## 結晶を並べたい（`BuildCalorimeter`）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"
#include "G4VisAttributes.hh"

G4LogicalVolume* BuildCalorimeter(
    const G4String& logicalName = "Calorimeter",
    G4int nColumns = 20,
    G4int nRows = 4)
{
    // 結晶の論理ボリュームと、その大きさを取得する
    auto cell = BuildCalorimeterCell();
    auto cellBox = static_cast<G4Box*>(cell->GetSolid());

    // 結晶は隙間なく並べるので、ピッチは結晶の幅と高さになる
    G4double pitchX = 2. * cellBox->GetXHalfLength();
    G4double pitchY = 2. * cellBox->GetYHalfLength();
    G4double halfZ = cellBox->GetZHalfLength();

    // 結晶を並べる外形（透明な空気の箱）を作る
    G4double halfX = 0.5 * nColumns * pitchX;
    G4double halfY = 0.5 * nRows * pitchY;
    auto envelopeSolid = new G4Box(logicalName + "Solid", halfX, halfY, halfZ);
    auto envelope = new G4LogicalVolume(
        envelopeSolid,                                              // G4VSolid
        G4NistManager::Instance()->FindOrBuildMaterial("G4_AIR"),   // G4Material
        logicalName,                                                // 名前
        nullptr,  // G4FieldManager（未使用）
        nullptr,  // G4VSensitiveDetector（未使用）
        nullptr   // G4UserLimits（未使用）
    );
    envelope->SetVisAttributes(G4VisAttributes::GetInvisible());

    // 結晶を格子状に並べる（中心が原点に来るように）
    for (G4int col = 0; col < nColumns; col++) {
        for (G4int row = 0; row < nRows; row++) {
            G4double x = (col - 0.5 * (nColumns - 1)) * pitchX;
            G4double y = (row - 0.5 * (nRows - 1)) * pitchY;
            new G4PVPlacement(
                nullptr,                      // 回転なし
                G4ThreeVector(x, y, 0.),      // 位置
                cell,                         // 配置する論理ボリューム
                logicalName + "Cell",         // 物理ボリュームの名前
                envelope,                     // 親（外形の論理ボリューム）
                false,                        // pMany（未使用）
                col * nRows + row,            // コピー番号（結晶の番号）
                true                          // 重なりチェック
            );
        }
    }

    return envelope;
}
```

`BuildCalorimeter`は、結晶を格子状に並べた外形の論理ボリュームを1つ返します。
既定値では、横20列 × 縦4段の80本です。
外形は透明にしているので、画面では結晶だけが見えます。

コピー番号は`col * nRows + row`です。
列ごとに番号を振るので、B5の`CellParameterisation`と同じ並び順になります。

:::{note}

80本程度であれば、この方法で十分です。
結晶の数がさらに増えるときは、`G4PVParameterised`や`G4PVReplica`を使うと、配置の記述を減らせます。
詳しくは[G4PVReplica](./geant4-physicalvolume-pvreplica.md)を参照してください。

:::

## カロリメーターを配置したい（`SetupCalorimeter`）

```cpp
G4VPhysicalVolume* SetupCalorimeter(
    G4VPhysicalVolume* parent,
    const G4ThreeVector& position = G4ThreeVector(0., 0., 2. * m),
    const G4String& physicalName = "Calorimeter")
{
    // 回転なしで配置する
    G4RotationMatrix rotation;

    // 外形の論理ボリュームを作る
    auto calorimeter = BuildCalorimeter();

    return new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        calorimeter,                        // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        0,                                  // コピー番号
        true                                // 重なりチェック
    );
}
```

`SetupCalorimeter`は、`BuildCalorimeter`で作った外形を親ボリューム（`parent`）の中に配置します。
既定では、実験室の中心から z = +2 m の位置に置きます。
位置は引数`position`で変えられます。

## 有感領域を設定したい（`ConstructSDandField`）

```cpp
#include "G4LogicalVolumeStore.hh"
#include "G4SDManager.hh"
#include "CalorimeterSD.hh"  // G4VSensitiveDetector を継承した自作クラス

void Geometry::ConstructSDandField()
{
    // 結晶の論理ボリュームを名前で取得する
    auto cell = G4LogicalVolumeStore::GetInstance()->GetVolume("CalorimeterCell");

    // SensitiveDetector を作って SDManager に登録し、結晶に設定する
    auto sd = new CalorimeterSD("CalorimeterSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(sd);
    cell->SetSensitiveDetector(sd);
}
```

`ConstructSDandField`は、結晶の論理ボリュームに`CalorimeterSD`を設定します。
結晶の中をステップが通るたびに、`CalorimeterSD::ProcessHits()`が呼ばれます。

カロリメーターでは、ステップで落としたエネルギーが0のときはヒットとして扱わない、という判断をします。
`ProcessHits()`の書き方は[ヒットの判断](geant4-sensor-processhits)のカロリメーターの節を参照してください。
結晶番号は、`aStep->GetPreStepPoint()->GetTouchableHandle()->GetCopyNumber()`で取得できます。

## Constructで組み立てたい

```cpp
G4VPhysicalVolume* Construct()
{
    // 実験室（World）を配置する
    auto world = SetupWorld();

    // カロリメーターを実験室の中に配置する
    SetupCalorimeter(world);

    return world;
}
```

`Construct()`では、`SetupWorld()`で実験室を配置し、その物理ボリュームを親として`SetupCalorimeter()`を呼び出します。
`ConstructSDandField()`は、`Construct()`の後に呼ばれます。
組み立ての流れは[ジオメトリを構築したい](geant4-geometry-construct)にまとめています。

## B5との違い

| 項目 | B5 | このページ |
| --- | --- | --- |
| 結晶の論理ボリューム | メンバー変数`fCellLogical` | `BuildCalorimeterCell()`の戻り値（名前で取得） |
| 並べる数 | `Constants.hh`の`kNofEmColumns`、`kNofEmRows` | `BuildCalorimeter()`の引数`nColumns`、`nRows` |
| 並べ方 | `G4PVParameterised`と自作の`CellParameterisation` | 二重ループで`G4PVPlacement` |
| 配置先 | 親ボリュームに直接配置 | 結晶を空気の外形に並べ、外形を配置 |
| x、y方向の位置 | `CellParameterisation`の中で計算 | `(col - 0.5 * (nColumns - 1)) * pitchX`など、中心が原点に来る式 |

:::{seealso}

- [](./geant4-geometry-world.md)
- [](./geant4-hodoscope.md)
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
