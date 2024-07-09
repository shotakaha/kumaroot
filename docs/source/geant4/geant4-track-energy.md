# トラックのエネルギーをしりたい（``G4Track::GetTotalEnergy``）

```cpp
G4double energy = aTrack->GetTotalEnergy();
G4double kinetic_energy = aTrack->GetKineticEnergy();
```

``GetTotalEnergy``でエネルギーの合計、
``GetKineticEnergy``で運動エネルギーの合計を取得できます。
