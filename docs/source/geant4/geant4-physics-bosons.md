# ボソンしたい（``ConstructBosons``）

```cpp
void PhysicsList::ConstructBosons()
{
    // pseudo-particles
    G4Geantino::Definition();
    G4ChargedGeantino::Definition();

    // gamma
    G4Gamma::Definition();

    // optical photon
    G4OpticalPhoton::Definition();
}
```

## リファレンス

- G4Geantino
- G4ChargedGeantino
- G4Gamma
- G4OpticalPhoton
