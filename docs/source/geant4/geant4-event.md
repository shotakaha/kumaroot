# イベント操作したい（`G4Event`）

```cpp
void MyEventAction::EndOfEventAction(const G4Event* event) {
    G4int eventID = event->GetEventID();
    auto hce = event->GetHCofThisEvent();

    if (hce) {
        auto hitsCollection = static_cast<MyHitsCollection*>(hce->GetHC(hitsCollectionID));
        // ヒット情報の解析など
    }
}
```

`G4Event`は「ひとつのイベント」を表すクラスです。
ユーザーが`G4Event`を直接インスタンス化することはありません。

このクラスは、ユーザーアクション設定の
[UserEventAction](./geant4-user-eventaction.md)において、
とくにイベントの終了時（`EndOfEventAction`）に、
イベント番号やヒット情報を取得する際に使用します。

```{toctree}
---
maxdepth: 1
---
geant4-event-eventid
geant4-event-primaryvertex
geant4-event-random
geant4-event-hc
geant4-event-trajectorycontainer
geant4-event-manager
```

## リファレンス

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)
