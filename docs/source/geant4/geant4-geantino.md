# geantinoしたい

```cfg
/gun/particle geantino
```

``geantino``は、どの物質とも相互作用をしない仮想粒子です。
粒子輸送のデバッグなどに使えるそうです。

また、``PrimaryGeneratorAction``で一時的な粒子として設定されることもあります。

```cpp
PrimaryGeneratorAction::PrimaryGeneratorAction()
{
    G4int n_particle = 1;
    fParticleGun = new G4ParticleGun(n_particle);

    G4ParticleTable *particle_table = new G4ParticleTable::GetParticleTable();
    G4ParticleDefinition *particle = particle_table->FindParticle("chargedgeantino");
    fParticleGun->SetParticleDefinition(particle);
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., 0.));
    fParticleGun->SetParticleEnergy(1*eV);
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(1., 0., 0.));
}
```
