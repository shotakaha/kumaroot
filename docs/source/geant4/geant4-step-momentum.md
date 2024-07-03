# ステップ点の運動量をしりたい（``GetMomentum``）

```cpp
auto pre_step = aStep-GetPreStepPoint();
G4ThreeVector momentum = pre_step->GetMomentum();
```

``GetMomentum``で運動量の合計を取得できます。

## ステップ点の運動方向をしりたい（``GetMomentum``）

```cpp
auto pre_step = aStep-GetPreStepPoint();
G4ThreeVector direction = pre_step->GetMomentumDirection();
```

``GetMomentumDirection``で運動量の単位ベクトル成分を取得できます。
