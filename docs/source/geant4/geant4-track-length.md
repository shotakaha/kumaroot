# トラックの長さをしりたい（``G4Track::GetTrackLength``）

```cpp
// G4Track *aTrack
G4double track_length = aTrack->GetTrackLength();
G4double step_length = aTrack->GetStepLength();

G4debug << "\t[Track::GetTrackLength] TrackLength=" << G4BestUnit{track_length, "Length"} << G4endl;
G4debug << "\t[Track::GetStepLength]  StepLength=" << G4BestUnit{step_length, "Length"} << G4endl;

// [Track::GetTrackLength] TrackLength=11.7177 cm
// [Track::GetStepLength]  StepLength=1.04428 cm
```

``GetTrackLength``でトラックの全飛程を取得できます。
また、``GetStepLength``で、直近のステップの長さを取得できます。

:::{seealso}

``Track::GetStepLength``と``Step::GetStepLength``は同じです。

- [](./geant4-step-length.md)

:::
