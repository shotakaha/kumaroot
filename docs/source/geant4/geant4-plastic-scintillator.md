# プラスチックシンチレータを作りたい

```cpp
// シンチレーター
G4Material *scintillator = G4Material:GetMaterial("G4_PLASTIC_SC_VINYLTOLUEN");

G4double width = 5.*cm;
G4double depth = 10.*cm;
G4double height = 1.*cm;

G4Box *detectorSolid = new G4Box(
    "detectorBox",
    0.5 * width,    // 幅
    0.5 * depth,    // 長さ
    0.5 * height,   // 厚み
)

G4LogicalVolume *detectorLogical = new G4LogicalVolume(
    detectorSolid,
    scintillator,
    "detectorLogical",
)
```

[付属サンプルB5のDetectorConstruction.cc](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/DetectorConstruction.cc)を参考にプラスチックシンチレーターを作成しました。

小型宇宙線検出器OSECHIで使っているプラスチックシンチレーターを作りました。
OSECHIでは幅5cm、長さ10cm、厚み1cmのプラシンを3枚重ねて使っています。

:::{note}

付属サンプルB5では、シンチレーターの材料にビニルトルエン（C9H10）を指定していました。
もしかしたら、実験によっては別の材料を使っているかもしれません。

:::

## 見た目を追加したい

```cpp
auto visAttributes = new G4VisAttribute(G4Colour(0.8888, 0.0, 0.0));
detectorLogical->SetVisAttributes(visAttributes);
fVisAttributes.push_back(visAttributes);
```

## 有感領域を追加したい

```cpp
auto sdManager = G4SDManager::GetSDMpointer();
G4String SDname;
auto detector = new DetectorSD(SDname="/detector");
fDetectorLogical->SetSensitiveDetector(detector);

```
