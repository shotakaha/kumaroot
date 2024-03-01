# マルチスレッド対応（``G4MTRunManager``）

```cpp
#include "G4MTRunManager.hh"

G4MTRunManager *runManager = new G4MTRunManager();
runManager->SetUserInitialization(new MYDetectorConstruction);
runManager->SetUserInitialization(new MYPhysicsList);
runManager->SetUserInitialization(new MYActionInitialization);
```

``G4RunManager``を``G4MTRunManager``クラスにすれば、マルチスレッド処理できます。
Geant4.11.0からマルチスレッドに対応しています。
ビルド時もデフォルトで``GEANT4_MULTITHREADED=ON``になっていました。
