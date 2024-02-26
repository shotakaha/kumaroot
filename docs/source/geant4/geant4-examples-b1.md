# B1したい（``examples/basic/B1/``）

```console
$ cd B1
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
$ ./exampleB1 run1.mac
$ ./exampleB1 run2.mac
```

``examples/basic/B1/``の中にビルド用ディレクトリを（``build``）を作成します。
ビルド用ディレクトリの中に移動して、``cmake``で実行ファイルをビルドします。

## ランマネージャーの作成

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
#include "G4RunManagerFactory.hh"

auto *runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default)
```

## 測定器の作成

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
#include "DetectorConstruction.hh"

DetectorConstruction *detector = new DetectorConstruction()
runManager->SetUserInitialization(detector);
```

ランマネージャーに測定器を追加します。
どのような測定器が追加されたのか、``B1DetectorConstruction.hh/.cc``で確認します。


```cpp
//////////////////////////////////////////////////
// include/DetectorConstruction.hh
//////////////////////////////////////////////////
#ifndef B1DetectorConstruction_h
#define B1DetectorConstruction_h 1

#include "G4VUserDetectorConstruction.hh"

namespace B1
{
    class DetectorConstruction : public G4VUserDetectorConstruction
    {
        public:
        protected:
    }
}

#endif
```

``DetectorConstruction``クラスは``G4VUserDetectorConstruction``抽象クラスを継承して作られており、クラス全体は``B1``という名前空間の中に作成されていました。
また、このヘッダファイルはインクルードガードしてありました。

```cpp
//////////////////////////////////////////////////
// src/DetectorConstruction.cc
//////////////////////////////////////////////////
#include "DetectorConstruction.hh"
```

測定器の構成を確認しました。
``World`` -> ``Envelope`` -> ``Shape1``、``Shape2``のように
物理ボリュームが定義されていました。
それぞれの内容を順番に確認してみます。

### Worldの定義

```cpp
// Get NIST material manager
G4NistManager *nist = G4NistManager::Instance()
G4Material *Water = nist->FindOrBuildMaterial("G4_WATER")
G4Material *Air = nist->FindOrBuildMaterial("G4_AIR")

// Size of the world
G4double worldXY = 1.2*m;
G4double worldZ = 1.2*m;

//
auto SWorld = new G4Box(
    "World",        // its name
    worldXY * 0.5,  // half x
    worldXY * 0.5,  // half y
    worldZ * 0.5,   // half z
)

auto LVWorld = new G4LogicalVolume(
    SWorld, // its solid
    Air, // its material
    "World",   // its name
);

G4boolean checkOverlaps = true
auto PVWorld = new G4PVPlacement(
    nullptr,          // no rotation,
    G4ThreeVector(),  // at (0, 0, 0)
    LVWorld,       // its logical volume
    "World",          // its name
    nullptr,          // its mother volume
    false,            // no boolean operation
    0,                // copy number
    checkOverlaps     // check overlaps
);
```

