# トラック番号をしりたい（``G4Track::GetTrackID``）

```cpp
// G4Track *aTrack
G4int track_id = aTrack->GetTrackID();
```

``GetTrackID``でトラック番号を取得できます。
トラック番号は1からはじまります。
イベントごとにリセットされます。

## 親トラックをしりたい（``G4Track::GetParentID``）

```cpp
G4int parent_id = aTrack->GetParentID();

if (parent_id == 0) {
    G4cout << "入射粒子の処理" << G4endl;
};
```

``GetParentID``で親トラックの番号を取得できます。
初期粒子は親を持たないため、親IDは0です。
