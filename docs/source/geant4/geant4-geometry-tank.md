# 水タンクを作りたい（``SetupTankVolume``）

```cpp
// include/Geometry.hh

#ifndef Geometry_h
#define Geometry_h 1

#include "G4VUserDetectorConstruction.hh"
#include "G4SystemOfUnit.hh"
#include "G4LogicalVolume.hh"

class Geometry : public G4VUserDetectorConstruction
{
  private:
    G4LogicalVolume* SetupTankVolume();
    G4String fTankLVName{"Tank"};
    G4String fTankMaterial{"G4_WATER"};
    G4double fTankDiameter = 39.3 * m;
    G4double fTankHeight = 41.4 * m;
};

#endif
```

``Geometry``クラスのヘッダーファイルの中で、
``SetupTankVolume``と関連する内部変数を定義します。

水タンクの大きさはスーパーカミオカンデ（直径39.3m、高さ41.4m）にしてあります。

## 水タンクを準備する

```cpp
G4LogicalVolume *Geometry::SetupWaterTank()
{
    // パラメーターの確認
    G4String logical_name = fTankLVName;     // "Tank"
    G4String material_name = fTankMaterial;  // "G4_WATER"
    G4double diameter = fTankDiameter;       // 39.3 * m;
    G4double height = fTankHeight;           // 41.4 * m;

    // 形状を定義
    G4double r_min{0. * cm};         // 底面の内径
    G4double r_max{0.5 * diameter};  // 底面の外径
    G4double half_z{0.5 * height};   // 円柱の高さ（の半分）
    G4double s_phi{0. * deg};        // 円の角度（始点）
    G4double d_phi{360. * deg};      // 円の角度（終点）
    auto solid = new G4Tubs(
        "tankSolid",    // ソリッド名
        r_min,
        r_max,
        half_z,
        s_phi,
        d_phi
    );

    // 材料を定義
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuild(material_name);

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logical_name, // 名前
    )

    // （オプション）ワイヤーフレームを着色
    auto color = new G4VisAttributes(true, G4Colour(0., 0.5, 1.)); // 青系
    logical->SetVisAttributes(color);

    return logical;
}
```

``G4Tubs``で円柱を作成しました。
円柱の材料を``G4_WATER``にしました。
水タンクの論理ボリュームができました。

## 水タンクを配置する

```cpp
G4VPhysicalVolume* SetVolumes()
{
    // Worldを準備する
    auto world = SetupWorldVolume();
    // Worldを配置する
    auto theWorld = new G4PVPlacement{...};

    // WaterTankを準備する
    auto tank = SetupWaterTankVolume();

    // タンクは縦置きにしたい
    G4RotationMatrix rotation = G4RotationMatrix(0., 90.*deg, 0.);
    G4ThreeVector direction = G4ThreeVector(0., 0., 0.);
    G4Transform3D origin = G4Transform3D(rotation, direction);

    new G4PVPlacement(
        origin,          // 子ボリュームの位置
        tank,            // 子ボリューム
        "TankPhysical",  // 名前
        theWorld,        // 親ボリューム
        false,           // no boolean operation
        0,               // G4int : copy number
        true,
    );

    return theWorld;
}
```

スーパーカミオカンデをイメージしているため、
水タンクを縦置きにしています。

``G4RotationMatrix``でY軸方向に90度回転させました。
縦置きにするために、どの引数を変更すればよいか、
よくわからなかったので、コンパイル＆実行して確認しながら調整しました。

ワールドの中心に配置したかったので、
``G4ThreeVector``は原点のままにしています。
