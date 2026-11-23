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

:::{seealso}

- [G4VUserPhysicsList](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPhysicsList.html)

:::
