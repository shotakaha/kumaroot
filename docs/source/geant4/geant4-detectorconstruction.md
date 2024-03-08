# 測定器を作りたい（``G4VUserDetectorConstruction``）

```cpp
// include/MYDetectorConstruction.hh

#ifndef MYDetectorConstruction_h
#define MYDetectorConstruction_h 1

#include "G4VUserDetectorConstruction.hh"

#include "G4VPhysicalVolume.hh"
#include "G4LogicalVolume.hh"

class MYDetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        DetectorConstruction() = default;
        ~DetectorConstruction() override = default;

        G4VPhysicalVolume* Construct() override;

    private:
        G4LogicalVolume *fWorldL
        G4LogicalVolume *fTankL
        G4LogicalVolume *fPmtL

}
#endif
```

```cpp
// src/MYDetectorConstruction.cc

#include "MYDetectorConstruction.hh"

G4VPhysicalVolume* DetectorConstruction::Construct()
{
    // ワールド
    G4Material *fAir = new G4Material(...);
    G4Box *fWorldS = new G4Box("worldS", ...);
    G4LogicalVolume *fWorldL = new G4LogicalVolume(fWorldS, fAir, "worldL");
    G4Transform3D location = G4Transform3D(nullptr, nullptr);
    G4VPhysicalVolume *fWorldP = new G4PVPlacement(location, fWorldL, "worldP", nullptr, ...);

    // 測定器（例：水タンク）
    G4LogicalVolume *fTankL = new G4LogicalVolume(...);
    new G4PVPlacement(...);

    // 検出器（例：光電子増倍管）
    G4LogicalVolume *fPmtL = new G4LogicalVolume(...);
    new G4PVPlacement(...);

    // 必ずワールドをリターンする
    return fWorldP
}
```

``MYDetectorConstruction``クラスは、``G4VUserDetectorConstruction``を継承して作成します。

``G4VSolid``、``G4LogicalVolume``、``G4VPhysicalVolume``を使って、Geant4の中に構造物を配置できます。
