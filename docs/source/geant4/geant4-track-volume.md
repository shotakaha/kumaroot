# トラックのボリュームをしりたい（``G4Track::GetVolume``）

```cpp
G4VPhysicalVolume *physical_volume = aTrack->GetVolume();
G4VPhysicalVolume *next_volume = aTrack->GetNextVolume();
G4LogicalVolume *logical_volume = aTrack->GetLogicalVolumeAtVertex();
```

物理ボリューム（``G4VPhysicalVolume``）は``G4Track``クラスのオブジェクトから取得できます。
``GetVolume``でトラックがある物理ボリュームを取得できます。
``GetNextVolume``で、トラックの進む先の物理ボリュームも取得できます。
また、``GetLogicalVolumeAtVertex``で論理ボリュームを直接取得できます。

取得した物理ボリューム（のポインター）を介して論理ボリュームを取得できます。
物理ボリュームの操作は[](./geant4-physicalvolume.md)を参照してください。

:::{note}

未チェックですが、
トラック：``aTrack->GetLogicalVolumeAtVertex()``と
ステップ：``aStep->GetPreStepPoint()->GetPhysicalVolume()->GetLogicalVolume()``は
同じになるはずです。

:::

:::{seealso}

- [](./geant4-step-steppoint-volume.md)

:::
