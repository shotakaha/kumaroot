# OpticalPhysicsしたい（``G4OpticalPhysics``）

```cpp
int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    G4OpticalPhysics *optical_physics = new G4OpticalPhysics{};

    physics->RegisterPhysics(optical_physics);
    rm->SetUserInitialization(physics);

    auto optical_params = G4OpticalParameters::Instance();

    // G4Cerenkovの設定
    optical_params->SetMaxNumPhotonsPerStep(100);
    optical_params->SetMaxBetaChangePerStep(10.0);
    optical_params->SetCerenkovStackPhotons(true);
    optical_params->SetCerenkovTrackSecondariesFirst(true);
    optical_params->SetCerenkovVerbosity(1);

    // G4Scintillationの設定
    optical_params->SetScintByParticleType(false);
    optical_params->SetScintTrackInfo(false);
    optical_params->SetScintTrackSecondariesFirst(true);
    optical_params->SetScintFiniteRiseTime(false);
    optical_params->SetScintStackPhotons(true);
    optical_params->SetScintVerboseLevel(1);

    // G4OpAbsorptionの設定
    optical_params->SetAbsorptionVerboseLevel(1);
}
```

``FTFP_BERT``モデルに``OpticalPhysics``を追加しています。
``G4OpticalPhysics``では、
チェレンコフ光（``G4Cerenkov``）、
シンチレーション光（``G4Scintillation``）、
吸収（``G4OpAbsorption``）、
レイリー散乱（``G4OpRayleigh``）、
ミー散乱（``G4OpMieHG``）、
波長変換（``G4OpWLS``と``G4OpWLS2``）、
境界での散乱（``G4OpBoundary``）、
の物理プロセスを通じて相互作用できるようになります。

また、``G4OpticalParameters``で、それぞれのプロセスのパラメーターを設定できます。

```{toctree}
---
maxdepth: 1
---
geant4-physics-cerenkov
geant4-physics-scintillation
geant4-physics-absorption
geant4-physics-opticalphoton
```

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

``G4OpticalParameters``の設定はマクロで変更できます。
``processActivation``でOpticalPhysicsで有効にする物理プロセスを選択できます。
デフォルトでは、関係するすべてのプロセスが有効になっています。

## リファレンス

- [G4OpticalPhysics](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalPhysics.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalParameters.html)
