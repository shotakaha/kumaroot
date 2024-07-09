# ステップ点のの電荷をしりたい（``G4StepPoint::GetCharge``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double charge = pre_step->GetCharge();
```

ステップの電荷を取得できます。

:::{note}

電荷はトラック情報から取得したほうがいいかもしれません。

```cpp
auto particle = aTrack->GetParticleDefinition();
G4double charge = particle->GetPDGCharge();
```

:::

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)
- [G4ParticleDefinition](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleDefinition.html)

:::
