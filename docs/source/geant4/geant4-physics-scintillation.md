# シンチレーション光したい（``G4Scintillation``）

```cpp
#include "G4Scintillation.hh"

G4Scintillation *process = G4Scintillation{};

process->SetScintillationYieldFactor(1.0);
process->SetTrackSecondariesFirst(true);
```

:::{seealso}

- [](./geant4-material-propertiestable.md)

:::

## シンチレーション光の数をしりたい（``GetNumPhotons``）

```cpp
G4int n_photons = sc->GetNumPhotons();
```
