# シミュレーションの流れ

Geant4のシミュレーションは、
検出器の構築、
物理プロセスの設定、
初期粒子の生成、
シミュレーションの実行、
そして検出器応答の取得という要素で構成されています。

これらの処理を効率的に管理するため、
シミュレーション進行を担当する4種類のManagerクラスが用意されており、
それぞれが隣接するクラスに処理を依頼したり、結果を受け取ったりする体制になっています。

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

## メイン関数のシーケンス図

`main`関数で`G4RunManager`がどのように処理を進めるかを確認し、
シーケンス図に整理しました。

:::{mermaid}

sequenceDiagram
    autonumber
    participant Main as main()
    participant RM as G4RunManager
    participant Geo as Geometry
    participant Phys as Physics
    participant AI as ActionInitialization
    participant PG as PrimaryGenerator
    participant RA as RunAction
    participant EA as EventAction
    participant TA as TrackingAction
    participant SA as SteppingAction
    participant Hit as SensorHit
    participant Gun as ParticleGun

    Main ->> RM: new G4RunManager()
    RM ->> Geo: Geometry()
    RM ->> Phys: Physics()
    RM ->> AI: ActionInitialization()
    AI ->> PG: Build()
    AI ->> RA: Build()
    AI ->> EA: Build()
    AI ->> TA: Build()
    AI ->> SA: Build()

    RM ->> RM: Initialize()
    RM ->> Geo: Construct()
    Geo ->> Geo: SetupVolumes()
    RM ->> Geo: ConstructSDandField()
    Geo ->> Hit: SetSensitiveDetector()

    RM ->> RM: BeamOn()
    RM ->> RA: BeginOfRunAction()
    RM ->> PG: GeneratePrimaries()
    PG ->> Gun: ParticleGun{}
    Gun ->> Gun: SetParticleDefinition()
    Gun ->> Gun: SetParticleMomentumDirection()
    Gun ->> Gun: SetParticleEnergy()
    Gun ->> Gun: SetParticlePosition()
    PG ->> PG: GeneratePrimaryVertex()

    RM ->> EA: BeginOfEventAction()
    RM ->> TA: PreUserTrackingAction()

    loop StepLoop
        alt Step in Sensitive Detector
            RM ->> Hit: ProcessHits()
            RM ->> SA: UserSteppingAction()
        else Step not in Sensitive Detector
            RM ->> SA: UserSteppingAction()
        end
    end

    RM ->> TA: PostUserTrackingAction()
    RM ->> EA: EndOfEventAction()
    RM ->> RA: EndOfRunAction()

    Main ->> RM: delete RunManager
    RM ->> Geo: ~Geometry()
    RM ->> AI: ~ActionInitialization()
    RM ->> PG: ~PrimaryGenerator()
    RM ->> SA: ~SteppingAction()
    RM ->> TA: ~TrackingAction()
    RM ->> EA: ~EventAction()
    RM ->> RA: ~RunAction()

:::

必須クラスの他に、各種ユーザーアクションや有感検出器を設定し、
それらがどのタイミングで処理されるのかを確認しました。
それぞれのタイミングを把握することで、Geant4の理解度が格段にあがり、
どのファイルに実装すればよいかも目星がつくようになりました。

:::{hint}

このシーケンス図は、Geant4をはじめるときに一番欲しかった情報かもしれないです。

:::

## ランの管理者（``G4RunManager``）

- [](./geant4-run-manager.md)

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

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## リファレンス

- [Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)
