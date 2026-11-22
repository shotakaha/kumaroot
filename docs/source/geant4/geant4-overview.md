# シミュレーションの流れ

Geant4のシミュレーションの全体の流れを、1枚のシーケンス図にまとめました。
まずは図で全体をつかみ、そのあとで各要素の役割を説明します。

:::{hint}

このシーケンス図は、Geant4をはじめるときに一番欲しかった情報かもしれないです。

:::

## シーケンス図

上から下へ時間が進みます。実線の矢印は「呼び出し」を表します。
`opt`で囲んだ部分は任意で、必要になったときだけ実装します。
`main()`での準備と、マクロ（`/run/initialize`、`/run/beamOn`）による実行は、どちらも同じ処理を呼び出します。

:::{mermaid}

sequenceDiagram
    autonumber
    participant Main as main()
    participant RM as G4RunManager
    participant EvM as G4EventManager
    participant TrM as G4TrackingManager
    participant StM as G4SteppingManager
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
        RM ->> EvM: ProcessOneEvent()
        EvM ->> EA: BeginOfEventAction()
        loop 各トラック（粒子ごと）
            EvM ->> TrM: ProcessOneTrack()
            opt TrackingActionを使う場合
                TrM ->> TA: PreUserTrackingAction()
            end
            loop 各ステップ
                TrM ->> StM: Stepping()
                opt SDが付いた体積の中
                    StM ->> SD: ProcessHits()
                end
                opt SteppingActionを使う場合
                    StM ->> SA: UserSteppingAction()
                end
            end
            opt TrackingActionを使う場合
                TrM ->> TA: PostUserTrackingAction()
            end
        end
        EvM ->> EA: EndOfEventAction()
    end
    RM ->> RA: EndOfRunAction()

    Note over Main,RM: ④ 終了する
    Main ->> RM: delete RunManager
    RM ->> RM: 登録したユーザークラスも削除

:::

## 図の解説

### 4つのManagerクラス

シミュレーションの進行は、次の4種類のManagerクラスが担当します。
それぞれが下位のManagerに処理を依頼し、処理が終わると呼び出し元に戻ります。

1. [G4RunManager](./geant4-run-manager.md):
   **G4Run**を管理するクラス。
   G4**Event**Managerにイベントの処理をお願いする。
2. [G4EventManager](./geant4-event-manager.md):
   **G4Event**を管理するクラス。
   G4**Tracking**Managerに粒子ごとの追跡（トラッキング）をお願いする。
3. ``G4TrackingManager``:
   **G4Track**を管理するクラス。
   G4**Stepping**Managerに1ステップずつの処理をお願いする。
4. ``G4SteppingManager``:
   **G4Step**を管理するクラス。
   1ステップ分の処理を実行する。

この中で、ユーザーが直接指示するのは``G4RunManager``だけでOKです。
残りの3つは、Geant4の内部で自動的に呼び出されます。

### 必須クラスと任意クラス

次の3つは必ず用意します。

- **DetectorConstruction**: 検出器の形状と材質を作る
- **PhysicsList**: どの物理プロセスを使うかを決める
- **ActionInitialization**: 各種ユーザーアクションを登録する

ActionInitializationの中で、次のクラスも登録します。
これらは、粒子の生成に必要な**PrimaryGeneratorAction**と、
必要になったときだけ追加する任意クラスです。

- **RunAction**: Run（シミュレーションの1回の実行）の開始と終了で処理する
- **EventAction**: Event（1個の初期粒子の処理）の開始と終了で処理する
- **TrackingAction**: Track（粒子1個の追跡）の開始と終了で処理する
- **SteppingAction**: Step（1ステップ）ごとに処理する
- **SensitiveDetector（SD）**: 検出器の体積に入った粒子から、検出情報（ヒット）を取り出す

どのクラスをどのファイルに実装すればよいかは、図の呼び出しタイミングを見ると分かります。
たとえば、1ステップごとに情報を集めたい場合はSteppingActionに書きます。

### 呼び出しのタイミング

- **①main()**: RunManagerを作り、必須クラスを渡します。
- **②Initialize()**: 検出器と物理プロセスを組み立てます。
  `main()`から直接呼ぶ場合と、マクロ`/run/initialize`から呼ぶ場合があります。
- **③BeamOn()**: 指定した回数だけ、イベント → トラック → ステップの順に処理を繰り返します。
  `main()`から直接呼ぶ場合と、マクロ`/run/beamOn`から呼ぶ場合があります。
- **④終了**: RunManagerを削除します。
  登録したユーザークラスは、RunManagerが削除するので、自分で`delete`する必要はありません。

:::{note}

マルチスレッド（MT）で実行する場合、ActionInitializationには`Build()`と`BuildForMaster()`の2つがあります。
RunActionの登録先がこの2つで異なります。詳しくは[ActionInitialization](./geant4-user-actioninitialization.md)を参照してください。

:::

## リファレンス

- [Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)
