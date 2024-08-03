# 相互作用したい（``FTFP_BERT``）

```cpp
#include "FTFP_BERT.hh"
#include "G4VModularPhysicsList.hh"

int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
}
```

``FTFP_BERT``はGeant4.10から標準になった相互作用モデルです。
高エネルギー物理学分野のひとは、まず、このモデルから使ってみればよいそうです。
