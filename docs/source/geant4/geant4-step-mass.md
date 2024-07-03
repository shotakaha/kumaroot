# ステップ点の質量をしりたい（``GetMass``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double mass = pre_step->GetMass();
```

## ステップ点の重さをしりたい（``GetWeight``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double weight = pre_step->GetWeight();
```
