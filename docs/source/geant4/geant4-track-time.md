# トラックの時刻をしりたい（``G4Track::GetGlobalTime``）

```cpp
// G4Track *aTrack;
G4double global_time = aTrack->GetGlobalTime();
G4double local_time = aTrack->GetLocalTime();
G4double proper_time = aTrack->GetProperTime();
```

``GetGlobalTime``でトラックが含まれるイベントが生成されてからの経過時間、
``GetLocalTime``でトラックが生成されてからの経過時間、
``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）を取得できます。
