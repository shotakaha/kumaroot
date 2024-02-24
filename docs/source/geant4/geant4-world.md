# 実験室を作りたい（``G4Box``）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager"


G4Material *Air = // G4_Airを取得

G4Double pX = 10.*meter;
G4Double pY = 10.*meter;
G4Double pZ = 10.*meter;
G4Box *world = new G4Box("World", pX, pY, pZ)

G4LogicalVolume *hall = new G4LogicalVolume(world, Air, "World", 0, 0)
```

実験室を10mx10mx10mの大きさで作ってみました。
地球上の実験室なので空気で満たしてあります。
測定器などはこの実験室の中に納まるように追加します。

:::{note}

外枠を定義しないと、測定器から飛び出した粒子がどこまでもシミューレートされてしまうため、測定器の外側の広さをあらかじめ定義する必要があります。
（たしか、こんな理由だったはず）

:::
