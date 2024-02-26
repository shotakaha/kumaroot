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

#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
```

測定器の構成を確認しました。
``World`` -> ``Envelope`` -> ``Shape1``、``Shape2``のように
物理ボリュームが定義されていました。
それぞれの内容を順番に確認してみます。

オブジェクトの変数名は、分かりやすくなるように変更しました。

### マテリアルの定義

```cpp
#include "G4NistManager.hh"
G4NistManager *nist = G4NistManager::Instance();
G4Material *Air = nist->FindOrBuildMaterial("G4_AIR");        // World
G4Material *Water = nist->FindOrBuildMaterial("G4_WATER");    // Envelope
G4Material *Tissue = nist->FindOrBuildMaterial("G4_A-150_TISSUE");     // Shape1
G4Material *Bone = nist->FindOrBuildMaterial("G4_BONE_COMPACT_ICRU");  // Shape2
```

使用さされているテリアルを集めてみました。
マテリアルの変数名は分かりやすい名前に変更しました。

すべてのマテリアルが``G4NistManager``を使ってNIST材料データベースを参照していました。
それぞれのマテリアルの詳細は公式ユーザーズガイドの[Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)で確認できます。

### Worldの定義

```cpp
// Size of the world
G4double worldXY = 1.2*m;
G4double worldZ = 1.2*m;

// 形状
auto SWorld = new G4Box(
    "World",        // its name
    worldXY * 0.5,  // half x
    worldXY * 0.5,  // half y
    worldZ * 0.5,   // half z
)

// ロジカルボリューム
auto LVWorld = new G4LogicalVolume(
    SWorld, // its solid
    Air, // its material
    "World",   // its name
);

// 物理ボリューム
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

``World``は実験室の部屋そのものみたいなものです。
この中に実験装置などを子ボリューム（daughter volume）として配置します。
すべてのボリュームの親に相当するため、親ボリューム（mother volume）は持ちません。
