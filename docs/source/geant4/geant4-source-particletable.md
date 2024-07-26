# 粒子したい（``G4ParticleTable``）

```cpp
G4ParticleTable *particle_table = G4ParticleTable::GetParticleTable();
```

粒子には質量、電荷、スピンなどの設定が必要です。
``G4ParticleTable``クラスを使って、粒子名で参照できます。
``GetParticlaTable()``で得た一覧オブジェクトはシングルトンになっています。

## Geantinoしたい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *geantino = particle_table->FindParticle("chargedgeantino");
```

``geantino``は、Geant4内の仮想粒子で、どの物質とも相互作用をしない粒子です。
Geant4の粒子輸送では、配置した物体の境界面で必ずステップが作成されます。

``geantino``を打ち込み、生成されたステップの情報を確認することで、
物体がきちんと配置されているかをデバッグできます。

## 電子・陽電子したい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *positron = particle_table->FindParticle("e+");
G4ParticleDefinition *electron = particle_table->FindParticle("e-");
```

## ミューオンしたい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *mu_plus = particle_table->FindParticle("mu+");
G4ParticleDefinition *mu_minus = particle_table->FindParticle("mu-");
```

## パイ中間子したい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *pi_plus = particle_table->FindParticle("pi+");
G4ParticleDefinition *pi_minus = particle_table->FindParticle("pi-");
G4ParticleDefinition *pi_zero = particle_table->FindParticle("pi0");
```

## K中間子したい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *k_plus = particle_table->FindParticle("kaon+");
G4ParticleDefinition *k_minus = particle_table->FindParticle("kaon-");
```

## 陽子したい

```cpp
auto particle_table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *proton = particle_table->FindParticle("proton");
```



## リファレンス

- [G4ParticleTable](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleTable.html)
- [PrimaryGeneratorAction.hh - Basic B5 - Geant4 Examples](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/include/PrimaryGeneratorAction.hh)
- [PrimaryGeneratorAction.cc - Basic B5 - Geant4 Examples](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/PrimaryGeneratorAction.hh)
