# シンチレーション光したい（`G4Scintillation`）

```cpp
#include "G4OpticalParameters.hh"

auto* params = G4OpticalParameters::Instance();
// 粒子の種類ごとに発光量を変えるか（デフォルト: false）
params->SetScintByParticleType(false);
// 光子に G4ScintillationTrackInformation を付けるか（デフォルト: false）
params->SetScintTrackInfo(false);
// 二次粒子（光子）を先に追跡するか（デフォルト: true）
params->SetScintTrackSecondariesFirst(true);
// 立ち上がり時間を使うか（デフォルト: false）
params->SetScintFiniteRiseTime(false);
// 光子をスタックに積むか（デフォルト: true）
params->SetScintStackPhotons(true);
// 詳細レベル（デフォルト: 1）
params->SetScintVerboseLevel(1);
```

`G4OpticalPhysics`が登録するシンチレーション過程（`G4Scintillation`）です。
シンチレータとして`SCINTILLATIONCOMPONENT1`などの物質特性が設定された物質で、光子を生成します。

## 光子数を設定したい（`SCINTILLATIONYIELD`）

```cpp
#include "G4MaterialPropertiesTable.hh"
#include "G4SystemOfUnits.hh"

auto* mpt = new G4MaterialPropertiesTable();
// 1 MeVあたりの平均光子数
mpt->AddConstProperty("SCINTILLATIONYIELD", 12000. / MeV);
// 光子数のばらつきを調整する係数
mpt->AddConstProperty("RESOLUTIONSCALE", 1.0);
```

`SCINTILLATIONYIELD`は、1 MeVあたりの平均光子数です。
平均が10を超えるとガウス分布、10以下ではポアソン分布で、実際の光子数を決めます。

## 発光成分を設定したい（`SCINTILLATIONCOMPONENT1`）

```cpp
// 発光スペクトル（エネルギー依存）
mpt->AddProperty("SCINTILLATIONCOMPONENT1", photonEnergy, emissionSpectrum);
// 減衰の時定数と、成分ごとの割合
mpt->AddConstProperty("SCINTILLATIONTIMECONSTANT1", 20. * ns);
mpt->AddConstProperty("SCINTILLATIONYIELD1", 1.0);
```

`SCINTILLATIONCOMPONENT1`がない物質では、光子は生成されません。
成分は`1`、`2`、`3`の3種類まで設定できます。
`SCINTILLATIONYIELD1`から`3`は割合です。デフォルトは、成分1が`1.0`、成分2と3が`0.0`です。

| プロパティ名 | 種類 | 説明 |
|---|---|---|
| `SCINTILLATIONCOMPONENTn` | エネルギー依存 | 成分nの発光スペクトル |
| `SCINTILLATIONTIMECONSTANTn` | 定数 | 成分nの時定数 |
| `SCINTILLATIONYIELDn` | 定数 | 成分nの割合 |
| `SCINTILLATIONRISETIMEn` | 定数 | 成分nの立ち上がり時間（`SetScintFiniteRiseTime(true)`のときだけ使う） |

## 立ち上がり時間を使いたい（`SetScintFiniteRiseTime`）

```cpp
params->SetScintFiniteRiseTime(true);
mpt->AddConstProperty("SCINTILLATIONRISETIME1", 3. * ns);
```

`true`にすると、光子の発生時刻に立ち上がり時間が加わります。
`SCINTILLATIONRISETIMEn`の設定を忘れると、正しく動作しません。

## 粒子ごとに発光量を変えたい（`SetScintByParticleType`）

```cpp
params->SetScintByParticleType(true);
mpt->AddProperty("PROTONSCINTILLATIONYIELD", protonEnergy, protonYield);
mpt->AddConstProperty("PROTONSCINTILLATIONYIELD1", 0.3);
```

`true`にすると、粒子の種類ごとに発光量の設定を使います。
Birksの飽和補正（`AddSaturation`）とは、同時に使えません。

