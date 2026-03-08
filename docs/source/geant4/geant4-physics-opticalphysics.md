# 光学物理したい（`G4OpticalPhysics`）

```cpp
#include "FTFP_BERT.hh"
#include "G4OpticalPhysics.hh"
#include "G4OpticalParameters.hh"

int main()
{
    // ベースとなる物理モジュールを指定する
    auto *physics = FTFP_BERT{};
    // 光学物理を追加する
    physics->RegisterPhysics(new G4OpticalPhysics{});
    // ランマネージャーに登録する
    rm->SetUserInitialization(physics);
    // 光学物理のグローバル設定
    ConfigureOpticalParameters();

    // ランマネージャーを初期化する
    rm->Initialize()
}
```

`G4OpticalPhysics`は、光学光子（`G4OpticalPhoton`）の相互作用を扱うための物理モジュールです。
`FTFP_BERT`のような物理モジュールには、光学物理のプロセスは含まれていないため、`RegisterPhysics`を使って、ユーザーが「トッピング」することで、光学物理のプロセスを有効にできます。

:::{note}

Geant4では、エネルギー領域や物理プロセスによって「光」のクラスが分かれています。
`G4Gamma`（ガンマ線）は、keV〜MeV以上の高エネルギー領域の光を「粒子」として扱うクラスです。
光電効果、コンプトン散乱、対生成などの物理プロセスに対応します。
`G4OpticalPhoton`（光学光子）は、eV領域（紫外線・可視光・赤外線など）の低エネルギー領域の光を「波」として扱うクラスです。
反射、屈折、吸収、波長変換などの物理プロセスに対応します。
また、`G4MaterialPropertiesTable`を使って光学特性を設定が必須です。

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

- [](./geant4-physics-cerenkov.md)
- [](./geant4-physics-scintillation.md)
- [](./geant4-physics-absorption.md)
- [](./geant4-physics-opticalphoton.md)
- [](./geant4-material-propertiestable.md)

:::

## 光学物理を調整したい（`G4OpticalParameters`）

```cpp
#include "G4OpticalParameters.hh"

void ConfigureOpticalParameters() {
    // 光学物理のパラメータを管理するための関数
    // 呼び出すタイミング:
    // - physics-RegisterPhysics(new G4OpticalPhysics{}) した後
    // - runManager->Initialize()する前

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
```

``G4OpticalParameters``の設定はマクロで変更できます。
``processActivation``でOpticalPhysicsで有効にする物理プロセスを選択できます。
デフォルトでは、関係するすべてのプロセスが有効になっています。

## リファレンス

- [G4OpticalPhysics](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalPhysics.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalParameters.html)
