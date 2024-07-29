# ステップポイントのタッチャブルしたい（``G4StepPoint::GetTouchableHandle``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();

auto aTouch = pre_step->GetTouchableHandle();
auto aNextTouch = pre_step->GetNextTouchableHandle();
```

``GetTouchableHandle``で、現在のステップポイントの物理ボリュームにアクセスできるようになります。
具体的な使い方は[](./geant4-touchable.md)に整理しました。

:::{seealso}

- [](./geant4-step-steppoint-volume.md)

:::
