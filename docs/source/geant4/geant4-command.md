# コマンド操作したい

コマンドラインを使って、アプリケーションを対話的に実行できます。
Qtを有効にしてビルドした場合、Qtウィンドウ上でコマンド操作できます。

付属サンプルで遊ぶときに使いそうなコマンドを列挙してみました。
また、対応する（と思われる）ソースコードも参考に載せておきました。

## ランを開始したい（``/run/beamOn``）

```cfg
/run/beamOn イベント数
/run/beamOn 1
/run/beamOn 100
```

``/run/beamOn イベント数``で指定したイベント数のランを開始します。
ランを開始すると``/run/initialize``でインターロックがかかり、測定器にアクセスできなくなります。

:::{seealso}

```cpp
auto rm = G4RunManagerFactory::CreateRunManager();
rm->Initialize();
rm->beamOn(イベント数);
```

:::

## 粒子数を変更したい（``/gun/number``）

```cfg
/gun/number 粒子数
/gun/number 1
/gun/number 100
```

``/gun/number 粒子数``で、1イベントで入射する粒子の数を変更できます。

:::{seealso}

```cpp
G4ParticleGun *gun = new G4ParticleGun(粒子数);
```

:::

## 粒子を変更したい（``/gun/particle``）

```cfg
/gun/particle 粒子名
/gun/particle mu-
/gun/particle e-
```

``/gun/particle 粒子名``で、1イベントで入射する粒子の種類を変更できます。

:::{seealso}

```cpp
G4ParticleTable *table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *particle = table->FindParticle("粒子名");
gun->SetParticleDefinition(particle);
```

:::

## 入射エネルギーを変更したい（``/gun/energy``）

```cfg
/gun/energy エネルギー 単位
/gun/energy 1. GeV
/gun/energy 500. MeV
```

入射エネルギーを変更できます。
単位を間違えるとエラーになります。

:::{seealso}

```cpp
G4double energy = 500. * MeV
gun->SetParticleEnergy(energy);
```

:::

## 入射位置を変更したい（``/gun/position``）

```cfg
/gun/position x y z 単位
/gun/position 10. 10. 10. cm
```

入射位置を変更できます。
単位を間違えるとエラーになります。

:::{seealso}

```cpp
G4ThreeVector position = G4ThreeVector(0., 0., -10. * cm);
gun->SetParticlePosition(position);
```

:::

## 入射方向を変更したい（``/gun/direction``）

```cfg
/gun/direction ex ey ez
/gun/direction 0 0 1  // z軸方向
/gun/direction 0 1 1  // y-z平面:45度
/gun/direction 0 1 2  // y-z平面：30度ちょい
```

入射方向を、入射位置からのベクトルで設定できます。
単位は不要です。

:::{seealso}

```cpp
G4ThreeVector direction = G4ThreeVector(0., 0., 1.);
gun->SetParticleMomentumDirection(direction);
```

:::
