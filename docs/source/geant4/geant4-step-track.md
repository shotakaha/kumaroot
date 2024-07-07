# ステップのトラックをしりたい（``GetTrack``）

```cpp
// G4Step *aStep
G4Track *track = aStep->GetTrack();
G4int track_id = track->GetTrackID();
```

該当するステップがあるトラック（``G4Track``）を取得できます。
トラックIDなどにアクセスできるようになります。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)

:::
