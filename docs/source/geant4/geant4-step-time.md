# ステップ点の時刻をしりたい（``GetGlobalTime`` / ``GetLocalTime`` / ``GetProperTime``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double global_time = pre_step->GetGlobalTime();
G4double local_time = pre_step->GetLocalTime();
G4double proper_time = pre_step->GetProperTime();

G4debug << "GlobalTime=" << G4BestUnit{global_time, "Time"} >> G4endl;
G4debug << "LocalTime=" << G4BestUnit{local_time, "Time"} >> G4endl;
G4debug << "ProperTime=" << G4BestUnit{proper_time, "Time"} >> G4endl;
// GlobalTime=532.954 ps
// LocalTime=356.027 ps
// ProperTime=0 ps
```

ステップの時刻を取得するメソッドは3種類あります。

``GetGlobalTime``でトラックが含まれるイベントが生成されてからの経過時間、
``GetLocalTime``でトラックが生成されてからの経過時間、
``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）を取得できます。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)

:::
