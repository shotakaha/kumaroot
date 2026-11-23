# 入射エネルギーしたい（`SetParticleEnergy`）

```cpp
#include "G4SystemOfUnits.hh"

G4double energy = 400 * MeV;
fParticleGun->SetParticleEnergy(energy);
```

```cfg
/gun/energy 400 MeV
```

`SetParticleEnergy`で入射粒子の運動エネルギーを変更できます。
マクロの`/gun/energy`も同じ設定です。
運動量をすでに設定していた場合は0にリセットされ、警告メッセージが出力されます。

:::{seealso}

- [G4ParticleGun](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleGun.html)

:::
