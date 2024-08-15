# 宇宙線ミューオンしたい

```cpp
PrimaryGeneratorAction::GeneratePrimaries(G4Event *aEvent)
{
    // イベントごとにランダムにしたいため
    // 1回のイベントで生成する粒子の数は1個にする
    G4int n_particle = 1;
    auto gun = new G4ParticleGun(n_particle);

    // 入射粒子を指定
    G4ParticleTable *table = new G4ParticleTable::GetParticleTable();
    G4ParticleDefinition *particle = table->FindParticle("mu-");
    gun->SetParticleDefinition(particle);

    // 入射位置を指定
    G4ThreeVector xyz{0., 0., 0.};
    gun->SetParticlePosition(xyz)

    // 入射エネルギーを指定
    G4double energy{1. * GeV};
    gun->SetParticleEnergy(energy);

    // 入射方向を指定
    G4ThreeVector direction{0., 0., 1.};
    gun->SetParticleMomentumDirection(direction);

    // イベントにvertexを追加
    gun->GeneratePrimaryVertex(aEvent);
}
```

地表に降り注ぐ宇宙線は、そのほとんどがミュー粒子と考えられます。
Geant4の[ミューオン](https://pdg.lbl.gov/2020/listings/rpp2020-list-muon.pdf)は、正ミューオン（``mu+``）、負ミューオン（``mu-``）がそれぞれ用意されています。

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
