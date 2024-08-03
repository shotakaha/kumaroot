# 相互作用したい（``G4VModularPhysicsList``）

粒子と物質の相互作用を定義するクラスは、必須クラスのひとつです。
Geant4で用意されている**Reference Physics List**を利用するのが簡単です。
このPhysicsListは``G4VModularPhysicsList``を継承したクラスです。

## 親クラス

- G4VModularPhysicsList

```cpp
G4VModularPhysicsList()
~G4VModularPhysicsList() override;
void ConstructParticle() override;
void ConstructProcess() override;
void RegisterPhysics(G4VPhysicsConstructor*);
```

``G4VModularPhysicsList``は``G4VUserPhysicList``を継承したクラスです。
``RegisterPhysics``で、他のリファレンス物理モデル（``G4VPhysicsConstructor``）を追加できます。

モデルの名前と内容は[Guide for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。
モデル名は、利用している相互作用モデルを使った命名規則になっています。

## メイン関数

```cpp
#include "FTFP_BERT.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);

}
```

メイン関数で Reference Physics Listを作成してRunManagerに追加します。

- [](./geant4-physics-ftfp_bert.md)
- [](./geant4-physics-opticalphysics.md)

## カスタムしたい（``G4VUserPhysicsList``）

定義されていない相互作用（やその組み合わせ）が必要な場合は``G4VUserPhysicsList``クラスを継承してユーザーがカスタムできるようになっています。

- G4VUserPhysicsList

```cpp
G4VUserPhysicList();
virtual ~G4VUserPhysicList();
virtual void ConstructParticle() = 0;
virtual void ConstructProcess() = 0;
virtual void SetCuts();
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``ConstructParticle()``と``ConstructProcess()``は、純粋仮想関数になっているため、自作クラスでoverrideが必要です。
``SetCuts()``は、粒子輸送の閾値を設定する仮想関数です。
overrideして閾値をカスタマイズできます。

```cpp
G4VUserPhysicList() = default;
~G4VUserPhysicList() = default;
void ConstructParticle() override;
void ConstructProcess() override;
void SetCuts() override;
```

- [](./geant4-physics-constructparticle.md)
- [](./geant4-physics-constructprocess.md)
