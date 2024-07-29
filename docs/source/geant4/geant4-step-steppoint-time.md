# ステップポイントのグローバル時刻をしりたい（``G4StepPoint::GetGlobalTime``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();
G4StepPoint *post_step = aStep->GetPostStepPoint();
G4Track *track = aStep->GetTrack();

G4double pre_time = pre_step->GetGlobalTime();
G4double post_time = post_step->GetGlobalTime();
G4double track_time = track->GetGlobalTime();

G4debug << "[PreStep]  GlobalTime=" << G4BestUnit{pre_time, "Time"} >> G4endl;
G4debug << "[PostStep] GlobalTime=" << G4BestUnit{post_time, "Time"} >> G4endl;
G4debug << "[Track]    GlobalTime=" << G4BestUnit{track_time, "Time"} >> G4endl;

// [PreStep]  GlobalTime=532.954 ps
// [PostStep] GlobalTime=567.787 ps
// [Track]    GlobalTime=567.787 ps
```

ステップの時刻を取得するメソッドは3種類あります。
``GetGlobalTime``で、トラックが含まれる**イベントが生成されてからの経過時間**が取得できます。

トラックのグローバル時刻はステップ終点の時刻と一致します。

:::{seealso}

- [](./geant4-track-time.md)

:::

## ローカル時刻をしりたい（``G4StepPoint::GetLocalTime``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();
G4StepPoint *post_step = aStep->GetPostStepPoint();
G4Track *track = aStep->GetTrack();

G4double pre_time = pre_step->GetLocalTime();
G4double post_time = post_step->GetLocalTime();
G4double track_time = track->GetLocalTime();

G4debug << "[PreStep]  LocalTime=" << G4BestUnit{pre_time, "Time"} >> G4endl;
G4debug << "[PostStep] LocalTime=" << G4BestUnit{post_time, "Time"} >> G4endl;
G4debug << "[Track]    LocalTime=" << G4BestUnit{track_time, "Time"} >> G4endl;

// [PreStep]  LocalTime=356.027 ps
// [PostStep] LocalTime=390.86 ps
// [Track]    LocalTime=390.86 ps
```

``GetLocalTime``で、**トラックが生成されてからの経過時間**が取得できます。
トラックのローカル時刻はステップ終点の時刻と一致します。

## 固有時刻をしりたい（``G4StepPoint::GetProperTime``）

```cpp
// G4Step *aStep
G4StepPoint *pre_step = aStep->GetPreStepPoint();
G4StepPoint *post_step = aStep->GetPostStepPoint();
G4Track *track = aStep->GetTrack();

G4double pre_time = pre_step->GetProperTime();
G4double post_time = post_step->GetProperTime();
G4double track_time = track->GetProperTime();

G4debug << "[PreStep]  ProperTime=" << G4BestUnit{pre_time, "Time"} >> G4endl;
G4debug << "[PostStep] ProperTime=" << G4BestUnit{post_time, "Time"} >> G4endl;
G4debug << "[Track]    ProperTime=" << G4BestUnit{track_time, "Time"} >> G4endl;

// [PreStep]  ProperTime=0 ps
// [PostStep] ProperTime=0 ps
// [Track]    ProperTime=0 ps
```

``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）が取得できます。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)

:::
