# 入射位置したい（``SetParticlePosition``）

```cpp
position = G4ThreeVector(x0, y0, z0);
gun->SetParticlePosition(position);
```

``SetParticlePosition``で入射位置を変更できます。
座標は``G4ThreeVector``で設定します。
