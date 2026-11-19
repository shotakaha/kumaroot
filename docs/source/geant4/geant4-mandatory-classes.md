# クラスを使いこなしたい

```cpp
// 疑似コード（main関数の骨組み）
int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    // 必須：測定器（継承が必要）
    rm->SetUserInitialization(new Geometry{});

    // 必須：物理リスト（既存のものを選べる）
    rm->SetUserInitialization(new FTFP_BERT{});

    // 実質必須：ユーザーアクション（ここで入射粒子などを登録する）
    rm->SetUserInitialization(new ActionInitialization{});

    rm->Initialize();
    rm->BeamOn(100);

    delete rm;
}
```

Geant4は、シミュレーションの枠組みを提供するツールキットです。
ユーザーは、Geant4が用意した基底クラスを継承し、自分の実験に合わせて中身のパーツを自作する必要があります。
自作したパーツを`main()`関数で登録してから実行します。

Geant4には、
粒子の輸送（particle transportation）、
物理過程の計算（physics process）、
イベントの管理（event management）、
ヒットの集計（hit collection）などの「Geant4が提供する共通基盤」のクラスと、
測定器の形状（detector geometry）、
入射粒子の生成（primary particle generation）、
ユーザーアクション（user action）などの「ユーザーが実装する部分」のクラスがあります。

C++のクラスの継承と仮想関数を使うことで、Geant4はユーザーが自作したクラスを、決まったタイミングで呼び出すことができます。

## Geant4のクラス構造

Geant4は大きく分けて次の8つのクラスカテゴリーで構成されています。

1. Run and Event
2. Tracking and Track
3. Geometry and Magnetic Field
4. Particle Definition and Matter
5. Physics
6. Hits and Digitization
7. Visualization
8. Interfaces

アプリを作成したり変更したりするときに、どのカテゴリーのクラスを変更すればよいかの目安になります。
詳細は、[Class Categories and Domains](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/classCategory.html)を参照してください。

:::{seealso}

