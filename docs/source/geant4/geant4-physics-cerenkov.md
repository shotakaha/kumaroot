# チェレンコフ放射したい（``G4Cerenkov``）

```cpp
#include "G4Cerenkov.hh"

G4Cerenkov* process = new G4Cerenkov{};

G4int max_photons = 300;
process->SetMaxNumPhotonsPerStep(max_photons);
process->SetTrackSecondariesFirst(true);
```

チェレンコフ放射は、物質に屈折率（``RINDEX``）が設定されているボリュームで生成されます。

:::{seealso}

- [](./geant4-material-propertiestable.md)

:::

## チェレンコフ光を数えたい（``GetNumPhotons``）

```cpp
G4int n_photons = cerenkov->GetNumPhotons();
```
