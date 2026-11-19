# ユーザーアクションしたい（`G4VUserActionInitialization`）

`G4VUserActionInitialization`は、ユーザーアクション（`RunAction`、`EventAction`など）をまとめて初期化するための抽象基底クラスです。
マルチスレッド環境に対応する枠組みとしてv9.6で導入されました。

:::{note}

v9.6以前は`SetUserAction`をmain関数などで、
個別に直接呼び出して、ユーザーアクションを初期化していました。

:::

## 親クラス（`public G4VUserActionInitialization`）

- [G4VUserActionInitialization](https://geant4.kek.jp/Reference/11.2.0/classG4VUserActionInitialization.html)

```cpp
class G4VUserActionInitialization {
  public:
    G4VUserActionInitialization() = default;
    virtual ~G4VUserActionInitialization() = default;

  public:
    virtual void Build() const = 0;
    virtual void BuildForMaster() const {};
};
```

親クラス（`G4VUserActionInitialization`）の主要なメンバー関数を抜粋しました。
コンストラクターとデストラクターは、親クラスの設定を引き継げばOKです。
`Build()`は、ユーザーアクションを設定するための純粋仮想関数で、必ずオーバーライドが必要です。
`BuildForMaster()`は、マルチスレッド環境で実行する場合に、
マスタースレッドで呼び出される関数です。
通常は、ここで`RunAction`のみを設定します。

:::{note}

ソースコードに次のようなコメントが残っていました。

```cpp
// Virtual method to be implemented by the user to instantiate user
// run action class object to be used by G4MTRunManager. This method
// is not invoked in the sequential mode. The user should not use
// this method to instantiate user action classes except for user
// run action.
virtual void BuildForMaster() const {}
```

コメントによると、`BuildForMaster()`の中ではRunActionクラス以外は使うべきではないとされています。

:::

## ActionInitialization

ユーザーアクションの初期化は、`G4VUserActionInitialization`を継承したクラスで行います。
`Build`は必ず定義します。
`BuildForMaster`は、マルチスレッドで`RunAction`を設定する場合に定義します（デフォルトでは何もしません）。

## ActionInitialization::Build

```cpp
void ActionInitialization::Build() const {
    // 入射粒子の設定（必須）
    SetUserAction(new PrimaryGeneratorAction{});

    // 各アクションの設定（必要に応じて追加）
    // ラン処理
    SetUserAction(new RunAction{});

    // イベント処理
    SetUserAction(new EventAction{});

    // トラッキング処理
    SetUserAction(new TrackingAction{});

    // ステップ処理
    SetUserAction(new SteppingAction{});

    // スタッキング処理
    SetUserAction(new StackingAction{});
}
```

`Build()`では、ワーカースレッド用のユーザーアクションを登録します。
主に、入射粒子（`PrimaryGeneratorAction`）、ラン処理（`RunAction`）、イベント処理（`EventAction`）などを`SetUserAction(...)`で設定します。

:::{seealso}

詳しくは

- [](./geant4-user-primarygeneratoraction.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)

に整理しました。
:::

## ActionInitialization::BuildForMaster

```cpp
void ActionInitialization::BuildForMaster() const {
    // マスタースレッド用のRunActionを登録
    SetUserAction(new RunAction{});
}
```

`BuildForMaster()`は、マルチスレッド環境でマスタースレッドだけが呼び出す初期化関数です。
シーケンシャルモードでは呼び出されません。
通常は`RunAction`のみを設定します。マスター側の`RunAction`では、ワーカーの結果の集計や出力などを担当させます。

:::{note}

マルチスレッドでは`RunAction`を`Build`と`BuildForMaster`の両方で設定します。
マスター用とワーカー用は別のインスタンスになります。

:::

## メイン関数（`main`）

```cpp
// プロジェクト名.cc（ここではToyMC.cc）

// ユーザー定義クラス
#include "ActionInitialization.hh"

// Geant4のクラス
#include "G4RunManagerFactory.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    // ジオメトリの設定（省略）
    // 物理モデルの設定（省略）

    // ユーザーアクションの設定
    rm->SetUserInitialization(new ActionInitialization{});

    // 実験開始（省略）
    rm->Initialize();
    rm->BeamOn(10);
    delete rm;
    return 0;
}
```

`main`関数での最小構成です。
`SetUserInitialization`に`ActionInitialization`を渡して、ユーザーアクション一式をRunManagerに登録します。

:::{seealso}

詳しくは
[](./geant4-main.md)
に整理しました。

:::

## ユーザー定義クラス（`ActionInitialization`）

そのまま流用できるテンプレートを示します。

### ヘッダーファイル（`include/ActionInitialization.hh`）

```cpp
// include/ActionInitialization.hh

#ifndef ACTION_INITIALIZATION_HH
#define ACTION_INITIALIZATION_HH 1

#include "G4VUserActionInitialization.hh"

// クラス名や名前空間は必要に応じて変更してください
namespace ToyMC
{

class ActionInitialization : public G4VUserActionInitialization
{
  public:
    ActionInitialization() = default;
    ~ActionInitialization() override = default;

  public:
    void BuildForMaster() const override;
    void Build() const override;
};

}  // namespace ToyMC

#endif  // ACTION_INITIALIZATION_HH
```

:::{note}

デフォルトのコンストラクター／デストラクターは省略できます。
ここでは、デフォルトを使っていることが分かるように明示しています。

:::

### ソースファイル（`src/ActionInitialization.cc`）

```cpp
// src/ActionInitialization.cc

// ユーザー定義クラス
#include "ActionInitialization.hh"
#include "PrimaryGeneratorAction.hh"

// 必要に応じて追加
#include "RunAction.hh"
#include "EventAction.hh"
#include "TrackingAction.hh"
#include "SteppingAction.hh"
#include "StackingAction.hh"

namespace ToyMC
{

void ActionInitialization::BuildForMaster() const {
    SetUserAction(new RunAction{});
}

void ActionInitialization::Build() const
{
    // 入射粒子の設定（必須）
    SetUserAction(new PrimaryGeneratorAction{});
    // 各ユーザーアクションの設定（必要なアクションを追加）
    SetUserAction(new RunAction{});
    SetUserAction(new EventAction{});
    SetUserAction(new TrackingAction{});
    SetUserAction(new SteppingAction{});
    SetUserAction(new StackingAction{});
}

}  // namespace ToyMC
```
