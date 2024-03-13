# ステップ情報したい（``G4Step``）

ステップ（``G4Step``）は、Geant4シミュレーションにおけるトラッキングの基本単位です。
ステップは**始点**（``PreStepPoint``）と**終点**（``PostStepPoint``）で構成されており、
それぞれの点での粒子の状態を取り出すことができます。

始点と終点は``G4StepPoint``クラスのオブジェクトなので[G4StepPoint Class Reference](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)を参照して、欲しい物理量を探します。

## 座標をしりたい（``GetPosition``）

```cpp
G4ThreeVector position = aStep->GetPreStepPoint()->GetPosition();
G4ThreeVector position = aStep->GetPreStepPoint()->GetPosition();
```

ステップ点の座標を取得できます。
座標の原点はワールドボリュームの中心です。

## 時刻をしりたい（``GetLocalTime``）

```cpp
G4double local_time = aStep->GetPreStepPoint()->GetLocalTime();
G4double global_time = aStep->GetPreStepPoint()->GetGlobalTime();
G4double proper_time = aStep->GetPreStepPoint()->GetProperTime();
```

``GetLocalTime``でトラックが生成されてからの経過時間、
``GetGlobalTime``でトラックが含まれるイベントが生成されてからの経過時間、
``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）を取得できます。

## 運動量をしりたい（``GetMomentum``）

```cpp
G4ThreeVector momentum = aStep->GetPreStepPoint()->GetMomentumDirection();
G4double total_momentum = aStep->GetPreStepPoint()->GetMomentum();
```

``GetMomentumDirection``で運動量の単位ベクトル成分、
``GetMomentum``で運動量の合計を取得できます。

## エネルギーをしりたい（``GetTotalEnergy``）

```cpp
G4double energy = aStep->GetPreStepPoint()->GetTotalEnergy();
G4double kinetic_energy = aStep->GetPreStepPoint()->GetKineticEnergy();
```

``GetTotalEnergy``でエネルギーの合計、
``GetKineticEnergy``で運動エネルギーの合計を取得できます。

## 速度をしりたい（``GetVelocity``）

```cpp
G4double velocity = aStep->GetPreStepPoint()->GetVelocity();
G4double beta = aStep->GetPreStepPoint()->GetBeta();
G4double gamma = aStep->GetPreStepPoint()->GetGamma();
```

``GetVelocity``で速度、
``GetBeta``でβ、
``GetGamma``でγファクターを取得できます。

## 電荷をしりたい（``GetCharge``）

```cpp
G4double charge = aStep->GetPreStepPoint()->GetCharge();
```

``GetCharge``で電荷を取得できます。

## ボリュームをしりたい（``GetPhysicalVolume``）

```cpp
G4VPhysicalVolume *physical_volume = aStep->GetPhysicalVolume();
G4int copy_number = physical_volume->GetCopyNumber();
G4String name = physical_volume->GetName();
G4LogicalVolume *logical_volume = physical_volume->GetLogicalVolume();
G4Material *material = logical_volume->GetMaterial();
```

``GetPhysicalVolume``でステップ点の物理ボリュームを取得できます。
論理ボリュームは物理ボリュームを介して取得できます。

## ステップの状態をしりたい（``GetStepStatus``）

```cpp
G4StepStatus status = aStep->GetPreStepPoint()->GetStepStatus();
G4StepStatus status = aStep->GetPostStepPoint()->GetStepStatus();
```

``GetStepStatus``で、ステップ点の境界の状態を取得できます。
``fWorldBoundary``はステップ点がワールド境界に到達した状態、
``fGeomBoundary``はステップ点が物質の境界に到達した状態です。
他の状態は[enum G4StepStatus](https://geant4.kek.jp/lxr/source//track/include/G4StepStatus.hh)で確認できます。
