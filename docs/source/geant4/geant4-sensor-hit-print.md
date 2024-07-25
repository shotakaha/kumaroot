# 出力したい（``G4VHit::Print``）

```cpp
void SensorHit::Print()
{
    G4debug << "SensorHit::Print" << G4endl;

    G4debug << "DetectorID" << fDetectorID << G4endl;
    G4debug << "TrackID" << fTrackID << G4endl;
    G4debug << "XYZ" << G4BestUnit(fXYZ, "Length") << G4endl;
    G4debug << "GlobalTime" << G4BestUnit(fGlobalTime, "Time") << G4endl;
    G4debug << "EnergyDeposit" << G4BestUnit(fEnergyDeposit, "Energy") << G4endl;
    G4debug << "TrackLength" << G4BestUnit(fTrackLength, "Length") << G4endl;
    G4debug << "StepLength" << G4BestUnit(fStepLength, "Length") << G4endl;
};
```

``Print``で、ヒット配列の値を確認しています。
