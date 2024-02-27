# 水を作りたい（``G4_WATER``）

```cpp
G4NistManager *nist = G4NistManager::Instance()
G4Material Water = nist->FindOrBuildMaterial("G4_WATER")
```

``G4_WATER``でNISTデータにある水を生成できます。

## カスタマイズしたい

```cpp
G4double a, z, density;
G4int nelements;

G4Element *H = new G4Element("Hydrogen", "H", z=1, a=1.00794*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.9994*g/mole);
G4Material *Water = new G4Material("Water", density=1.0*g/cm3, nelements=2);
Water->AddElement(H, 2);
Water->AddElement(O, 1);
```

``G4Element``と``G4Material``を使ってカスタマイズした水を生成できます。
質量数や密度は適切な文献を参照してください。
