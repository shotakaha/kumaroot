# ステップの二次粒子数をしりたい（``G4Step::GetNumberOfSecondariesInCurrentStep``）

```cpp
// G4Step *aStep
G4int n2nd = aStep->GetNumberOfSecondariesInCurrentStep();
```

現在のステップで発生した二次粒子の数を取得します。
