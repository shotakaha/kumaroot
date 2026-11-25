# ステップのエネルギー損失をしりたい（`G4Step::GetTotalEnergyDeposit`）

```cpp
// エネルギー損失
G4double energy_deposit = aStep->GetTotalEnergyDeposit();
G4debug << G4BestUnit{energy_deposit, "Energy"} << G4endl;
```

`GetTotalEnergyDeposit`で、現在のステップのエネルギー損失の総量を取得できます。
カロリメーターのような検出器の`ProcessHits`で、ヒットのエネルギーを記録する場合に使います。

:::{seealso}

- [](./geant4-sensor-processhits.md)
- [](./geant4-step.md)

:::
