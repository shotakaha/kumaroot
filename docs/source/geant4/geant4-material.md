# 材料を調達したい（``G4NistManager``）

```cpp
#include "G4NistManager.hh"

G4NistManager *nistManager = new G4NistManager::GetInstance();

G4Element *H = nistManager->FindOrBuildElement("G4_H")
G4Element *O = nistManager->FindOrBuildElement("G4_O")

G4Material *H2O = nistManager->FindOrBuildMaterial("G4_WATER")
G4Material *Air = nistManager->FindOrBuildMaterial("G4_AIR")
```

``G4NistManager``を使って、NISTの材料データベースにある元素や化合物などを調達できます。
元素（``G4Element``）が欲しい時は``FindOrBuildElement``メソッド、
物質（``G4Material``）が欲しい時は``FindOrBuildElement``メソッドを使います。

利用可能なマテリアル名は[Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)を参照してください。

水素（``G4_H``）からカリフォルニウムまでの元素や、
水（``G4_WATER``）、空気（``G4_AIR``）、
素粒子・原子核実験でよく利用するような材料（``G4_lXe``、``G4_PbWO4``、``G4_STAINLESS-STEEL``、``G4_Galactic``（＝真空））なども定義されています。

一般的な物質が欲しい場合は、まずこのリストから探すのがよいと思います。

## 特殊な材料を調達したい（``BuildMaterialWithNewDensity``）

```cpp
auto nistManager = G4NistManager::Instance();
nistManager->FindOrBuildMaterial("G4_Ar");  // density = 1.66201 mg/cm3
G4double density = 1.782 * mg/cm3;
nistManager->BuildMaterialWithNewDensity("Ar_heavy", "G4_Ar", density);
```

``G4NistManager::BuildMaterialWithNewDensity``メソッドで、NISTの材料データベースを基にしながら、密度などを変更できます。

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





