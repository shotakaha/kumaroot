# 光学特性したい（`G4MaterialPropertiesTable`）

```cpp
// 素材：水（G4_WATER）
auto nm = G4NistManager::Instance();
auto water = nm->FindOrBuildMaterial("G4_WATER");

// プロパティを設定（水の事前定義値を使用）
auto mpt = new G4MaterialPropertiesTable{};
mpt->AddProperty("RINDEX", "Water");  // 事前定義値（素材名の文字列を渡す）
// mpt->AddProperty("ABSLENGTH", ...);  // 必要に応じて追加
// mpt->AddProperty("RAYLEIGH", ...);
// mpt->AddProperty("MIEHG", ...);

// 水に光学特性を設定
water->SetMaterialPropertiesTable(mpt);
```

`G4MaterialPropertiesTable`でマテリアルの光学特性を設定できます。
[](geant4-physics-opticalphysics)の物理モジュールを利用する場合は必須です。

OpticalPhysicsの物理プロセスを使う場合、
素材の屈折率（`RINDEX`）や
吸収長（`ABSLENGTH`）などの性質をユーザーが設定する必要があります。
それぞれの物理プロセスで必要なパラメーターの設定は
[Configuration - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html#configuration)を参照してください。

Geant4には、次の素材の屈折率の事前定義値があります。
素材名は、`Air`（空気）、`Water`（水）、`PMMA`（アクリル樹脂／ポリメタクリル酸メチル）、`Fused Silica`（石英ガラス）です。

## チェレンコフ光したい（`RINDEX`）

```cpp
// AddProperty("キー名", std::vector配列, std::vector配列)
// photon_energy, refractive_index, absorption_length は std::vector<G4double>（下のシンチレーションの例を参照）
mpt->AddProperty("RINDEX", photon_energy, refractive_index);
mpt->AddProperty("ABSLENGTH", photon_energy, absorption_length);
```

チェレンコフ光の生成には屈折率（`RINDEX`）の設定が必須です。
他の光学特性（`ABSLENGTH`など）は省略可能ですが、
`RINDEX`が設定されていないと`G4Cerenkov`プロセスは光子を生成しません。

:::{note}

`photon_energy`の範囲が狭すぎると、その範囲外の波長のチェレンコフ光が生成されません。
可視光〜紫外域まで含めておくのが一般的です。

:::

`G4MaterialPropertiesTable`の設定だけでは不十分で、
物理リストに`G4Cerenkov`プロセスを登録する必要があります。
詳細は[](geant4-physics-opticalphysics)を参照してください。

また、次のメソッドで光子の生成量やトラッキング順序を制御できます。

```cpp
auto cerenkovProcess = new G4Cerenkov{};
cerenkovProcess->SetMaxNumPhotonsPerStep(100);   // 1ステップあたりの光子数の上限
cerenkovProcess->SetTrackSecondariesFirst(true); // 光子を親粒子より先にトラッキング
```

`SetMaxNumPhotonsPerStep`の上限は、デフォルトでは`G4OpticalParameters`から設定されます。
変更したい場合に、このメソッドを使います。

## シンチレーション光したい（`SCINTILLATIONYIELD`）

```cpp
auto material = new G4Material{
    "LXe",
    54.,                // z
    131.29 * g / mole,  // a
    3.020 * g / cm3     // density
};

std::vector<G4double> photon_energy = { 7.0 * eV, 7.07 * eV, 7.14 * eV };
std::vector<G4double> scintillation = { 0.1, 1.0, 0.1 };
std::vector<G4double> refractive_index  = { 1.59, 1.57, 1.54 };
std::vector<G4double> absorption_length  = { 35. * cm, 35. * cm, 35. * cm };

auto property = new G4MaterialPropertiesTable{};
// 波長に依存するプロパティ
property->AddProperty("RINDEX", photon_energy, refractive_index);
property->AddProperty("ABSLENGTH", photon_energy, absorption_length);
property->AddProperty("SCINTILLATIONCOMPONENT1", photon_energy, scintillation);
property->AddProperty("SCINTILLATIONCOMPONENT2", photon_energy, scintillation);

// 波長に依存しないプロパティ
property->AddConstProperty("RESOLUTIONSCALE", 1.0);
property->AddConstProperty("SCINTILLATIONYIELD", 12000. / MeV);
property->AddConstProperty("SCINTILLATIONTIMECONSTANT1", 20. * ns);
property->AddConstProperty("SCINTILLATIONTIMECONSTANT2", 45. * ns);
property->AddConstProperty("SCINTILLATIONYIELD1", 1.0);
property->AddConstProperty("SCINTILLATIONYIELD2", 0.0);

// 物質にプロパティを設定
material->SetMaterialPropertiesTable(property);
```

`examples/extended/optical/LXe/`のサンプルを参考にしています。
屈折率と吸収長の他に、シンチレーション光のプロパティ（光量や時定数）をいくつか設定しています。

`SCINTILLATIONYIELD`は「1 MeVあたりの光子数」で指定します。
`SCINTILLATIONCOMPONENT1`と`SCINTILLATIONCOMPONENT2`は、
速い成分（Fast）と遅い成分（Slow）の相対発光スペクトル（絶対強度ではない）です。
それぞれの減衰時定数が`SCINTILLATIONTIMECONSTANT1`と`SCINTILLATIONTIMECONSTANT2`、
全体に対する割合が`SCINTILLATIONYIELD1`と`SCINTILLATIONYIELD2`（合計が1.0になるように設定）です。

`RESOLUTIONSCALE`は光子数の統計ゆらぎを制御します。
1.0でポアソン統計相当のゆらぎ、0にすると光子数が決定論的（ゆらぎなし）になります。

:::{note}

チェレンコフ光と同様、`G4MaterialPropertiesTable`の設定だけでは不十分で、
物理リストに`G4Scintillation`プロセスを登録する必要があります。

:::

:::{note}

重粒子（陽子やアルファ線）ではエネルギー損失に対して発光量が非線形になる
（Birksの消光則）ため、
`G4Scintillation::AddSaturation`で補正することがあります。
`G4OpticalPhysics`を使うと、`G4EmSaturation`が自動で設定されます。
`G4OpticalPhysics`を使わない場合は、補正を省略すると重粒子の発光量が過大評価されることがあります。

:::

- [](geant4-physics-scintillation)

## 波長変換したい（`WLSCOMPONENT`）

```cpp
// photon_energy は昇順の std::vector<G4double>
// 吸収長、発光スペクトル（波長変換の相対強度）
std::vector<G4double> wls_absorption_length = { 1.0 * m, 0.5 * m, 0.1 * m };
std::vector<G4double> wls_emission = { 0.1, 1.0, 0.1 };

auto mptWLS = new G4MaterialPropertiesTable{};
mptWLS->AddProperty("WLSABSLENGTH", photon_energy, wls_absorption_length);
mptWLS->AddProperty("WLSCOMPONENT", photon_energy, wls_emission);
// 吸収してから再発光するまでの時間
mptWLS->AddConstProperty("WLSTIMECONSTANT", 0.5 * ns);

wlsFiber->SetMaterialPropertiesTable(mptWLS);
```

`WLSABSLENGTH`は、波長変換する光子を吸収するまでの長さ、
`WLSCOMPONENT`は、吸収した光子を再発光する波長の分布です。
`WLSTIMECONSTANT`は、再発光までの時間です。

波長変換は`G4OpWLS`プロセスで行われるため、物理リストで有効にする必要があります。
具体例は[](geant4-examples-wls)を参照してください。

## 検出効率したい（`EFFICIENCY`）

```cpp
// photon_energy は昇順の std::vector<G4double>
// 光電面の検出効率（例）
std::vector<G4double> efficiency = { 0.10, 0.25, 0.20 };

auto photocathodeSurface = new G4OpticalSurface{"Photocathode"};
auto mptPMT = new G4MaterialPropertiesTable{};
mptPMT->AddProperty("EFFICIENCY", photon_energy, efficiency);
photocathodeSurface->SetMaterialPropertiesTable(mptPMT);
```

`EFFICIENCY`は、光学表面で吸収された光子が検出される確率です。
光電面では、この値を量子効率に近似できます。
値の作り方と、光電面への適用方法は[](geant4-qe)を参照してください。

## 光学表面したい（`G4OpticalSurface`）

```cpp
auto surface = new G4OpticalSurface{"Surface"};
surface->SetType(dielectric_dielectric);
surface->SetFinish(ground);  // rough surface
surface->SetModel(unified);  // UNIFIED model

auto surfaceProperty = new G4MaterialPropertiesTable{};
// surfaceProperty->AddProperty(...); // 表面の光学特性を設定
surface->SetMaterialPropertiesTable(surfaceProperty);
```

`ground`（粗い表面）と`unified`モデルを使う場合は、`surfaceProperty`に反射率などの表面の光学特性を設定してください。

作成した`G4OpticalSurface`は、`G4LogicalBorderSurface`に登録して、2つの物理ボリュームの境界に適用します。

## 反射率したい（`REFLECTIVITY`）

```cpp
// photon_energy は昇順の std::vector<G4double>
// 表面の反射率（例）
std::vector<G4double> reflectivity = { 0.90, 0.90, 0.90 };

auto surfaceProperty = new G4MaterialPropertiesTable{};
surfaceProperty->AddProperty("REFLECTIVITY", photon_energy, reflectivity);
surface->SetMaterialPropertiesTable(surfaceProperty);
```

`REFLECTIVITY`は、光子が光学表面で反射する割合を波長ごとに指定します。
ミラーや反射面など、反射率を指定したい表面で使います。
上の`surfaceProperty`に登録して、`G4OpticalSurface`に設定します。

## リファレンス

- [G4MaterialPropertiesTable](https://geant4.kek.jp/Reference/11.4.0/classG4MaterialPropertiesTable.html)
- [Material Properties Table](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html)
- [RefractiveIndex Database](https://refractiveindex.info/)
