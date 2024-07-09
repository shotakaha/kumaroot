# イベント数をしりたい（``G4Run::GetNumberOfEvents``）

```cpp
G4int n_events = aRun->GetNumberOfEvents();
```

ランのイベント数を取得できます。

```cpp
G4int n_events = aRun->GetNumberOfEvents();
if (n_events == 0 ) return;
```

イベント数がわかると、イベントがないランをスキップできます。
