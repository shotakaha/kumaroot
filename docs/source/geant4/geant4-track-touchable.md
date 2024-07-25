# トラックのタッチャブルしたい（``G4Track::GetTouchableHandle``）

```cpp
// G4Track *aTrack
auto aTouch = aTrack->GetTouchableHandle();
auto aNextTouch = aTrack->GetTouchableHandle();
```

``GetTouchableHandle``で、現在のトラックの物理ボリュームにアクセスできるようになります。
具体的な使い方は[](./geant4-touchable.md)に整理しました。
