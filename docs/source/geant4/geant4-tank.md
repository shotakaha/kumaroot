# 水タンクを作りたい

```cpp
// 水タンクの寸法
G4double diameter = 39.3*m;
G4double height = 41.4*m

// ソリッド（形状）の作成
// 内径, 外径, 高さ, sphi, dphi
G4double rmin, rmax, z, sphi, dphi;
G4Tubs *Stank = new G4Tubs(
    "Tank",
    rmin=0.,
    rmax=0.5*diameter,
    z=0.5*height,
    sphi=0.,
    dphi=360.,
)

// ロジカルボリュームの作成
G4LogicalVolume *LVtank = new G4LogicalVolume(
    Stank,    // G4VSolid
    Water,    // G4Material: 「水（Water）」は先に作っておく
    "Tank",   // G4String
)

// 物理ボリュームの作成
G4RotationMatrix rotation = G4RotationMatrix();
G4ThreeVector direction = G4ThreeVector(0., 0., 0.);
G4Transform3D location = G4Transform3D(rotation, direction);

G4bool checkOverlaps = true

new G4PVPlacement(
    location,  // 配置する場所（G4Transform3D）
    LVtank,    // 配置するボリューム（G4LogicalVolume）
    "Tank",    // 名前
    LVworld,   // 親ボリューム（G4LogicalVolume）
    false,     // no boolean operation
    0,         // copy number
    checkOverlaps
)
```

水タンクを配置してみました。
タンクのサイズはスーパーカミオカンデ（直径39.3m、高さ41.4m）にしてあります。
