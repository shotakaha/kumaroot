# 実験室を作りたい（``DefineWorldVolume``）

実験室（＝ワールド）の定義し、論理物体を返す関数を作成します。
これを``DetectorConstruction::Construct``の中で呼び、物理物体として配置します。

## DefineWorldVolume

ワールドのボリュームを定義します。
引数で論理物体の名前を設定できるようになっています。

```cpp
G4LogicalVolume *DefineWorldVolume(const G4String &name){

    // 実験室の素材を決める
    G4NistManager *nm = new G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_AIR");

    // 実験室の大きさ
    G4double halfX = 50.0 * cm;
    G4double halfY = 50.0 * cm;
    G4double halfZ = 50.0 * cm;

    // 実験室の形状
    auto solid = new G4Box(
        "worldSolid",    // 名前
        halfX,
        halfY,
        halfZ,
    )

    // 実験室
    auto logical = new G4LogicalVolume(
        solid,       // G4VSolid
        material,    // G4Material
        name,        // 名前
        nullptr,     // G4FieldManager
        nullptr,     // G4VSensitiveDetector
        nullptr,     // G4UserLimits
    )

    G4cout << "World: "
    << "x=" << 2 * halfX / cm << " cm, "
    << "y=" << 2 * halfY / cm << " cm, "
    << "z=" << 2 * halfZ / cm << " cm, "
    << "of " << material->GetName()
    << G4endl;

    return logical
}
```

## DetectorConstruction.hh

```cpp
#ifndef DetectorConstruction_h
#define DetectorConstruction_h 1

#include "G4VPhysicalVolume.hh"

class DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        G4VPhysicalVolume* Construct() override;
}

#endif DetectorConstruction_h
```

## DetectorConstruction.cc

```cpp
#include "DetectorConstruction.hh"

#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4VPhysicalVolume.hh"
#include "G4NistManager.hh"

G4VPhysicalVolume* DetectorConstruction::Construct()
{
    // 実験室の論理物体を取得する
    auto pWorldLogical = DefineWorldVolume("WorldLogical")

    // 実験室の置き場所を決める
    G4RotationMatrix rotation = G4RotationMatrix();       // 回転 : なし
    G4ThreeVector direction = G4ThreeVector(0., 0., 0.);  // 方向 :  (0, 0, 0)
    G4Transform3D location = G4Transform3D(rotation, direction)  // 座標

    // 実験室を配置する
    G4VPhysicalVolume *pWorldPhysical = new G4PVPlacement(
        location,         // G4Transform3D : 論理ボリュームを配置する座標
        pWorldLogical,    // G4LogicalVolume : 配置する論理ボリューム
        "WorldPhysical",  // G4String : この物理ボリュームの名前
        0,                // G4LogicalVolume: 親ボリュームはなし
        false,            // G4bool pMany（廃止）
        0,                // G4int pCopyNo : コピー番号
        true              // G4bool check overlaps
    )

    return pWorldPhysical;
}
```

測定器シミュレーションを実行する実験室（通称：World）を作成しました。
実験室は50m立方の箱型としました。
どうしてこの大きさにしたかというと、この中にスーパーカミオカンデを配置してみたいからです。

まず、実験室の形を決めます。
箱型の実験室なので``G4Box``を使いました。
``G4Box``のサイズに関係する引数はすべて**半分の長さ**で指定することになっているので0.5倍してあります。

次に実験室の材質を決めます。
地球にある実験室なので空気で満たしました。

最後に、置き場所を決めます。
これで、最上位の親ボリュームである実験室の完成です。
あとは、測定装置をこの中に納まるように並べるだけです。

:::{note}

Geant4では生成された粒子が「実験室の外側に飛び出す」か「運動量がゼロになる」まで、素粒子反応が繰り返されます。なので、ある程度の外枠を定義しておかないと、必要のない計算にまで時間をかけてしまうことになります。

:::

## 見えなくする

```cpp
pWorldLogical->SetVisAttributes(G4VisAttributes::GetInvisible());
```
