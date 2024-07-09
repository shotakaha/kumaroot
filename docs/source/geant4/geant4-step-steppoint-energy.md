# ステップ点のエネルギーをしりたい（``G4StepPoint::GetTotalEnergy``）

```cpp
// G4Step *aStep;
G4StepPoint *pre_step = aStep->GetPreStepPoint();

G4double total_energy = pre_step->GetTotalEnergy();
G4double kinetic_energy = pre_step->GetKineticEnergy();

```
