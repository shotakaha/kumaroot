# メイン関数したい（`main()`）

```cpp
// ユーザー定義クラスを読み込む
#include "Geometry.hh"
#include "ActionInitialization.hh"

// Geant4のクラスを読み込む
#include "G4RunManagerFactory.hh"
#include "G4UIExecutive.hh"
#include "G4UImanager.hh"
#include "G4VisExecutive.hh"
#include "FTFP_BERT.hh"    // 標準の物理モデルのひとつ

int main(int argc, char** argv)
{
    // 引数がなければ対話モード
    G4UIExecutive* ui = nullptr;
    if (argc == 1) {
        ui = new G4UIExecutive(argc, argv);
    }

    auto rm = G4RunManagerFactory::CreateRunManager();

    // ジオメトリの設定
    auto geometry = new Geometry{};
    rm->SetUserInitialization(geometry);

    // 物理モデルの設定
    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);

    // ユーザーアクションの設定
    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);

    // 可視化の設定
    auto vis = new G4VisExecutive(argc, argv);
    vis->Initialize();

    auto UImanager = G4UImanager::GetUIpointer();
    if (!ui) {
        // バッチモード: 引数で指定したマクロを実行する
        UImanager->ApplyCommand("/control/execute " + G4String(argv[1]));
    }
    else {
        // 対話モード: 初期化マクロを実行してから、セッションを開始する
        UImanager->ApplyCommand("/control/execute init_vis.mac");
        ui->SessionStart();
        delete ui;
    }

    delete vis;
    delete rm;
    return 0;
}
```

Geant4でシミュレーションを実行する`main()`関数の構成例です。
引数がなければ対話モード、引数があれば指定したマクロを実行するバッチモードになります。
この切り替えは、ユーザーが`main()`関数に書く必要があります。

対話モードとバッチモードで、設定は同じです。
そのため、`main()`は1つにまとめ、`argc`で分岐しています。
Geant4の付属サンプル（`B1`など）も、この書き方です。

このサンプルでは、次の3つの要素を設定しています。

1. `geometry` : `G4VUserDetectorConstruction`を継承したユーザー定義クラス
2. `physics` : `FTFP_BERT`（Geant4標準の物理モデルのひとつ）
3. `actions` : `G4VUserActionInitialization`を継承したユーザー定義クラス

:::{seealso}

- [](./geant4-user-detectorconstruction.md)
- [](./geant4-user-physicslist.md)
- [](./geant4-user-actioninitialization.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)

:::

## 引数したい（`argc`と`argv`）

```cpp
int main(int argc, char** argv)
{
    G4UIExecutive* ui = nullptr;
    if (argc == 1) {
        ui = new G4UIExecutive(argc, argv);
    }

    auto vis = new G4VisExecutive(argc, argv);
    vis->Initialize();
    // ...
}
```

`argc`は引数の数で、プログラム名も含みます。
`argv[0]`はプログラム名、`argv[1]`は最初の引数です。

たとえば`./myGeant4App run1.mac`と実行すると、`argc`は`2`、`argv[1]`は`"run1.mac"`になります。
引数がないとき（`argc == 1`）だけ、`G4UIExecutive`を作成して対話モードにしています。

`G4UIExecutive`と`G4VisExecutive`には、`argc`と`argv`をそのまま渡しています。
Geant4が引数を解釈するためです。
引数の扱いは、アプリケーションごとに変えられます。
たとえば、付属サンプルの`B4`は、`-m`オプションでマクロを指定します。

## バッチ処理したい（マクロを引数で実行）

```cpp
if (!ui) {
    // バッチモード: 引数で指定したマクロを実行する
    UImanager->ApplyCommand("/control/execute " + G4String(argv[1]));
}
```

バッチモードでは、`argv[1]`のマクロを`/control/execute`で実行します。
マクロは、実行するときのカレントディレクトリからの相対パスで探されます。
マクロがあるディレクトリで実行するか、絶対パスで指定してください。

このサンプルは`rm->Initialize()`を呼びません。
そのため、バッチモードで使うマクロには`/run/initialize`が必要です。

```cfg
/run/initialize
/run/beamOn 100
```

:::{note}

マクロが見つからないときは、エラーが表示されます。
ただし、終了コードは`0`のままです。
スクリプトで失敗を検出する場合は、出力も確認してください。

:::

## クラスが呼ばれる順番を確認したい

以下は、仮想的な例です。
実際の順番は、Geant4のバージョンやアプリケーションの構成によって変わります。

```cpp
// 疑似コード
G4RunManagerFactory::CreateRunManager();
new Geometry{};
new FTFP_BERT{};
new ActionInitialization{};

// rm->Initialize() で、検出器をセットアップする
Geometry::Construct();
Geometry::ConstructSDandField();

// rm->BeamOn() で、入射粒子をセットアップし、イベントを実行する
ActionInitialization::Build();
new PrimaryGenerator{};
PrimaryGenerator::GeneratePrimaries();

// 有感検出器での処理
TrackerSD::Initialize();
TrackerSD::ProcessHits();   // ステップごとに呼ばれる
TrackerSD::EndOfEvent();

delete rm;
delete geometry;
delete physics;
delete actions;
```

流れを理解するための例として読んでください。
`GeneratePrimaries()`は、イベントごとに呼ばれます。

## リファレンス

- [How to Define the main() Program](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html)
