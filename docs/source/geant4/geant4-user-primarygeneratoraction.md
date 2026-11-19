# 粒子生成したい（`G4VUserPrimaryGeneratorAction`）

```cpp
// 疑似コード
class PrimaryGenerator : public G4VUserPrimaryGeneratorAction {
  public:
    PrimaryGenerator();                              // 粒子銃を作る
    ~PrimaryGenerator() override;                    // 粒子銃を消す
    void GeneratePrimaries(G4Event* aEvent) override;  // 必須（1イベントごとに呼ばれる）
};

void PrimaryGenerator::GeneratePrimaries(G4Event* aEvent) {
    // 入射粒子の種類、位置、方向、エネルギーを設定する
    // イベントに一次粒子を追加する
}
```

`G4VUserPrimaryGeneratorAction`は、一次粒子（入射粒子）を生成するクラスです。
ほとんどのアプリで必要になるため、実質的に必須のクラスです。

このクラスを継承すると、イベントごとに入射粒子の種類、位置、方向、エネルギーを設定できます。
`G4ParticleGun`などを使えば、短いコードで入射粒子を生成できます。

`GeneratePrimaries()`は、イベントごとに呼ばれる純粋仮想関数です。
この関数の中で、入射粒子の種類、位置、方向、エネルギーを設定し、`GeneratePrimaryVertex()`を呼ぶことで、そのイベントに一次粒子が追加されます。

`G4ParticleGun`は、コンストラクターで1回だけ作成し、デストラクターで`delete`します。
粒子の定義（`G4ParticleDefinition`）は、Geant4が管理します。
そのため、ユーザーが`delete`してはいけません。

## 一次粒子を生成するクラスを作りたい（`G4VUserPrimaryGeneratorAction`）

```cpp
class PrimaryGenerator : public G4VUserPrimaryGeneratorAction {
  // ...
};
```

`G4VUserPrimaryGeneratorAction`を`public`に継承したクラスを作成します。
クラス名は`PrimaryGenerator`など、わかりやすい名前にします。

入射粒子を生成するために使う`G4ParticleGun`は、コンストラクターで1回だけ作成します。
イベントごとに作成すると、解放されずにメモリーリークの原因になります。

:::{note}

`G4ParticleGun`は、`new`で作成して、メンバー変数に保持します。
デストラクターで`delete`して、解放します。
親クラスのデストラクターは`virtual`なので、この自作クラスのデストラクターも呼ばれます。

:::

## 一次粒子を生成したい（`GeneratePrimaries`）

```cpp
void PrimaryGenerator::GeneratePrimaries(G4Event* aEvent)
{
    // 入射粒子の種類を設定する
    auto table = G4ParticleTable::GetParticleTable();
    auto particle = table->FindParticle("mu-");
    fParticleGun->SetParticleDefinition(particle);

    // 入射位置を設定する
    fParticleGun->SetParticlePosition(G4ThreeVector(0., 0., 0.));

    // 入射方向を設定する
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., 0., 1.));

    // 運動エネルギーを設定する
    fParticleGun->SetParticleEnergy(1. * GeV);

    // イベントに一次粒子を追加する
    fParticleGun->GeneratePrimaryVertex(aEvent);
}
```

`GeneratePrimaries()`は、イベントごとに呼ばれます。
この中で、入射粒子の種類、位置、方向、エネルギーを設定します。
最後に`GeneratePrimaryVertex()`を呼ぶと、そのイベントに一次粒子が追加されます。

上の例では、`G4ParticleGun`を使ってミューオン（`mu-`）を1 GeVで入射しています。
`G4ParticleGun`は、Geant4標準の粒子生成クラスのひとつです。
運動量やエネルギーを設定する場合は、必ず単位をつけてください。
`1 GeV`のつもりで`1`と書いてしまうと、Geant4の内部単位（MeV）として扱われ、意図しないエネルギーになります。

:::{note}

`G4ParticleTable::GetParticleTable()`は、粒子の一覧を管理するクラスを返します。
`FindParticle("mu-")`で、名前から粒子の定義を取得します。
粒子の名前を間違えると`nullptr`が返るので、必ず確認してください。

:::

:::{caution}

`GeneratePrimaries()`の中で`new`を使ってはいけません。
この関数はイベントごとに呼ばれるため、`new`すると解放されずにメモリーリークの原因になります。

:::

## 親クラスのメソッドを確認したい

親クラス（`G4VUserPrimaryGeneratorAction`）の主なメンバー関数は、次のとおりです。

```cpp
G4VUserPrimaryGeneratorAction();
virtual ~G4VUserPrimaryGeneratorAction() = default;
virtual void GeneratePrimaries(G4Event* aEvent) = 0;
```

- コンストラクターとデストラクターは、親クラスの定義を引き継ぎます。
- `GeneratePrimaries()`は純粋仮想関数です。自作クラスで必ず`override`します。

## 自作クラスの例を見たい（`PrimaryGenerator`）

```cpp
// include/PrimaryGenerator.hh

#ifndef PrimaryGenerator_h
#define PrimaryGenerator_h 1

#include "G4VUserPrimaryGeneratorAction.hh"

class G4ParticleGun;
class G4Event;

namespace ToyMC
{

class PrimaryGenerator : public G4VUserPrimaryGeneratorAction
{
  public:
    PrimaryGenerator();
    ~PrimaryGenerator() override;

    void GeneratePrimaries(G4Event* aEvent) override;

  private:
    G4ParticleGun* fParticleGun = nullptr;
};

}  // namespace ToyMC

#endif
```

```cpp
// src/PrimaryGenerator.cc

#include "PrimaryGenerator.hh"

#include "G4Event.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4SystemOfUnits.hh"

namespace ToyMC
{

PrimaryGenerator::PrimaryGenerator()
{
    // 1回のGeneratePrimaryVertex()で生成する粒子の数
    G4int n_particles = 1;
    fParticleGun = new G4ParticleGun(n_particles);
}

PrimaryGenerator::~PrimaryGenerator()
{
    delete fParticleGun;
}

void PrimaryGenerator::GeneratePrimaries(G4Event* aEvent)
{
    // ...（上の例と同じ）
}

}  // namespace ToyMC
```

この例では、粒子銃（`G4ParticleGun`）を、メンバー変数`fParticleGun`で保持しています。
`GeneratePrimaries()`は、その粒子銃を設定してから、イベントに一次粒子を追加します。

:::{note}

`#ifndef`から`#endif`は、インクルードガードです。
同じヘッダーを複数回読み込んでも、クラスが二重に定義されないようにします。

:::

## 登録したい（`ActionInitialization`）

```cpp
void ActionInitialization::Build() const
{
    SetUserAction(new ToyMC::PrimaryGenerator{});
}
```

`PrimaryGenerator`は、`G4VUserActionInitialization::Build()`の中で作成し、`SetUserAction()`で登録します。
マルチスレッドで実行すると、ワーカースレッドごとに`Build()`が呼ばれます。
そのため、入射粒子の生成も、ワーカースレッドごとに作成されます。

:::{note}

`new`で作成したオブジェクトを`SetUserAction()`に渡すと、所有権は登録先に移ります。
そのため、`delete`を自分で書く必要はありません。

:::

:::{seealso}

- [](./geant4-mandatory-classes.md)
- [](./geant4-user-actioninitialization.md)
- [](./geant4-source-particlegun.md)
- [](./geant4-source-gps.md)

:::
