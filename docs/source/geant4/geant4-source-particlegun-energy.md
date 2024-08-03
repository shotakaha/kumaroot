# 入射エネルギーしたい（``SetParticleEnergy``）

```cpp
G4double energy = 400 * MeV;
gun->SetParticleEnergy(energy);
```

``SetParticleEnergy``で入射粒子のエネルギーを変更できます。
運動量をすでに設定していた場合は0に変更されるようです。
