# タッチャブルしたい（``G4TouchableHistory``）

```cpp
// G4Step *aStep
G4Touchable aTouch = aStep->GetPreStepPoint()->GetTouchableHandle();

G4int depth = aTouch->GetHistoryDepth();
auto pv = aTouch->GetVolume();
auto solid = aTouch->GetSolid();
G4int replica_number = aTouch->GetReplicaNumber();
G4int copy_number = aTouch->GetCopyNumber();
```

``G4VTouchable``は、現在のステップ点（``G4StepPoint``）やトラック（``G4Track``）が持つ物理ボリューム情報のポインターです。

レプリカ番号を取得するために使います。

## リファレンス

- [G4TouchableHistory](https://geant4.kek.jp/Reference/11.2.0/classG4TouchableHistory.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)
- [Touchables: Uniquely Identifying a Volume - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/Geometry/geomTouch.html)
