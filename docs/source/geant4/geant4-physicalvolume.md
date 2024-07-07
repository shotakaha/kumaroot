# 物理ボリュームしたい（``G4VPhysicalVolume``）

```cpp
// ステップ（の始点）の物理ボリュームを取得
auto pre_step = aStep->GetPreStepPoint();
auto pv = pre_step->GetPhysicalVolume();

auto name = pv->GetName();
G4int copy_number = pv->GetCopyNo();

auto lv = pv->GetLogicalVolume();
auto mv = pv->GetMotherLogical();
auto material = lv->GetMaterial();
```

物理ボリュームから論理ボリュームにアクセスできます。

:::{seealso}

- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
