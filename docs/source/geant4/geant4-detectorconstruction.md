# 測定器を作りたい（``G4VUserDetectorConstruction``）

```cpp
// include/MYDetectorConstruction.hh

#ifndef MYDetectorConstruction_hh
#define MYDetectorConstruction_hh 1

#include "G4VUserDetectorConstruction.hh"
#include "G4LogicalVolume.hh"

class MYDetectorConstruction : public G4VUserDetectorConstruction
{
    private:
        G4LogicalVolume *fLVworld
        G4LogicalVolume *fLVtank
        G4LogicalVolume *fLVpmt


}
#endif
```

```cpp
// src/MYDetectorConstruction.cc

#include "MYDetectorConstruction.hh"

class MYDetectorConstruction : public G4VUserDetectorConstruction
{

}
```

``MYDetectorConstruction``クラスは、``G4VUserDetectorConstruction``を継承して作成します。


``G4VSolid``、``G4LogicalVolume``、``G4VPhysicalVolume``を使って、Geant4の中に構造物を配置できます。

## 形状したい（``G4VSolid``）


## 材質したい（``G4LogicalVolume``）

## 配置したい（``G4VPhysicalVolume``）
