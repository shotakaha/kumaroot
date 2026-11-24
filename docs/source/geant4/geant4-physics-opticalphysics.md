# 光学物理したい（`G4OpticalPhysics`）

```cpp
#include "FTFP_BERT.hh"
#include "G4OpticalPhysics.hh"
#include "G4OpticalParameters.hh"
#include "G4RunManagerFactory.hh"

int main()
{
    auto* rm = G4RunManagerFactory::CreateRunManager();

    // ベースとなる物理リストを指定する
    auto* physics = new FTFP_BERT{};
    // 物理モジュール（G4OpticalPhysics）を追加する
    physics->RegisterPhysics(new G4OpticalPhysics{});
    // ランマネージャーに登録する
    rm->SetUserInitialization(physics);

    // 光学物理のグローバル設定（定義は後述）
    ConfigureOpticalParameters();

    // ランマネージャーを初期化する
    rm->Initialize();
}
```

`G4OpticalPhysics`は、光学光子（`G4OpticalPhoton`）とその相互作用を登録する物理モジュールです。
`FTFP_BERT`のような物理リストに、`RegisterPhysics`で追加して有効にします。

## 含まれる物理プロセス

`G4OpticalPhysics`は、次の物理プロセスを登録します。

- `G4Cerenkov`：チェレンコフ光の発生
- `G4Scintillation`：シンチレーション光の発生
- `G4OpAbsorption`：光の吸収
- `G4OpRayleigh`：レイリー散乱
- `G4OpMieHG`：ミー散乱（Henyey-Greenstein 位相関数）
- `G4OpBoundaryProcess`：境界での反射・屈折・全反射
- `G4OpWLS`、`G4OpWLS2`：波長変換（WLS）

:::{note}

Geant4には`G4Gamma`と`G4OpticalPhoton`の2種類の「光」の粒子クラスがあります。
`G4Gamma`は「ガンマ線」を表すクラスで、光電効果やコンプトン散乱、対生成などのプロセスが割り当てられます。
`G4OpticalPhoton`は「光学光子」を表すクラスで、反射や屈折、吸収、波長変換などの光学プロセスが割り当てられます。

:::

:::{note}

光学プロセスを動かすには、物質に`G4MaterialPropertiesTable`で屈折率（`RINDEX`）などを設定する必要があります。
設定がない物質では、光学光子は追跡されません。

:::

:::{seealso}

- [](geant4-physics-cerenkov)
- [](geant4-physics-scintillation)
- [](geant4-physics-absorption)
- [](geant4-physics-opticalphoton)
- [](geant4-material-propertiestable)

:::

## パラメータを調整したい（`G4OpticalParameters`）

```cpp
#include "G4OpticalParameters.hh"

void ConfigureOpticalParameters() {
    // 光学物理のパラメータを管理するための関数
    // 呼び出すタイミング:
    // - RegisterPhysics(new G4OpticalPhysics{}) の後
    // - rm->Initialize() の前

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

`G4OpticalParameters`は、光学プロセスのパラメータを管理するためのシングルトンです。
`G4OpticalPhysics`を登録した後、`rm->Initialize()`の前に、`G4OpticalParameters::Instance()`で取得したインスタンスに対してパラメータを設定します。

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

`/process/optical/`コマンドを使って、マクロから光学プロセスのパラメータ（`G4OpticalParameters`）を変更できます。
`/process/optical/verbose`で、光学プロセスの詳細なログを出力できます。
`processActivation`で、光学物理に含まれる各プロセスの有効・無効を切り替えられます。
`processActivation`は`/run/initialize`より前（PreInit）でだけ使えます。
`cerenkov/`や`scintillation/`などのパラメータ設定コマンドは、PreInitとIdleのどちらでも使えます。

## リファレンス

- [G4OpticalPhysics](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalPhysics.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalParameters.html)
