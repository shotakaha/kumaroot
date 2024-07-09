# すべてのヒット配列をしりたい（``HCofThisEvent`` / ``DCofThisEvent``）

```cpp
G4HCofThisEvent *hce = aEvent->GetHCofThisEvent()
G4DCofThisEvent *dce = aEvent->GetDCofThisEvent()
```

ひとつのイベントに含まれる、すべてのヒット情報の配列（``HitsCollection``）を取得できます。

## ヒット配列をしりたい（``HC``）

```cpp
G4HCofThisEvent *hce = aEvent->GetHCofThisEvent()
G4int n_hc = hce->GetNumberOfCollections();
G4VHitsCollection *hc = hce->GetHC(id);
hc->PrintAllHits();
```

## ヒット情報をしりたい（``Hit``）

```cpp
G4HCofThisEvent *hce = aEvent->GetHCofThisEvent()
G4int n_hc = hce->GetNumberOfCollections();
G4VHitsCollection *hc = hce->GetHC(id);
G4int hc->GetSize();
G4VHit *hit = hc->GetHit(id);
hit->Print();
```

``GetNumberOfCollections``でリストの要素数を取得できます。
要素のインデックスを指定して、ヒット情報（``G4VHitsCollection``）を取得できます。

:::{seealso}

- [G4HCofThisEvent](https://geant4.kek.jp/Reference/11.2.0/classG4HCofThisEvent.html)
- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4DCofThisEvent](https://geant4.kek.jp/Reference/11.2.0/classG4DCofThisEvent.html)
- [G4VDigiCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VDigiCollection.html)

:::
