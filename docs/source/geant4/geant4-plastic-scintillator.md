# プラスチックシンチレータを作りたい

```cpp

G4double width = 5.*cm;
G4double depth = 10.*cm;
G4double height = 1.*cm;

G4Box *SBox = new G4Box(
    "Plastic Scintillator",
    0.5 * width,    // 幅
    0.5 * depth,    // 長さ
    0.5 * height,   // 厚み
)

G4LogicalVolume *LVBox = new G4LogicalVolume(
    SBox,
    ...,     // G4Material: あとで調べる
    "Plastic Scintillator",
)
```

小型宇宙線検出器OSECHIで使っているプラスチックシンチレーターを作りました。
OSECHIでは幅5cm、長さ10cm、厚み1cmのプラシンを3枚重ねて使っています。
