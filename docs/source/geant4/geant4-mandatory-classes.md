# クラスの自作度

Geant4は**ツールキット**として配布されており、カスタマイズ要素のかたまりです。
はじめての場合、どのファイルを参考にすればよいのか、よく分かりませんでした。
ドキュメントや講習会スライドをいくつか読んでみて、
どいういうときに、どのファイル（のクラスやメソッド）を編集すればよいのかが、
ようやく分かってきたので整理してみました。

また、それぞれのファイルをどれくらいカスタマイズする必要があるかの
【自作度】を★の数で表してみました。

## メイン関数【★★・・・】

:自作度: ★★・・・

```cpp
int main(int argc, char** argv)
{
    // RunManagerを作成
    auto *runManager = G4RunManagerFactory::CreateRunManager();

    // 必須ユーザークラスを設定
    runManager->SetUserInitialization(new DetectorConstruction);
    runManager->SetUserInitialization(new PhysicsList);
    runManager->SetUserInitialization(new ActionInitialization);

    // Geant4のカーネルを初期化
    runManager->Initialize()

    // シミューレーションを開始
    runManager->BeamOn()

    // あと片付け
    delete runManager;
}
```

メイン関数の必要な要素を抜粋しました。
これに対話モードや、可視化ツールとスコアリングの設定などを追加します。
付属サンプルのメイン関数を使い回せばよいので、自作度は高くありません。

## DetectorConstruction（必須クラス）【★★★★★】

:自作度: ★★★★★

測定器のジオメトリを作成するクラスです。
``G4VUserDetectorConstruction``を継承して作成します。
純粋仮想関数である``Construct``の自作が必要です。

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

## PhysicsList（必須クラス）【★・・・・】

:自作度: ★・・・・

物理の相互作用モデルを設定するクラスです。
必須クラスですが、定義済みのモデルを使うことができるので、自作度は高くありません。

基本的な相互作用モデルは、Geant4チームが用意してくれたクラスを利用できます。
さらに、それらを組み合わせて定義されたプリセットもいくつか用意されています。
まずはその中から自分の目的にあったモデルを選べばOKです。

相互作用をモデルをカスタマイズしたい場合は、``G4VModularPhysicsList``を継承したクラスを作成します。
基本的な相互作用クラスから、利用したい相互作用を選択し、``RegisterPhysics``を使って追加します。

本気で相互作用モデルを実装したい場合は、``G4VPhysicsList``を継承したクラスを作成すればよいと思いますが、これはかなり上級者向けだと思います。

:::{mermaid}
classDiagram
    G4VUserPhysicsList <|-- G4VModularPhysicsList
    G4VModularPhysicsList <|-- FTFP_BERT
    G4VModularPhysicsList <|-- QBBC
    G4VModularPhysicsList <|-- QGSP_BERT
    G4VModularPhysicsList <|-- QGSP_BIC
    class G4VUserPhysicsList {
        +G4VUserPhysicsList()
        +virtual ~G4VUserPhysicList()
        +G4VUserPhysicsList(const G4VUserPhysicsList &aPhysicsList)
        +void Construct()
        +virtual void ConstructParticle() = 0
        +virtual void ConstructProcess() = 0
        +virtual void SetCuts()
    }
    class G4VModularPhysicsList {
        +G4VModularPhysicsList()
        +virtual ~G4VModularPhysicsList
        +virtual void ConstructParticle()
        +virtual void ConstructProcess()
        +void RegisterPhysics(G4VPhysicsConstructor *aPhysics)
        +void ReplacePhysics(G4VPhysicsConstructor *aPhysics)
        +void RemovePhysics(G4VPhysicsConstructor *aPhysics)
    }
:::

## ActionInitialization（必須クラス）【★・・・・】

:自作度: ★・・・・

ユーザーアクションを設定するクラスです。
``G4VUserActionInitialization``を継承して作成します。
純粋仮想関数である``Build``の中で、自分の目的に必要なユーザーアクションを設定します。
必須クラスですが、自作度は低く、使い回しが可能です。

