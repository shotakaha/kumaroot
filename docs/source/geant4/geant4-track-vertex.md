# トラックの一次粒子をしりたい（``G4Track::GetVertexPosition``）

```cpp
G4ThreeVector vertex_position = aTrack->GetVertexPosition();
G4ThreeVector vertex_momentum_direction = aTrack->GetVertexMomentumDirection();
G4Double vertex_kinetic_energy = aTrack->GetVertexKineticEnergy();

G4debug << G4BestUnit(vertex_position, "Length") << G4endl;
// 0.000945927 0.00107488 -9.7208 cm

G4debug << G4BestUnit(vertex_momentum_direction, "Length") << G4endl;
// 265.486 111.94 957.594 um

G4debug << G4BestUnit(vertex_kinetic_energy, "Energy") << G4endl;
// 1.43995 MeV
```
