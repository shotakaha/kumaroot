# 方向をランダムにしたい（``G4RandomDirection``）

```cpp
#include "G4RandomDirection.hh"

// 球面一様分布
G4ThreeVector direction = G4RandomDirection{};

// z方向の角度を指定
G4ThreeVector direction = G4RandomDirection{cosTheta};
```

``G4RandomDirection``で、ランダムな方向ベクトルを取得できます。

2種類のシグネチャを持っています。
``G4RandomDirection{}``は、球面一様分布を生成し、x、y、z方向に等方的に広がるベクトルを取得できます。

``G4RandomDirection{cosTheta}``は、Z軸方向の角度の広がり方を$\cos \theta$で指定して、範囲を限定したベクトルを取得できます。

## リファレンス

クラスリファレンスで検索できなかったため、
インストールされたヘッダーファイルを確認しました。

- ``${geant4-config --prefix}/include/Geant4/G4RandomDirection.hh``
