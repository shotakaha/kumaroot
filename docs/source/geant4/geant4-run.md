# ランしたい（``G4Run``）

```cpp
aRun->GetNumberOfEvents()
```

ユーザーアクション設定の``RunAction``。

## イベント数をしりたい（``GetNumberOfEvents``）

```cpp
aRun->GetNumberOfEvents()
```

ランのイベント数を取得できます。
イベントがないランはスキップできます。

```cpp
G4int n_events = aRun->GetNumberOfEvents();
if (n_events == 0 ) return;
```



