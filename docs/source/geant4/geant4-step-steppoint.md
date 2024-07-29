# ステップポイントしたい（``G4Step::GetPreStepPoint``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();
G4StepPoint *post_step = aStep->GetPostStepPoint();
```

ステップは始点と終点で構成されています。
``GetPreStepPoint`` で始点、
``GetPostStepPoint`` で終点の
``G4StepPoint``オブジェクトを取得できます。
