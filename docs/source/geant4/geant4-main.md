# メイン関数したい（``main()``）

```cpp
#include "Geometry.hh"              // G4VUserDetectorConstructionを継承した自作クラス
#include "ActionInitialization.hh"  // G4VUserActionInitializationを継承した自作クラス

#include "G4RunManagerFactory.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto geometry = new Geometry{};
    rm->SetUserInitialization(detector);

    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);

    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);

    rm->Initialize();

    G4int n_events = 100;
    rm->BeamOn(n_events);

    delete rm;
    return 0;
}
```

バッチモードで実行する場合の必要最低限の``main()``関数です。

1. G4RunManagerFactory
2. G4VisExecutive
3. G4UImanager

:::{seealso}

- [](./geant4-user-detectorconstruction.md)
- [](./geant4-user-physicslist.md)
- [](./geant4-user-actioninitialization.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)

:::

## リファレンス

- [How to Define the main() Program](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html)
