# イベント操作したい（`G4Event`）

```cpp
#include "G4BestUnit.hh"
#include "G4Event.hh"
#include "G4HCofThisEvent.hh"
#include "G4SDManager.hh"

void MyEventAction::EndOfEventAction(const G4Event* event)
{
    // イベント番号
    G4int eventID = event->GetEventID();

    // コレクションのIDは、初回だけ取得してメンバー変数に保存する
    if (fHitsCollectionID < 0) {
        fHitsCollectionID = G4SDManager::GetSDMpointer()->GetCollectionID("AbsorberHitsCollection");
    }

    auto* hce = event->GetHCofThisEvent();
    if (!hce) return;
    auto* hitsCollection = static_cast<MyHitsCollection*>(hce->GetHC(fHitsCollectionID));
    if (!hitsCollection) return;

    // ヒットごとのエネルギー付与を合計する
    G4double totalEdep = 0.;
    for (std::size_t i = 0; i < hitsCollection->entries(); ++i) {
        totalEdep += (*hitsCollection)[i]->GetEdep();
    }

    G4cout << "Event " << eventID << ": total energy deposit = "
           << G4BestUnit(totalEdep, "Energy") << G4endl;
}
```

`G4Event`は「ひとつのイベント」を表すクラスです。
ユーザーが`G4Event`を直接インスタンス化することはありません。

このクラスは、ユーザーアクション設定の
[UserEventAction](geant4-user-eventaction)において、
とくにイベントの終了時（`EndOfEventAction`）に、
イベント番号やヒット情報を取得する際に使用します。
`MyEventAction`や`MyHitsCollection`は、ユーザーが定義したクラスです。
`fHitsCollectionID`は、コンストラクタで`-1`に初期化しておきます。

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

- [G4Event](https://geant4.kek.jp/Reference/11.4.0/classG4Event.html)
