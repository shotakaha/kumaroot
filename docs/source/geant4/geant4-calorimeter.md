# 電磁カロリメーターしたい

[付属サンプルB5](https://github.com/Geant4/geant4/tree/master/examples/basic/B5)でカロリメーターを使っています。
カロリメーターは密度の高い結晶シンチレーターを並べて設置し、通過する粒子が落とすエネルギーをシンチレーション光に変換して、吸収したエネルギーを測定する検出器のひとつです。

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        G4PhysicalVolume* Construct() override;
        void ConstructSDandField() override;
    private:
        G4LogicalVolume* fCellLogical = nullptr;
}
```

まず``B5/include/DetectorConstruction.hh``で定義されているメソッドやメンバー変数を確認します。

電磁カロリメータの論理ボリューム（``fCellLogical``）はプライベート変数で用意されていました。
``Construct``メソッドの中でCSI結晶を用意し、それを複製して電磁カロリメーターを組みたてています。
また、``ConstructSDandField``メソッドで有感領域を設定しているようです。

```cpp
G4PhysicalVolume* DetectorConstruction::Construct()
{
    // 材料を調達
    ConstructMaterials();
    auto csI = G4Material::GetMaterial("G4_CESIUM_IODIDE");

    // CsIカロリメーター
    auto emCalorimeterSolid = new G4Box(
        "EMCalorimeterBox",
        1.5*m,
        30.*cm,
        15.*cm);

    auto emCalorimeterLogical = new G4LogicalVolume(
        emCalorimeterSolid,
        csI,
        "EMCalorimeterLogical");

    new G4PVPlacement(
        nullptr,
        G4ThreeVector(0., 0., 2.*m),
        emCalorimeterLogical,
        "EMCalorimeterPhysical",
        secondArmLogical,
        false
        0,
        checkOverlaps);

    // 電磁カロリメーターのセル
    auto cellSolid = new G4Box(
        "cellBox",
        7.5*cm,
        7.5*cm,
        15.*cm);

    fCellLogical = new G4LogicalVolume(
        cellSolid,
        csI,
        "cellLogical");

    G4VPVParameterisation* cellParam = new CellParameterisation();
    new G4PVParameterised(
        "cellPhysical",
        fCellLogical,
        emCalorimeterLogical,
        kXAxis,
        kNofEmCells,
        cellParam);

    // 可視化オプション
    G4VisAttributes invisibleYellow(false, G4Colour::Yellow());
    emCalorimeterLogical->SetVisAttributes(invisibleYellow);
    fCellCalorimeterLogical->SetVisAttributes(yellow);
}
```
