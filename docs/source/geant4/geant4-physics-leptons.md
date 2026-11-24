# レプトンしたい（``ConstructLeptons``）

```cpp
void PhysicsList::ConstructLeptons()
{
    // electron
    G4Electron::Definition();
    G4Positron::Definition();

    // muon
    G4MuonMinus::Definition();
    G4MuonPlus::Definition();

    // neutrino
    G4NeutrinoE::Definition();
    G4NeutrinoMu::Definition();
    G4AntiNeutrinoE::Definition();
    G4AntiNeutrinoMu::Definition();
}
```

:::{seealso}

- [G4VUserPhysicsList](https://geant4.kek.jp/Reference/11.4.0/classG4VUserPhysicsList.html)

:::
