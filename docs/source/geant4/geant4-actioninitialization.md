# ユーザーアクションしたい（``G4VUserActionInitialization``）

```cpp
// include/ActionInitialization.hh
#ifndef ActionInitialization_H
#define ActionInitialization_H 1

#include "G4VUserActionInitialization.hh"

namespace プロジェクト名
{
class ActionInitialization : public G4VUserActionInitialization
{
    public:
        ActionInitialization();
        virtual ~ActionInitialization();
        virtual void BuildForMaster() const;
        virtual void Build() const;

}
}  // プロジェクト名
#endif
```

ユーザーアクションは``G4VUserActionInitialization``を継承したクラスを自作します。
そのメンバーには仮想関数として``BuildForMaster``と``Build``を定義します。

``BuildForMaster``はマルチスレッドモードのマスタースレッド用のユーザーアクションです。
とくに追加設定は必要はありません。

``Build``はワーカースレッド用のユーザーアクションです。
こちらはカスタマイズ設定が必要です。

```cpp
// src/ActionInitialization.cc
#include "ActionInitialization.hh"   // <-- G4VUserActionInitializationを継承した自作クラス

#include "PrimaryGeneratorAction.hh"  // <-- G4VUserPrimaryGeneratorActionを継承した自作クラス
#include "EventAction.hh"             // <-- G4UserEventActionを継承した自作クラス
#include "TrackingAction.hh"          // <-- G4UserTrackingActionを継承した自作クラス
#include "SteppingAction.hh"          // <-- G4UserSteppingActionを継承した自作クラス

namespace プロジェクト名
{

ActionInitialization::ActionInitialization() {;}
ActionInitialization::~ActionInitialization() {;}

////////////////////////////////////////////////////////////////////////////////
void ActionInitialization::BuildForMaster() const {;}

////////////////////////////////////////////////////////////////////////////////
void ActionInitialization::Build() const
{
    SetUserAction(new PrimaryGeneratorAction);
    SetUserAction(new EventAction);
    SetUserAction(new TrackingAction);
    SetUserAction(new SteppingAction);
}

}
```
