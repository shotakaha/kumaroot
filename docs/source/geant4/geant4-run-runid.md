# ラン番号をしりたい（`G4Run::GetRunID`）

```cpp
// void MyRunAction::EndOfRunAction(const G4Run* aRun) の中
G4int run_id = aRun->GetRunID();
```

## G4Stepからラン番号をしりたい

```cpp
#include "G4Run.hh"
#include "G4RunManager.hh"

const G4Run* run = G4RunManager::GetRunManager()->GetCurrentRun();
G4int run_id = run->GetRunID();
```

`G4Step`からは、現在の`G4Run`に直接アクセスできません。
そのため、`G4RunManager`を経由して`G4Run`を取得し、ランIDを取り出します。

## G4Trackからラン番号をしりたい

```cpp
#include "G4Run.hh"
#include "G4RunManager.hh"

const G4Run* run = G4RunManager::GetRunManager()->GetCurrentRun();
G4int run_id = run->GetRunID();
```

`G4Track`からも、現在の`G4Run`に直接アクセスできません。
`G4Step`の場合と同じく、`G4RunManager`を経由して取得します。

## G4Eventからラン番号をしりたい

```cpp
#include "G4Run.hh"
#include "G4RunManager.hh"

const G4Run* run = G4RunManager::GetRunManager()->GetCurrentRun();
G4int run_id = run->GetRunID();
```

`G4Event`からも、`G4Run`に直接アクセスできません。
同じく`G4RunManager`を経由して取得します。

:::{seealso}

- [G4Run](https://geant4.kek.jp/Reference/11.2.0/classG4Run.html)

:::
