# 水タンクを作りたい

```cpp
// 水タンクの寸法
G4double diameter = 39.3*m;
G4double height = 41.4*m

// ソリッド（形状）の作成
// 内径, 外径, 高さ, sphi, dphi
G4double rmin, rmax, z, sphi, dphi;
G4Tubs *pTankSolid = new G4Tubs(
    "TankSolid",
    rmin=0.,
    rmax=0.5*diameter,
    z=0.5*height,
    sphi=0.*deg,
    dphi=360.*deg,
)

// ロジカルボリュームの作成
G4LogicalVolume *pTankLogical = new G4LogicalVolume(
    pTankSolid,     // G4VSolid : 形状
    pWater,         // G4Material : 素材（「水」は先に作っておく）
    "TankLogical",  // G4String : 名前
)

// 物理ボリュームの作成
G4RotationMatrix rotation = G4RotationMatrix();
G4ThreeVector direction = G4ThreeVector(0., 0., 0.);
G4Transform3D location = G4Transform3D(rotation, direction);

new G4PVPlacement(
    location,        // G4Transform3D : 配置する場所
    pTankLogical,    // G4LogicalVolume : 子ボリューム
    "TankPhysical",  // G4String : 名前
    pWorldLogical,   // G4LogicalVolume : 親ボリューム
    false,           // no boolean operation
    0,               // G4int : copy number
    true,
)
```

水タンクを配置してみました。
タンクのサイズはスーパーカミオカンデ（直径39.3m、高さ41.4m）にしてあります。

## 色をつけたい（``SetVisAttributes``）

```cpp
G4VisAttributes *attributes = new G4VisAttributes(true, G4Colour(0., 0.5, 1.));
pTankLogical->SetVisAttributes(attributes)
```
