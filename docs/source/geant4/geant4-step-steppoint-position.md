# ステップ点の座標をしりたい（``G4StepPoint::GetPosition``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4ThreeVector position = pre_step->GetPosition();

G4debug << position << G4endl;
// (2.83459,1.19586,5)

G4debug << G4BestUnit{position, "Length"} << G4endl;
// 2.83459 1.19586 0.5 cm
```

ステップの位置を取得できます。
この座標は**世界座標**と呼ぶようで、ワールドボリュームの中心が原点になっています。

:::{note}

座標は``G4ThreeVector``クラスのオブジェクトですが、そのまま単位操作できました。

```cpp
// メートルに変換
G4debug << position / m << G4endl;
// (0.0283459,0.0119586,0.005)
```

:::

## 中点にしたい

```cpp
auto pre_step = aStep->GetPreStepPoint();
auto post_step = aStep->GetPostStepPoint();

G4ThreeVector position = pre_step->GetPosition() + post_step->GetPosition();
position /= 2.;
```

ステップの中点を、粒子の座標としたい場合の計算方法です。
始点と終点の座標を取得し、2で割っています。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4ThreeVector](https://geant4.kek.jp/Reference/11.2.0/classCLHEP_1_1Hep3Vector.html)

:::
