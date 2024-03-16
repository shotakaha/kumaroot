# シミュレーションの流れ

Geant4シミュレーションにはさまざまな管理者（manager）が登場し、シミュレーションの進行管理を手伝ってくれます。
また、測定の基本単位は「ラン（Run）」で、実際の素粒子物理学分野の実験手順を、パソコンの中で再現した作りになっています。

詳細は[Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)を参照してください。

## メイン関数

```cpp
int main()
{
    auto runManager = G4RunManagerFactory::CreateRunManager();
    runManager->SetUserInitialization(new DetectorConstruction);  // <-- G4VUserDetectorConstructionを継承した自作クラス（必須）
    runManager->SetUserInitialization(new PhysicsList);    // <-- G4ModularPhysicsList もしくはG4VUserPhysicsListを継承した自作クラス（必須）
    runManager->SetUserInitialization(new ActionInitialization);  // <-- ユーザーアクションの設定>

    // ActionInitializationの内容
    // SetUserAction(PrimaryGeneratorAction);  // <-- G4VUserPrimaryGeneratorAction>
    // SetUserAction(RunAction);  // <-- G4UserRunActionを継承したクラス
    // SetUserAction(EventAction);  // <-- G4UserEventActionを継承したクラス
    // SetUserAction(TrackingAction);  // <-- G4UserTrackingActionを継承したクラス
    // SetUserAction(SteppingAction);  // <-- G4UserSteppingActionを継承したクラス

    runManager->Initialize();
    G4int nEvents
    runManager->BeamOn(nEvents);

    delete runManager;
}
```



## 管理者の体制

1. ``G4RunManager``: G4**Event**Managerにイベント処理ををお願いする。
2. ``G4EventManager``: G4**Tracking**Managerにトラッキング処理をお願いする。終了したらG4**Run**Managerに報告する。
3. ``G4TrackingManager``: G4**Stepping**Managerにステッピング処理をお願いする。終了したらG4**Event**Managerに報告する。
4. ``G4SteppingManager``: ステッピング処理を実行する。終了したらG4**Tracking**Managerに報告する。

シミュレーションの中で管理者は上のような順番になっています。
それぞれが隣り合った管理者に処理をお願いしたり、報告を受けたりする体制となっています。

## ランの管理（``G4RunManager``）

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

イベントの進行管理を担当します。
イベント（``G4Event``）は、素粒子反応事象の基本単位です。
1回のランの中で、複数のイベント（＝素粒子反応）が発生します。

1イベントごとに、入射した粒子の情報（粒子の種類、位置、方向、エネルギー）や、
生成された粒子ごとの飛跡（``G4Track``）を管理してくれます。

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
