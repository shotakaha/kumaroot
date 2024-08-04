# マテリアルのプロパティしたい（``G4MaterialPropertiesTable``）

```cpp
// 素材：水（G4_WATER）
G4NistManager *nm = new G4NistManager::GetInstance();
G4Material *material = nm->FindOrBuildMaterial("G4_WATER");


// プロパティを設定（水のpre-defined値を使用）
G4MaterialPropertiesTable *mpt = new G4MaterialPropertiesTable();
mpt->AddProperty("RINDEX", "Water");

material->SetMaterialPropertiesTable(table);
```

OpticalPhysicsの物理プロセスを使う場合、
素材の屈折率（``RINDEX``）や
吸収長（``ABSLENGTH``）などの性質をユーザーが設定する必要があります。
それぞれの物理プロセスで必要なパラメーターの設定は
[Configuration - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html#configuration)を参照してください。

なお、Geant v11.0 から
``Air``（空気）、
``Water``（水）、
``PMMA``（アクリル樹脂／ポリメタクリル酸メチル）、
``Fused Silica``（石英ガラス）
に対して屈折率のpre-defined値が追加されています。

## チェレンコフ光したい

```cpp
property->AddProperty("RINDEX", photon_energy, refractive_index, n_entries);
property->AddProperty("ABSLENGTH", photon_energy, absorption, n_entries);
```

## シンチレーション光したい

```cpp
G4Material *material = new G4Material{
    "LXe",
    54.,                // z
    131.29 * g / mole,  // a
    3.020 * g / cm3     // density
};

std::vector<G4double> photon_energy = { 7.0 * eV, 7.07 * eV, 7.14 * eV };
std::vector<G4double> scintillation = { 0.1, 1.0, 0.1 };
std::vector<G4double> refractive_index  = { 1.59, 1.57, 1.54 };
std::vector<G4double> absorption_length  = { 35. * cm, 35. * cm, 35. * cm };

G4MaterialPropertiesTable *property = new G4MaterialPropertiesTable();
// 波長に依存するプロパティ
property->AddProperty("RINDEX", photon_energy, refractive_index);
property->AddProperty("ABSLENGTH", photon_energy, absorption_length);
property->AddProperty("SCINTILLATIONCOMPONENT1", photon_energy, scintillation);
property->AddProperty("SCINTILLATIONCOMPONENT2", photon_energy, scintillation);

// 波長に依存しないプロパティ
property->AddConstProperty("RESOLUTIONSCALE", 1.0);
property->AddConstProperty("SCINTILLATIONYIELD", 12000. / MeV);
property->AddConstProperty("SCINTILLATIONTIMECONSTANT1", 20. * ns);
property->AddConstProperty("SCINTILLATIONTIMECONSTANT2", 45. * ns);
property->AddConstProperty("SCINTILLATIONYIELD1", 1.0);
property->AddConstProperty("SCINTILLATIONYIELD2", 0.0);

// 物質にプロパティを設定
material->SetMaterialPropertiesTable(property);
```

``examples/extended/optical/LXe/``のサンプルを参照しました。
屈折率と吸収長の他に、シンチレーション光のプロパティ（光量や時定数）をいくつか設定しています。
シンチレーション光は2種類設定できるようです。

- [](./geant4-physics-scintillation.md)

## OpticalSurfaceしたい

```cpp
G4OpticalSurface surface = new G4OpticalSurface("Surface");
surface->SetType(dielectric_dielectric);
surface->SetFinish(ground);  // rough surface
surface->SetModel(unified);  // UNIFIED model
surface->SetMaterialPropertiesTable(表面のプロパティ);
```

## リファレンス

- [Material Properties Table](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html)
- [RefractiveIndex Database](https://refractiveindex.info/)
