# 粒子の種類を変更したい（``SetParticleDefinition``）

```cpp
G4ParticleGun *gun = new G4ParticleGun(1);
G4ParticleTable *table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *particle = table->FindParticle("粒子名");
gun->SetParticleDefinition(particle);
```

``SetParticleDefinition``で入射する粒子の種類を変更できます。

ただし、粒子名をそのまま設定することはできません。
まず``G4ParticleTable``から粒子情報（質量、電荷、スピンなど）を取得して、
それを``SetParticleDefinition``に渡す手順になっています。

## リファレンス

- [G4ParticleTable](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleTable.html)
- [PDG Identifiers - Particle Data Group](https://pdg.lbl.gov/2024/pdgid/PDGIdentifiers.html)
