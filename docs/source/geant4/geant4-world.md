# 実験室を作りたい

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PhysicalVolume.hh"
#include "G4NistManager"

G4Double pX = 50.*m;
G4Double pY = 50.*m;
G4Double pZ = 50.*m;
G4Box *SWorld = new G4Box(
    "World",
    0.5*pX,
    0.5*pY,
    0.5*pZ)

G4LogicalVolume *LVWorld = new G4LogicalVolume(
    SWorld,  // G4VSolid
    Air,     // G4Material: 「空気（Air）」は先に作っておく
    "World"  // G4String
)

G4bool checkOverlaps = true;

G4RotationMatrix rotation = G4RotationMatrix()
G4ThreeVector direction = G4ThreeVector(0., 0., 0.)
G4Transform3D location = G4Transform3D(rotation, direction)

G4VPhysicalVolume *PVWorld = new G4PVPlacement(
    location,    // G4Transform3D
    LVWorld,     // G4LogicalVolume
    "World",     // G4String
    0,           // G4LogicalVolume: 親ボリュームはなし
    false,       // G4bool pMany（廃止）
    0,           // G4int pCopyNo
    checkOverlaps,
)
```

測定器シミュレーションを実行する実験室（通称：World）を作成しました。

まず、実験室の形（ソリッド）を作成します。
独自ルールとして、変数名に``S*``を付けることにしました。
この実験室は``G4Box``を使って、50mx50mx50mのサイズで作ってあります。
``G4Box``のサイズに関係する引数はすべて半分の長さで指定することになっているので0.5倍してあります。
どうして巨大な実験室にしたかというと、この中にスーパーカミオカンデを配置してみたいからです。

ソリッドの形状を決めたら、ロジカルボリュームを作成します。
独自ルールとして、変数名に``LV*``を付けることにしました。
地球にある実験室なので空気で満たしておきました。

最後に、ロジカルボリュームを配置して物理ボリュームを作成します。
独自ルールとして、変数名に``PV*``を付けることにしました。

このあとは``PVWorld``オブジェクトを最上位の親ボリュームとして、
測定器のロジカルボリュームをこの中に納まるように配置していくことになります。

:::{note}

Geant4では生成された粒子が「実験室の外側に飛び出す」か「運動量がゼロになる」まで、素粒子反応が繰り返されます。なので、ある程度の外枠を定義しておかないと、必要のない計算にまで時間をかけてしまうことになります。

:::
