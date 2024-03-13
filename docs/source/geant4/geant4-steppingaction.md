# SteppingActionしたい（``G4UserSteppingAction``）

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

## ステップの現在情報が欲しい

```cpp
G4ThreeVector position = aStep->GetPreStepPoint()->GetPosition();
G4double local_time = aStep->GetPreStepPoint()->GetLocalTime();
G4ThreeVector momentum = aStep->GetPreStepPoint()->GetMomentum();
G4double total_energy = aStep->GetPreStepPoint()->GetTotalEnergy();
G4double kinetic_energy = aStep->GetPreStepPoint()->GetKineticEnergy();
```

ステップの現在情報は、ステップの始点（``aStep->GetPreStepPoint``）から取得します。始点（と終点）は``G4StepPoint``クラスのオブジェクトなので[G4StepPoint Class Reference](https://apc.u-paris.fr/~franco/g4doxy/html/classG4StepPoint.html)を参照すれば、欲しい物理量を確認できます。

## ボリュームをしりたい

```cpp
G4LogicalVolume *the_volume = aStep->GetPreStepPoint()->GetTouchableHandle()->GetVolume()->GetLogicalVolume()
```

現在のステップの場所は、``aStep->GetPreStepPoint()``のボリュームで判断します。
スコアリング対象のボリュームかどうかの条件に利用できます。

## 時刻がほしい

```cpp

```

## エネルギー損失を知りたい（``GetTotalEnergyDeposit``）

```cpp
G4double the_total_energy_deposit = aStep->GetTotalEnergyDeposit();
G4double the_non_ionizing_energy_deposit = aStep->GetNonIonizingEnergyDeposit();
```

現在のステップで発生したエネルギー損失を取得できます。
この値を足し上げると、トラック全体のエネルギー損失が計算できます。

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

