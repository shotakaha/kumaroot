# ステップの二次粒子数をしりたい（``G4Step::GetNumberOfSecondariesInCurrentStep``）

```cpp
// G4Step *aStep
G4int n2nd = aStep->GetNumberOfSecondariesInCurrentStep();
```

現在のステップで発生した二次粒子の数を取得します。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.4.0/classG4Step.html)

:::
