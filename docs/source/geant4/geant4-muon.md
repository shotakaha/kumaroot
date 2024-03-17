# ミューオンしたい

```cfg
/gun/particle mu-
/gun/particle mu+
```

ミューオンは正ミューオン（``mu+``）、負ミューオン（``mu-``）が用意されています。

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

鉛直下向きに打ち込んで、宇宙線として使っています。
