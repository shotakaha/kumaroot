# イベント番号をしりたい（``G4Event::EventID``）

```cpp
// G4Event *aEvent;
G4int event_id = aEvent->GetEventID();
```

## イベント番号を出力したい（``G4Event::Print``）

```cpp
// G4Event *aEvent
aEvent->Print();
```

``G4Event::Print()``を確認したら、イベントIDを出力する関数でした。

:::{seealso}

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)

:::

## G4Stepからイベント番号をしりたい

```cpp
G4EventManager* em = G4EventManager::GetEventManager();
G4Event* event = em->GetConstCurrentEvent();
G4int event_id = event->GetEventID();
```

``G4Step``オブジェクトから、現在の``G4Event``には直接アクセスできません。
しかたがないので、``G4RunManager``オブジェクトから直接``G4Event``にアクセスし、イベントIDを取得します。
