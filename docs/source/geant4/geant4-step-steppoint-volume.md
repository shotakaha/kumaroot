# ステップポイントのボリュームをしりたい（``G4StepPoint::GetPhysicalVolume``）

```cpp
// G4Step *aStep

// 現在のステップのボリュームを取得する
G4StepPoint *pre_step = aStep->GetPreStepPoint();
auto current_volume = pre_step->GetPhysicalVolume();

// 次のステップのボリュームを取得する
G4StepPoint *post_step = aStep->GetPostStepPoint();
auto next_volume = post_step->GetPhysicalVolume();
```

物理ボリューム（``G4VPhysicalVolume``）は``G4StepPoint``クラスのオブジェクトから取得できます。
現在のステップのボリューム情報は、ステップの始点（``PreStepPoint``）から取得します。
また、次のボリューム情報は``PostStepPoint``から取得します。

取得した物理ボリューム（のポインター）を介して論理ボリュームを取得できます。
物理ボリュームの操作は[](./geant4-physicalvolume.md)を参照してください。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)

:::
