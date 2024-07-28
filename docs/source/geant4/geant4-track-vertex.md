# トラックの入射点をしりたい（``G4Track::GetVertexPosition``）

```cpp
G4ThreeVector position = aTrack->GetVertexPosition();
G4debug << G4BestUnit(position, "Length") << G4endl;
// 0.000945927 0.00107488 -9.7208 cm
```

## トラックの入射エネルギーをしりたい（``G4Track::GetKineticEnergy``）

```cpp
G4Double kinetic_energy = aTrack->GetVertexKineticEnergy();
G4debug << G4BestUnit(kinetic_energy, "Energy") << G4endl;
// 1.43995 MeV
```

## トラックの入射方向をしりたい（``G4Track::GetVertexMomentumDirection``）

```cpp
G4ThreeVector direction = aTrack->GetVertexMomentumDirection();
G4debug << G4BestUnit(direction, "Length") << G4endl;
// 265.486 111.94 957.594 um


```
