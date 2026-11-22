# シミュレーションの流れ

Geant4のシミュレーションの全体の流れを1枚のシーケンス図にまとめました。

:::{hint}

このシーケンス図はGeant4をはじめるときに一番欲しかった情報かもしれないです。

:::

## シーケンス図

時間は上から下へ進みます。
実線の矢印は「呼び出し」を表します。
`opt`で囲んだ部分は任意で、必要になったときだけ実装します。

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

## シーケンス図から分かる内部処理のポイント

### 用語

シミュレーションは、次の4つの単位が入れ子になって進みます。

| 用語 | 意味 |
|---|---|
| Run | `BeamOn()`1回分の実行単位 |
| Event | 初期粒子1個の処理単位 |
| Track | 1個の粒子の追跡単位（二次粒子も含む） |
| Step | 粒子が1ステップ進む単位 |

### Managerが処理を分担する

4つのManagerクラスが、それぞれの単位を担当します。

- **G4RunManager**: Runを管理し、Eventの処理を依頼する
- **G4EventManager**: Eventを管理し、Trackの処理を依頼する
- **G4TrackingManager**: Trackを管理し、Stepの処理を依頼する
- **G4SteppingManager**: 1ステップの処理を実行する

ユーザーが直接呼ぶのは**G4RunManagerだけ**です。残りのManagerは、Geant4の内部で自動的に呼ばれます。

### 処理は4段階で進む

1. **①main()で準備**: RunManagerを作り、必須クラスを渡す
2. **②Initialize()で構築**: 検出器と物理プロセスを組み立てる
3. **③BeamOn()で実行**: Run → Event → Track → Step の順に入れ子で繰り返す
4. **④終了**: RunManagerを削除する。登録したユーザークラスも一緒に削除される

### 任意のアクションは決まったタイミングで呼ばれる

RunAction、EventAction、TrackingAction、SteppingActionは、図の対応する位置で自動的に呼ばれます。
実装しなければ呼ばれません（図の`opt`の部分）。

## 自作アプリで押さえるポイント

### 必須クラス

次の5つは、自作アプリで必ず用意します。

| クラス | 役割 | 主に書く場所 |
|---|---|---|
| main() | RunManagerを作り、必須クラスを渡す | `main.cc` |
| DetectorConstruction | 検出器の形状と材質を作る | `Construct()` |
| PhysicsList | 使う物理プロセスを決める | `ConstructParticle()`、`ConstructProcess()` |
| ActionInitialization | 各アクションを登録する | `Build()`、`BuildForMaster()` |
| PrimaryGeneratorAction | 初期粒子を作る | `GeneratePrimaries()` |

### 任意クラス

必要になったときだけ追加します。たとえば、1ステップごとに情報を集めたいならSteppingActionに書きます。

| クラス | 役割 | 登録場所 |
|---|---|---|
| RunAction | Runの開始と終了で処理する | ActionInitialization |
| EventAction | Eventの開始と終了で処理する | ActionInitialization |
| TrackingAction | Trackの開始と終了で処理する | ActionInitialization |
| SteppingAction | Stepごとに処理する | ActionInitialization |
| SensitiveDetector | 検出器の体積から検出情報（ヒット）を取り出す | DetectorConstruction の `ConstructSDandField()` |

### main()とマクロ

`Initialize()`と`BeamOn()`は、`main()`から直接呼ぶこともできます。
マクロ（`/run/initialize`、`/run/beamOn`）から呼ぶこともできます。
附属サンプルはマクロで呼んでいます。

### マルチスレッド

マルチスレッド（MT）で実行する場合、ActionInitializationには`Build()`と`BuildForMaster()`の2つがあります。
RunActionの登録先がこの2つで異なります。詳しくは[ActionInitialization](./geant4-user-actioninitialization.md)を参照してください。

## リファレンス

- [Basic concept of Run](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/run.html)
