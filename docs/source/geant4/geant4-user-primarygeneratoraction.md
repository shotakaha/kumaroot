# 一次粒子したい（``G4VUserPrimaryGeneratorAction``）

一次粒子（入射粒子）を定義するクラスは、必須クラスのひとつで、
``G4VUserPrimaryGeneratorAction``クラスを継承して作成します。
``G4VUserPrimaryGeneratorAction::GeneratePrimaries``が純粋仮想関数になっていて、
一次粒子を生成する作業はこの関数をオーバーライドして実装します。

ここではクラス名を``PrimaryGeneratorAction``としました。
また、必要な論理物体（G4LogicalVolume）を作成する関数も用意しました。

## ヘッダーファイル

```cpp
// //////////////////////////////////////////////////
// include/PrimaryGeneratorAction.hh
// //////////////////////////////////////////////////
#include "G4VUserPrimaryGeneratorAction.hh"

namespace 名前空間
{
class PrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
    public:
        PrimaryGeneratorAction();
        ~PrimaryGeneratorAction() override;

        void GeneratePrimaries(G4Event *aEvent) override;
}
} // 名前空間
```

## ソースファイル

```cpp
// //////////////////////////////////////////////////
// src/PrimaryGeneratorAction.cc
// //////////////////////////////////////////////////
#include "PrimaryGeneratorAction.hh"

namespace 名前空間
{
// //////////////////////////////////////////////////
// コンストラクター
// //////////////////////////////////////////////////
PrimaryGeneratorAction::PrimaryGeneratorAction
{

}

// //////////////////////////////////////////////////
// デストラクター
// //////////////////////////////////////////////////
PrimaryGeneratorAction::~PrimaryGeneratorAction
{

}

// //////////////////////////////////////////////////
// 一次粒子の生成の生成に必要な関数
// //////////////////////////////////////////////////
void PrimaryGeneratorAction::GeneratePrimaries(G4Event *aEvent)
{

}

} // 名前空間
```

## メイン関数

```cpp
int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    // DetectorConstruction
    // PhysicsList

    auto actions = new ActionInitialization;
    rm->SetUserInitialization(actions);
}
```

:::{caution}

`PrimaryGeneratorAction`は、メイン関数の中ではなく、
`ActionInitialization`クラスの中でセットアップします。

:::

## リファレンス

- [G4VUserPrimaryGeneratorAction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPrimaryGeneratorAction.html)
