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

```{toctree}
geant4-command
geant4-macro
gean4-batch
```


:::{seealso}
- [](./geant4-detectorconstruction.md)
- [](./geant4-physicslist.md)
- [](./geant4-actioninitialization.md)
:::
