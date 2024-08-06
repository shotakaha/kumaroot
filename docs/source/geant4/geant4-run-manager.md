# RunManagerしたい（``G4RunManagerFactory``）

```cpp
#include "G4RunManagerFactory.hh"
auto rm = G4RunManagerFactory::CreateRunManager();

// デフォルト：マルチスレッド処理
// auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);

// シングルスレッド
// auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
```

**G4RunManager**は、ラン（``G4Run``）の進行管理を担当します。
また、実験責任者の役割を担っていて、ユーザーが``main()``関数から話しかけるのも、このインスタンスのみでOKです。

ユーザーは、RunManagerを介して、
ジオメトリ配置、
相互作用モデル、
入射粒子、
有感検出器、などの設定を指示することで、
Geant4シミュレーションを実行します。

:::{note}

以前は``G4RunManager``クラスを使っていました。
Geant4.11でマルチスレッド対応が追加されたため、
[G4RunManagerFactory](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)を通じて、インスタンスを作成するのがよいみたいです。

:::

## 実験を開始したい（``G4RunManager::Initialize``）

```cpp
rm->SetUserInitialization(new Geometry{});
rm->SetUserInitialization(new FTFP_BERT{});
rm->SetUserInitialization(new ActionInitialiation{});

rm->Initialize();
```

``Initialize``で、
ジオメトリの配置、
相互作用の定義、入射粒子の条件など、
シミュレーションに必要な初期設定が完了します。

また、ラン実行中は、測定器の構造や相互作用などが
途中で変更されないように管理してくれます。

## 粒子を入射したい（``G4RunManager::BeamOn``）

```cpp
G4int n_events = 100;
rm->BeamOn(n_events);
```

``BeamOn``で粒子を入射（発生）できます。
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
