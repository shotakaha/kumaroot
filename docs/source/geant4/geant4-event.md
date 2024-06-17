# イベント情報したい（``G4Event``）

[G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)はイベント情報を管理するクラスです。

## イベント番号をしりたい（``GetEventID``）

```cpp
G4int event_id = aEvent->GetEventID()
```

## 一次粒子をしりたい（``GetPrimaryVertex``）

```cpp
G4int n_vertex = aEvent->GetNumberOfPrimaryVertex();
G4PrimaryVertex vertex = aEvent->GetPrimaryVertex(id);
```

## 飛跡情報をしりたい（``GetTrajectoryContainer``）

```cpp
G4TrajectoryContainer *tjc = aEvent->GetTrajectoryContainer();
```

## ヒット情報をしりたい（``GetHCofThisEvent``）

```cpp
G4HCofThisEvent *hc = aEvent->GetHCofThisEvent()
G4DCofThisEvent *dc = aEvent->GetDCofThisEvent()
```

## リファレンス

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)
- [G4TrajectoryContainer](https://geant4.kek.jp/Reference/11.2.0/classG4TrajectoryContainer.html)
- [G4VTrajectory](https://geant4.kek.jp/Reference/11.2.0/classG4VTrajectory.html)
- [G4PrimaryVertex](https://geant4.kek.jp/Reference/11.2.0/classG4PrimaryVertex.html)
- [G4PrimaryParticle](https://geant4.kek.jp/Reference/11.2.0/classG4PrimaryParticle.html)
- [G4HCofThisEvent](https://geant4.kek.jp/Reference/11.2.0/classG4HCofThisEvent.html)
- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4DCofThisEvent](https://geant4.kek.jp/Reference/11.2.0/classG4DCofThisEvent.html)
- [G4VDigiCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VDigiCollection.html)
