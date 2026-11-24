# ParticleGunしたい（`G4ParticleGun`）

```cpp
G4int n_particles = 1;
G4ParticleGun* fParticleGun = new G4ParticleGun(n_particles);
```

`G4ParticleGun`はGeant4標準の粒子生成クラスのひとつです。
種類、方向、座標、エネルギーなどを固定した1種類の入射粒子を生成できます。

:::{caution}

あくまで1種類のParticleGunを生成するクラスです。
上記のサンプルで`n_particles=100`にした場合、
同じ設定の粒子が100個生成されます。

粒子をランダムに入射したい場合は、`n_particles=1`に設定し、
`BeamOn(100)`のようにイベント数を増やすとよいです。

:::

```{toctree}
---
maxdepth: 1
---
geant4-source-particlegun-definition
geant4-source-particlegun-energy
geant4-source-particlegun-momentum
geant4-source-particlegun-direction
geant4-source-particlegun-position
```

## ランダムに入射したい

```cpp
void PrimaryGeneratorAction::GeneratePrimaries(G4Event* /*aEvent*/)
{
    // aTargetLogical : 入射標的の論理ボリューム
    auto* box = dynamic_cast<G4Box*>(aTargetLogical->GetSolid());

    G4double target_x = box->GetXHalfLength() * 2.;
    G4double target_y = box->GetYHalfLength() * 2.;
    G4double target_z = box->GetZHalfLength() * 2.;

    G4double factor = 0.8;
    G4double x0 = factor * target_x * (G4UniformRand() - 0.5);
    G4double y0 = factor * target_y * (G4UniformRand() - 0.5);
    G4double z0 = -0.5 * target_z;

    G4ThreeVector position(x0, y0, z0);
    fParticleGun->SetParticlePosition(position);
}
```

`G4UniformRand`を使って入射場所をランダムに設定できます。
寸法は`G4LogicalVolume`ではなく、そのsolid（ここでは`G4Box`）から取得します。
付属サンプルB1では、エンベロープの`G4Box`から寸法を取得して、座標を決めていました。

## イベントに追加したい（`GeneratePrimaryVertex`）

```cpp
// G4EventにGunを追加する
fParticleGun->GeneratePrimaryVertex(aEvent);
```

`GeneratePrimaryVertex`で、作成したParticleGunをイベントに追加します。

## リファレンス

- [G4ParticleGun](https://geant4.kek.jp/Reference/11.4.0/classG4ParticleGun.html)
