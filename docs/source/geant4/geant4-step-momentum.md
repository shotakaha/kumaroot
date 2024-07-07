# ステップ点の運動量をしりたい（``GetMomentum``）

```cpp
auto pre_step = aStep-GetPreStepPoint();
G4ThreeVector momentum = pre_step->GetMomentum();

G4debug << momentum << G4endl;
// (0.382287,0.161188,1.37889)

G4debug << G4BestUnit(momentum, "Energy") << G4endl;
// 0.382287 0.161188 1.37889 MeV
```

``GetMomentum``で運動量の合計を取得できます。

:::{note}

``G4BestUnit``のカテゴリーに運動量（``Momentum``）はありません。
単位のオーダーは同じになると思うので、``Energy``で代用しています。

:::

## ステップ点の運動方向をしりたい（``GetMomentumDirection``）

```cpp
auto pre_step = aStep-GetPreStepPoint();
G4ThreeVector direction = pre_step->GetMomentumDirection();

G4debug << direction << G4endl;
(0.265486,0.11194,0.957594)
```

``GetMomentumDirection``で運動量の単位ベクトル成分を取得できます。

:::{note}

あるイベントの、あるステップに対して
``GetMomentum``と
``GetMomentumDirection``で
得られた値を並べてみました。

```cpp
G4debug << momenum << G4endl;
// (0.382287,0.161188,1.37889)

G4debug << direction << G4endl;
// (0.265486,0.11194,0.957594)
```

それぞれの違いがいまいち分かっていません。

:::
