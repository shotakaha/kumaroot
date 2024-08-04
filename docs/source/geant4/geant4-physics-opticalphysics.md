# OpticalPhysicsしたい（``G4OpticalPhysics``）

```cpp
int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    G4OpticalPhysics *optical_physics = new G4OpticalPhysics{};

    physics->RegisterPhysics(optical_physics);
    rm->SetUserInitialization(physics);

    auto optical_params = G4OpticalParameters::Instance();
    optical_params->SetWSLTimeProfile("delta");
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

## マクロで設定したい（``/process/optical/``）

```cfg
/process/optical/verbose 1

# /process/optical/processActivation KEY bool
/process/optical/processActivation Cerenkov true
/process/optical/processActivation Scintillation true
/process/optical/processActivation OpAbsorption true
/process/optical/processActivation OpRayleigh true
/process/optical/processActivation OpMieHG true
/process/optical/processActivation OpBoundary true
/process/optical/processActivation OpWLS true
/process/optical/processActivation OpWLS2 true
```

``processActivation``でOpticalPhysicsで有効にする物理プロセスを選択できます。
デフォルトでは、関係するすべてのプロセスが有効になっています。
