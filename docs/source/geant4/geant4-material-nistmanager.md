# 定義済みのマテリアルを使いたい（``G4NistManager::Instance``）

```cpp
#include "G4NistManager.hh"

G4NistManager *nm = new G4NistManager::GetInstance();

G4Element *H = nm->FindOrBuildElement("G4_H")
G4Element *O = nm->FindOrBuildElement("G4_O")

G4Material *H2O = nm->FindOrBuildMaterial("G4_WATER")
G4Material *Air = nm->FindOrBuildMaterial("G4_AIR")
```

いろいろな元素や化合物の基本的な特性は、
NISTの材料データベースに整理されています。
``G4NistManager``で、この材料データベースから材料を取り寄せることができます。

## 物質取り寄せたい（``G4NistManager::FindOrBuildMaterial``）

``FindOrBuildMaterial``で物質（``G4Material``）を取得できます。
利用可能なマテリアル名は[Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)を参照してください。

水（``G4_WATER``）、
空気（``G4_AIR``）、
素粒子・原子核実験でよく利用するような材料（``G4_lXe``、``G4_PbWO4``、``G4_STAINLESS-STEEL``、``G4_Galactic``（＝真空））なども定義されています。

一般的な物質が欲しい場合は、まずこのデータベースから探すのがよいと思います。

## 元素を取り寄せたい（``G4NistManager::FindOrBuildElement``）

```cpp
G4NistManager *nm = new G4NistManager::GetInstance();
G4Element *H = nm->FindOrBuildElement("G4_H")
G4Element *O = nm->FindOrBuildElement("G4_O")
```

``FindOrBuildElement``メソッドで
元素（``G4Element``）を取得できます。
水素（``G4_H``）からカリフォルニウムまでの元素が登録されています。

## 特殊な材料を調達したい（``G4NistManager::BuildMaterialWithNewDensity``）

```cpp
auto nm = G4NistManager::Instance();
nm->FindOrBuildMaterial("G4_Ar");  // density = 1.66201 mg/cm3
G4double density = 1.782 * mg/cm3;
nm->BuildMaterialWithNewDensity("Ar_heavy", "G4_Ar", density);
```

``BuildMaterialWithNewDensity``メソッドで、NISTの材料データベースを基にしながら、密度などを変更できます。

## 一括で調達したい

[付属サンプルB5のDetectorConstruction](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/DetectorConstruction.cc)では``ConstructMaterials()``関数を作成し、利用する材料を一括して調達しています。
それを``DetectorConstruction::Construct()``の中で呼び出し、ジオメトリを作成するときは``G4Material::GetMaterial("材料名")``で作成しています。

これはそのまま真似するとよいなと思ったので、関連するソースを抜粋してみました。

```cpp
// \file プロジェクト名/include/DetectorConstruction.hh
// \brief Definition of the プロジェクト名::DetectorConstruction class

#ifndef プロジェクト名_DetectorConstruction_h
#define プロジェクト名_DetectorConstruction_h 1

// 必要なG4ヘッダーをインクルードする

namespace プロジェクト名
{
    class DetectorConstruction : public G4VUserDetectorConstruction
    {
        public:
            G4PhysicalVolume* Construct() override;
            void ConstructMaterials();
    }
}

#endif
```

```cpp
// \file プロジェクト名/src/DetectorConstruction.cc
// \brief Implementation of the プロジェクト名::DetectorConstruction class

#include "DetectorConstruction.hh"

// 必要なG4ヘッダーをインクルードする

namespace プロジェクト名
{
    G4VPhysicalVolume* DetectorConstruction::Construct()
    {
        ConstructMaterials();  // <-- 材料を一括で調達
        auto air = G4Material::GetMaterial("G4_AIR");

        // 検出器のジオメトリを定義する
        auto worldSolid = new G4Box(...);
        auto worldLogical = new G4LogicalVolume(...);
        auto worldPhysical = new G4PVPlacement(...);

        // 最後はワールドをリターンする
        return worldPhysical;
    }

    void DetectorConstruction::ConstructMaterials()
    {
        auto nistManager = G4NistManager::Instance();
        // Air
        nistManager->FindOrBuildMaterial("G4_AIR");
        // Water
        nistManager->FindOrBuildMaterial("G4_WATER");
        // Vacuum (Galactic)
        nistManager->FindOrBuildMaterial("G4_Galactic");
        // Vacuum (Air with low density)
        auto air = G4Material::GetMaterial("G4_AIR");
        G4double density = 1.0e-5 * air->GetDensity();
        nistManager->BuildMaterialWithNewDensity("AIR_LOW", "G4_AIR", density);

        G4cout << G4endl << "The materials defined are : " << G4endl << G4endl;
        G4cout << *(G4Material::GetMaterialTable()) << G4endl;
    }
}
```
