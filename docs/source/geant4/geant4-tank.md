# 水タンクを作りたい

## 水タンクを定義する関数

```cpp
G4LogicalVolume *DefineWaterTank(const G4String &name){

    // 材料を準備する
    G4NistManager *nm = G4NistManager::Instance();
    auto material = nm->FindOrBuild("G4_WATER");

    // サイズを定義する
    G4double diameter = 39.3 * m;
    G4double height = 41.4 * m;

    // ソリッド（形状）の作成
    // 内径, 外径, 高さ, sphi, dphi
    G4double rmin, rmax, z, sphi, dphi;
    auto solid = new G4Tubs(
        "tankSolid",
        rmin=0.,
        rmax=0.5*diameter,
        z=0.5*height,
        sphi=0.*deg,
        dphi=360.*deg,
    )

    // 論理物体の作成
    auto logical = new G4LogicalVolume(
        solid,     // G4VSolid : 形状
        material,  // G4Material : 素材（「水」は先に作っておく）
        name,      // 名前（引数で指定）
    )

    // ワイヤーフレームを着色（オプション）
    auto color = new G4VisAttributes(true, G4Colour(0., 0.5, 1.)); // 青系
    logical->SetVisAttributes(color);

    return logical;
}
```

タンクのサイズはスーパーカミオカンデ（直径39.3m、高さ41.4m）にしてあります。

## 使い方

``DetectorConstruction::Construct()``の中で使います。

```cpp
G4VPhysicalVolume* DetectorConstruction::Construct(){
    // 論理物体を取得
    auto pWorldLogical = DefineWorlfVolume("world");
    auto pTankLogical = DefineWaterTank("waterTank");

    // 物理ボリュームの作成
    // タンクを縦置きにする
    G4RotationMatrix rotation = G4RotationMatrix(0., 90.*deg, 0.);
    G4ThreeVector direction = G4ThreeVector(0., 0., 0.);
    G4Transform3D location = G4Transform3D(rotation, direction);

    new G4PVPlacement(
        location,        // G4Transform3D : 配置する座標
        pTankLogical,    // G4LogicalVolume : 子ボリューム
        "TankPhysical",  // G4String : 名前
        pWorldLogical,   // G4LogicalVolume : 親ボリューム
        false,           // no boolean operation
        0,               // G4int : copy number
        true,
    )
}
```

水タンクを配置できました。
