# 光学特性したい（`G4MaterialPropertiesTable`）

```cpp
// 素材：水（G4_WATER）
auto nm = G4NistManager::Instance();
auto water = nm->FindOrBuildMaterial("G4_WATER");

// プロパティを設定（水のpre-defined値を使用）
auto mpt = new G4MaterialPropertiesTable{};
mpt->AddProperty("RINDEX", water);  // pre-defined値（マテリアルのポインタを渡す）
mpt->AddProperty("ABSLENGTH", ...);
mpt->AddProperty("RAYLEIGH", ...);
mpt->AddProperty("MIEHG", ...);

// 水に屈折率を設定
water->SetMaterialPropertiesTable(mpt);
```

`G4MaterialPropertiesTable`でマテリアルの光学特性を設定できます。
[光学物理](./geant4-physics-opticalphysics.md)の物理モジュールを利用する場合は必須です。

OpticalPhysicsの物理プロセスを使う場合、
素材の屈折率（``RINDEX``）や
吸収長（``ABSLENGTH``）などの性質をユーザーが設定する必要があります。
それぞれの物理プロセスで必要なパラメーターの設定は
[Configuration - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html#configuration)を参照してください。

なお、Geant v11.0 から
``Air``（空気）、
``Water``（水）、
``PMMA``（アクリル樹脂／ポリメタクリル酸メチル）、
``Fused Silica``（石英ガラス）
に対して屈折率のpre-defined値が追加されています。

## チェレンコフ光したい

```cpp
// AddProperty("キー名", std::vector配列, std::vector配列)
// AddProperty("キー名", 配列, 配列, 配列の数)
mpt->AddProperty("RINDEX", photon_energy, refractive_index, n_entries);
mpt->AddProperty("ABSLENGTH", photon_energy, absorption, n_entries);
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
詳細は[](./geant4-physics-opticalphysics.md)を参照してください。

また、以下のようなメソッドで光子の生成量やトラッキング順序を制御できます。

```cpp
auto cerenkovProcess = new G4Cerenkov{};
cerenkovProcess->SetMaxNumPhotonsPerStep(100);   // 1ステップあたりの光子数の上限
cerenkovProcess->SetTrackSecondariesFirst(true); // 光子を親粒子より先にトラッキング
```

`SetMaxNumPhotonsPerStep`を設定しないと、
荷電粒子の数が多い場合にシミュレーションが極端に遅くなることがあります。

## シンチレーション光したい

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

``examples/extended/optical/LXe/``のサンプルを参照しました。
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
`G4EmSaturation`と`AddSaturation`で補正することがあります。
省略すると重粒子の発光量が過大評価されることがあります。

:::

- [](./geant4-physics-scintillation.md)

## OpticalSurfaceしたい

```cpp
auto surface = new G4OpticalSurface{"Surface"};
surface->SetType(dielectric_dielectric);
surface->SetFinish(ground);  // rough surface
surface->SetModel(unified);  // UNIFIED model

auto surfaceProperty = new G4MaterialPropertiesTable{};
// surfaceProperty->AddProperty(...); // 表面の光学特性を設定
surface->SetMaterialPropertiesTable(surfaceProperty);
```

## リファレンス

- [G4MaterialPropertiesTable](https://geant4.kek.jp/Reference/11.2.0/classG4MaterialPropertiesTable.html)
- [Material Properties Table](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html)
- [RefractiveIndex Database](https://refractiveindex.info/)
