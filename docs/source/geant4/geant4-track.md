# トラックしたい（``G4Track``）

トラック（``G4Track``）は、粒子の進む方向のオブジェクトです。
ステップと同等の情報を持っていますが、薄皮一枚くらい上位のオブジェクト（というイメージ）です。

トラック情報は``G4UserTrackingAction``クラスをフックにしてカスタマイズするのに使います。

## 座標をしりたい（``GetPosition``）

```cpp
G4ThreeVector position = aTrack->GetPosition();
```

トラックの座標を取得できます。
座標の原点はワールドボリュームの中心です。

## 時刻をしりたい（``GetLocalTime``）

```cpp
G4double local_time = aTrack->GetLocalTime();
G4double global_time = aTrack->GetGlobalTime();
G4double proper_time = aTrack->GetProperTime();
```

``GetLocalTime``でトラックが生成されてからの経過時間、
``GetGlobalTime``でトラックが含まれるイベントが生成されてからの経過時間、
``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）を取得できます。

## 運動量をしりたい（``GetMomentum``）

```cpp
G4ThreeVector momentum = aTrack->GetMomentumDirection();
G4double total_momentum = aTrack->GetMomentum();
```

``GetMomentumDirection``で運動量の単位ベクトル成分、
``GetMomentum``で運動量の合計を取得できます。

## エネルギーをしりたい（``GetTotalEnergy``）

```cpp
G4double energy = aTrack->GetTotalEnergy();
G4double kinetic_energy = aTrack->GetKineticEnergy();
```

``GetTotalEnergy``でエネルギーの合計、
``GetKineticEnergy``で運動エネルギーの合計を取得できます。

## ボリュームをしりたい（``GetPhysicalVolume``）

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

## 粒子をしりたい

```cpp
aTrack->GetDynamicParticle();
aTrack->GetParticleDefinition();
```

