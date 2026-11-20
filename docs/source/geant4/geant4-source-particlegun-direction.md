# 入射方向したい（`SetParticleMomentumDirection`）

```cpp
G4ThreeVector direction = G4ThreeVector(0., -1., 0.);
fParticleGun->SetParticleMomentumDirection(direction);
```

```cfg
/gun/direction 0 -1 0
```

`SetParticleMomentumDirection`で入射方向を変更できます。
方向は（x, y, z）で指定します。大きさは問わず、内部で単位ベクトルに正規化されます。
上のサンプルは−y方向に入射しています。
マクロの`/gun/direction`も同じ方向を設定します。

:::{note}

重力場を設定していなければ、Geant4では標準では重力は考慮されません。
そのため、横から打っても、上から打っても同じ結果になります。
ただ、ミューオンを上から入射したほうが、見た目的に宇宙線っぽくなります。

:::

## ランダムに入射したい

```cpp
#include "G4RandomDirection.hh"

G4ThreeVector direction = G4RandomDirection();
fParticleGun->SetParticleMomentumDirection(direction);
```

`G4RandomDirection`で、どの向きも同じ確率の（等方的な）単位ベクトルを取得できます。

:::{seealso}

[](geant4-random-direction)

:::
