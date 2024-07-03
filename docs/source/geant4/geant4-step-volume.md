# ステップ点のボリュームをしりたい（``GetPhysicalVolume``）

```cpp
G4PreStepPoint pre_step = aStep->GetPreStepPoint();
G4VPhysicalVolume *physical_volume = pre_step->GetPhysicalVolume();
G4int copy_number = physical_volume->GetCopyNo();
G4String name = physical_volume->GetName();
G4LogicalVolume *logical_volume = physical_volume->GetLogicalVolume();
G4Material *material = logical_volume->GetMaterial();
```

ステップのボリューム情報は、``PreStepPoint``から取得できます。
``GetPhysicalVolume``でステップ（の始点）がある物理ボリュームを取得し、
その物理ボリュームを介して論理ボリュームを取得できます。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)

:::
