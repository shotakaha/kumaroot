# シミュレーションの流れ

Geant4のシミュレーションの全体の流れを、1枚のシーケンス図にまとめました。

:::{hint}

このシーケンス図は、Geant4をはじめるときに一番欲しかった情報かもしれません。

:::

## シーケンス図

時間は上から下へ進みます。実線の矢印は呼び出しを表し、`opt`で囲んだ部分は任意です。

:::{mermaid}

sequenceDiagram
    autonumber
    participant Main as main()
    participant RM as G4RunManager
    participant EM as G4EventManager
    participant TM as G4TrackingManager
    participant SM as G4SteppingManager
    participant DC as DetectorConstruction
    participant PL as PhysicsList
    participant AI as ActionInitialization
    participant PG as PrimaryGeneratorAction
    participant RA as RunAction
    participant EA as EventAction
    participant TA as TrackingAction
    participant SA as SteppingAction
    participant SD as SensitiveDetector

    Note over Main,AI: ① main()で準備する
    Main ->> RM: new G4RunManager()
    Main ->> DC: new DetectorConstruction()
    Main ->> RM: SetUserInitialization(DC)
    Main ->> PL: new PhysicsList()
    Main ->> RM: SetUserInitialization(PL)
    Main ->> AI: new ActionInitialization()
    Main ->> RM: SetUserInitialization(AI)

    Note over RM,SD: ② Initialize()で検出器と物理を構築する
    RM ->> PL: ConstructParticle() / ConstructProcess()
    RM ->> DC: Construct()
    RM ->> DC: ConstructSDandField()
    opt 有感検出器（SD）を使う場合
        DC ->> SD: SetSensitiveDetector()
    end

    Note over RM,SA: ③ BeamOn()で実行する
    RM ->> RA: BeginOfRunAction()
    loop 各イベント
        RM ->> PG: GeneratePrimaries()
        RM ->> EM: ProcessOneEvent()
        EM ->> EA: BeginOfEventAction()
        loop 各トラック（粒子ごと）
            EM ->> TM: ProcessOneTrack()
            opt TrackingActionを使う場合
                TM ->> TA: PreUserTrackingAction()
            end
            loop 各ステップ
                TM ->> SM: Stepping()
                opt SDが付いた体積の中
                    SM ->> SD: ProcessHits()
                end
                opt SteppingActionを使う場合
                    SM ->> SA: UserSteppingAction()
                end
            end
            opt TrackingActionを使う場合
                TM ->> TA: PostUserTrackingAction()
            end
        end
        EM ->> EA: EndOfEventAction()
    end
    RM ->> RA: EndOfRunAction()

    Note over Main,RM: ④ 終了する
    Main ->> RM: delete RunManager
    RM ->> RM: 登録したユーザークラスも削除

:::

## シーケンス図の解説

この図は、準備、構築、実行、終了の順に進みます。
`main()`では、`RunManager`を作り、検出器や物理プロセスなどを渡します。
`Initialize()`で検出器と物理プロセスを組み立てたあと`BeamOn()`で実行します。

シミュレーションの実行は入れ子構造になっています。
`BeamOn()`1回分が**Run**で、その中に初期粒子1個分の処理である**Event**が並びます。
Eventの中には粒子1個の追跡である**Track**が並び、Trackの中には1ステップ分の**Step**が並びます。

この入れ子構造に対して、Managerクラスが分担されています。
**RunManager**がEventの処理をEventManagerに任せ、**EventManager**がTrackの処理をTrackingManagerに任せ、**TrackingManager**がStepの処理を**SteppingManager**に任せます。
ユーザーが直接操作するのはRunManagerだけで、残りはGeant4が自動的に呼び出してくれます。

## 自作アプリ開発のポイント

自作アプリ開発では、まず5つのクラスを用意します。
`main()`、`DetectorConstruction`、`PhysicsList`、`ActionInitialization`、`PrimaryGeneratorAction`です。

`main()`は`RunManager`を作って必須クラスを渡すだけです。
検出器の形状と材質は`DetectorConstructionのConstruct()`で、使う物理プロセスは`PhysicsList`の`ConstructProcess()`で決めます。
初期粒子は`PrimaryGeneratorAction`の`GeneratePrimaries()`で作ります。
`ActionInitialization`は、これらと任意クラスを登録する場所です。

任意クラスは、必要になったときだけ追加します。
`RunAction`、`EventAction`、`TrackingAction`、`SteppingAction`は`ActionInitialization`に登録します。
登録がない場合、図の`opt`の部分は呼ばれません。
たとえば、1ステップごとに情報を集めたいなら`SteppingAction`に書きます。

`SensitiveDetector`は、`DetectorConstruction`の`ConstructSDandField()`で登録します。
検出器のボリュームに入った粒子からヒット情報を取り出す役割の任意クラスです。

`Initialize()`と`BeamOn()`は`main()`から呼ぶこともできますし、マクロ（`/run/initialize`、`/run/beamOn`）から呼ぶこともできます。
附属サンプルはマクロで呼んでいます。

マルチスレッドで実行する場合は、`ActionInitialization`の`Build()`と`BuildForMaster()`で登録先が変わるものがあります。
詳しくは[ActionInitialization](./geant4-user-actioninitialization.md)を参照してください。

## リファレンス

- [Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)
