# チェレンコフ放射したい（`G4Cerenkov`）

```cpp
#include "G4Cerenkov.hh"

auto params = G4OpticalParameters::Instance();
// 1ステップで生成されるチェレンコフの最大数
params->SetMaxNumPhotonsPerStep(100);
// 1ステップ内で許容されるβの変化の最大値
params->SetMaxBetaChangePerStep(10.0);
// 光子トラッキングのタイミング（true: 即座、false: 後回し）
params->SetCerenkovTrackSecondariesFirst(true);
// スタック追加のタイミング（true: 即座（推奨））
params->SetCerenkovStackPhotons(true);
// デバッグ出力の詳細レベル
params->SetCerenkovVerbosity(0);
```

チェレンコフ放射の主要なパラメーターとデフォルト値です。
`SetMaxNumPhotonsPerStep`で、1ステップで生成されるチェレンコフ光子の最大数を設定できます。
非常に多くの光子が生成される場合は、この値を調整しないとシミュレーションが遅くなります。

`SetMaxBetaChangePerStep`で、1ステップ内で許容されるβの変化率を設定できます。
ステップ内のβの変化率が大きい（例：急な減速など）と、チェレンコフ光子の生成数が不正確になるため調整が必要です。
デフォルトの`10`は「制限なし」に近い値です。
精度が必要な場合は0.01〜0.1程度にするとよいそうです。

`SetTrackSecondariesFirst`で、光子トラッキングのタイミングを設定できます。
`SetCerenkovStackPhotons`で、生成された光子をイベントに追加するタイミングを設定できます。
どちらも`true`が推奨されています。

物質に屈折率（``RINDEX``）が設定されているボリュームで生成されます。

## 設定値を確認したい

```cpp
G4OpticalParameters::Instance()->GetCerenkovMaxPhotonsPerStep(); // 100
G4OpticalParameters::Instance()->GetCerenkovMaxBetaChange();     // 10.0
G4OpticalParameters::Instance()->GetCerenkovTrackSecondariesFirst(); // true
```

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

## チェレンコフ光を記録したい

```cpp
G4bool MyProcessHits(G4Step* step, G4TouchableHistory*) {
    // トラックを取得
    G4Track* track = step->GetTrack();

    // チェレンコフ光だけを記録
    if (track->GetDefinition() != G4OpticalPhoton::Definition())
    {
        return false;
    }

    // チェレンコフ光の生成プロセス名を確認
    if (track->GetCreatorProcess() &&
        track->GetCreatorProcess()->GetProcessName() != "Cerenkov")
    {
        return false;
    }

    // ...記録したい情報を取得...
```

トラックの粒子の種類と生成プロセスを確認して、チェレンコフ光かどうかは判別できます。
`G4VSensitiveDetector::ProcessHits`を継承した`MyProcessHits`の中に書くのがよいと思います。

:::{note}

`G4OpticalPhoton`は、エネルギーの小さな光子（1.5eV〜6.2eV）を指します。

:::

## チェレンコフ光を数えたい（``GetNumPhotons``）

```cpp
G4int n_photons = cerenkov->GetNumPhotons();
```
