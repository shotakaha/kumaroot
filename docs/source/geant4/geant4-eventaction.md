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

## イベント開始したい（``BeginOfEventAction``）

```cpp
void EventAction::BeginOfEventAction(const G4Event *aEvent)
{
    // 内部変数（プライベート変数など）の初期化など
    fEnergyDeposit = 0;
}
```

``BeginOfEventAction``はイベント開始に実行されるメソッドです。
イベントごとのデータを代入するために用意した変数は、ここで初期化できます。

## イベント終了したい（``EndOfEventAction``）

```cpp
void EventAction::EndOfEventAction(const G4Event *aEvent)
{


}
```

``EndOfEventAction``はイベントの終わりに実行されるメソッドです。
イベントごとデータを集計して、イベントサマリーを表示できます。
