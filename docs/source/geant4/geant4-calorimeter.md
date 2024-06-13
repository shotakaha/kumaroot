# 電磁カロリメーターしたい

[付属サンプルB5](https://github.com/Geant4/geant4/tree/master/examples/basic/B5)は、電磁カロリメーターが使われています。
このサンプルを参考に、再構築してみます。

:::{note}

カロリメーターは密度の高い結晶シンチレーターを並べて設置し、通過する粒子が落とすエネルギーをシンチレーション光に変換して、吸収したエネルギーを測定する検出器のひとつです。

:::

## CsI結晶を定義する関数

```cpp
G4LogicalVolume *DefineCellVolume(const G4String &name)
{
    // 材料を準備する
    G4NistManager *nm = new G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_CESIUM_IODIDE");

    // 結晶を作成する
    G4double halfX = 7.5 * cm;    // 幅: 15cm
    G4double halfY = 7.5 * cm;    // 高: 15cm
    G4double halfZ = 15.0 * cm;   // 長: 30cm

    auto solid = new G4Box(
        "cellBox",
        halfX,
        halfY,
        halfZ,
    );

    // 論理物体を作成する
    auto logical = new G4LogicalVolume(
        solid,
        CsI,
        name,
    )

    // 結晶を着色する
    G4VisAttributes color = G4VisAttributes(G4Colour::Yellow());
    logical->SetVisAttributes(color);

    return logical;
}
```

## 電磁カロリメーターを定義する関数

```cpp
G4LogicalVolume *DefineCalorimeterVolume(const G4String &name)
{
    // 材料を準備する
    G4NistManager *nm = new G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_CESIUM_IODIDE");

    // カロリメーターを作成する
    G4double halfX = 1.5 * m;    // 幅: 300cm
    G4double halfY = 30.0 * cm;  // 高:  60cm
    G4double halfZ = 15.0 * cm;  // 長:  30cm

    auto solid = G4Box(
        "emcBox",
        halfX,
        halfY,
        halfZ
    );

    auto logical = new G4LogicalVolume(
        solid,
        material,
        name,
    )

    // カロリメータは着色しない（？）
    G4VisAttributes invisible(false, G4Colour::Yellow());
    // メモ：直接初期化
    // コンストラクタを呼び出してオブジェクトを直接初期化
    // クラスのコンストラクタが引数を取る場合によく使われる

    logical->SetVisAttributes(invisible);

    return logical;
}
```

## 使い方

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

    // CsIカロリメーター

    auto emCalorimeterLogical = new DefineCalorimeterVolume("EMCalorimeterLogical");

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
    fCellLogical = new DefineCellVolume("cellLogical");

    G4VPVParameterisation* cellParam = new CellParameterisation();
    new G4PVParameterised(
        "cellPhysical",
        fCellLogical,
        emCalorimeterLogical,
        kXAxis,
        kNofEmCells,
        cellParam);
}
```
