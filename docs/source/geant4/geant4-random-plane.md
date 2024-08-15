# 位置をランダムにした（``G4PlaneVectorRandom``）

```cpp
#include "G4RandomTools.hh"

G4ThreeVector normal{0., 0., 1.};
G4ThreeVector position = G4PlaneVectorRandom(normal);
```

法線ベクトル（``normal``）に垂直な平面上に、一様に広がるベクトルを生成します。

## リファレンス

クラスリファレンスで検索できなかったため、
インストールされたヘッダーファイルを確認しました。

- ``${geant4-config --prefix}/include/Geant4/G4RandomTools.hh``
