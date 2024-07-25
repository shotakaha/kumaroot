# 元素したい（``G4Material``）

```cpp
#include "G4Material.hh"
#include "G4Element.hh"

G4Element *N = new G4Element("Nitrogen", "N", z=7., a=14.01*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8., a=16.00*g/mole);

G4Material *Air = new G4Material("Air", density=1.29*mg/cm3, nelements=2);
Air->AddElement(N, 70.*perCent);
Air->AddElement(O, 30.*perCent);
```

NISTのデータベースにない物質も作れます。
``G4Material``、``G4Element``、``G4Isotope``などを使って自分で作成する必要があります。
上記のサンプルでは、酸素と窒素だけで構成された「空気」を作成してみました。

:::{note}

NISTのデータベースに``G4_AIR``があります。
窒素75.5%、酸素23.2%、アルゴン1%、炭素0.01%の構成となっています。
通常はこちらを使うのがよいと思います。

:::
