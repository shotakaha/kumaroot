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

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
