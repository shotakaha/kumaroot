# ランマネージャー（``G4RunManager``）

```cpp
#include "G4RunManagerFactory.hh"

auto *runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);
```

[CreateRunManager](https://apc.u-paris.fr/~franco/g4doxy4.11/html/classG4RunManagerFactory.html)をって、
その場にあったランマネージャーを作成できます。

## シングルスレッドしたい（``G4RunManager``）

```cpp
#include "G4RunManager.hh"

G4RunManager* runManager = new G4RunManager();
```

## マルチスレッドしたい（``G4MTRunManager``）

```cpp
#include "G4RunManager.hh"

G4MTRunManager * runManager = new G4MTRunManager();
```

