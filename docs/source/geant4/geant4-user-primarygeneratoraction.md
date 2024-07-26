# 一次粒子したい（``G4VUserPrimaryGeneratorAction``）

一次粒子（入射粒子）を定義するクラスは、必須クラスのひとつで、
``G4VUserPrimaryGeneratorAction``クラスを継承して作成します。

## 親クラス

- [G4VUserPrimaryGeneratorAction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPrimaryGeneratorAction.html)

```cpp
G4VUserPrimaryGeneratorAction();
virtual ~G4VUserPrimaryGeneratorAction() = default;
virtual void GeneratePrimaries(G4Event *aEvent) = 0;
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``GeneratePrimaries()``は、イベントの一次粒子を設定するための関数です。
純粋仮想関数になっているため、自作クラスでoverrideが必要です。

## PrimaryGeneratorクラス

クラス名を``PrimaryGenerator``としました。

```cpp
// //////////////////////////////////////////////////
// include/PrimaryGenerator.hh
// //////////////////////////////////////////////////

#ifndef PrimaryGenerator_h
#define PrimaryGenerator_h 1

#include "G4VUserPrimaryGeneratorAction.hh"

namespace ToyMC
{

class PrimaryGenerator : public G4VUserPrimaryGeneratorAction
{
    public:
        PrimaryGenerator() = default;
        ~PrimaryGenerator() = default;

        void GeneratePrimaries(G4Event *aEvent) override;
};

}; // namespace ToyMC

#endif
```
