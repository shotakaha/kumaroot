# 空気を作りたい（``G4_AIR``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *air = nm->FindOrBuildMaterial("G4_AIR")
```

``G4_AIR``でNISTデータにある空気を生成できます。
炭素C（0.000124）、窒素N（0.755268）、酸素O（0.231781）、アルゴンAr（0.012827）が含まれています。

## カスタマイズしたい

```cpp
G4double a, z, density;
G4int nelements;

G4Element *N = new G4Element("Nitrogen", "N", z=7, a=14.01*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=16.00*g/mole);
G4Material *Air = new G4Material("Air", density=1.290*mg/cm3, nelements=2);
Air->AddElement(N, 70.*perCent);
Air->AddElement(O, 30.*perCent);
```

自分のプロジェクトで使っていた空気です。
``G4Element``と``G4Material``を使って、窒素Nと酸素Oだけで作ってありました。

:::{note}

この空気の組成はユーザーガイドの[Define a Mixture by Fractional Mass](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/materialDef.html#define-a-mixture-by-fractional-mass)から取ってきたもののようです。

:::
