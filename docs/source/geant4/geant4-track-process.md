# トラックの相互作用をしりたい（``G4Track::GetCreatorProcess``）

```cpp
// G4Track *aTrack
G4VProcess *process = aTrack->GetCreatorProcess();

G4String name = process->GetProcessName();
```

``GetCreatorProcess``で、現在のトラックが生成された相互作用を確認できます。
相互作用の種類によって、ステップ処理を分岐させたいときに使います。
