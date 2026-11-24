# チェレンコフ放射したい（`G4Cerenkov`）

```cpp
#include "G4OpticalParameters.hh"

auto* params = G4OpticalParameters::Instance();
// 1ステップあたりの最大光子数（デフォルト: 100）
params->SetCerenkovMaxPhotonsPerStep(100);
// 1ステップあたりのβの最大変化量[%]（デフォルト: 10.0、0で制限なし）
params->SetCerenkovMaxBetaChange(10.0);
// 二次粒子のトラッキング順序（デフォルト: true）
params->SetCerenkovTrackSecondariesFirst(true);
// 光子をスタックに積むか（デフォルト: true）
params->SetCerenkovStackPhotons(true);
// 詳細レベル（デフォルト: 1）
params->SetCerenkovVerboseLevel(1);
```

`G4OpticalPhysics`が登録するチェレンコフ過程（`G4Cerenkov`）です。
屈折率（`RINDEX`）が設定された物質中で荷電粒子の速さが光速を超えるときに発生します。

## 発生数を制限したい（`SetCerenkovMaxPhotonsPerStep`）

```cpp
params->SetCerenkovMaxPhotonsPerStep(100);
```

1ステップで生成する光子の最大数です。
発生する光子数が多すぎると計算時間が増えるため、必要に応じて上限値を下げてください。
デフォルトは100です。

## βの変化を制限したい（`SetCerenkovMaxBetaChange`）

```cpp
params->SetCerenkovMaxBetaChange(10.0);
```

1ステップでの速さβの変化量を、パーセントで指定します。
`0`にするとこの制限は無効になります。

## チェレンコフ光の生成を止めたい（`SetCerenkovStackPhotons`）

```cpp
params->SetCerenkovStackPhotons(false);
```

`false`にすると、チェレンコフ光子は1つも生成されません。
荷電粒子の軌跡やエネルギー損失だけを調べたいときに使います。
デフォルトは`true`です。

## 親粒子の追跡順を変えたい（`SetCerenkovTrackSecondariesFirst`）

```cpp
params->SetCerenkovTrackSecondariesFirst(true);
```

`true`のとき、光子を生成したステップで親粒子を一時停止し、生成された光子を先に追跡します。
`false`にすると、親粒子は停止せず、光子は並行して扱われます。
デフォルトは`true`です。

## 屈折率を設定したい（`RINDEX`）

```cpp
#include "G4MaterialPropertiesTable.hh"

auto* mpt = new G4MaterialPropertiesTable();
mpt->AddProperty("RINDEX", photonEnergy, refractiveIndex);
material->SetMaterialPropertiesTable(mpt);
```

`RINDEX`は光子エネルギーに依存する屈折率です。
チェレンコフ光はこの値が設定された物質でのみ発生します。

:::{seealso}

- [](geant4-material-propertiestable)

:::

## 設定値を確認したい（`GetCerenkovMaxPhotonsPerStep`）

```cpp
G4int    maxPhotons = params->GetCerenkovMaxPhotonsPerStep(); // 100
G4double maxBeta    = params->GetCerenkovMaxBetaChange();     // 10.0
G4bool   secFirst   = params->GetCerenkovTrackSecondariesFirst(); // true
```

## マクロで設定したい（`/process/optical/cerenkov/`）

```cfg
/process/optical/cerenkov/setMaxPhotons 100
/process/optical/cerenkov/setMaxBetaChange 10.0
/process/optical/cerenkov/setStackPhotons true
/process/optical/cerenkov/setTrackSecondariesFirst true
/process/optical/cerenkov/verbose 1
```

これらのコマンドは、`/run/initialize`の前（PreInit）と後（Idle）のどちらでも使えます。
値は、コードの`SetCerenkov...`と同じ意味です。

## チェレンコフ放射を止めたい（`processActivation`）

```cfg
/process/optical/processActivation Cerenkov false
```

`processActivation`は`/run/initialize`の前（PreInit）でだけ使えます。

## チェレンコフ光を記録したい（`GetCreatorProcess`）

```cpp
#include "G4OpticalPhoton.hh"
#include "G4VProcess.hh"

G4bool MyProcessHits(G4Step* step, G4TouchableHistory*)
{
    G4Track* track = step->GetTrack();

    // 光学光子だけを対象にする
    if (track->GetDefinition() != G4OpticalPhoton::Definition()) {
        return false;
    }

    // 生成プロセスが"Cerenkov"でなければ除外する（一次粒子は生成プロセスが nullptr）
    const G4VProcess* process = track->GetCreatorProcess();
    if (!process || process->GetProcessName() != "Cerenkov") {
        return false;
    }

    // ...記録したい情報を取得...
    return true;
}
```

`G4VSensitiveDetector::ProcessHits`の中で使います。
生成プロセスが`nullptr`の光子は一次粒子なので、必ず判定してください。

## チェレンコフ光を数えたい（`GetNumPhotons`）

```cpp
#include "G4Cerenkov.hh"

// 親粒子のポストステップ過程から"Cerenkov"を探す
G4ProcessVector* procVec = step->GetTrack()->GetDefinition()
                               ->GetProcessManager()
                               ->GetPostStepProcessVector(typeDoIt);
for (G4int i = 0; i < procVec->entries(); ++i) {
    if ((*procVec)[i]->GetProcessName() == "Cerenkov") {
        auto* cerenkov = static_cast<G4Cerenkov*>((*procVec)[i]);
        G4int nPhotons = cerenkov->GetNumPhotons();
    }
}
```

`GetNumPhotons`は、直前のステップで生成した光子数です。累積値ではありません。
`SteppingAction`などのステップごとの処理で呼んでください。

:::{seealso}

- [](geant4-physics-opticalphysics)
- [](geant4-material-propertiestable)
- [G4Cerenkov](https://geant4.kek.jp/Reference/11.2.0/classG4Cerenkov.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.2.0/classG4OpticalParameters.html)

:::
