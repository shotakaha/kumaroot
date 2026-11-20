# ラン操作したい（`G4Run`）

```cpp
void MyRunAction::EndOfRunAction(const G4Run* run)
{
    // ランの番号
    G4int runID = run->GetRunID();

    // 処理したイベント数
    G4int nEvents = run->GetNumberOfEvent();

    G4cout << "Run " << runID << ": " << nEvents << " events processed" << G4endl;
}
```

`G4Run`はラン情報を管理するクラスです。
`G4Run`は、ユーザーアクション設定の
[UserRunAction](geant4-user-runaction)の
`BeginOfRunAction`と`EndOfRunAction`の引数として渡されます。
[UserEventAction](geant4-user-eventaction)などから情報を取得したいときにも使います。

```{toctree}
---
maxdepth: 1
---
geant4-run-runid
geant4-run-events
geant4-run-eventvector
geant4-run-random
```

## リファレンス

- [G4Run](https://geant4.kek.jp/Reference/11.4.0/classG4Run.html)
