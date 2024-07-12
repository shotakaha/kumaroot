# ランダムに入射したい（``G4RandomDirection``）

```cpp
G4ThreeVector direction = G4RandomDirection{};
particle->SetParticleMomentumDirection(direction);
```

``G4RandomDirection``で、ランダムな単位ベクトルを取得できます。
