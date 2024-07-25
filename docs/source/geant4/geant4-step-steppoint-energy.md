# ステップ点のエネルギーをしりたい（``G4StepPoint::GetTotalEnergy``）

```cpp
// G4Step *aStep;
G4StepPoint *pre_step = aStep->GetPreStepPoint();

// エネルギー
G4double total_energy = pre_step->GetTotalEnergy();

// 運動エネルギー
G4double kinetic_energy = pre_step->GetKineticEnergy();
```

``GetTotalEnergy``でエネルギーの合計、
``GetKineticEnergy``で運動エネルギーの合計を取得できます。
