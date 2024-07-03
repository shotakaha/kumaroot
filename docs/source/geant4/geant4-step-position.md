# ステップ点の座標をしりたい（``GetPosition``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4ThreeVector position = pre_step->GetPosition();
```

ステップの位置を取得できます。
この座標は**世界座標**と呼ぶようで、ワールドボリュームの中心が原点になっています。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4ThreeVector](https://geant4.kek.jp/Reference/11.2.0/classCLHEP_1_1Hep3Vector.html)

:::
