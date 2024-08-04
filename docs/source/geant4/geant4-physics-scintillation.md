# シンチレーション光したい（``G4Scintillation``）

```cpp
#include "G4Scintillation.hh"

auto params = G4OpticalParameters::Instance();
params->SetScintByParticleType(false);
params->SetScintTrackInfo(false);
params->SetScintTrackSecondariesFirst(true);
params->SetScintFiniteRiseTime(false);
params->SetScintStackPhotons(true);
params->SetScintVerboseLevel(1);
```

## プロパティしたい

シンチレーション光の生成に必要なプロパティです。

| プロパティ名 | 種類 | 説明 | 単位 |
|---|---|---|---|
| ``RESOLUTIONSCALE`` | Constant | Factor to vary width of yield distribution | なし |
| ``SCINTILLATIONYIELD`` | Constant | Mean yield (number of particle produce per energy) | 1/Energy |

シンチレーション光を構成する要素（コンポーネント）ごとの設定もできます。
コンポーネントは3種類まで設定できます。

| プロパティ名 | 種類 | 説明 | 単位 |
|---|---|---|---|
| ``SCINTILLATIONCOMPONENT1`` | Energy-dependent | Energy spectrum for decay component 1 | なし |
| ``SCINTILLATIONRISETIME1`` | Constant | Rise time for component 1 | Time |
| ``SCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 | Time |
| ``SCINTILLATIONYIELD1`` | Constant | Relative yield of component 1 | なし |

粒子ごとのプロパティを設定できます。
それぞれ3種類まで設定できます。

| プロパティ名 | 種類 | 説明 | 単位 |
|---|---|---|---|
| ``ALPHASCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for alphas | Time |
| ``ALPHASCINTILLATIONYIELD`` | Energy-dependent | Yield vector for alphas | 1/Energy |
| ``ALPHASCINTILLATIONYIELD1`` | Constant | Relative yield of component 1 for alphas | なし |
| ``ALPHASCINTILLATIONYIELD2`` | Constant | Relative yield of component 2 for alphas | なし |
| ``ALPHASCINTILLATIONYIELD3`` | Constant | Relative yield of component 3 for alphas | なし |
| ``DEUTERONSCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for deuterons | Time |
| ``DEUTERONSCINTILLATIONYIELD`` | Energy-dependent | Yield vector for deuterons | 1/Energy |
| ``ELECTRONSCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for electrons | Time |
| ``ELECTRONSCINTILLATIONYIELD`` | Energy-dependent | Yield vector for electrons | 1/Energy |
| ``IONSCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for ions | Time |
| ``IONSCINTILLATIONYIELD`` | Energy-dependent | Yield vector for ions | 1/Energy |
| ``PROTONSCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for protons | Time |
| ``PROTONSCINTILLATIONYIELD`` | Energy-dependent | Yield vector for protons | 1/Energy |
| ``TRITONSCINTILLATIONTIMECONSTANT1`` | Constant | Time constant for component 1 for tritons | Time |
| ``TRITONSCINTILLATIONYIELD`` | Energy-dependent | Yield vector for tritons | 1/Energy |



:::{seealso}

- [](./geant4-material-propertiestable.md)

:::

## マクロで設定したい（``/process/optical/scintillation/``）

```cfg
/process/optical/scintillation/setByParticleType false
/process/optical/scintillation/setTrackInfo false
/process/optical/scintillation/setScintTrackSecondariesFirst true
/process/optical/scintillation/setFiniteRiseTime false
/process/optical/scintillation/setStackPhotons true
/process/optical/scintillation/verbose 1
```

シンチレーション光の設定はマクロでもできます。
上の値は、それぞれの設定のデフォルト値です。

## シンチレーション光の数をしりたい（``GetNumPhotons``）

```cpp
G4int n_photons = sc->GetNumPhotons();
```
