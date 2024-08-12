# クラスの自作度

Geant4は**ツールキット**として配布されており、
Geant4が用意したクラスを継承して、ユーザーが自身の目的に合わせて
カスタマイズする必要があります。

使いはじめたときは、どのファイルを、
どうカスタマイズするのかよく分かりませんでしたが、
ドキュメントや講習会スライドをいくつか読んでみて、
Geant4の概要が分かってきた気がしたので、整理してみました。

それぞれのファイルをどれくらいカスタマイズする必要があるかの
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

基本的に付属サンプルのメイン関数をコピーして使い始めればよいと思いますが、
きっと少しずつ手を加えたくなるため、自作度は【★★・・・】としました。

## DetectorConstruction【★★★★★】

:自作度: ★★★★★

測定器のジオメトリを作成するクラスです。
``G4VUserDetectorConstruction``を継承して作成します。

自分の実験に合わせてユーザーが実装する必要があります。
自作度は【★★★★★】です。

:::{seealso}

- [](./geant4-user-detectorconstruction.md)

:::

## PhysicsList【★・・・・】

:自作度: ★・・・・

物理の相互作用モデルを設定するクラスです。
基本的な相互作用モデルは、Geant4チームが用意してくれたクラスを利用できます。
さらに、それらを組み合わせて定義されたプリセットもいくつか用意されています。
まずはその中から自分の目的にあったモデルを選べばOKです。

Geant4が用意したモデルを使うところからはじめたらよいため、
自作度は【★・・・・】にしました。

:::{seealso}

- [](./geant4-user-physicslist.md)

:::

相互作用をモデルをカスタマイズしたい場合は、``G4VModularPhysicsList``を継承したクラスを作成します。
基本的な相互作用クラスから、利用したい相互作用を選択し、``RegisterPhysics``を使って追加します。

本気で相互作用モデルを実装したい場合は、``G4VPhysicsList``を継承したクラスを作成すればよいと思いますが、これはかなり上級者向けだと思います。

## ActionInitialization【★・・・・】

:自作度: ★・・・・

ユーザーアクションを設定するクラスです。
``G4VUserActionInitialization``を継承して作成します。
付属サンプルの使い回しでOKなため【★・・・・】としました。

:::{seealso}

- [](./geant4-user-actioninitialization.md)

:::

## PrimaryGeneratorAction【★★★★・】

:自作度: ★★★★・

入射粒子の初期条件を設定するクラスです。
``G4VUserPrimaryGeneratorAction``を継承して作成します。
自分の実験に合わせてユーザーが実装する必要があります。

Geant4が用意した``G4ParticleGun``や``G4GeneralParticleSource``などの
粒子生成クラスを使うことができるため、
自作度は【★★★★・】としました。

:::{seealso}

- [](./geant4-user-primarygeneratoraction.md)

:::

## SteppingAction【★・・・・】／SensitiveDetector【★★★★★】

:自作度: ★★★★★

ステップごとのユーザーアクションを設定するクラスです。
``G4UserSteppingAction``クラスを継承して作成します。
必須クラスではないですが、ユーザーの目的にあった物理量を取得するために、作成する必要があります。

ただし、より便利な``G4VSensitiveDetector``クラスが用意されているため、
まずはそちらを作成するところからはじめるとよいでしょう。
自作度は【★★★★★】です。

:::{seealso}

- [](./geant4-user-steppingaction.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## TrackingAction【★・・・・】

:自作度: ★・・・・

トラックごとのユーザーアクションを設定するクラスです。
``G4UserSteppingAction``クラスを継承して作成します。

最初はなくてもよいクラスなので、自作度は【★・・・・】です。

:::{seealso}

- [](./geant4-user-trackingaction.md)

:::

## EventAction【★・・・・】

:自作度: ★・・・・

イベントごとのユーザーアクションを設定するクラスです。
``G4UserEventAction``クラスを継承して作成します。
最初はなくてもよいクラスなので、自作度は【★・・・・】です。

:::{seealso}

- [](./geant4-user-eventaction.md)

:::

## RunAction【★・・・・】

:自作度: ★・・・・

ランごとのユーザーアクションを設定するクラスです。
``G4UserRunAction``クラスを継承して作成します。
最初はなくてもよいクラスなので、自作度は【★・・・・】です。

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
