# 入射方向を変更したい（``SetParticleMomentumDirection``）

```cpp
G4ThreeVector direction = G4ThreeVector(0., -1., 0.);
gun->SetParticleMomentumDirection(direction);
```

```SetParticleMomentumDirection``で入射方向を変更できます。
方向は（x, y, z）の単位ベクトルで指定します。
上のサンプルは鉛直下向きに入射しています。

:::{note}

Geant4の世界には重力がないと思うので、横から打っても、上から打っても同じだと思います。
ただ、ミューオンを上から入射したほうが、見た目的に宇宙線っぽくなります。

:::
