# イベントのヒット配列したい（``G4HCofThisEvent``）

```cpp
// G4HCofThisEvent *aHCE;
aHCE->AddHitsCollection(G4int id, G4VHitsCollection *aHC);

// IDを指定してヒット配列を追加する
G4int aID = 0;
auto aHC = new SensorHitsCollection{};
aHCE->AddHitsCollection(aID, aHC)

// IDを指定してヒット配列を取得する
auto hitsCollection = aHCE->GetHC(aID);
```

``AddHitsCollection``で、現在のイベント（``G4Event``）が保持する
``G4HCofThisEvent``（のポインター）に、
データ取得するためのヒット配列を追加できます。

有感検出器クラスの``Initialize``と``EndOfEvent``で、
HCofThisEventに出し入れするときに使います。

## リファレンス

- [G4HCofThisEvent](https://geant4.kek.jp/Reference/11.2.0/classG4HCofThisEvent.html)
