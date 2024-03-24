# ミューオンしたい

```cfg
/gun/particle mu-
/gun/particle mu+
```

[ミューオン](https://pdg.lbl.gov/2020/listings/rpp2020-list-muon.pdf)は正ミューオン（``mu+``）、負ミューオン（``mu-``）が用意されています。

```cpp
G4ParticleTable *particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *muon_m = particle_table->FindParticle("mu-");
G4ParticleDefinition *muon_p = particle_table->FindParticle("mu+");
```

## 宇宙線ミューオンしたい

```cpp
PrimaryGeneratorAction::PrimaryGeneratorAction()
{
    G4int n_particle = 1;
    fParticleGun = new G4ParticleGun(n_particle);

    G4ParticleTable *particle_table = new G4ParticleTable::GetParticleTable();
    G4ParticleDefinition *particle = particle_table->FindParticle("mu-");
    fParticleGun->SetParticleDefinition(particle);
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., 0.));
    fParticleGun->SetParticleEnergy(500*MeV);
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., 1., 0.));
}
```

宇宙線ミューオンなので、鉛直下向きに打ち込んでいます。
