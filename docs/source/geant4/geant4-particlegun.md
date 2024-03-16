# 入射粒子したい（``G4ParticleGun``）

```cpp
G4int n_particles = 100;
G4ParticleGun *aParticleGun = new G4ParticleGun(n_particles);
```

## 粒子の種類を変更したい（``SetParticleDefinition``）

```cpp
G4ParticleTable *table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *particle = table->FindParticle("粒子名");
aParticleGun->SetParticleDefinition(particle);
```

入射粒子の種類を変更できます。
ただし、粒子名をそのまま``SetParticleDefinition``することはできません。
まず``G4ParticleTable``から粒子情報（質量、電荷、スピンなど）を取得して、
それを``SetParticleDefinition``に渡す手順になっています。

## エネルギーを変更したい（``SetParticleEnergy``）

```cpp
aParticleGun->SetParticleEnergy(400*MeV);
```

``SetParticleEnergy``で入射粒子のエネルギーを変更できます。
運動量をすでに設定していた場合は0に変更されるようです。

## 運動量を変更したい（``SetParticleMomentum``）

```cpp
aParticleGun->SetParticleMomentum(400*MeV);
```

``SetParticleMomentum``で入射粒子の運動量を変更できます。
エネルギーを設定していなかった場合、入射粒子の質量を考慮したエネルギーが設定されます。

## 入射方向を変更したい（``SetParticleMomentumDirection``）

```cpp
G4ThreeVector direction = G4ThreeVector(0., 0., 1.);
aParticle->SetParticleMomentumDirection(direction);
```

```SetParticleMomentumDirection``で入射方向を変更できます。
方向は（x, y, z）の単位ベクトルで指定します。

## 入射場所を変更したい（``SetParticlePosition``）

```cpp
position = G4ThreeVector(x0, y0, z0);
aParticleGun->SetParticlePosition(position);
```

``SetParticlePosition``で入射位置を変更できます。
座標は``G4ThreeVector``で設定します。

## ランダムに入射したい

```cpp
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
```

``G4UniformRand``を使って入射場所をランダムに設定できます。
付属サンプルB1では、標的となる論理ボリュームのサイズを利用して、座標を決めていました。

