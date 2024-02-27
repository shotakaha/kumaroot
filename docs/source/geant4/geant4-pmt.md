# PMTを作りたい

```cpp
G4Tubs *SPmt = new G4Tubs(
    "PMT",    // G4String
    0.,       // G4double: 内径
    3.81*cm,  // G4double: 外径 （3in.管）
    1*cm,     // G4double: 高さ（厚み）
    0.,       // G4double sphi,
    360.,     // G4double dphi,
)

G4LogicalVolume *LVPmt = new G4LogicalVolume(
    SPmt,      // G4VSolid: 使用するソリッドオブジェクト
    Acrylic,   // G4Material: アクリルは先に用意しておく
    "PMT",     // G4String
)
```

光電子増倍管（PMT）の入射窓（だけ）を作成した。
PMTに入射した光子の数を知りたい場合は、``G4SensitiveDetector``を追加し、データを残す必要があります（あとで追加する）
