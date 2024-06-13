# 水を作りたい（``G4_WATER``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *water = nm->FindOrBuildMaterial("G4_WATER")
```

``G4_WATER``でNISTデータにある水を生成できます。

## 水蒸気したい（``GA_WATER_VAPOR``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *vapor = nm->FindOrBuildMaterial("G4_WATER_VAPOR")
```

``G4_WATER_VAPOR``で水蒸気を生成できます。
密度が ``0.000756182*g/cm3``に設定された水です。

## カスタマイズしたい

```cpp
G4double a, z, density;
G4int nelements;

G4Element *H = new G4Element("Hydrogen", "H", z=1, a=1.00794*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.9994*g/mole);
G4Material *fWater = new G4Material("Water", density=1.0*g/cm3, nelements=2);
Water->AddElement(H, 2);
Water->AddElement(O, 1);
```

``G4Element``と``G4Material``を使ってカスタマイズした水を生成できます。
質量数や密度は適切な文献を参照してください。

## 光学特性したい

```cpp
const G4int entries = 35;

// Optical Photonのエネルギー
G4double photon_energy[entries] = {
    2.034*eV, 2.068*eV, 2.103*eV, 2.139*eV,
    2.177*eV, 2.216*eV, 2.256*eV, 2.298*eV,
    2.341*eV, 2.386*eV, 2.433*eV, 2.481*eV,
    2.532*eV, 2.585*eV, 2.640*eV, 2.697*eV,
    2.757*eV, 2.820*eV, 2.885*eV, 2.954*eV,
    3.026*eV, 3.102*eV, 3.181*eV, 3.265*eV,
    3.353*eV, 3.446*eV, 3.545*eV, 3.649*eV,
    3.760*eV, 3.877*eV, 4.002*eV, 4.136*eV,
    4.275*eV, 4.427*eV, 4.591*eV
    };

// エネルギーごとの反射率
G4double refractive_index[entries] = {
    1.3435, 1.344,  1.3445, 1.345,  1.3455,
    1.346,  1.3465, 1.347,  1.3475, 1.348,
    1.3485, 1.3492, 1.35,   1.3505, 1.351,
    1.3518, 1.3522, 1.3530, 1.3535, 1.354,
    1.3545, 1.355,  1.3555, 1.356,  1.3568,
    1.3572, 1.358,  1.3585, 1.359,  1.3595,
    1.36,   1.3608, 1.3608, 1.3608, 1.3608
    };

// エネルギーごとの吸収長
G4double absorption_length[nEntries] = {
    3.448*m,  4.082*m,  6.329*m,  9.174*m, 12.346*m, 13.889*m,
    15.152*m, 17.241*m, 18.868*m, 20.000*m, 26.316*m, 35.714*m,
    45.455*m, 47.619*m, 52.632*m, 52.632*m, 55.556*m, 52.632*m,
    52.632*m, 47.619*m, 45.455*m, 41.667*m, 37.037*m, 33.333*m,
    30.000*m, 28.500*m, 27.000*m, 24.500*m, 22.000*m, 19.500*m,
    17.500*m, 14.500*m, 14.500*m, 14.500*m, 14.500*m
    };

// AddConstProperty(キー, 特性値, 数）
// AddProperty(キー, 光子のエネルギー, 特性値, 数）
G4MaterialPropertiesTable *mpt = new G4MaterialPropertiesTable();
mpt->AddProperty("RINDEX", photon_energy, refractive_index, entries);
mpt->AddProperty("ABSLENGTH", photon_energy, absorption_length, entries);
fWater->SetMaterialPropertiesTable(mpt)
```

[G4MaterialPropetiesTable](https://geant4.kek.jp/Reference/11.2.0/classG4MaterialPropertiesTable.html)で、材料の特性を追加できます。
G4Material自体は材料の特性を持たないため、自分で追加する必要があります。
光子の波長（を変換したエネルギー）ごとの屈折率と吸収長は、文献値を参考にしたり、自分で測定したりして定義します。
