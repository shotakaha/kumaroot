# 粒子生成したい（``G4VUserPrimaryGeneratorAction``）

一次粒子（入射粒子）を定義するクラスは、必須クラスのひとつで、
``G4VUserPrimaryGeneratorAction``クラスを継承して作成します。

## 親クラス

- [G4VUserPrimaryGeneratorAction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPrimaryGeneratorAction.html)

```cpp
G4VUserPrimaryGeneratorAction();
virtual ~G4VUserPrimaryGeneratorAction() = default;
virtual void GeneratePrimaries(G4Event *aEvent) = 0;
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``GeneratePrimaries()``は、イベントの一次粒子を設定するための関数です。
純粋仮想関数になっているため、自作クラスでoverrideが必要です。

## PrimaryGeneratorクラス

クラス名を``PrimaryGenerator``としました。

```cpp
// //////////////////////////////////////////////////
// include/PrimaryGenerator.hh
// //////////////////////////////////////////////////

#ifndef PrimaryGenerator_h
#define PrimaryGenerator_h 1

#include "G4VUserPrimaryGeneratorAction.hh"

namespace ToyMC
{

class PrimaryGenerator : public G4VUserPrimaryGeneratorAction
{
    public:
        PrimaryGenerator() = default;
        ~PrimaryGenerator() = default;

        void GeneratePrimaries(G4Event *aEvent) override;
};

}; // namespace ToyMC

#endif
```

## GeneratePrimaries

```cpp
void PrimaryGenerator::GeneratePrimaries(G4Event *aEvent)
{
    // 入射粒子の数を設定
    G4int n_particles = 1;
    G4ParticleGun *gun = new G4ParticleGun(n_particles);

    // 入射粒子の種類を設定
    auto table = G4ParticleTable::GetParticleTable();
    auto particle = table->FindParticle("mu-");
    gun->SetParticleDefinition(particle);

    // 入射粒子の座標を設定
    G4ThreeVector xyz{0., 0., 0.};
    gun->SetParticlePosition{xyz};

    // 入射粒子の方向を設定
    G4ThreeVector direction{0., 0., 1.};
    gun->SetParticleMomentumDirection(direction);

    // 入射粒子のエネルギーを設定
    G4double energy{1. * GeV};
    gun->SetParticleEnergy(energy);

    // イベントに追加
    gun->GeneratePrimaryVertex(aEvent);
}
```

``G4ParticleGun``を使ってミューオンを入射しています。
``G4ParticleGun``はGeant4標準の粒子生成クラスのひとつです。

:::{seealso}

- [](./geant4-source-particlegun.md)
- [](./geant4-source-gps.md)

:::
