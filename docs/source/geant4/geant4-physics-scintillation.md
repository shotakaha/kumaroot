# シンチレーション光したい（``G4Scintillation``）

```cpp
#include "G4Scintillation.hh"

auto sc = G4Scintillation{};
```

## シンチレーション光の数をしりたい（``GetNumPhotons``）

```cpp
G4int n_photons = sc->GetNumPhotons();
```
