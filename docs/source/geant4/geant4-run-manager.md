# RunManagerしたい（``G4RunManagerFactory``）

```cpp
#include "G4RunManagerFactory.hh"
auto rm = G4RunManagerFactory::CreateRunManager();

// デフォルト：マルチスレッド処理
// auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);

// シングルスレッド
// auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
```

`G4RunManager`はGeant4シミュレーション全体を統括する中核的なシングルトンです。
ジオメトリ構築（`G4VUserDetectorConstruction`）、
物理プロセスの定義（`G4VUserPhysicsList`）、および
ユーザーアクション（`G4UserRunAction`など）を登録し、
初期化、実行、終了までの一連の流れを管理します。

`G4RunManager`はクラス名の通り「実験責任者」の役割を担っており、
ユーザーは`main()`関数からこのインスタンスに話しかけて実験（シミュレーション）を指示します。

:::{note}

以前は``G4RunManager``クラスを使っていました。
Geant4.11でマルチスレッド対応が追加されたため、
[G4RunManagerFactory](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)を通じて、インスタンスを作成するのがよいみたいです。

:::

## 実験を開始したい（`G4RunManager::Initialize`）

```cpp
auto rm = new G4RunManager();
rm->SetUserInitialization(new MyGeometry{});
rm->SetUserInitialization(new MyPhysics{});
rm->SetUserInitialization(new MyAction{});
rm->Initialize();
```

ユーザーは、メインとなるファイルの中で`G4RunManager`クラスを
明示的に`new`で生成し、各種の設定をした後に、`Initialize()`や`BeamOn()`を呼び出します。
また、シミューレーション実行中は、測定器の構造や相互作用などが
途中で変更されないように管理してくれます。

## 粒子を入射したい（``G4RunManager::BeamOn``）

```cpp
G4int n_events = 100;
rm->BeamOn(n_events);
```

`BeamOn`で粒子を入射（発生）できます。
引数にイベント数を設定して、1回のランで複数回のイベントを実行できます。

## マクロで操作したい（``/run/``）

```cfg
/run/numberOfThreads 8
/run/initialize
/run/beamOn 100
```

``/run/``コマンドでマクロ操作できます。
マルチスレッドモードのアプリの場合、使用するスレッドの数もマクロから変更できます。

## シングルスレッドしたい（``G4RunManagerType::Serial``）

```cpp
#include "G4RunManagerFactory.hh"

auto* rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
```

``G4RunManagerType::Serial``で、
シングルスレッドモードに変更できます。

:::{hint}

Geant4.11からマルチスレッドに対応しましたが、
マルチスレッド処理できることと、
その出力結果が正しいかどうかは別物です。

Geant4はあくまでシミュレーションをするためのツールキットであるため、その出力結果の妥当性はユーザーが確認＆判断する必要があります。

Geant4講習会2024に参加し、エキスパートたちに聞いたところ、
マルチスレッドのアプリはデバッグが超大変だよと言ってました。
まず、シングルスレッドで十分テスト＆デバッグしてから、
マルチスレッド化にトライするのがよいそうです。

:::

## マルチスレッドしたい（``G4RunManagerType::Default``）

```cpp
#include "G4RunManagerFactory.hh"

auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);
rm->SetNumberOfThreads(8);
```

マルチスレッド機能を有効にしてビルドしていると、
デフォルトでマルチスレッドモードになります。
``SetNumberOfThreads``でスレッド数を変更できます。

:::

このクラスは、Geant4本体をビルドした環境に応じたランマネージャーを作成します。
具体的には、マルチスレッド機能が有効な場合は``G4MTRunManager``、
無効な場合は``G4RunManager``のインスタンスを作成します。

:::



## ランマネージャーを取得したい（``GetRunManager``）

```cpp
auto* rm = G4RunManager::GetRunManager();
auto* rm = G4RunManagerFactory::GetMasterRunManager();
```

作成済みのランマネージャーへのポインターを取得できます。

:::{seealso}

- [G4RunManagerFactory - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)
- [G4RunManager - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)

:::
