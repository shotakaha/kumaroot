# ステップの長さをしりたい（`G4Step::GetStepLength`）

```cpp
G4double step_length = aStep->GetStepLength();

G4debug << "\t[Step::GetStepLength] StepLength=" << G4BestUnit{step_length, "Length"} << G4endl;
// [Step::GetStepLength] StepLength=1.04428 cm
```

`GetStepLength`でステップの長さを取得できます。
この長さは、粒子が多重散乱してジグザグに移動した長さです。

:::{seealso}

- [](./geant4-track-length.md)

:::


## 荷電粒子だけ飛跡長を数えたい（`GetPDGCharge`）

```cpp
G4double stepLength = 0.;
if (step->GetTrack()->GetDefinition()->GetPDGCharge() != 0.) {
  stepLength = step->GetStepLength();
}
```

飛跡長を層ごとに足し合わせるときは、荷電粒子のステップだけを数えます。
[B4のサンプル](geant4-examples-b4)でも同じ書き方をしています。

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-track-length.md)
- [](./geant4-examples-b4.md)

:::
