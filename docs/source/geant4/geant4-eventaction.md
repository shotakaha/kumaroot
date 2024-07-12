# イベントアクションしたい（``G4UserEventAction``）

イベントごとのデータを収集したい場合は、
``G4UserEventAction``クラスを継承したクラスを作成します。

```cpp

#include "G4UserEventAction.hh"

#include "RunAction.hh"

class EventAction: public G4UserEventAction
{
    public:
        EventAction(RunAction *aAction);
        ~EventAction() override = default;

        void BeginOfEventAction(const G4Event *aEvent) override;
        void EndOfEventAction(const G4Event *aEvent) override;
    private:
        fEnergyDeposit = -1;
}
```

:::{seealso}

- [](./geant4-event.md)
- [](./geant4-analysismanager.md)

:::


## 初期化したい（``EventAction``）

```cpp
EventAction::EventAction(RunAction* /* aAction */)
{

}
```

## イベント開始したい（``BeginOfEventAction``）

```cpp
void EventAction::BeginOfEventAction(const G4Event *aEvent)
{
    // イベント操作
    aEvent->Print();
    G4int event_id = aEvent->GetEventID();
    G4String random_status = aEvent->GetRandomNumberStatus();

    // 内部変数（プライベート変数など）の初期化など
    fEnergyDeposit = 0;
}
```

``BeginOfEventAction``はイベント開始に実行されるメソッドです。
イベントごとのデータを代入するために用意した変数は、ここで初期化できます。

:::{note}

ヒット情報（``G4THitMap``や``G4THitsCollection``）はここで初期化します。

:::

:::{seealso}

- [](./geant4-event.md)

:::


## イベント終了したい（``EndOfEventAction``）

```cpp
void EventAction::EndOfEventAction(const G4Event *aEvent)
{

    auto am = G4AnalysisManager::Instance();
    G4int id1 = am->GetH1Id("名前");
    am->FillH1(id1, 値);

}
```

``EndOfEventAction``はイベントの終わりに実行されるメソッドです。
イベントごとデータを集計して、イベントサマリーを表示できます。
