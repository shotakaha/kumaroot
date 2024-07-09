# トラックの運動量をしりたい（``G4Track::GetMomentum``）

```cpp
// G4Track *aTrack
G4double momentum = aTrack->GetMomentum();
G4ThreeVector momentum_direction = aTrack->GetMomentumDirection();
```

``GetMomentumDirection``で運動量の単位ベクトル成分、
``GetMomentum``で運動量の合計を取得できます。
