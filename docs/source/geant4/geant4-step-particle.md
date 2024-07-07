# トラックの粒子をしりたい（``GetParticleDefinition``）

```cpp
// G4Step *aStep
G4Track *track = aStep->GetTrack();

auto particle = track->GetParticleDefinition()

G4debug << "ParticleName=" << particle->GetParticleName() << G4endl;
G4debug << "PDGEncoding=" << particle->GetPDGEncoding() << G4endl;
// ParticleName=gamma
// PDGEncoding=22

// ParticleName=mu-
// PDGEncoding=13
```

:::{seealso}

- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)
- [G4ParticleDefinition](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleDefinition.html)

:::
