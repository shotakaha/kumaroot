# プラスチックシンチレータを作りたい

```cpp
// シンチレーター
G4NistManager *nm = new G4NistManager::Instance()
G4Material *scintillator = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");
```

[付属サンプルB5のDetectorConstruction.cc](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/DetectorConstruction.cc)を参考にプラスチックシンチレーターを作成しました。

:::{note}

付属サンプルB5では、シンチレーターの材料にビニルトルエン（C9H10）を指定していました。
もしかしたら、実験によっては別の材料を使っているかもしれません。

:::

## シンチレーターバーを作りたい

```cpp
G4LogicalVolume *DefineDetectorVolume(const G4String &name){

    // 材料を調達する
    G4NistManager *nm = new G4NistManager::Instance()
    auto material = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

    // 形状を定義する
    G4double halfX = 2.5 * cm;
    G4double halfY = 5.0 * cm;
    G4double halfZ = 0.5 * cm;

    auto solid = new G4Box(
        "detectorSolid",
        halfX,    // 幅
        halfY,    // 長さ
        halfZ,   // 厚み
    )

    // 論理物体を定義する
    auto logical = new G4LogicalVolume(
        solid,     // G4VSolid
        material,  // G4Material
        name,      // 名前（引数で指定）
    )

    // ワイヤフレームの色を変更（オプション）
    auto color = new G4VisAttribute(G4Colour(0.8888, 0.0, 0.0));
    logical->SetVisAttributes(color);

    return logical;

    // 物理物体の配置は別にする
}
```

小型宇宙線検出器OSECHIで使っているプラスチックシンチレーターを想定して作成しました。
OSECHIでは幅5cm、長さ10cm、厚み1cmのプラシンを3枚重ねて使っています。

## 有感領域を追加したい

```cpp
auto sdManager = G4SDManager::GetSDMpointer();
G4String SDname;
auto detector = new DetectorSD(SDname="/detector");
fDetectorLogical->SetSensitiveDetector(detector);
```
