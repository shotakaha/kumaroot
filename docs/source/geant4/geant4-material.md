# マテリアルしたい（``G4NistManager``）

```cpp
#include "G4NistManager.hh"

G4NistManager *nistManager = new G4NistManager::GetPointer();
G4Element *H = nistManager->FindOrBuildElement("G4_H")
G4Element *O = nistManager->FindOrBuildElement("G4_O")
```

G4NistManagerを使って、NISTの材料データベースにある元素や化合物などのマテリアルを作成できます。

利用可能なマテリアル名は[Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)を参照してください。
素粒子・原子核実験でよく利用するような材料（``G4_lXe``、``G4_PbWO4``、``G4_STAINLESS-STEEL``、``G4_Galactic``（＝真空））も定義されています。

## カスタマイズしたい（``G4Material`` / ``G4Element``）

```cpp
#include "G4Material.hh"
#include "G4Element.hh"

G4Element *N = new G4Element("Nitrogen", "N", z=7., a=14.01*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8., a=16.00*g/mole);

G4Material *Air = new G4Material("Air", density=1.29*mg/cm3, nelements=2);
Air->AddElement(N, 70.*perCent);
Air->AddElement(O, 30.*perCent);
```

マテリアルはカスタマイズできます。
NISTのデータベースにない材料を使う場合は``G4Material``、``G4Element``、``G4Isotope``などを使って自分で作成する必要があります。
上記のサンプルでは、酸素と窒素だけで構成された「空気」を作成してみました。

:::{note}

NISTのデータベースに``G4_Air``があります。
窒素75.5%、酸素23.2%、アルゴン1%、炭素0.01%の構成となっています。
通常はこちらを使うのがよいと思います。

:::

```{toctree}
---
maxdepth: 1
---
geant4-water
geant4-air
geant4-acrylic
geant4-glass
```
