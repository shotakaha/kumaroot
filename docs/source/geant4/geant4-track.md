# トラック操作したい（`G4Track`）

```cpp
// void UserSteppingAction(const G4Step* aStep) の中

// ステップからトラックを取得する
const G4Track* track = aStep->GetTrack();

// トラックのID
auto track_id = track->GetTrackID();

// 生成位置（トラックが生成されたときの位置）
auto vertex = track->GetVertexPosition();

// 現在のステップ数
auto step_number = track->GetCurrentStepNumber();
```

`G4Track`はトラック情報を管理するクラスです。
ユーザーアクション設定の
[UserTrackingAction](geant4-user-trackingaction)や
[UserSteppingAction](geant4-user-steppingaction)から
情報を取得したいときに使います。

:::{note}

トラックは、粒子が進んできた情報を含んでいて、
トラックが生成されたときの情報（生成位置など）と、
最新のステップの状態（現在のステップ数など）を取得できます。

:::

```{toctree}
---
maxdepth: 1
---
geant4-track-trackid
geant4-track-step
geant4-track-stepnumber
geant4-track-length
geant4-track-particle
geant4-track-position
geant4-track-time
geant4-track-momentum
geant4-track-energy
geant4-track-volume
geant4-track-vertex
geant4-track-status
geant4-track-touchable
geant4-track-process
```

## リファレンス

- [G4Track](https://geant4.kek.jp/Reference/11.4.0/classG4Track.html)
