# 実験室を作りたい（``World``）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4VPhysicalVolume.hh"
#include "G4NistManager.hh"

// 実験室の大きさ
G4Double fWorldX = 50.*m;
G4Double fWorldY = 50.*m;
G4Double fWorldZ = 50.*m;

// 実験室の形を決める
G4double width, length, height;
G4Box *fWorldS = new G4Box(
    "WorldS",
    width=0.5*fWorldX,
    length=0.5*fWorldY,
    height=0.5*fWorldZ)

// 実験室の材質を決める
G4NistManager *fNist = new G4NistManager::Instance();
G4Material *fAir = fNist->FindOrBuildMaterial("G4_AIR");
G4LogicalVolume *fWorldL = new G4LogicalVolume(
    fWorldS,  // G4VSolid    形状
    fAir,     // G4Material  物質
    "WorldL"  // G4String
)

// 実験室の置き場所を決める
G4RotationMatrix rotation = G4RotationMatrix();  // no rotation
G4ThreeVector direction = G4ThreeVector(0., 0., 0.);  // at (0, 0, 0)
G4Transform3D location = G4Transform3D(rotation, direction)

G4VPhysicalVolume *fWorldP = new G4PVPlacement(
    location,    // G4Transform3D
    fWorldL,     // G4LogicalVolume
    "WorldP",    // G4String
    0,           // G4LogicalVolume: 親ボリュームはなし
    false,       // G4bool pMany（廃止）
    0,           // G4int pCopyNo
    True         // G4bool check overlaps
)
```

測定器シミュレーションを実行する実験室（通称：World）を作成しました。
実験室は50m立方の箱型としました。
どうしてこの大きさにしたかというと、この中にスーパーカミオカンデを配置してみたいからです。

まず、実験室の形を決めます。
箱型の実験室なので``G4Box``を使いました。
``G4Box``のサイズに関係する引数はすべて**半分の長さ**で指定することになっているので0.5倍してあります。

次に実験室の材質を決めます。
地球にある実験室なので空気で満たしました。

最後に、置き場所を決めます。
これで、最上位の親ボリュームである実験室の完成です。
あとは、測定装置をこの中に納まるように並べるだけです。

:::{note}

Geant4では生成された粒子が「実験室の外側に飛び出す」か「運動量がゼロになる」まで、素粒子反応が繰り返されます。なので、ある程度の外枠を定義しておかないと、必要のない計算にまで時間をかけてしまうことになります。

:::
