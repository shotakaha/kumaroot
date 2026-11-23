# ステップのエネルギー損失をしりたい（``G4Step::GetTotalEnergyDeposit``）

```cpp
// エネルギー損失
G4double energy_deposit = aStep->GetTotalEnergyDeposit();

// イオン化によらないエネルギー損失
G4double energy_deposit = aStep->GetNonIonizingEnergyDeposit();
```

現在のステップで落としたエネルギーの総量を取得できます。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)

:::
