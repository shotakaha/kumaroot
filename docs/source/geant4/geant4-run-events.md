# イベント数をしりたい（`G4Run::GetNumberOfEvent`）

```cpp
// void MyRunAction::EndOfRunAction(const G4Run* aRun) の中
G4int n_events = aRun->GetNumberOfEvent();

if (n_events == 0) {
    return;
}
```

`GetNumberOfEvent()`は、ランで処理が終わったイベント数を返します。
各イベントの処理が終わるたびに増えます。
そのため、イベントの処理中に読むと、現在のイベントはまだ数えられていません。
`GetNumberOfEventToBeProcessed()`は、`BeamOn`で要求されたイベント数です。

イベント数がわかると、イベントがないランをスキップできます。
