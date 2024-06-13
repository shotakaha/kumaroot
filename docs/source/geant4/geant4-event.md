# イベント情報したい（``G4Event``）

[G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4Event.html)はイベント情報を管理するクラスです。

## イベント番号をしりたい（``GetEventID``）

```cpp
G4int event_id = aEvent->GetEventID()
```

## 一次粒子をしりたい（``GetPrimaryVertex``）

```cpp
G4int n_vertex = aEvent->GetNumberOfPrimaryVertex();
G4PrimaryVertex vertex = aEvent->GetPrimaryVertex(n_vertex);
```

## ヒット情報をしりたい（``GetHCofThisEvent``）

```cpp
G4HCofThisEvent *hc = aEvent->GetHCofThisEvent()
G4DCofThisEvent *dc = aEvent->GetDCofThisEvent()
```
