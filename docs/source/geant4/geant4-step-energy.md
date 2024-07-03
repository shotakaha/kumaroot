# ステップのエネルギー損失をしりたい（``GetTotalEnergyDeposit``）

```cpp
G4double energy_deposit = aStep->GetTotalEnergyDeposit();
```

該当のステップで落としたエネルギーの総量を取得できます。

## ステップ点のエネルギーをしりたい

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double total_energy = pre_step->GetTotalEnergy();
G4double kinetic_energy = pre_step->GetKineticEnergy();
```

``GetTotalEnergy``でエネルギーの合計、
``GetKineticEnergy``で運動エネルギーの合計を取得できます。
