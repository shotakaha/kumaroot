# ステップポイントの質量をしりたい（``G4StepPoint::GetMass``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double mass = pre_step->GetMass();
```
