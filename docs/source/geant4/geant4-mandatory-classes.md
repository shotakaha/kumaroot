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
    auto *rm = G4RunManagerFactory::CreateRunManager();

    // 必須ユーザークラスを設定
    auto geometry = new Geometry{}
    rm->SetUserInitialization(geometry);
    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);

    // Geant4のカーネルを初期化
    rm->Initialize()

    // シミューレーションを開始
    G4int n_runs = 10
    rm->BeamOn(n_runs)

    // あと片付け
    delete rm;
}
```

メイン関数の必要な要素を抜粋しました。
これに対話モードや、可視化ツールとスコアリングの設定などを追加します。
付属サンプルのメイン関数を使い回せばよいので、自作度は高くありません。

## DetectorConstruction【★★★★★】

:自作度: ★★★★★

測定器のジオメトリを作成するクラスです。
自分の実験に合わせてユーザーが実装する必要があります。
``G4VUserDetectorConstruction``を継承して作成します。

:::{seealso}

- [](./geant4-user-detectorconstruction.md)

:::

## PhysicsList【★・・・・】

:自作度: ★・・・・

物理の相互作用モデルを設定するクラスです。
必須クラスですが、定義済みのモデルを使うことができるので、自作度は高くありません。

:::{seealso}

- [](./geant4-user-physicslist.md)

:::

基本的な相互作用モデルは、Geant4チームが用意してくれたクラスを利用できます。
さらに、それらを組み合わせて定義されたプリセットもいくつか用意されています。
まずはその中から自分の目的にあったモデルを選べばOKです。

相互作用をモデルをカスタマイズしたい場合は、``G4VModularPhysicsList``を継承したクラスを作成します。
基本的な相互作用クラスから、利用したい相互作用を選択し、``RegisterPhysics``を使って追加します。

本気で相互作用モデルを実装したい場合は、``G4VPhysicsList``を継承したクラスを作成すればよいと思いますが、これはかなり上級者向けだと思います。

## ActionInitialization【★・・・・】

:自作度: ★・・・・

ユーザーアクションを設定するクラスです。
``G4VUserActionInitialization``を継承して作成します。
付属サンプルの使い回しでOKです。

:::{seealso}

- [](./geant4-user-actioninitialization.md)

:::

## PrimaryGeneratorAction【★★★★・】

:自作度: ★★★★・

入射粒子の初期条件を設定するクラスです。
自分の実験に合わせてユーザーが実装する必要があります。
``G4VUserPrimaryGeneratorAction``を継承して作成します。

:::{seealso}

- [](./geant4-user-primarygeneratoraction.md)

:::

## SteppingAction【★★★★★】

:自作度: ★★★★★

ステップごとのユーザーアクションを設定するクラスです。
必須クラスではないですが、ユーザーの目的にあった物理量を取得するために、作成する必要があります。
``G4UserSteppingAction``クラスを継承して作成します。
また、どちらかというと有感検出器（``G4VSensitiveDetector``）を作成したほうがよいです。

:::{seealso}

- [](./geant4-user-steppingaction.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## TrackingAction【★・・・・】

:自作度: ★・・・・

トラックごとのユーザーアクションを設定するクラスです。
``G4UserSteppingAction``クラスを継承して作成します。
ユーザー実装が必要なユースケースがわかりません。

:::{seealso}

- [](./geant4-user-trackingaction.md)

:::

## EventAction【★★・・・】

:自作度: ★★・・・

イベントごとのユーザーアクションを設定するクラスです。
``G4UserEventAction``クラスを継承して作成します。

:::{seealso}

- [](./geant4-user-eventaction.md)

:::

## RunAction【★・・・・】

:自作度: ★・・・・

ランごとのユーザーアクションを設定するクラスです。
``G4UserRunAction``クラスを継承して作成します。

:::{seealso}

- [](./geant4-user-runaction.md)

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
