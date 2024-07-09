# ステップ点したい（``G4Step::GetPreStepPoint``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();
G4StepPoint *post_step = aStep->GetPostStepPoint();
```
