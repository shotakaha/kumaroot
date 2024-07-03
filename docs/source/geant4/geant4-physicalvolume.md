# 物理ボリュームしたい（``G4VPhysicalVolume``）

```cpp
// ステップ（の始点）の物理ボリュームを取得
auto pre_step = aStep->GetPreStepPoint();
auto physical_volume = pre_step->GetPhysicalVolume();

auto name = physical_volume->GetName();
auto logical_volume = physical_volume->GetLogicalVolume();
auto mother_volume = physical_volume->GetMotherLogical();
```

物理ボリュームから論理ボリュームにアクセスできます。

:::{seealso}

- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