| 粒子 | 接頭辞 | 発光量 | 時定数 |
|---|---|---|---|
| 陽子 | `PROTON` | `PROTONSCINTILLATIONYIELD`、`...YIELDn` | `PROTONSCINTILLATIONTIMECONSTANTn` |
| 重陽子 | `DEUTERON` | 同上 | 同上 |
| 三重陽子 | `TRITON` | 同上 | 同上 |
| α粒子 | `ALPHA` | 同上 | 同上 |
| イオン | `ION` | 同上 | 同上 |
| 電子 | `ELECTRON` | 同上 | 同上 |

粒子ごとの時定数がない場合は、`SCINTILLATIONTIMECONSTANTn`が使われます。

:::{note}

`SetScintByParticleType`を`true`にすると、物質の`SCINTILLATIONYIELD`は使われません。

:::

## 発光成分を識別したい（`G4ScintillationTrackInformation`）

```cpp
#include "G4ScintillationTrackInformation.hh"

// 光子のトラック情報から発光成分を取得する
G4VUserTrackInformation* info = track->GetUserInformation();
if (G4ScintillationTrackInformation::IsScintillationTrackInformation(info)) {
    auto* sti = G4ScintillationTrackInformation::Cast(info);
    G4ScintillationType type = sti->GetScintillationType();  // Fast、Medium、Slow
}
```

`SetScintTrackInfo(true)`にすると、光子のトラックに`G4ScintillationTrackInformation`が付きます。
どの発光成分から生まれた光子かを、`GetScintillationType()`で判別できます。

## シンチレーション光の生成を止めたい（`SetScintStackPhotons`）

```cpp
params->SetScintStackPhotons(false);
```

`false`にすると、シンチレーション光子は1つも生成されません。
デフォルトは`true`です。

## 親粒子の追跡順を変えたい（`SetScintTrackSecondariesFirst`）

```cpp
params->SetScintTrackSecondariesFirst(true);
```

`true`のとき、光子を生成したステップで親粒子を一時停止し、生成された光子を先に追跡します。
`false`にすると、親粒子は停止せず、光子は並行して扱われます。デフォルトは`true`です。

## マクロで設定したい（`/process/optical/scintillation/`）

```cfg
/process/optical/scintillation/setByParticleType false
/process/optical/scintillation/setTrackInfo false
/process/optical/scintillation/setFiniteRiseTime false
/process/optical/scintillation/setStackPhotons true
/process/optical/scintillation/setTrackSecondariesFirst true
/process/optical/scintillation/verbose 1
```

これらのコマンドは、`/run/initialize`の前（PreInit）と後（Idle）のどちらでも使えます。

## シンチレーション光を数えたい（`GetNumPhotons`）

```cpp
#include "G4ProcessVector.hh"
#include "G4Scintillation.hh"

// 親粒子のポストステップ過程から"Scintillation"を探す
G4ProcessVector* procVec = step->GetTrack()->GetDefinition()
                               ->GetProcessManager()
                               ->GetPostStepProcessVector(typeDoIt);
for (G4int i = 0; i < procVec->entries(); ++i) {
    if ((*procVec)[i]->GetProcessName() == "Scintillation") {
        auto* scint = static_cast<G4Scintillation*>((*procVec)[i]);
        G4int nPhotons = scint->GetNumPhotons();
    }
}
```

`GetNumPhotons`は、直前のステップで生成した光子数です。累積値ではありません。
`SteppingAction`などのステップごとの処理で呼んでください。

:::{seealso}

- [](geant4-physics-opticalphysics)
- [](geant4-material-propertiestable)
- [G4Scintillation](https://geant4.kek.jp/Reference/11.4.0/classG4Scintillation.html)
- [G4OpticalParameters](https://geant4.kek.jp/Reference/11.4.0/classG4OpticalParameters.html)

:::
