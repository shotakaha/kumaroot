# トラックのステップ数をしりたい（``G4Track::GetCurrentStepNumber``）

```cpp
// G4Track *aTrack
G4int step_number = aTrack->GetCurrentStepNumber();
```

現在のトラックが持つステップのステップ数を取得します。
ヒット情報を確認するときに、ステップが進んでいるかどうかを判断できます。
