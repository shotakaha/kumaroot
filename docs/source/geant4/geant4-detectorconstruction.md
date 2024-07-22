# 測定器したい（``G4VUserDetectorConstruction``）

測定器の構造を定義するクラスは、必須クラスのひとつで、
``G4VUserDetectorConstruction``クラスを継承して作成します。
``G4VUserDetectorConstruction::Construct``が純粋仮想関数になっていて、
測定器を建設する作業はこの関数をオーバーライドして実装します。

ここではクラス名を``DetectorConstruction``としました。
また、必要な論理物体（G4LogicalVolume）を作成する関数も用意しました。

:::{hint}

付属サンプルの多くは``Construct()``関数の中で、必要な構造体をまとめて定義しています。これは、可読性＆カスタマイズ性がよくないと感じます。
個人的には測定器の構成要素ごとに論理物体を返す関数にするとよいと思います。

:::

## メイン関数

```cpp
#include "DetectorConstruction.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto detector = new DetectorConstruction{};
    rm->SetUserInitialization(detector);

}
```

メイン関数では、
``DetectorConstruction``のインスタンスを作成し、
``SetUserInitialization``でRunManagerに追加します。

## ヘッダーファイル

```cpp
// //////////////////////////////////////////////////
// include/DetectorConstruction.hh
// //////////////////////////////////////////////////

#include "G4VUserDetectorConstruction.hh"
#include "G4LogicalVolume.hh"
#include "G4SystemOfUnits.hh"

namespace 名前空間
{

class DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        DetectorConstruction();
        ~DetectorConstruction();
        G4PhysicalVolume* Construct();

        // サブ関数（オプション）
        G4LogicalVolume* CreateWorldVolume(const G4String &pName);
        G4LogicalVolume* CreateDetectorVolume(const G4String &pName);
        G4LogicalVolume* CreateSubDetectorVolume(const G4String &pName);

    private:
        // ワールドの大きさ
        G4double fWorldX = 15. * cm;
        G4double fWorldY = 15. * cm;
        G4double fWorldZ = 15. * cm;

        // 測定器の大きさ
        G4double fDetectorX = 5. * cm;
        G4double fDetectorY = 5. * cm;
        G4double fDetectorZ = 5. * cm;
}
} // 名前空間
```

:::{hint}

測定器のサイズはプライベート変数で定義しました。
すでに大きさが決まっている場合は、ソースにハードコードして
しまっても問題ないと思います。

:::

## ソースファイル

```cpp
// //////////////////////////////////////////////////
// src/DetectorConstruction.cc
// //////////////////////////////////////////////////

#include "DetectorConstruction.hh"

namespace 名前空間
{
// //////////////////////////////////////////////////
// コンストラクター
// //////////////////////////////////////////////////
DetectorConstruction::DetectorConstruction()
{

}

// //////////////////////////////////////////////////
// デストラクター
// //////////////////////////////////////////////////
DetectorConstruction::~DetectorConstruction()
{

}

// //////////////////////////////////////////////////
// 論理物体を準備する関数（オプション）
// //////////////////////////////////////////////////
G4LogicalVolume* DetectorConstruction::DefineWorldVolume(const G4String &name){...};
G4LogicalVolume* DetectorConstruction::DefineDetectorVolume(const G4String &name){...};
G4LogicalVolume* DetectorConstruction::DefineSubDetectorVolume(const G4String &name){...};

// //////////////////////////////////////////////////
// 測定器の建設に実装が必要な関数
// //////////////////////////////////////////////////
G4VPhysicalVolume *DetectorConstruction::Construct()
{
    // 論理物体を取得する
    auto worldLogical = DefineWorldVolume("world");
    auto detectorLogical = DefineDetectorVolume("detector");

    // ワールドを配置する
    G4Transform3D location = G4Transform3D(nullptr, nullptr);
    G4VPhysicalVolume *world = new G4PVPlacement(
        location,
        worldLogical,    // G4LogicalVolume: 配置する論理物体
        "worldPhysical",
        nullptr,         // G4LogicalVolume: 親となる論理物体
        ...);

    // 測定器を配置する
    G4Transform3D location = G4Transform3D(nullptr, nullptr);
    new G4PVPlacement(
        location,
        detectorLogical,  // G4LogicalVolume: 配置する論理物体
        "detectorP",
        worldLogical,     // G4LogicalVolume: 親となる論理物体
        ...);

    return world;
}

} // 名前空間
```

:::{seealso}

- [](./geant4-pvplacement.md)
- [](./geant4-pvreplica.md)
- [](./geant4-world.md)

:::



## リファレンス

- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)
