# 光学物理したい（`G4OpticalPhysics`）

```cpp
#include "FTFP_BERT.hh"
#include "G4OpticalPhysics.hh"
#include "G4OpticalParameters.hh"
#include "G4RunManagerFactory.hh"

int main()
{
    auto* rm = G4RunManagerFactory::CreateRunManager();

    // ベースとなる物理モジュールを指定する
    auto* physics = new FTFP_BERT{};
    // 光学物理を追加する
    physics->RegisterPhysics(new G4OpticalPhysics{});
    // ランマネージャーに登録する
    rm->SetUserInitialization(physics);
    // 光学物理のグローバル設定
    ConfigureOpticalParameters();

    // ランマネージャーを初期化する
    rm->Initialize();
}
```

`G4OpticalPhysics`は、光学光子（`G4OpticalPhoton`）の相互作用を扱うための物理モジュールです。
`FTFP_BERT`のような物理モジュールには、光学物理のプロセスは含まれていないため、`RegisterPhysics`を使って、ユーザーが追加することで、光学物理のプロセスを有効にできます。

:::{note}

Geant4では、粒子によって「光」のクラスが分かれています。
`G4Gamma`はガンマ線を表す粒子クラスで、光電効果、コンプトン散乱、対生成などの相互作用を扱います。
`G4OpticalPhoton`は光学光子（eV領域の紫外線・可視光・赤外線など）を表す粒子クラスで、反射、屈折、吸収、波長変換などの相互作用を扱います。
また、`G4MaterialPropertiesTable`を使って光学特性を設定することが必須です。

:::

## 光学物理のプロセス

- 光の発生
    - チェレンコフ光（`G4Cerenkov`）
    - シンチレーション光（`G4Scintillation`）
- 媒質中での輸送
    - 吸収（`G4OpAbsorption`）
    - レイリー散乱（`G4OpRayleigh`）
    - ミー散乱（`G4OpMieHG`）
    - 波長変換（`G4OpWLS` / `G4OpWLS2`）
- 境界での散乱
  - 反射・屈折・全反射（`G4OpBoundary`）

:::{seealso}

- [](geant4-physics-cerenkov)
- [](geant4-physics-scintillation)
- [](geant4-physics-absorption)
- [](geant4-physics-opticalphoton)
- [](geant4-material-propertiestable)

:::

## 光学物理を調整したい（`G4OpticalParameters`）

```cpp
#include "G4OpticalParameters.hh"

void ConfigureOpticalParameters() {
    // 光学物理のパラメータを管理するための関数
    // 呼び出すタイミング:
    // - RegisterPhysics(new G4OpticalPhysics{}) の後
    // - rm->Initialize() の前

    // OpticalPhysicsのパラメーター設定
    auto* params = G4OpticalParameters::Instance();

    // G4Cerenkovの設定
    params->SetCerenkovMaxPhotonsPerStep(100);
    params->SetCerenkovMaxBetaChange(10.0);
    params->SetCerenkovStackPhotons(true);
    params->SetCerenkovTrackSecondariesFirst(true);
    params->SetCerenkovVerboseLevel(1);

    // G4Scintillationの設定
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

`G4OpticalParameters`を使って、光学物理のパラメーターを変更できます。
`G4OpticalParameters::Instance()`はシングルトンになっているため、どこからでもグローバルに設定できます。

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
/process/optical/processActivation QuasiCerenkov true
/process/optical/processActivation QuasiScintillation true
```

`G4OpticalParameters`の設定はマクロでも変更できます。
`processActivation`で、OpticalPhysicsで有効にする物理プロセスを選択できます。
デフォルトでは、上のプロセスすべてが有効になっています。

## リファレンス

- [G4OpticalPhysics](https://geant4.kek.jp/Reference/11.4.0/classG4OpticalPhysics.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.4.0/classG4OpticalParameters.html)
