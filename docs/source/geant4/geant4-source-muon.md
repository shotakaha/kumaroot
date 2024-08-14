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

## 天頂角分布したい

```cpp
#include "G4UniformRand.hh"
#include "G4ThreeVector.hh"
#include "G4PhysicalConstants.hh"

G4ThreeVector RandomMuonDirection() const
{
    // 天頂角（zenith angle）
    G4double u = G4UniformRand();
    G4double theta = std::acos(std::sqrt(u));

    // 方位角（azimuth angle）
    G4double v = G4UniformRand();
    G4double phi = CLHEP::twopi * v;

    // 運動方向を計算
    G4double sinTheta = std::sin(theta);
    G4double cosTheta = std::cos(theta);
    G4double sinPhi = std::sin(phi);
    G4double cosPhi = std::cos(phi);

    G4double x = sinTheta * cosPhi;
    G4double y = sinTheta * sinPhi;
    G4double z = cosTheta;

    G4ThreeVector direction{x, y, z};
    return direction;
};
```

宇宙線が降り注ぐ方向は $\cos^{2}\theta$ に比例することが知られています。

:::{math}

R & := \cos^{2}\theta \\
\cos \theta & = \sqrt{R} \\
\theta & = \cos^{-1} R = \arccos R

:::

天頂角 $\theta$ と
方位角 $\phi$ の値を使って、
方向ベクトルは次のように計算できます。

:::{math}

x & = \sin\theta \cos\phi \\
y & = \sin\theta \sin\phi \\
z & = \cos\theta

:::
