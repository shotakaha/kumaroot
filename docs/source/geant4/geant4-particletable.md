# 粒子したい（``G4ParticleTable``）

```cpp
G4ParticleTable *particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *positron = particle_table->FindParticle("e+");
G4ParticleDefinition *muon = particle_table->FindParticle("mu+");
G4ParticleDefinition *pion = particle_table->FindParticle("pi+");
G4ParticleDefinition *kaon = particle_table->FindParticle("kaon+");
G4ParticleDefinition *proton = particle_table->FindParticle("proton");
```

附属サンプルB5から抜粋しました。
粒子を指定する際は、質量、電荷、スピンなどの設定が必要です。
``G4ParticleTable``を使うと、粒子名で参照できます。

## リファレンス

- [PrimaryGeneratorAction.hh - Basic B5 - Geant4 Examples](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/include/PrimaryGeneratorAction.hh)
- [PrimaryGeneratorAction.cc - Basic B5 - Geant4 Examples](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/PrimaryGeneratorAction.hh)
