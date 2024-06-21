# geantinoしたい

```cfg
/gun/particle geantino
```

``geantino``は、どの物質とも相互作用をしないGeant4内の仮想粒子です。
ワールド内にある物体の境界面だけでステップが残るため、
物体がきちんと配置されているかのデバッグにに使えます。

また、``PrimaryGeneratorAction``で一時的な粒子として設定されることもあります。

```cpp
PrimaryGeneratorAction::PrimaryGeneratorAction()
{
    G4int n_particle = 1;
    auto aGun = new G4ParticleGun(n_particle);

    G4ParticleTable *table = new G4ParticleTable::GetParticleTable();
    G4ParticleDefinition *particle = particle_table->FindParticle("chargedgeantino");
    aGun->SetParticleDefinition(particle);
    aGun->SetParticlePosition(G4ThreeVector(0., 0., 0.));
    aGun->SetParticleEnergy(1 * GeV);
    aGun->SetParticleMomentumDirection(G4ThreeVector(0., 0., 1.));
}
```
