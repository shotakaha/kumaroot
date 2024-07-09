# トラックの座標をしりたい（``G4Track::GetPosition``）

```cpp
// G4Track *aTrack
G4ThreeVector position = aTrack->GetPosition();
```

トラックの座標を取得できます。
座標の原点はワールドボリュームの中心です。
