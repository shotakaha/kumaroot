# 入射位置したい（`SetParticlePosition`）

```cpp
#include "G4SystemOfUnits.hh"

G4ThreeVector position(0. * cm, 0. * cm, -10. * cm);
fParticleGun->SetParticlePosition(position);
```

```cfg
/gun/position 0 0 -10 cm
```

`SetParticlePosition`で入射位置を変更できます。
座標は`G4ThreeVector`で設定します。
単位を付けないと、Geant4の内部単位（mm）として扱われます。
マクロの`/gun/position`もこの位置を設定します。デフォルトの単位は`cm`です。

:::{caution}

入射位置は、ワールド体積の内側にある必要があります。
:::

このサンプルはコンストラクタで設定しているため、全イベントで同じ位置から入射します。
イベントごとに位置を変えたい場合は、`GeneratePrimaries`の中で`SetParticlePosition`を呼び出します（[](geant4-source-particlegun)）。

:::{seealso}

- [G4ParticleGun](https://geant4.kek.jp/Reference/11.4.0/classG4ParticleGun.html)

:::
