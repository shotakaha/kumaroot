# トラックのボリュームをしりたい（``G4Track::GetVolume``）

```cpp
G4VPhysicalVolume *physical_volume = aTrack->GetVolume();
G4VPhysicalVolume *next_volume = aTrack->GetNextVolume();
G4LogicalVolume *logical_volume = aTrack->GetLogicalVolumeAtVertex();
```

``GetVolume``でトラックがある物理ボリュームを取得できます。
``GetNextVolume``で、トラックの進む先の物理ボリュームも取得できます。
これはステップとトラックのコンセプトの違いを感じられる部分だと思います。

また、``GetLogicalVolumeAtVertex``で論理ボリュームを直接取得できます。

:::{note}

未チェックですが、
トラック：``aTrack->GetLogicalVolumeAtVertex()``と
ステップ：``aStep->GetPreStepPoint()->GetPhysicalVolume()->GetLogicalVolume()``は
同じになるはずです。

:::
