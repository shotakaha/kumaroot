# ステップのエネルギー損失をしりたい（``G4Step::GetTotalEnergyDeposit``）

```cpp
// エネルギー損失
G4double energy_deposit = aStep->GetTotalEnergyDeposit();

// イオン化によらないエネルギー損失
G4double energy_deposit = aStep->GetNonIonizingEnergyDeposit();
```

現在のステップで落としたエネルギーの総量を取得できます。
