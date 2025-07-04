# 相互作用したい（`G4VModularPhysicsList`）

`G4VModularPhysicsList`は、シミュレーションで使用する物理モデルを
モジュール形式で構成できるようにするための基底クラスです。
v4.8.0で導入されました。

この枠組みにより、ユーザーはGeant4が提供する**Reference Physics List**を
選んで柔軟に物理モデルを構築できます。

:::{note}

v4.8.0以前は
`G4VUserPhysicList`を継承して、ユーザー自身がすべての粒子と
物理過程を定義する必要があったそうです。

この方法はコードの可読性・保守性に乏しく、
物理モデルの再利用も困難だったため、
モジュール形式の`G4VModularPhysicsList`が導入されたようです。

:::

## 親クラス（`G4VModularPhysicsList`）

```cpp
class G4VModularPhysicsList {
  public:
    G4VModularPhysicsList();
    virtual ~G4VModularPhysicsList() override;

  public:
    virtual void ConstructParticle() override;
    virtual void ConstructProcess() override;
    void RegisterPhysics(G4VPhysicsConstructor*);
}
```

親クラス（`G4VModularPhyisicsList`）の主要なメンバー関数を抜粋しました。

`RegisterPhysics`で、
Geant4が提供している物理モデルや、
他のリファレンス物理モデル（`G4VPhysicsConstructor`を継承した自作クラス）を簡単に追加できます。

モデルの名前と内容は[Guide for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。
モデル名は、利用している相互作用モデルを使った命名規則になっています。

## メイン関数（`main`）

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

    // 実験開始（省略）
    rm->Initialize();
    rm->BeamOn();
    delete rm;
    return 0;
}
```

メイン関数で物理モデルを設定する最小構成です。
FTFPモデル（`FTFP_BERT`）に
光学モデル（`G4OpticalPhysics`）を追加し、
`SetUserInitialization`を使ってRunManagerに登録しています。

:::{seealso}

使用した物理モデルは

- [](./geant4-physics-ftfp_bert.md)
- [](./geant4-physics-opticalphysics.md)

に整理しました。

:::

また、`G4VUserPhysicsConstructor`を継承して、完全自作の相互作用モジュールを作ることができます。

- [](./geant4-physics-constructparticle.md)
- [](./geant4-physics-constructprocess.md)
