# geantinoしたい（`geantino`）

```cfg
/gun/particle geantino
```

`geantino`は、どの物質とも相互作用をしないGeant4内の仮想粒子です。
ワールド内にある物体の境界でだけステップが区切られるため、
物体がきちんと配置されているかのデバッグに使えます。

また、`PrimaryGeneratorAction`で一時的な粒子として設定されることもあります。

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

## 磁場中で曲げたい（`chargedgeantino`）

```cfg
/run/initialize
/globalField/setValue 0 0 1 tesla
/gun/particle chargedgeantino
/gun/energy 100 MeV
/gun/position 0 0 0 cm
/gun/direction 1 0 0
/tracking/verbose 1
/run/beamOn 1
```

`chargedgeantino`は電荷（+1 e）を持つため、磁場中で軌跡が曲がります。
一方、`geantino`は電荷が0なので曲がりません。
同じ設定で両方を実行すると、違いを比べられます。

:::{seealso}

- [G4ParticleGun](https://geant4.kek.jp/Reference/11.4.0/classG4ParticleGun.html)

:::
