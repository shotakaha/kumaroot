# geantinoしたい

```cfg
/gun/particle geantino
```

``geantino``は、どの物質とも相互作用をしないGeant4内の仮想粒子です。
ワールド内にある物体の境界でだけステップが区切られるため、
物体がきちんと配置されているかのデバッグに使えます。

また、``PrimaryGeneratorAction``で一時的な粒子として設定されることもあります。

```cpp
#include "G4SystemOfUnits.hh"

PrimaryGeneratorAction::PrimaryGeneratorAction()
{
    // fParticleGunはメンバー変数（G4ParticleGun*）
    fParticleGun = new G4ParticleGun(1);

    G4ParticleTable* table = G4ParticleTable::GetParticleTable();
    G4ParticleDefinition* particle = table->FindParticle("chargedgeantino");
    fParticleGun->SetParticleDefinition(particle);
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., 0.));
    fParticleGun->SetParticleEnergy(1 * GeV);
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., 0., 1.));
}

PrimaryGeneratorAction::~PrimaryGeneratorAction()
{
    delete fParticleGun;
}
```