- [](./geant4-main.md)
- [](./geant4-user-detectorconstruction.md)
- [](./geant4-user-physicslist.md)
- [](./geant4-user-actioninitialization.md)
- [](./geant4-user-primarygeneratoraction.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## クラスの継承と仮想関数・純粋仮想関数

Geant4の使い方を理解するには、次の3つの仕組みを知っておく必要があります。

```cpp
// 基底クラス（Geant4が用意する）
class G4VUserDetectorConstruction {
  public:
    virtual G4VPhysicalVolume* Construct() = 0;  // 純粋仮想関数
    virtual void ConstructSDandField();           // 仮想関数
};

// 派生クラス（ユーザーが書く）
class Geometry : public G4VUserDetectorConstruction {
  public:
    G4VPhysicalVolume* Construct() override;      // 必ず実装する
};
```

- **継承**：`class Geometry : public G4VUserDetectorConstruction`のように、基底クラスの機能を引き継いで、新しいクラスを作ります。
- **仮想関数**：`virtual`を付けた関数は、派生クラスで上書き（`override`）できます。Geant4は、基底クラスのポインターを通して、この関数を呼びます。
- **純粋仮想関数**：`= 0`を付けた関数は、基底クラスでは実装しません。派生クラスで必ず実装する必要があります。

`G4VUserDetectorConstruction`で見ると、次のようになります。
`Construct()`は純粋仮想関数なので、ユーザーの`Geometry`が実装します。
`ConstructSDandField()`は仮想関数で、既定では何もしません。有感検出器や場が必要なときだけ実装します。

クラスの関係は、次の図のとおりです。

:::{mermaid}

classDiagram
    class G4VUserDetectorConstruction {
        <<abstract>>
        +Construct()* G4VPhysicalVolume
        +ConstructSDandField() void
    }
    class Geometry {
        +Construct() G4VPhysicalVolume
        +ConstructSDandField() void
    }
    G4VUserDetectorConstruction <|-- Geometry

:::

Geant4の`RunManager`は、ユーザーの`Geometry`を基底クラスのポインターで保持しています。
初期化のときは、基底クラスのポインターを通して`Construct()`を呼び出します。
この呼び出しで、ユーザーの`Geometry::Construct()`が実行されます。

:::{mermaid}

sequenceDiagram
    participant RM as G4RunManager
    participant Base as G4VUserDetectorConstruction*
    participant Geo as Geometry

    RM ->> Base: Construct()
    Base ->> Geo: Geometry::Construct()（仮想関数として呼ばれる）
    Geo -->> RM: ワールドの物理ボリューム

:::

:::{note}

`Geometry`が`Construct()`を実装していないと、`Geometry`は抽象クラスのままです。
その場合、`new Geometry{}`はコンパイルエラーになります。

:::

:::{note}

`virtual`と`override`は、組にして使います。
`override`を付けておくと、関数名や引数を間違えたときに、コンパイラーがエラーを出します。

:::

:::{note}

純粋仮想関数を1つでも持つクラスは、抽象クラスと呼ばれます。
抽象クラスは、そのままでは`new`できません。
Geant4の基底クラスは、ユーザーが派生クラスを作って使うことを前提にしています。

:::

## 継承が必要なクラス

次のクラスを設定しないと、`RunManager`がエラーで止まります。

| クラス | 役割 | 純粋仮想関数 | 未設定のときのエラー |
| --- | --- | --- | --- |
| `G4VUserDetectorConstruction` | 測定器の形状を作る | `Construct()` | `G4VUserDetectorConstruction is not defined!` |
| `G4VUserPhysicsList` | 物理過程を設定する | `ConstructParticle()`、`ConstructProcess()` | `G4VUserPhysicsList is not defined!` |

物理リストは、自作せずに、Geant4が用意したリファレンス物理リスト（`FTFP_BERT`など）を使えます。
詳しくは、[](./geant4-user-physicslist.md)を参照してください。

測定器は、必ず自作します。
詳しくは、[](./geant4-user-detectorconstruction.md)を参照してください。

## 継承が実質的に必要なクラス

次のクラスは、実際のアプリではほぼ必ず作ります。
入射粒子を生成するには、`G4VUserPrimaryGeneratorAction`が必要です。

| クラス | 役割 | 純粋仮想関数 | 省略したときの影響 |
| --- | --- | --- | --- |
| `G4VUserPrimaryGeneratorAction` | 入射粒子を生成する | `GeneratePrimaries()` | `BeamOn()`で`G4VUserPrimaryGeneratorAction is not defined!`のエラー |
| `G4VUserActionInitialization` | ユーザーアクションを登録する | `Build()` | ユーザーアクションを登録する標準の場所がなくなる |

`G4VUserPrimaryGeneratorAction`は、`G4ParticleGun`などを使えば、自分でほとんど書かずに済みます。
詳しくは、[](./geant4-user-primarygeneratoraction.md)を参照してください。

:::{note}

マルチスレッドで実行する場合、入射粒子の生成は、ワーカースレッドごとに作成する必要があります。
そのため、`G4VUserPrimaryGeneratorAction`は、`G4VUserActionInitialization::Build()`の中で作成します。

:::

## 継承なしで使えるクラス

次のクラスは、継承しなくても、Geant4が用意したものをそのまま使えます。

| クラス | 役割 | 利用例 |
| --- | --- | --- |
| `FTFP_BERT` | 物理リスト | `new FTFP_BERT{}` |
| `G4OpticalPhysics` | 光学過程の物理モデル | `physics->RegisterPhysics(new G4OpticalPhysics{})` |
| `G4ParticleGun` | 粒子を1つずつ入射する | 入射粒子の設定に使う |
| `G4GeneralParticleSource` | 粒子の位置・方向・エネルギー分布を設定する | 入射粒子の設定に使う |
| `G4MultiFunctionalDetector` | 検出器の物理量を集計する | `G4PSEnergyDeposit`などを登録する |

## 継承が任意のクラス

次のクラスは、作らなくてもエラーになりません。
基底クラスの関数は、何もしない実装になっています。
必要になったときだけ、継承して上書きします。

| クラス | 役割 | 作るタイミング |
| --- | --- | --- |
| `G4UserRunAction` | ランの開始と終了で処理する | 結果を集計して表示するとき |
| `G4UserEventAction` | イベントの開始と終了で処理する | イベントごとの値をまとめるとき |
| `G4UserTrackingAction` | 飛跡（トラック）の開始と終了で処理する | 飛跡ごとの情報を調べるとき |
| `G4UserSteppingAction` | ステップごとに処理する | ステップごとの値を調べるとき |

有感検出器（`G4VSensitiveDetector`）は、検出器でのヒットを記録するときだけ作ります。
`ProcessHits()`は純粋仮想関数なので、作る場合は必ず実装します。
`G4MultiFunctionalDetector`を使えば、自作せずに済むこともあります。

## 自作度の目安

「自作度」は、ユーザーがそのクラスを、どれくらい書き換える必要があるかの目安です。

| クラス | 自作度 | 理由 |
| --- | --- | --- |
| `main()`関数 | ★★・・・ | 付属サンプルをコピーして始められる |
| `G4VUserDetectorConstruction` | ★★★★★ | 実験の形状を書く必要がある |
| `G4VModularPhysicsList` | ★・・・・ | リファレンス物理リストを選べば十分 |
| `G4VUserActionInitialization` | ★・・・・ | 付属サンプルを流用しやすい |
| `G4VUserPrimaryGeneratorAction` | ★★★★・ | `G4ParticleGun`などを使えば、少し書けば済む |
| `G4VSensitiveDetector` | ★★★★★ | 記録する物理量に合わせて書く必要がある |
| `G4UserRunAction` / `G4UserEventAction` / `G4UserTrackingAction` | ★・・・・ | 最初は作らなくてよい |
| `G4UserSteppingAction` | ★・・・・ | 最初は作らなくてよい |
