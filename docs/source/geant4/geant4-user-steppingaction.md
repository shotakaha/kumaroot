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
// SteppingAction.hh
#ifndef SteppingAction_H
#define SteppingAction_H 1

#include "G4UserSteppingAction.hh"

namespace プロジェクト名
{
class SteppingAction : public G4UserSteppingAction
{
    public:
        SteppingAction();
        ~SteppingAction() override = default;

        // 基底クラスを上書きする
        void UserSteppingAction(const G4Step* aStep) override;

    private:
        EventAction *fEventAction = nullptr;
        G4LogicalVolume *fScoringVolume = nullptr;

}

}  // プロジェクト名
#endif
```

ステッピングアクションは``G4UserSteppingAction``を継承したクラスを自作します。
仮想関数として定義されている``UserSteppingAction``を実装します。


```cpp
void SteppingAction::UserSteppingAction(const G4Step *aStep)
{
    // スコアリングボリュームを取得する
    if (!fScoringVolume) {
        const auto detector = static_cast<const DetectorConstruction*>(G4RunManager::GetRunManager()->GetUserDetectorConstruction());
        fScoringVolume = detector->GetScoringVolume();
    }

    // ステップがあるボリュームを取得する
    G4LogicalVolume *pVolume = aStep->GetPreStepPoint()->GetTouchableHandle()->GetVolume()->GetLogicalVolume();

    // スコアリングすべきか判断する
    if (pVolume != fScoringVolume) return;

    // このステップのエネルギー損失を取得する
    G4double energy_deposit = aStep->GetTotalEnergyDeposit();
}
```

## ステップの現在情報が欲しい

現在のステップの情報は、**ステップの始点**（``aStep->GetPreStepPoint``）から取得します。
始点（と終点）は``G4StepPoint``クラスのオブジェクトなので[G4StepPoint Class Reference](https://apc.u-paris.fr/~franco/g4doxy/html/classG4StepPoint.html)を参照しながら、欲しい物理量を探します。

## ボリュームをしりたい

```cpp
G4LogicalVolume *current_volume = aStep->GetPreStepPoint()->GetTouchableHandle()->GetVolume()->GetLogicalVolume()
```

現在のステップの論理ボリュームを取得します。
スコアリング対象のボリュームかどうかの条件に利用できます。

## エネルギー損失を知りたい（``GetTotalEnergyDeposit``）

```cpp
G4double the_total_energy_deposit = aStep->GetTotalEnergyDeposit();
G4double the_non_ionizing_energy_deposit = aStep->GetNonIonizingEnergyDeposit();
```

現在のステップで発生したエネルギー損失を取得できます。
この値を足し上げると、トラック全体のエネルギー損失が計算できます。

:::{note}

``aStep->GetPreStepPoint()->GetTotalEnergy()`` との関係がよく分かっていません。

:::

## トラックが欲しい（``GetTrack``）

```cpp
G4Track *pTrack = aStep->GetTrack()
```

## ステップの長さが欲しい（``GetStepLength``）

```cpp
G4double the_step_length = aStep->GetStepLength();
```

## ステップ前後の差をしりたい

```cpp
G4double delta_energy = aStep->GetDeltaEnergy();
G4double delta_time->GetDeltaTime();
G4ThreeVector delta_momentum = aStep->GetDeltaMomentum();
G4ThreeVector delta_position->GetDeltaPosition();
```

``GetDelta*``メソッドで、ステップの始点（``PreStepPoint``）と終点（``PostStepPoint``）の差を取得できます。
