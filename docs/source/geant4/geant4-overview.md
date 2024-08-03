# シミュレーションの流れ

Geant4にはシミュレーション進行を担当する4種類のManagerクラスがあります。
それぞれが隣り合ったManagerクラスに処理をお願いしたり、結果を受けたりする体制が組まれています。

1. ``G4RunManager``:
**G4Run**を管理するクラス。
G4**Event**Managerにイベント処理ををお願いする。
2. ``G4EventManager``:
**G4Event**を管理するクラス。
G4**Tracking**Managerにトラッキング処理をお願いする。
イベント処理が終了したらG4**Run**Managerに報告する。
3. ``G4TrackingManager``:
**G4Track**を管理するクラス。
G4**Stepping**Managerにステッピング処理をお願いする。
トッラッキング処理が終了したらG4**Event**Managerに報告する。
4. ``G4SteppingManager``:
**G4Step**を管理するクラス。
ステッピング処理を実行する。
ステッピング処理が終了したらG4**Tracking**Managerに報告する。

この中で、ユーザーが直接指示するのは``G4RunManager``だけでOKです。

## メイン関数のフローチャート

``main()``関数で``G4RunManager``がどのように処理を進めるかを、
フローチャートに整理しました。

```console
main
|-- RunManager
|    |-- Geometry::Geometry()
|    |-- Physics::Physics()
|    \-- ActionInitialization::ActionInitialization()
|        \-- ActionInitialization::Build()
|            |-- PrimaryGenerator::PrimaryGenerator()
|            |-- RunAction::RunAction()
|            |-- EventAction::EventAction()
|            |-- TrackingAction::TrackingAction()
|            \-- SteppingAction::SteppingAction()
|
|   // RunManagerを初期化
|   // 1. 測定器の設定
|   // 2. 有感検検出器の設定
|   // 3. ジオメトリのロック
|-- RunManager::Initialize()
|    |-- Geometry::Construct()
|    |   \-- Geometry::SetupVolumes()
|    \-- Geometry::ConstructSDandField()
|        |-- Sensor::Sensor{}
|        |-- SDManager::GetSDMpointer()
|        \-- Geometry::SetSensitiveDetector()
|
|   // ビームを入射
|   // 1. ラン開始時のアクションを処理
|   // 2. 入射粒子を設定
|   // 3. イベント開始時のアクションを処理
|   // 4. トラッキング開始前のアクションを処理
|   // 5. 有感検出器にヒットがあったときの処理
|   // 6. ステッピング中の処理
|   // 7. トラッキング終了後のアクションを処理
|   // 8. イベント終了時のアクションを処理
|   // 9. ラン終了時のアクションを処理
|-- RunManager::BeamOn()
|    |-- RunAction::BeginOfRunAction()
|    |-- PrimaryGenerator::GeneratePrimaries()
|    |   |-- ParticleGun{}
|    |   |    |-- SetParticleDefinition()
|    |   |    |-- SetParticleMomentumDirection()
|    |   |    |-- SetParticleEnergy()
|    |   |    \-- SetParticlePosition()
|    |   \-- GeneratePrimaryVertex()
|    |-- EventAction::BeginOfEventAction()
|    |-- TrackingAction::PreUserTrackingAction()
|    |
|    |   // ステップが有感検出器にある場合
|    |   // 1. ProcessHitsの処理
|    |   // 2. UserSteppingActionの処理
|    |-- SensorHit::ProcessHits()
|    |   \-- SensorHit{}
|    |-- SteppingAction::UserSteppingAction()
|    |-- SensorHit::ProcessHits()
|    |   \-- SensorHit{}
|    |-- SteppingAction::UserSteppingAction()
|    |
|    |   // ステップが有感検出器にない場合
|    |   // 1. UserSteppingActionの処理
|    |-- SteppingAction::UserSteppingAction()
|    |-- SteppingAction::UserSteppingAction()
|    |-- TrackingAction::PostUserTrackingAction()
|    |
|    |-- // 複数のトラックがある場合
|    |-- //   PreUserTrackingAction
|    |-- //   PreSteppingAction or ProcessHits
|    |-- //   PostUserTrackingAction
|    |-- // 上記の処理を繰り返す
|    |
|    |-- EventAction::EndOfEventAction()
|    \-- RunAction::EndOfRunAction()
|
|-- delete RunManager
|    |-- Geometry::~Geometry()
|    |-- ActionInitialization::~ActionInitialization()
|    |-- PrimaryGenerator::~PrimaryGenerator()
|    |-- SteppingAction::~SteppingAction()
|    |-- TrackingAction::~TrackingAction()
|    |-- EventAction::~EventAction()
|    \-- RunAction::~RunAction()
|
exit
```

必須クラスの他に、各種ユーザーアクションや有感検出器を設定し、
それらがどのタイミングで処理されるのかを確認しました。
それぞれのタイミングを把握することで、Geant4の理解度が格段にあがり、
どのファイルに実装すればよいかも目星がつくようになりました。

:::{hint}

このフローチャートは、Geant4をはじめるときに一番欲しかった情報かもしれないです。

:::

## ランの管理者（``G4RunManager``）

``G4RunManager``はラン（``G4Run``）の進行管理を担当します。
ランは測定の基本単位で、ビーム入射（``BeamOn``）するごとにランが1つ実行されます。``BeamOn(回数)``で、複数回のランをまとめて実行できます。

``G4RunManager``は、
シミュレーションの実験責任者的な存在なので、
ユーザーは基本的にこの人に指示を与えればOKです。

ユーザーが定義した測定器を組み立てたり、
必要な粒子と相互作用を登録してくれたり、
入射粒子の条件を設定してくれたりします。
また、ラン実行中は、測定器の構造や相互作用などが変更できないようにも
管理してくれます。

:::{note}

Geant4にはさまざまなユーザーフックが用意されています。
Event、Tracking、Steppingでどのような処理をするかは、
ユーザー自身で条件をカスタムして指定する必要があります。

:::

## イベントの管理者（``G4EventManager``）

- [](./geant4-event-manager.md)

## トラックの管理者（``G4TrackingManager``）

トラッキングの進行管理を担当します。
トラッキング（``G4Tracking``）は飛跡の基本単位です。
飛跡には始点と終点があり、その間の移動の様子（``G4Track``）を管理してくれます。

また、イベントによっては途中で二次粒子（や、さらにその二次粒子）が発生することもあります。
トラッキング処理の順番を整理してくれる担当者（``G4StackingManager``）と協力して、
1イベントの中で発生したすべての粒子の飛跡情報を測定してくれます。

## ステップの管理者（``G4SteppingManager``）

``G4SteppingManager``は、シミュレーションの中で粒子が進む最小距離であるステップ（``G4Step``）の進行管理を担当します。
ステップは、移動前、移動中、移動後の3つの状態で管理されます。

## 測定の基本はステップ（``G4Step``）

```cpp
// G4Step *aStep は事前に定義済み
G4double energy_deposit = aStep->GetTotalEnergyDeposit();
```

測定の基本単位はステップ（``G4Step``）です。
[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)や
[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)の
リファレンスを確認し、できること（得られる物理量など）を把握しておくと、
自分のアプリケーション作成に役立つはずです。

## リファレンス

- [Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)
