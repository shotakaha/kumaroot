# チェレンコフ放射したい（``G4Cerenkov``）

```cpp
#include "G4Cerenkov.hh"

auto cerenkov = new G4Cerenkov{};
cerenkov->SetMaxNumPhotonsPerStep(数値);
```

## チェレンコフ光を数えたい（``GetNumPhotons``）

```cpp
G4int n_photons = cerenkov->GetNumPhotons();
```
