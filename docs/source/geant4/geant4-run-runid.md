# ラン番号をしりたい（``G4Run::GetRunID``）

```cpp
// G4Run *aRun;
G4int run_id = aRun->GetRunID();
```

## G4Stepからラン番号をしりたい

```cpp
G4RunManager* rm = G4RunManager::GetRunManager();
G4Run* run = rm->GetCurrentRun();
G4int run_id = run->GetRunID();
```

``G4Step``オブジェクトから、現在の``G4Run``には直接アクセスできません。
しかたがないので、``G4RunManager``オブジェクトから直接``G4Run``にアクセスしランIDを取得します。
