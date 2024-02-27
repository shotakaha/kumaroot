# 空気を作りたい（``G4_AIR``）

```cpp
G4NistManager *nist = G4NistManager::Instance()
G4Material Air = nist->FindOrBuildMaterial("G4_AIR")
```

``G4_AIR``でNISTデータにある空気を生成できます。
炭素C（0.000124）、窒素N（0.755268）、酸素O（0.231781）、アルゴンAr（0.012827）が含まれています。

## カスタマイズしたい

```cpp
G4double a, z, density;
G4int nelements;

G4Element *N = new G4Element("Nitrogen", "N", z=7, a=14.0067*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.9994*g/mole);
G4Material *Air = new G4Material("Air", density=1.29*g/cm3, nelements=2);
Air->AddElement(N, 70.*perCent);
Air->AddElement(O, 30.*perCent);
```

``G4Element``と``G4Material``を使ってカスタマイズした空気を生成できます。
窒素Nと酸素Oだけが含まれた空気を作ってみました。
