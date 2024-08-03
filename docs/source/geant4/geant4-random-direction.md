# 方向をランダムにしたい（``G4RandomDirection``）

```cpp
#include "G4RandomDirection.hh"

G4ThreeVector direction = G4RandomDirection{};
G4ThreeVector angle = G4RandomDirection{cosTheta};
```

``G4RandomDirection``で、ランダムな単位ベクトルを取得できます。
一様乱数（``G4UniformRand``）を使って、等方的に広がる3次元の方向ベクトルが生成されます。
生成されたベクトルは長さ1に正規化されています。

また、引数``cosTheta``を設定すると、
Z軸方向に対する$\cos \theta$の角度の範囲で方向ベクトルを生成できます。

## リファレンス

