# イベント番号を取得したい（``G4Event::EventID``）

```cpp
void MyEventAction::BeginOfEventAction(const G4Event* event) {
    G4int event_id = aEvent->GetEventID();
    G4cout << "=== Begin Event #" << event_id << G4endl;
}
```

`G4Event::GetEventID()`で、現在のイベント番号を取得できます。
イベント番号は0から始まる整数になっています。

`BeginOfEventAction()`の中では進捗確認用に表示、
`EndOfEventAction()`の中では記録用に取得するとよいです。

## イベント番号を出力したい（``G4Event::Print``）

```cpp
// G4Event *aEvent
aEvent->Print();
```

`G4Event::Print()`でイベント番号などの基本情報を出力できます。

:::{seealso}

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)

:::

## G4Stepからイベント番号を取得したい

```cpp
void MySteppingAction::UserSteppingAction(const G4Step* step) {
    G4EventManager* em = G4EventManager::GetEventManager();
    const G4Event* event = em->GetConstCurrentEvent();
    if (event) {
        G4int event_id = event->GetEventID();
        G4cout << "Current Event ID: " << event_id <<G4endl;
    }
}
```

`G4Step`オブジェクトから、現在の`G4Event`には直接アクセスできません。
そのため`G4EventManager`を介して現在のイベントを取得します。

## G4Trackからイベント番号を取得したい

```cpp
void MyTrackingAction::PreUserTrackingAction(const G4Track* track) {
    G4EventManager *em = G4EventManager::GetEventManager();
    const G4Event* event = em->GetConstCurrentEvent();
    if (event) {
        G4int event_id = event->GetEventID();
        G4cout << "Current Event ID: " << event_id <<G4endl;
    }
}
```

`G4Track`オブジェクトから、現在の`G4Event`には直接アクセスできません。
そのため`G4EventManager`を介して現在のイベントを取得します。

## G4Runからイベント番号を取得したい

```cpp
void MyRunAction::EndOfRunAction(const G4Run* aRun) {
    G4int n_events = aRun->GetNumberOfEvent();
    G4cout << "Total events processed in this run: " << n_events << G4endl;
}
```

`G4Run`は「イベントの集合」を表すオブジェクトです。
すでに完了したイベントたちのイベントIDを取得することはできません。
代わりに`GetNumberOfEvents`でイベント数を取得できます。
