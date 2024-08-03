# 入射粒子を分布したい（``G4GeneralParticleSource``）

```cpp
G4GeneralParticleSource gps = G4GeneralParticleSource();
gps->GeneratePrimaryVertex(aEvent);
```

``G4GeneralParticleSource``はGeant4標準の粒子生成クラスのひとつです。
``G4ParticleGun``と異なり、入射粒子を平面上に分布させて生成できます。
また、マクロのみで操作できます。

```{toctree}
geant4-source-gps-position
geant4-source-gps-angle
```

## 入射粒子のマクロしたい

| コマンド名 | 引数 | デフォルト値 | 内容 |
|---|---|---|---|
| ``/gps/list`` | | | 利用可能な粒子名のリストを表示する |
| ``/gps/particle`` | 粒子名 | geantino | 入射粒子名を設定 |
| ``/gps/direction`` | Px Py Pz | 1 0 0 | 入射方向を設定 |
| ``/gps/energy`` | E 単位 | 1 MeV | 入射エネルギーを設定 |
| ``/gps/position`` | X Y Z 単位 | 0 0 0 cm | 入射位置を設定 |
| ``/gps/time`` | t0 単位 | 0 ns | 入射時刻を設定 |
| ``/gps/number`` | N | 1 | 入射粒子数を設定 |
| ``/gps/source/multiplevertex`` | flag | false | trueにすると複数のvertexを生成できる |
| ``/gps/source/flatsampling`` | flag | false | trueにするとソースの強度が無視される |

## リファレンス

- [G4GeneralParticleSource](https://geant4.kek.jp/Reference/11.2.0/classG4GeneralParticleSource.html)
- [Geant4 General Particle Source - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/generalParticleSource.html)
