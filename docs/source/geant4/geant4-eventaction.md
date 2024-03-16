# イベントアクションしたい（``G4UserEventAction``）

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

```cpp
void EventAction::BeginOfEventAction(const G4Event *aEvent)
{
    // 内部変数（プライベート変数など）の初期化など
    fEnergyDeposit = 0;
}
```

```cpp
void EventAction::EndOfEventAction(const G4Event *aEvent)
{


}
```
