# ユーザーアクションしたい（`G4VUserActionInitialization`）

```cpp
// 疑似コード
class ActionInitialization : public G4VUserActionInitialization {
  public:
    void Build() const override;           // 必須：ワーカースレッド用
    void BuildForMaster() const override;  // 任意：マスタースレッド用
};

void ActionInitialization::Build() const {
    // ワーカースレッドごとに、ユーザーアクションを登録する
    SetUserAction(new PrimaryGeneratorAction{});
    SetUserAction(new RunAction{});
    SetUserAction(new EventAction{});
}

void ActionInitialization::BuildForMaster() const {
    // マスタースレッドでは、RunActionだけを登録する
    SetUserAction(new RunAction{});
}
```

`G4VUserActionInitialization`は、ユーザーアクション（`RunAction`、`EventAction`など）をまとめて初期化するための基底クラスです。
マルチスレッド環境に対応する枠組みとして、v9.6で導入されました。

:::{seealso}

v9.6以前は、main関数RunManagerが`SetUserAction`を個別に直接呼び出して、ユーザーアクションを初期化していました。
v9.6.4のサンプル`examples/basic/B1/exampleB1.cc`にもその名残がありました。

```cpp
// v9.6.4: examples/basic/B1/exampleB1.cc（抜粋）
G4RunManager* runManager = new G4RunManager;

runManager->SetUserInitialization(new B1DetectorConstruction());
G4VModularPhysicsList* physicsList = new QBBC;
runManager->SetUserInitialization(physicsList);

// main関数で、ユーザーアクションを直接登録する
runManager->SetUserAction(new B1PrimaryGeneratorAction());
runManager->SetUserAction(new B1SteppingAction());
runManager->SetUserAction(new B1EventAction());
runManager->SetUserAction(new B1RunAction());

runManager->Initialize();
```

:::

## 初期化クラスを作りたい（`ActionInitialization`）

```cpp
class ActionInitialization : public G4VUserActionInitialization {
  // ...
};
```

`G4VUserActionInitialization`を継承したクラスを作成します。
クラス名は`ActionInitialization`など、わかりやすい名前にします。
コンストラクターとデストラクターは、デフォルトのままで構いません。

`Build()`は必ず実装します。
`BuildForMaster()`は、マルチスレッドで`RunAction`を登録する場合に実装します。
どちらも`const`な仮想関数なので、派生クラスでオーバーライドするときも`const`を付けます。

:::{note}

親クラスのデストラクターに`virtual`が付いているのは、`RunManager`が基底クラスのポインターで削除するためです。
`virtual`がないと、派生クラスのデストラクターが呼ばれません。

:::

## ワーカースレッドしたい（`Build`）

```cpp
void ActionInitialization::Build() const {
    // 入射粒子の設定（必須）
    SetUserAction(new PrimaryGeneratorAction{});

    // 各アクションの設定（必要に応じて追加）
    SetUserAction(new RunAction{});       // ラン処理
    SetUserAction(new EventAction{});     // イベント処理
    SetUserAction(new TrackingAction{});  // トラッキング処理
    SetUserAction(new SteppingAction{});  // ステップ処理
    SetUserAction(new StackingAction{});  // スタッキング処理
}
```

`Build()`では、ワーカースレッドごとに使うユーザーアクションを登録します。
入射粒子（`PrimaryGeneratorAction`）は必ず登録します。
ラン処理（`RunAction`）やイベント処理（`EventAction`）などは、必要なものだけ`SetUserAction(...)`で登録します。

マルチスレッドでは、`Build()`がワーカースレッドの数だけ呼ばれます。
そのため、各スレッドに独立したオブジェクトが作られます。

:::{seealso}

詳しくは

- [](./geant4-user-primarygeneratoraction.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)

に整理しました。

:::

## マスタースレッドしたい（`BuildForMaster`）

```cpp
void ActionInitialization::BuildForMaster() const {
    // マスタースレッド用のRunActionを登録する
    SetUserAction(new RunAction{});
}
```

`BuildForMaster()`は、マルチスレッド環境でマスタースレッドだけが呼び出す関数です。
シーケンシャルモードでは呼び出されません。
通常は`RunAction`のみを登録します。マスター側の`RunAction`では、ワーカーの結果の集計や出力などを担当させます。

:::{note}

マルチスレッドでは、`RunAction`を`Build()`と`BuildForMaster()`の両方で登録します。
マスター用とワーカー用は、別のインスタンスになります。

:::

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

## 親クラスのメソッドを確認したい

親クラス（`G4VUserActionInitialization`）の主要なメンバー関数は、次のとおりです。

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

- `Build()`は純粋仮想関数です。自作クラスで必ず`override`します。
- `BuildForMaster()`は仮想関数で、既定では何もしません。マルチスレッドで`RunAction`を登録するときだけ`override`します。
- コンストラクターとデストラクターは、親クラスの設定をそのまま引き継げばOKです。

親クラスの詳しい説明は、[G4VUserActionInitialization](https://geant4.kek.jp/Reference/11.2.0/classG4VUserActionInitialization.html)を参照してください。

## 自作クラスの例を見たい（`ActionInitialization`）

そのまま流用できるテンプレートを示します。

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

`#ifndef`から`#endif`は、インクルードガードです。
同じヘッダーを複数回読み込んでも、クラスが二重に定義されないようにします。

デフォルトのコンストラクター／デストラクターは省略できます。
ここでは、デフォルトを使っていることが分かるように明示しています。

:::

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

## main()関数に登録したい

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
    rm->SetUserInitialization(new ToyMC::ActionInitialization{});

    // 実験開始（省略）
    rm->Initialize();
    rm->BeamOn(10);
    delete rm;
    return 0;
}
```

`SetUserInitialization()`に`ActionInitialization`を渡して、ユーザーアクション一式をRunManagerに登録します。
`G4RunManagerFactory::CreateRunManager()`は、ビルド設定に応じてマルチスレッドまたはシーケンシャルのRunManagerを作成します。
どちらの場合も、`main()`関数の書き方は変わりません。

:::{note}

`new`で作成したオブジェクトを`SetUserInitialization()`に渡すと、所有権は`RunManager`に移ります。
そのため、`main()`関数で`delete`する必要はありません。

:::

:::{seealso}

詳しくは

- [](./geant4-main.md)

に整理しました。

:::
