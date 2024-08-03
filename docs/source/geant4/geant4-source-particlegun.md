# 入射粒子したい（``G4ParticleGun``）

```cpp
G4int n_particles = 1;
G4ParticleGun *gun = new G4ParticleGun(n_particles);
```

``G4ParticleGun``はGeant4標準の粒子生成クラスのひとつです。
種類、方向、座標、エネルギーなどを固定した1種類の入射粒子を生成できます。

:::{caution}

あくまで1種類のParticleGunを生成するクラスです。
上記のサンプルで``n_particles=100``にした場合、
同じ設定の粒子が100個生成されます。

粒子をランダムに入射したい場合は、``n_particles=1``に設定し、
``BeamOn(100)``のようにイベント数を増やすとよいです。

:::

## 粒子の種類を変更したい（``SetParticleDefinition``）

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

## エネルギーを変更したい（``SetParticleEnergy``）

```cpp
G4double energy = 400 * MeV;
gun->SetParticleEnergy(energy);
```

``SetParticleEnergy``で入射粒子のエネルギーを変更できます。
運動量をすでに設定していた場合は0に変更されるようです。

## 運動量を変更したい（``SetParticleMomentum``）

```cpp
G4ParticleGun *gun = new G4ParticleGun(1);
gun->SetParticleMomentum(400 * MeV);
```

``SetParticleMomentum``で入射粒子の運動量を変更できます。
エネルギーを設定していなかった場合、入射粒子の質量を考慮したエネルギーが設定されます。

## 入射方向を変更したい（``SetParticleMomentumDirection``）

```cpp
G4ThreeVector direction = G4ThreeVector(0., -1., 0.);
gun->SetParticleMomentumDirection(direction);
```

```SetParticleMomentumDirection``で入射方向を変更できます。
方向は（x, y, z）の単位ベクトルで指定します。
上のサンプルは鉛直下向きに入射しています。

:::{note}

Geant4の世界には重力がないと思うので、横から打っても、上から打っても同じだと思います。
ただ、ミューオンを上から入射したほうが、見た目的に宇宙線っぽくなります。

:::

## 入射場所を変更したい（``SetParticlePosition``）

```cpp
position = G4ThreeVector(x0, y0, z0);
gun->SetParticlePosition(position);
```

``SetParticlePosition``で入射位置を変更できます。
座標は``G4ThreeVector``で設定します。

## ランダムに入射したい

```cpp
void PrimaryGeneratorAction::GeneratePrimaries(G4Event* /*aEvent*/)
{
    // aTargetLogical : 入射標的の論理ボリューム

    G4double target_x = aTargetLogical->GetXHalfLength() * 2.;
    G4double target_y = aTargetLogical->GetYHalfLength() * 2.;
    G4double target_z = aTargetLogical->GetZHalfLength() * 2.;

    G4double factor = 0.8;
    G4double x0 = factor * target_x * (G4UniformRand() - 0.5);
    G4double x0 = factor * target_y * (G4UniformRand() - 0.5);
    G4double z = -0.5 * target_z

    position = G4ThreeVector(x0, y0, z0);
    aParticleGun->SetParticlePosition(position);
}
```

``G4UniformRand``を使って入射場所をランダムに設定できます。
付属サンプルB1では、標的となる論理ボリュームのサイズを利用して、座標を決めていました。

## イベントに追加したい（``GeneratePrimaryVertex``）

```cpp
// G4EventにGunを追加する
gun->GeneratePrimaryVertex(aEvent);
```

``GeneratePrimaryVertex``で、作成したParticleGunをイベントに追加します。

## リファレンス

- [G4ParticleGun](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleGun.html)
- [G4ParticleTable](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleTable.html)
- [G4PrimaryParticle](https://geant4.kek.jp/Reference/11.2.0/classG4PrimaryParticle.html)
- [G4PrimaryVertex](https://geant4.kek.jp/Reference/11.2.0/classG4PrimaryVertex.html)
- [PDG Identifiers - Particle Data Group](https://pdg.lbl.gov/2024/pdgid/PDGIdentifiers.html)
