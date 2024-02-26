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

## マネージャーの定義

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
#include "G4UIExecutive.hh"
#include "G4RunManagerFactory.hh"
#include "G4VisExecutive.hh"
#include "G4UImanager.hh"

G4UIExecutive *ui = new G4UIExecutive(argc, argv);
auto *runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default)
G4VisManager *visManager = new G4VisExecutive;
G4UImanager *uiManager = G4UImanager::GetUIpointer();
```

``exampleB1.cc``で使われているマネージャーたちを集めてみました。
4種類のマネージャーがいますが、ランの管理人が``G4RunManagerFactory``クラスで、その他はビジュアライズ関係の管理人たちです。


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
G4double worldXY = 25*cm;
G4double worldZ = 50*cm;

// 形状
auto SWorld = new G4Box(
    "World",        // its name
    0.5 * worldXY,  // half x
    0.5 * worldXY,  // half y
    0.5 * worldZ,   // half z
)

// ロジカルボリューム
auto LVWorld = new G4LogicalVolume(
    SWorld, // its solid
    Air, // its material
    "World",   // its name
);

// 物理ボリューム
G4boolean checkOverlaps = true

G4Transform3D transform = G4Transform3D(
    G4RotationMatrix(),    // no rotation
    G4ThreeVector()        // at (0, 0, 0)
);
auto PVWorld = new G4PVPlacement(
    transform,
    LVWorld,       // its logical volume
    "World",          // its name
    nullptr,          // its mother volume
    false,            // no boolean operation
    0,                // copy number
    checkOverlaps     // check overlaps
);

return PVWorld;
```

``World``は実験室の部屋そのものみたいなものです。
この中に実験装置などを子ボリューム（daughter volume）として配置します。
すべてのボリュームの親に相当するため、親ボリューム（mother volume）は持ちません。

まず、``G4Box``を使って実験室の大きさを指定します。
長さ部分の引数には、実際の長さの半分の値を指定します。
これは、``G4Box``の中心を原点としてオブジェクトが作成されるためです。

次に``G4LogicalVolume``で実験室に空気を詰めます。
そして``G4PVPlacement``で実験室を配置します。
ここでは原点に配置しています。

### Envelopeの定義

```cpp

G4double envelopeXY = 20*cm
G4double envelopeZ = 30*cm

auto SEnvelope = new G4Box(
    "Envelope",
    0.5 * envelopeXY,
    0.5 * envelopeXY,
    0.5 * envelopeZ,
);

auto LVEnvelope = new G4LogicalVolume(
    SEnvelope,
    Water,
    "Envelope"
);

G4Transform3D transform = G4Transform3D(
    G4RotationMatrix(),    // no rotation
    G4ThreeVector()        // at (0, 0, 0)
);

new G4PVPlacement(
    transform,
    LVEnvelope,        // its logical volume
    "Envelope",        // its name
    LVWorld,           // its mother volume (logical volume)
    false,             // no boolean operation
    0,                 // copy number
    checkOverlaps
);
```

ビームを照射するエリアを定義します。
実験室と同じように``G4Box``で直方体の容器（``Envelope``）を作成し、
そこに水を満たし、実験室の原点に揃えて配置してあります。

### Shape1の定義

```cpp
// 円錐状のオブジェクト
auto SShape1 = G4Cons(
    "Shape1",
    ...
)

auto LVShape1 = new G4LogicalVolume(
    SShape1,
    Tissue,
    "Shape1",
);

G4ThreeVector position = G4ThreeVector(0, 2*cm, -7*cm);
G4RotationMatrix rotation = G4RotationMatrix();
G4Transform3D transform = G4Transform3D(rotation, position)
new G4PVPlacement(
    transform,
    LVShape1,
    "Shape1",
    LVEnvelope,
    false,
    0,
    checkOverlaps
);
```

``G4Cons``で作成された円錐状のオブジェクトが、水の入った容器に中に配置されています。

### Shape2の定義

```cpp
// 台形柱のオブジェクト
auto SShape2 = new G4Trd(
    "Shape2",
    ...
);

auto LVShape2 = new G4LogicalVolume(
    SShape2,
    Bone,
    "Shape2",
)

G4RotationMatix rotation = G4RotationMatix();
G4ThreeVector position = G4ThreeVector(0, -1*cm, 7*cm);
G4Transform3D transform = G4Transform3D(rotation, position);
new G4PVPlacement(
    transform,
    LVShape2,
    "Shape2",
    LVEnvelope,
    false,
    0,
    checkOverlaps
);
```

``G4Trd``で作成された台形柱状のオブジェクトが、水の入った容器の中に配置されています。

## 物理モデル

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
#include "QBBC.hh"

G4VModularPhysicsList *physicsList = new QBBC;
runManager->SetUserInitialization(physicsList)
```

``QBBC``というpre-defined packageを使っています。

## ユーザーアクション

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
#include "ActionInitialization.hh"

runManager->SetUserInitialization(new ActionInitialization());
```

ランマネージャーにユーザーアクションを追加します。
どのようなアクションが設定されるかは``ActionInitialization.hh/.cc``で確認します。

```cpp
//////////////////////////////////////////////////
// include/ActionInitialization.hh
//////////////////////////////////////////////////
#ifndef B1ActionInitialization_h
#define B1ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"

namespace B1 {
    class ActionInitialization : public G4VUserActionInitialization
    {
        public:
    }
}

#endif
```

```cpp
//////////////////////////////////////////////////
// src/ActionInitialization.cc
//////////////////////////////////////////////////

#include "ActionInitialization.hh"
#include "PrimaryGeneratorAction.hh"
#include "RunAction.hh"
#include "EventAction.hh"
#include "SteppingAction.hh"

void ActionInitialization::Build() const
{
    auto primaryGeneragorAction = new PrimaryGeneratorAction;
    setUserAction(primaryGeneratorAction);

    auto runAction = new RunAction;
    setUserAction(runAction);

    auto eventAction = new EventAction(runAction);
    setUserAction(eventAction);

    auto steppingAction = new SteppingAction(eventAction);
    setUserAction(steppingAction);
}
```

``ActionInitialization::Build``の中で、分割されたユーザー設定が順番に読み込まれていました。
