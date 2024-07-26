# ステッピングアクションしたい（``G4UserSteppingAction``）

ステップごとのデータを収集したい場合は、
``G4UserSteppingAction``クラスを継承したクラスを作成します。

:::{hint}

測定器のヒット情報を取得するときにステップ情報へのアクセスが必要になります。
その場合は、迷わず[G4VSensitiveDetectorクラス](./geant4-sensor-sensitivedetector.md)を使いましょう。

:::

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## 親クラス

- [G4UserSteppingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserSteppingAction.html)

```cpp
G4UserSteppingAction();
virtual ~G4UserSteppingAction() = default;
virtual void UserSteppingAction(const G4Step*){};
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``UserSteppingAction()``は、ステッピング処理で実行される関数です。
仮想関数になっているため、設定は必須ではありません。
必要に応じて自作クラスでoverrideします。

## SteppingActionクラス

```cpp
// include/SteppingAction.hh

#ifndef SteppingAction_h
#define SteppingAction_h 1

#include "G4UserSteppingAction.hh"

namespace ToyMC
{

class SteppingAction : public G4UserSteppingAction
{
  public:
    SteppingAction() = default;
    ~SteppingAction() = default;

    void UserSteppingAction(const G4Step* aStep) override;
}

}  // namespace ToyMC

#endif
```

ステッピングアクションは``G4UserSteppingAction``を継承したクラスを自作します。
仮想関数として定義されている``UserSteppingAction``を実装します。

## 境界判断したい

```cpp
auto pre_step = aStep->GetPreStepPoint();
auto status = pre_step->GetStepStatus();

if (status == fWorldBoundary) { "ワールド境界の外に到達" };
if (status == fGeomBoundary) { "ジオメトリ境界に到達 = いまのボリュームに入射した" };
if (status == fUserDefinedLimit) { "ユーザー設定のリミットに到達" };
if (status == fUndefined) { "ステップが未定義" };
```
