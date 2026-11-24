# トラックのステップ数をしりたい（``G4Track::GetCurrentStepNumber``）

```cpp
// G4Track *aTrack
G4int step_number = aTrack->GetCurrentStepNumber();
```

現在のトラックが持つステップのステップ数を取得します。
ヒット情報を確認するときに、ステップが進んでいるかどうかを判断できます。

:::{seealso}

- [G4Track](https://geant4.kek.jp/Reference/11.4.0/classG4Track.html)

:::
