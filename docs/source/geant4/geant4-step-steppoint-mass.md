# ステップポイントの質量をしりたい（``G4StepPoint::GetMass``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double mass = pre_step->GetMass();
```

:::{seealso}

- [G4StepPoint](https://geant4.kek.jp/Reference/11.4.0/classG4StepPoint.html)

:::
