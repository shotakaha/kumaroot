# トラック操作したい（``G4Track``）

``G4Track``はトラック情報を管理するクラスです。
ユーザーアクション設定の
[UserTrackingAction](./geant4-user-trackingaction.md)や
[UserSteppingAction](./geant4-user-steppingaction.md)から
情報を取得したいときに使います。

:::{note}

トラックは、粒子が進んできた情報を含んでいて、
トラックが生成されたときの情報と、
最新のステップの状態を取得できます。

:::

```{toctree}
---
maxdepth: 1
---
geant4-track-trackid
geant4-track-step
geant4-track-length
geant4-track-particle
geant4-track-position
geant4-track-time
geant4-track-momentum
geant4-track-energy
geant4-track-volume
geant4-track-vertex
geant4-track-status
geant4-trackingaction
```

## リファレンス

- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)
