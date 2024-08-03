# Optical Photonしたい（``G4OpticalPhysics``）



```cpp
#include "G4OpticalPhoton.hh"

auto physics = G4OpticalPhoton::Definition();

// 以下の2つのstaticメソッドはDefinition()と同じ
auto physics = G4OpticalPhoton::OpticalPhotonDefinition();
auto physics = G4OpticalPhoton::OpticalPhoton();
```

