# ホドスコープを作りたい

[付属サンプルB5](https://github.com/Geant4/geant4/tree/master/examples/basic/B5)でホドスコープを使っています。
ホドスコープは短冊状のシンチレーターを並べて設置することで、粒子が通過した場所をわかるようにした飛跡検出器のひとつです。

どのように作成しているのか、ソースコードを分解して整理してみます。

```cpp
// B5/include/DetectorConstruction.hh
class DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        G4PhysicalVolume* Construct() override;
        void ConstructSDandField() override;
    private:
        G4LogicalVolume *fHodoscopeLogical = nullptr;
}
```

まず``B5/include/DetectorConstruction.hh``で定義されているメソッドやメンバー変数を確認します。

ホドスコープの論理ボリューム（``fHodoscopeLogical``）はプライベート変数で用意されていました。
``Construct``メソッドの中でホドスコープを組み立て、
``ConstructSDandField``メソッドで有感領域を設定しているようです。

```cpp
// B5/src/DetectorConstruction.cc

G4PhysicalVolume* DetectorConstruction::Construct() {

    // 材料を調達
    ConstructMaterials();  // 材料を一括調達する自作メソッド
    auto scintillator = G4Material::GetMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

    // 棒状の物体を作成
    auto hodoscopeSolid = new G4Box(
        "hodoscopeBox",
        5.*cm,
        20.*cm,
        0.5*.cm
        );

    // シンチレーターにする
    fHodoscopeLogical = new G4LogicalVolume(
        hodoscopeSolid,
        scintillator,
        "hodoscopeLogical"
        );

    // シンチレーターを並べる
    for (auto i=0; i < kNofHodoscopes; i++) {
        G4double x1 = (i - kNofHodoscopes/2) * 10. * cm;
        new G4PVPlacement(
            nullptr,
            G4ThreeVector(x1, 0., -1.5*m),
            fHodoscopeLogical,
            "hodoscopePhysical",
            firstArmLogical,    // mother volume
            false,
            i,    // Copy No.
            checkOverlaps
        );
    }

    // 可視化オプション
    G4VisAttributes red(G4Colour::Red());
    fHodoscopeLogical->SetVisAttributes(red);
}
```

``Construct``メソッドの中で、ホドスコープに関する部分を抜き出してみました。
ホドスコープに使うシンチレーターは、大きさが10 cm x 40 cm x 1の直方体で作ってありました。
また、赤色で表示されるように可視化属性（``G4VisAttributes``）が設定してあります。

このシンチレーターを``kNofHodoscopes``個を並べて（``G4VUserPlacement``）、ホドスコープを組み立てています。

```cpp
// B5/include/Constants.hh

constexpr G4int kNofHodoscopes = 15;
```

シンチレーターの数は``B5/include/Constants.hh``で15本に設定されています。

```cpp
#include "HodoscopeSD.hh"
#include "G4SDManager.hh"

void DetectorConstruction::ConstructSDandField()
{
    auto sdManager = G4SDManager::GetSDMpointer();
    G4String SDname;

    auto hodoscope = new HodoscopeSD(SDname="/hodoscope");
    sdManager->AddNewDetector(hodoscope);
    fHodoscopeLogical->SetSensitiveDetector(hodoscope);
}
```

ホドスコープを通過した粒子を検出できるように、有感領域を設定する必要があります。
シンチレーターの論理ボリューム（``fHodoscopeLogical``）に対して、``HodoscopeSD``オブジェクトが設定されていました。
