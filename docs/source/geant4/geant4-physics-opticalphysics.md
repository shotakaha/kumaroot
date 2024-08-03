# OpticalPhysicsしたい（``G4OpticalPhysics``）

```cpp
int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    G4OpticalPhysics *optical_physics = new G4OpticalPhysics{};

    physics->RegisterPhysics(optical_physics);
    rm->SetUserInitialization(physics);
}
```

``FTFP_BERT``モデルに``OpticalPhysics``を追加しています。

このOpticalPhysicsでは、
吸収（``G4OpAbsorption``）、
レイリー散乱（``G4OpRayleigh``）、
ミー散乱（``G4OpMieHG``）、
波長変換（``G4OpWLS``と``G4OpWLS2``）、
境界での散乱（``G4OpBoundary``）、
の物理プロセスを通じて相互作用できるようになります。

:::{seealso}

- [](./geant4-physics-opticalphoton.md)
- [](./geant4-material-propertiestable.md)

:::
