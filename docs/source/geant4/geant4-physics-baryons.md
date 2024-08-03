# バリオンしたい（``ConstructBaryons``）

```cpp
void PhysicsList::ConstructBaryons()
{
    // proton
    G4Proton::ProtonDefinition();
    G4AntiProton::Definition();

    // neutron
    G4Neutron::Definition();
    G4AntiNeutron::Definition();
}
```
