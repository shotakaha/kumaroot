# 自作が必要なクラスたち

## 必須クラス

### DetectorConstruction

測定器のジオメトリを作成するクラスです。
``G4VUserDetectorConstruction``を継承して作成します。
純粋仮想関数である``Construct``を自分で実装します。
``SensitiveDetector``などの設定フックとして``ConstructSDandField``が用意されています。

:::{mermaid}
classDiagram
    G4VUserDetectorConstruction <|-- DetectorConstruction
    class DetectorConstruction{
      +DetectorConstruction() = default
      +~DetectorConstruction() override = default
      +G4VPhysicalVolume* Construct()
      +G4VPhysicalVolume* ConstructSDandField()
    }
    class G4VUserDetectorConstruction{
      +G4VUserDetectorConstruction()
      +virtual ~G4VUserDetectorConstruction()
      +virtual G4VPhysicalVolume* Construct() = 0
      +virtual void ConstructSDandField()
    }
:::

### PhysicsList

物理の相互作用モデルを設定するクラスです。
Geant4が用意している``G4VModularPhysicsList``の具象クラスがあるので、まずはそこから該当しそうなものを選びます。
より詳細な相互作用モデルを実装したい場合は、``G4VPhysicsList``を継承して作成します。

:::{mermaid}
classDiagram
    G4VUserPhysicsList <|-- G4VModularPhysicsList
    G4VModularPhysicsList <|-- FTFP_BERT
    G4VModularPhysicsList <|-- QBBC
    G4VModularPhysicsList <|-- QGSP_BERT
    G4VModularPhysicsList <|-- QGSP_BIC
:::

### ActionInitialization

ユーザーアクションを設定するクラスです。
``G4VUserActionInitialization``を継承して作成します。
純粋仮想関数である``Build``を自分で実装します。
マルチスレッド機能を有効にしているときは、ここの内容が``Worker``ノードで実行されます。
マスターノードの実行内容を設定するためのフックとして``BuildForMaster``が用意されています。

:::{mermaid}

classDiagram
    G4VUserActionInitialization <|-- ActionInitialization
    class ActionInitialization{
      +ActionInitialization() = default
      +~ActionInitialization() override = default
      +void BuidForMaster() const override
      +void Build() const override
    }
    class G4VUserActionInitialization{
      +G4VUserActionInitialization()
      +virtual ~G4VUserActionInitialization()
      +virtual void BuildForMaster() const
      +virtual void Build() const = 0
    }
:::

### PrimaryGeneratorAction

入射粒子の初期条件を設定するクラスです。
``G4VUserPrimaryGeneratorAction``を継承して作成します。
純粋仮想関数である``GeneratePrimaries``を自分で実装します。

:::{mermaid}

classDiagram
    G4VUserPrimaryGeneratorAction <|-- PrimaryGeneratorAction
    class PrimaryGeneratorAction{
      +PrimaryGeneratorAction() = default
      +~PrimaryGeneratorAction() override = default
      +void GeneratePrimaries(G4Event *aEvent)
    }
    class G4VUserPrimaryGeneratorAction{
      +G4VUserPrimaryGeneratorAction()
      +virtual ~G4VUserPrimaryGeneratorAction()
      +virtual void GeneratePrimaries(G4Event *aEvent)=0
    }
:::

## ユーザーフック用のクラス

1. ``RunAction: public G4UserRunAction``
1. ``EventAction: public G4UserEventAction``
1. ``TrackingAction: public G4UserTrackingAction``
1. ``SteppingAction: public G4UserSteppingAction``

```cpp
// RunManagerを作成
G4RunManager *runManager = new G4RunManager;

// 必須ユーザークラスを設定
runManager->SetUserInitialization(new MYDetectorConstruction);
runManager->SetUserInitialization(new MYPhysicsList);
runManager->SetUserInitialization(new MYActionInitialization);

// Geant4のカーネルを初期化
runManager->Initialize()
```

``MYDetectorConstruction``、
``MYPhysicsList``、
``MYActionInitialization``は
ユーザーが必ず作成しないといけない必須クラスです。

ソースコードを読むときにこのことを知っていると、
内容を読み解くときの助けになるはずです。

アプリケーションを作成したい場合、
これらを順番に実装していけばOKです。

## ``DetectorConstruction``クラス

測定器を定義するためのクラスです。
``G4VUserDetectorConstruction``クラスを継承して作成します。

このクラスの中で実験室（worldと呼びます）を作成し、
その中にその中に測定器を配置します。
使っている物質の組成や性質、検出器の要素などもこのクラスで定義します。

## ``PhysicsList``クラス

粒子と物質の相互作用を定義するためのクラスです。
``G4VUserPhsyicsList``クラスもしくは
``G4ModularPhysicsList``クラスを継承して作成します。

Geant4にいくつかの定義済みの相互作用モデルがあるので、
まずはそれを使ってみるとよいと思います。

## ``ActionInitialization``クラス

一次粒子の条件を定義するクラスです。

## Geant4のクラス構造

Geant4は大きく分けて8つのクラスカテゴリーで構成されています。

1. Run and Event
2. Tracking and Track
3. Geometry and Magnetic Field
4. Particle Definition and Matter
5. Physics
6. Hits and Digitization
7. Visualization
8. Interfaces

アプリケーションを作成したり、変更したりする場合に、
どのカテゴリーのクラスをいじればよいか、あたりをつける目安になると思います。

詳細は[Class Categories and Domains](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/classCategory.html)で確認できます。
