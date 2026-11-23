# トラックの状態をしりたい（``G4Track::GetTrackStatus``）

`GetTrackStatus()`で、トラックの状態（`G4TrackStatus`）を取得できます。
状態は`fAlive`（追跡を継続）や`fStopAndKill`（追跡を停止して消滅）などの値で表されます。

```cpp
// G4Track *aTrack;
G4int status = aTrack->GetTrackStatus();
```

:::{seealso}

- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)

:::
