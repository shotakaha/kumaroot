# ステップ情報したい（``G4Step``）

ステップ（``G4Step``）は、Geant4シミュレーションにおけるトラッキングの基本単位です。
ステップは**始点**（``PreStepPoint``）と**終点**（``PostStepPoint``）で構成されていて、
それぞれの場所での粒子の状態を取り出すことができます。

始点（と終点）は``G4StepPoint``クラスのオブジェクトなので[G4StepPoint Class Reference](https://apc.u-paris.fr/~franco/g4doxy/html/classG4StepPoint.html)を参照して、欲しい物理量を探します。

## 座標をしりたい（``GetPosition``）

```cpp
G4ThreeVector position = aStep->GetPreStepPoint()->GetPosition();
G4ThreeVector position = aStep->GetPreStepPoint()->GetPosition();
```

ステップ点の座標を取得できます。
座標の原点はワールドボリュームの中心です。

## ボリュームをしりたい

```cpp
G4VPhysicalVolume *physical_volume = aStep->GetPhysicalVolume();
G4int copy_number = physical_volume->GetCopyNumber();
G4String name = physical_volume->GetName();
G4LogicalVolume *logical_volume = physical_volume->GetLogicalVolume();
G4Material *material = logical_volume->GetMaterial();
```

ステップ点のボリュームを取得できます。
ボリュームの情報も取得できます。

## ステップの状態をしりたい（``GetStepStatus``）

```cpp
G4StepStatus status = aStep->GetPreStepPoint()->GetStepStatus();
G4StepStatus status = aStep->GetPostStepPoint()->GetStepStatus();
```

``GetStepStatus``で、ステップ点の境界の状態を取得できます。

- ``fWorldBoundary``: ステップがワールド境界に到達した状態
- ``fGeomBoundary``: ステップが物質の境界に到達した状態
- ``fAtRestDoItProc``:
- ``fAlongStepDoItProc``:
- ``fPostStepDoItProc``:
- ``fUserDefinedLimit``:
