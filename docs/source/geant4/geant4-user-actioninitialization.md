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

ユーザーアクションの初期化には
`G4VUserActionInitialization`を継承したクラスを自作します。
このクラスの中で、`Build`と`BuildForMaster`を定義する必要があります。

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

`Build()`
にはワーカースレッド用のユーザーアクションを登録します。
ここでは主に、
入射粒子の設定（`PrimaryGeneratorAction`）、
ラン処理の設定（`RunAction`）、
イベント処理の設定（`EventAction`）などを
`SetUserAction(...)`を使って設定します。

:::{seealso}

詳しくは

- [](./geant4-primarygeneratoraction.md)
- [](./geant4-runaction.md)
- [](./geant4-eventaction.md)
- [](./geant4-trackingaction.md)
- [](./geant4-steppingaction.md)

に整理しました。
:::

## ActionInitialization:BuildForMaster

```cpp
void ActionInitialization::BuildForMaster() const {
    // マスタースレッド用のRunActionを登録
    SetUserAction(new RunAction{});
}
```

`BuildForMaster()`はマルチスレッド環境のマスタースレッド専用の初期化関数です。
シーケンシャルモードでは呼び出されません。
通常はRunActionのみをここで設定し、ラン単位での集計処理のほか、
ファイル操作などを設定します。

:::{note}

`RunAction`の設定は、`Build`と`BuildForMaster`の両方に必要です。

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
    rm->BeamOn();
    delete rm;
    return 0;
}
```

メイン関数でユーザーアクションを設定する最小構成です。
`SetUserInitialization`を使って、ユーザーアクション一式（`ActionInitialization`）をRunManagerに登録しています。

:::{seealso}

詳しくは
[](./geant4-main.md)
に整理しました。

:::

## ユーザー定義クラス（`ActionInitialization`）

コピペして利用できるテンプレートを作成しました。

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
    ~ActionInitialization() = default;

  public:
    void BuildForMaster() const override;
    void Build() const override;
};

};  // namespace ToyMC

#endif  // ACTION_INITIALIZATION_HH
```

:::{note}

デフォルトコンストラクター／デストラクターを使う場合は、省略可能です。
ここではデフォルトであることを忘れないために明示してあります。

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

//////////////////////////////////////////////////
void ActionInitialization::BuildForMaster() const {
    SetUserAction(new RunAction{});
}
//////////////////////////////////////////////////

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
