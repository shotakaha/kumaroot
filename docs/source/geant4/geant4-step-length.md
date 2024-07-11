# ステップの長さをしりたい（``G4Step::StepLength``）

```cpp
G4double step_length = aStep->GetStepLength();

G4debug << "\t[Step::GetStepLength] StepLength=" << G4BestUnit{step_length, "Length"} << G4endl;
//[Step::GetStepLength] StepLength=1.04428 cm
```

``GetStepLength``でステップの長さを取得できます。
この長さは、粒子が多重散乱してジグザグに移動した長さです
