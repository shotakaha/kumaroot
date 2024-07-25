# メイン関数したい（``main()``）

```cpp
int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto detector = new DetectorConstruction{};
    rm->SetUserInitialization(detector);

    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);

    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);

    rm->Initialize();

    G4int nevents = 100;
    rm->BeamOn(nevents);

    delete rm;
    return 0;
}
```

1. G4RunManagerFactory
2. G4VisExecutive
3. G4UImanager

```{toctree}
geant4-command
geant4-macro
geant4-batch
```

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