マルチスレッド機能が有効なときは、``Build``の内容が``Worker``ノードで実行されます。
``Master``ノードの設定フックとして``BuildForMaster``が用意されていますが、こちらは基本的にそのままでよいはずです。

:::{note}

このクラスは、マルチスレッド機能に対応するために用意されたラッパー的なクラスだと思います。
``Build``の中の``SetUserAction``で設定する各種のユーザーアクションクラスを編集するほうが多いと思います。

```cpp
void ActionInitialization::Build()
{
    SetUserAction(new RunAction);
    SetUserAction(new EventAction);
    SetUserAction(new StackingAction);
    SetUserAction(new TrackingAction);
    SetUserAction(new SteppingAction);
}
```

:::

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

## PrimaryGeneratorAction（必須クラス）【★★★★・】

:自作度: ★★★★・

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

## SteppingAction【★★★★★】

:自作度: ★★★★★

ステップごとのユーザーアクションを設定するクラスです。
``G4UserSteppingAction``クラスを継承して作成します。
ユーザー設定用のフックとして``UserSteppingAction``が用意されています。

必須クラスではないですが、自分の目的にあった物理量を取得するために、結局作成することになると思います。

:::{mermaid}
classDiagram
    G4UserSteppingAction <|-- SteppingAction
    class G4UserSteppingAction{
      +G4UserSteppingAction()
      +virtual ~G4UserSteppingAction()
      +virtual void UserSteppingAction(const G4Step *aStep)
    }
    class SteppingAction{
      +SteppingAction() = default
      +~SteppingAction() override = default
      +void UserSteppingAction(const G4Step *aStep)
    }
:::

### TrackingAction【★★・・・】

:自作度: ★★・・・

トラックごとのユーザーアクションを設定するクラスです。
``G4UserSteppingAction``クラスを継承して作成します。
ユーザー設定用のフックとして``UserSteppingAction``が用意されています。

:::{mermaid}
classDiagram
    G4UserTrackingAction <|-- TrackingAction
    class G4UserTrackingAction{
      +G4UserTrackingAction()
      +virtual ~G4UserTrackingAction()
      +virtual void PreUserTrackingAction(const G4Track *aTrack)
      +virtual void PostUserTrackingAction(const G4Track *aTrack)
    }
    class TrackingAction{
      +TrackingAction() = default
      +~TrackingAction() override = default
      +void PreUserTrackingAction(const G4Track *aTrack)
      +void PostUserTrackingAction(const G4Track *aTrack)
    }
:::

### EventAction【★★★★・】

:自作度: ★★★★・

イベントごとのユーザーアクションを設定するクラスです。

:::{mermaid}
classDiagram
    G4UserEventAction <|-- EventAction
    class G4UserEventAction{
      +G4UserEventAction()
      +virtual ~G4UserEventAction()
      +virtual void BeginOfEventAction(const G4Event *aEvent)
      +virtual void EndOfEventAction(const G4Event *aEvent)
    }
    class EventAction{
      +EventAction() = default
      +~EventAction() override = default
      +void BeginOfEventAction(const G4Event *aEvent)
      +void EndOfEventAction(const G4Event *aEvent)
    }
:::

## RunAction【★★・・・】

:自作度: ★★・・・

ランごとのユーザーアクションを設定するクラスです。

:::{mermaid}
classDiagram
    G4UserRunAction <|-- RunAction
    class G4UserRunAction{
      +G4UserRunAction()
      +virtual ~G4UserRunAction()
      +virtual void BeginOfRunAction(const G4Run *aRun)
      +virtual void EndOfRunAction(const G4Run *aRun)
    }
    class RunAction{
      +RunAction() = default
      +~RunAction() override = default
      +void BeginOfRunAction(const G4Run *aRun)
      +void EndOfRunAction(const G4Run *aRun)
    }
:::




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
