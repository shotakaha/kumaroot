# データを詰めたい（``SensorHit::Fill``）

```cpp
#include "SensorHit.hh"    // 自作のG4VHitクラス

#include "G4SystemOfUnit.hh"
#include "G4RunManager.hh"
#include "G4EventManager.hh"
#include "G4Step.hh"

void SensorHit::Fill(G4Step *aStep)
{
    // G4Run
    // G4Event
    //
    // G4Step
    fEnergyDeposit = aStep->GetTotalEnergyDeposit() / MeV;

    // G4StepPoint
    auto pre_step = aStep->GetPreStepPoint();
    fStepXYZ = pre_step->GetPosition() / mm;
    fStepGlobalTime = pre_step->GetGlobalTime() / ns;
    fStepTotalEnergy = pre_step->GetTotalEnergy() / MeV;

    // G4Track
    auto track = aStep->GetTrack();
    fTrackID = track->GetTrackID();
    fTrackParentID = track->GetParentID();
    fStepID = track->GetCurrentStepNumber();
    fTrackLength = track->GetTrackLength() / mm;
    fStepLength = track->GetStepLength() / mm;
    fTrackXYZ = track->GetPosition() / mm;
    fTrackTotalEnergy = track->GetTotalEnergy() / MeV;
    // fTrackKineticEnergy
    // fTrackMomentum
    // fTrackMomentumDirection
    fVertexXYZ = track->GetVertexPosition() / mm;
    // fVertexKineticEnergy
    // fVertexMomentumDirection

    // G4TouchableHistory
    auto touch = pre_step->GetTouchableHandle();
    fHistoryDepth = touch->GetHistoryDepth();
    fCopyNumber = touch->GetCopyNumber();
    fReplicaNumber = touch->GetReplicaNumber();

    // G4VPhysicalVolume
    auto pv = pre_step->GetPhysicalVolume();
    fDetectorID = pv->GetCopyNo();
    fPVName = pv->GetName();

    // G4LogicalVolume
    auto lv = pv->GetLogicalVolume();
    fLVName = lv->GetName();

    // G4ParticleDefinition
    auto particle = track->GetParticleDefinition();
    fParticleName = particle->GetParticleName();
    fParticleID = particle->GetPDGEncoding();
};
```

``Fill``で、``G4Step``からアクセスできる物理量を（ほぼ）すべて取得しています。

ラン番号とイベント番号は、ステップからは取得できないため、
G4RunManagerとG4EventManagerに直接聞いています。

## リファレンス

- [G4RunManager](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)
- [G4EventManager](https://geant4.kek.jp/Reference/11.2.0/classG4EventManager.html)
- [G4Run](https://geant4.kek.jp/Reference/11.2.0/classG4Run.html)
- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)
- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)
- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)
- [G4TouchableHistory](https://geant4.kek.jp/Reference/11.2.0/classG4TouchableHistory.html)
- [G4ParticleDefinition](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleDefinition.html)
