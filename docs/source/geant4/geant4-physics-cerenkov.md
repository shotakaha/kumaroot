# チェレンコフ放射したい（``G4Cerenkov``）

```cpp
#include "G4Cerenkov.hh"

G4Cerenkov* process = new G4Cerenkov{};

G4int max_photons = 300;
process->SetMaxNumPhotonsPerStep(max_photons);
process->SetTrackSecondariesFirst(true);
```

チェレンコフ放射は、物質に屈折率（``RINDEX``）が設定されているボリュームで生成されます。

## プロパティしたい

| プロパティ名 | 種類 | 説明 | 単位 |
|---|---|---|---|
| ``RINDEX`` | Energy-dependent | 屈折率 | なし |

:::{seealso}

- [](./geant4-material-propertiestable.md)

:::

## マクロで設定したい（``/process/optical/cerenkov/``）

```cfg
/process/optical/cerenkov/setMaxPhotons 100
/process/optical/cerenkov/setMaxBetaChange 10.0
/process/optical/cerenkov/setStackPhotons true
/process/optical/cerenkov/setTrackSecondariesFirst true
/process/optical/cerenkov/verbose 1  # initialisation
```

チェレンコフ放射の設定はマクロでもできます。
上の値は、それぞれの設定のデフォルト値です。

## チェレンコフ光を数えたい（``GetNumPhotons``）

```cpp
G4int n_photons = cerenkov->GetNumPhotons();
```

