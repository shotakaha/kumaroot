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
