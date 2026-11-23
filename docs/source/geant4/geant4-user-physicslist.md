# 物理リストしたい（`G4VModularPhysicsList`）

```cpp
// 疑似コード
auto physics = new FTFP_BERT{};                    // 既存の物理リストを選ぶ
physics->RegisterPhysics(new G4OpticalPhysics{});  // 物理モデルを追加する
rm->SetUserInitialization(physics);                // RunManagerに登録する
```

`G4VModularPhysicsList`は、相互作用の種類と物理モデルをまとめたモジュール型の**物理リスト**の基底クラスです。
よく使われる組み合わせについては、Geant4開発チームが**リファレンス物理リスト**としてプリセットを用意しています。
ユーザーは基本的にこのプリセットからアプリに必要な物理モデルを追加して使います。


:::{note}

モジュール型の物理リストは、Geant4 4.7.1のリリースノートに導入が記載されています。

:::

## 物理リストのクラスを作りたい（`G4VModularPhysicsList`）

自作の物理リストは、`G4VModularPhysicsList`を継承して作ります。
ただし、よく使う組み合わせは、既存のリファレンス物理リストを選ぶほうが簡単です。

```cpp
// 抜粋・簡略化
class G4VModularPhysicsList : public G4VUserPhysicsList {
  public:
    G4VModularPhysicsList();
    ~G4VModularPhysicsList() override;

    void ConstructParticle() override;
    void ConstructProcess() override;
    void RegisterPhysics(G4VPhysicsConstructor*);
};
```

- `ConstructParticle()`：粒子の種類を生成します。
- `ConstructProcess()`：各粒子に、物理過程を登録します。
- `RegisterPhysics()`：物理モデル（`G4VPhysicsConstructor`）を登録します。

`ConstructParticle()`と`ConstructProcess()`は、`G4VModularPhysicsList`が実装しています。
そのため、自作クラスで書き換える必要はありません。
登録した物理モデルの内容に従って、粒子と物理過程が作られます。

:::{note}

`G4VUserPhysicsList`は、粒子と物理過程を、ユーザーがすべて自分で実装する基底クラスです。
`G4VModularPhysicsList`は、その派生クラスです。
物理モデルを部品として登録できるため、組み合わせを変えやすくなります。

:::

## 既存の物理リストを選びたい（`FTFP_BERT`）

```cpp
auto physics = new FTFP_BERT{};
```

`FTFP_BERT`は、`G4VModularPhysicsList`を継承した、リファレンス物理リストの1つです。
高エネルギー領域は`FTFP`、低エネルギー領域は`BERT`のハドロンモデルを使います。
具体的な内容は、[](./geant4-physics-ftfp-bert.md)を参照してください。

## 物理モデルを追加したい（`RegisterPhysics`）

```cpp
physics->RegisterPhysics(new G4OpticalPhysics{});
```

`RegisterPhysics()`は、物理モデルを物理リストに追加します。
`G4OpticalPhysics`は、光学光子に関する物理過程をまとめたものです。
具体的な内容は、[](./geant4-physics-opticalphysics.md)を参照してください。

物理モデルの名前と内容は、[Guide for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。

## 物理リストを登録したい（`SetUserInitialization`）

```cpp
// プロジェクト名.cc（ここではToyMC.cc）

// Geant4のクラス
#include "FTFP_BERT.hh"
#include "G4OpticalPhysics.hh"
#include "G4RunManagerFactory.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    // ジオメトリの設定（省略）

    // 物理モデルの設定
    auto physics = new FTFP_BERT{};
    physics->RegisterPhysics(new G4OpticalPhysics{});
    rm->SetUserInitialization(physics);

    // ユーザーアクションの設定（省略）

    rm->Initialize();
    rm->BeamOn(100);

    return 0;
}
```

`main()`関数で物理リストを作成し、`SetUserInitialization()`で`RunManager`に登録します。
`RunManager`に登録する前に、`RegisterPhysics()`で物理モデルを追加しておきます。

:::{note}

`RunManager`に登録した物理リストは、`RunManager`が終了するときに`delete`されます。
そのため、`main()`関数で`delete physics;`と書く必要はありません。

:::

:::{seealso}

完全に自作の相互作用モジュールを作る場合は、`G4VPhysicsConstructor`を継承します。

- [](./geant4-physics-constructparticle.md)
- [](./geant4-physics-constructprocess.md)

:::
