# ユーザーアクションしたい（``G4VUserActionInitialization``）

## 親クラス

- [G4VUserActionInitialization](https://geant4.kek.jp/Reference/11.2.0/classG4VUserActionInitialization.html)

```cpp
G4VUserActionInitialization() = default;
virtual ~G4VUserActionInitialization() = default;
virtual void Build() const = 0;
virtual void BuildForMaster() const {};
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``Build()``は、ユーザーアクションを設定するための関数です。
純粋仮想関数になっているため、自作クラスでoverrideが必要です。
``BuildForMaster()``は、マルチスレッド環境で実行する場合に、
RunActionの設定が必要です。

:::{note}

ソースコードに以下のようにコメントされていました。

```cpp
// Virtual method to be implemented by the user to instantiate user
// run action class object to be used by G4MTRunManager. This method
// is not invoked in the sequential mode. The user should not use
// this method to instantiate user action classes except for user
// run action.
virtual void BuildForMaster() const {}
```

``BuildForMaster()``の中ではRunActionクラス以外は使ってはいけないようです。

:::

## ActionInitializationクラス

```cpp
// include/ActionInitialization.hh

#ifndef ActionInitialization_h
#define ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"

namespace ToyMC
{

class ActionInitialization : public G4VUserActionInitialization
{
  public:
    ActionInitialization() = default;
    ~ActionInitialization() = default;

  public:
    void BuildForMaster() const override;
    void Build() const override;
};

};  // namespace ToyMC

#endif
```

ユーザーアクションは``G4VUserActionInitialization``を継承したクラスを自作します。
そのメンバーには仮想関数として``BuildForMaster``と``Build``を定義します。

``BuildForMaster``はマルチスレッドモードのマスタースレッド用のユーザーアクションです。
とくに追加設定は必要はありません。

``Build``はワーカースレッド用のユーザーアクションです。
こちらはカスタマイズ設定が必要です。

:::

## メイン関数

```cpp
// プロジェクト名.cc
#include "G4RunManagerFactory.hh"

#include "ActionInitialization.hh"  // <-- 自作クラス

int main()
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);
}
```

メイン関数で、``ActionInitialization``のインスタンスを作成し、
``SetUserInitialization``を使ってRunManagerに登録します。



## ソースファイル

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
    // 必須の設定
    SetUserAction(new PrimaryGeneratorAction);
    // 任意の設定
    SetUserAction(new RunAction);
    SetUserAction(new EventAction);
    SetUserAction(new TrackingAction);
    SetUserAction(new SteppingAction);
    SetUserAction(new StackingAction);
}

}
```

ユーザーアクションは``Build``メソッドに追加すればよいです。
それぞれ自作クラスで定義して``SetUserAction``を使って渡します。

``PrimaryGeneratorAction``の設定は必須です。
その他のアクション設定は任意です。

:::{seealso}
- [](./geant4-primarygeneratoraction.md)
- [](./geant4-runaction.md)
- [](./geant4-eventaction.md)
- [](./geant4-trackingaction.md)
- [](./geant4-steppingaction.md)
:::
