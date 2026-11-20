# 入射運動量したい（`SetParticleMomentum`）

```cpp
#include "G4SystemOfUnits.hh"

fParticleGun->SetParticleMomentum(400 * MeV);
```

```cfg
/gun/momentumAmp 400 MeV
```

`SetParticleMomentum`で入射粒子の運動量（MeV/c）を変更できます。
マクロの`/gun/momentumAmp`も同じ運動量の大きさを設定します。
`/gun/momentum`は運動量ベクトル（px py pz）を受け取る別のコマンドです。

運動エネルギーは、次の条件で決まります。

- 粒子の種類を設定済みの場合、質量を考慮した運動エネルギー（`sqrt(p²+m²)−m`）が設定されます。
- 粒子の種類が未設定の場合、質量は0とみなされ、運動量の値がそのままエネルギーとして設定されます。
- 運動エネルギーをすでに設定していた場合は、警告メッセージが出力されて、運動量で上書きされます。
