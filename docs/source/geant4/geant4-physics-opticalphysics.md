# OpticalPhysicsしたい（`G4OpticalPhysics`）

`G4OpticalPhysics`は、光子（`G4OpticalPhoton`）などの光学的な相互作用を扱うための物理モジュールです。
このクラスを`RegisterPhysics`で追加することで、以下のような光に関するプロセスを有効にできます。

- チェレンコフ光（`G4Cerenkov`）
- シンチレーション光（`G4Scintillation`）
- 吸収（`G4OpAbsorption`）
- レイリー散乱（`G4OpRayleigh`）
- ミー散乱（`G4OpMieHG`）
- 波長変換（`G4OpWLS``と``G4OpWLS2`）
- 境界での散乱（`G4OpBoundary`）

:::{seealso}

- [](./geant4-physics-cerenkov.md)
- [](./geant4-physics-scintillation.md)
- [](./geant4-physics-absorption.md)
- [](./geant4-physics-opticalphoton.md)
- [](./geant4-material-propertiestable.md)

:::

## メイン関数（`main`）

```cpp
int main()
{
    // 物理モデルの設定
    auto* physics = new FTFP_BERT{};
    physics->RegisterPhysics(new G4OpticalPhysics{});
    rm->SetUserInitialization(physics);

    // 光学物理のパラメーターを設定（後述）
    ConfigureOpticalParameters();

    // 実験開始（省略）
    rm->Initialize();
    rm->BeamOn();

    delete rm;
    return 0;
}
```

メイン関数で物理モデルを設定する部分を抜粋しました。
メインの相互作用（`FTFP_BERT`モデル）に
`OpticalPhysics`を追加し、
`G4OpticalParameters`のパラメーターを変更しています。

## パラメーターしたい（`G4OpticalParameters`）

```cpp
void ConfigureOpticalParameters() {

    // OpticalPhysicsのパラメーター設定
    auto* params = G4OpticalParameters::Instance();

    // G4Cerenkovの設定
    params->SetMaxNumPhotonsPerStep(100);
    params->SetMaxBetaChangePerStep(10.0);
    params->SetCerenkovStackPhotons(true);
    params->SetCerenkovTrackSecondariesFirst(true);
    params->SetCerenkovVerbosity(1);

    // G4Scintillationの設定
    params->SetScintYieldFactor(1.0);
    params->SetScintExcitationRatio(0.0);
    params->SetScintByParticleType(false);
    params->SetScintTrackInfo(false);
    params->SetScintTrackSecondariesFirst(true);
    params->SetScintFiniteRiseTime(false);
    params->SetScintStackPhotons(true);
    params->SetScintVerboseLevel(1);

    // G4OpAbsorptionの設定
    params->SetAbsorptionVerboseLevel(1);
}
```

`G4OpticalParameters`を使って、光に相互作用パラメーターをグローバルに制御できます。
`G4OpticalParameters::Instance()`はシングルトンになっているため、どこからでも呼び出すことができます。

## マクロで設定したい（`/process/optical/`）

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
