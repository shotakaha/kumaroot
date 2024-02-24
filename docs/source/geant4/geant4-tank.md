# 水タンクを作りたい

```cpp
// ソリッド（形状）の作成
G4double rmin, rmax, sphi, dphi;
G4double diameter = 39.3*m;
G4double height = 41.4*m

G4Tubs *STank = new G4Tubs(
    "Tank",
    rmin=0.,
    rmax=0.5 * diameter,
    z=0.5*height,
    sphi=0.,
    dphi=360.,
)

// ロジカルボリュームの作成
G4LogicalVolume *LVTank = new G4LogicalVolume(
    STank,    // G4VSolid
    Water,    // G4Material: 「水（Water）」は先に作っておく
    "Tank",   // G4String
)

// 物理ボリュームの作成
G4RotationMatrix *rotation = G4RotationMatrix();
G4ThreeVector *direction = G4ThreeVector(0., 0., 0.);
G4Transform3D *location = G4Transform3D(rotation, direction);

G4bool checkOverlaps = true

new G4PVPlacement(
    location,  // G4Transform3D
    LVTank,    // G4LogicalVolume: 配置するボリューム（LogicalVolume）
    "Tank",    // G4String
    LVWorld,   // G4LogicalVolume: 親ボリューム（Logical Volume）
    false,     // G4bool pManyは廃止らしい
    0,         // G4int pCopyNo
    checkOverlaps
)
```

水タンクを配置してみました。
タンクのサイズはスーパーカミオカンデ（直径39.3m、高さ41.4m）にしてあります。
