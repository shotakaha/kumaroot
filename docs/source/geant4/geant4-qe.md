# 量子効率を設定したい（`EFFICIENCY`）

光電子増倍管（PMT）の光電面は、入射した光子を光電子に変換する確率（量子効率，QE）を持ちます。
Geant4では、この確率を光学表面の`EFFICIENCY`として与えます。

附属サンプル（`LXe`、`DMX`、`wls`）は、`EFFICIENCY`を`{1., 1.}`のような定数で設定しています。
ここでは、メーカーのデータシートのように多数の点で与えられたQE曲線を、`EFFICIENCY`に渡す方法を説明します。

## QEのテーブルを用意したい（`PmtQETable`）

光子のエネルギー（`energy`）と、そのエネルギーでのQEを対にして持つ構造体を作ります。
データシートの値をそのまま書き写せるように、単位は`eV`で書きます。

```cpp
#include <vector>

#include "G4SystemOfUnits.hh"

// 光電面の量子効率（QE）のテーブル
struct PmtQETable {
    std::vector<G4double> energy;  // 光子のエネルギー（昇順）
    std::vector<G4double> qe;      // 各エネルギーでの量子効率（0〜1）
};

// データシートから読み取った量子効率
inline const PmtQETable kDefaultPmtQE = {
    // energy [eV]
    {
        1.5000 * eV, 1.8000 * eV, 1.8300 * eV, 1.8600 * eV, 1.8900 * eV,
        1.9200 * eV, 1.9500 * eV, 1.9800 * eV, 2.0100 * eV, 2.0400 * eV,
        2.0700 * eV, 2.1000 * eV, 2.1300 * eV, 2.1600 * eV, 2.1900 * eV,
        2.2200 * eV, 2.2500 * eV, 2.2800 * eV, 2.3100 * eV, 2.3400 * eV,
        2.3700 * eV, 2.4000 * eV, 2.4300 * eV, 2.4600 * eV, 2.4900 * eV,
        2.5200 * eV, 2.5500 * eV, 2.5800 * eV, 2.6100 * eV, 2.6400 * eV,
        2.6700 * eV, 2.7000 * eV, 2.7300 * eV, 2.7600 * eV, 2.7900 * eV,
        2.8200 * eV, 2.8500 * eV, 2.8800 * eV, 2.9100 * eV, 2.9700 * eV,
        3.0000 * eV, 3.0300 * eV, 3.0600 * eV, 3.0900 * eV, 3.1200 * eV,
        3.1800 * eV, 3.2100 * eV, 3.2400 * eV, 3.3600 * eV, 3.3900 * eV,
        3.4200 * eV, 3.4800 * eV, 3.5100 * eV, 3.5400 * eV, 3.6000 * eV,
        3.6300 * eV, 3.6600 * eV, 3.7200 * eV, 3.7500 * eV, 3.8100 * eV,
        3.8400 * eV, 3.9000 * eV, 3.9300 * eV, 3.9900 * eV, 4.0200 * eV,
        4.0800 * eV, 4.1100 * eV, 4.1700 * eV, 4.2300 * eV, 4.2600 * eV,
        4.3200 * eV, 4.3500 * eV, 4.4100 * eV,
    },
    // qe [-]
    {
        0.0007, 0.0017, 0.0024, 0.0057, 0.0081,
        0.0106, 0.0156, 0.0205, 0.0253, 0.0358,
        0.0431, 0.0505, 0.0578, 0.0745, 0.0838,
        0.0912, 0.0985, 0.1071, 0.1243, 0.1329,
        0.1427, 0.1526, 0.1619, 0.1712, 0.1784,
        0.1855, 0.1933, 0.2011, 0.2108, 0.2205,
        0.2284, 0.2363, 0.2418, 0.2474, 0.2518,
        0.2561, 0.2603, 0.2645, 0.2663, 0.2682,
        0.2697, 0.2713, 0.2719, 0.2725, 0.2744,
        0.2763, 0.2770, 0.2776, 0.2744, 0.2713,
        0.2682, 0.2651, 0.2621, 0.2591, 0.2532,
        0.2474, 0.2365, 0.2256, 0.2134, 0.2011,
        0.1923, 0.1834, 0.1698, 0.1561, 0.1415,
        0.1269, 0.1116, 0.0963, 0.0792, 0.0621,
        0.0398, 0.0175, 0.0000,
    },
};
```

テーブルの値は、データシートの値をそのまま使います。
別の光電面に切り替えるときは、この構造体の値だけを差し替えます。

## 光電面の光学表面にQEを設定したい（`BuildPhotocathodeSurface`）

`EFFICIENCY`を持つ`G4MaterialPropertiesTable`を作り、光電面の`G4OpticalSurface`に登録します。
関数にしておくと、アプリが変わっても同じ関数を呼べます。

```cpp
#include "G4LogicalSkinSurface.hh"
#include "G4LogicalVolume.hh"
#include "G4MaterialPropertiesTable.hh"
#include "G4OpticalSurface.hh"

// 光電面の論理ボリュームに、QEを持つ光学表面を貼る
G4LogicalSkinSurface* AttachPhotocathodeSurface(
    G4LogicalVolume* photocathode,
    const PmtQETable& table = kDefaultPmtQE,
    const G4String& name = "PhotocathodeSurface")
{
    // QEを EFFICIENCY として登録する（間は線形補間される）
    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("EFFICIENCY", table.energy, table.qe);

    // 光電面の光学表面（金属として光子を吸収する簡易モデル）
    auto surface = new G4OpticalSurface(
        name, glisur, polished, dielectric_metal);
    surface->SetMaterialPropertiesTable(mpt);

    return new G4LogicalSkinSurface(name, photocathode, surface);
}
```

`BuildPmtPhotocathode()`を使うアプリでは、光電面の論理ボリュームを作った後に呼び出します。

```cpp
auto photocathode = BuildPmtPhotocathode(/* ... */);
AttachPhotocathodeSurface(photocathode);              // 既定のQEテーブル
// AttachPhotocathodeSurface(photocathode, myTable);  // 別のQEテーブル
```

## 注意

:::{caution}

- **エネルギー範囲の外は端の値になります。** テーブルの範囲は1.5〜4.41 eVです。Geant4は範囲の外側で端の値を返します。1.5 eVより低いエネルギーでは0.0007、4.41 eVより高いエネルギーでは0になります。範囲外でQEを0にしたい場合は、テーブルの両端に0の点を追加してください。
- **エネルギーは昇順で与えます。** Geant4はエネルギーの順番に依存して補間します。
- **入射窓の透過は別に扱います。** 入射窓の透過は`RINDEX`と`ABSLENGTH`で表します（[](./geant4-geometry-pmt.md)を参照）。データシートのQEが窓の透過を含んでいる場合は、ここで透過率を掛けないでください。二重に減衰します。
- **旧コードとの違い。** 過去の実験で使ったコードは、区間の左端の値を使う階段状の計算でした。Geant4の`EFFICIENCY`は線形補間されるため、同じデータでも結果が少し変わります。
- **`EFFICIENCY`は検出確率として使われます。** `G4OpBoundaryProcess`は`G4BooleanRand(fEfficiency)`で判定し、成功した光子を`Detection`として扱います（`source/processes/optical/include/G4OpBoundaryProcess.hh`）。

:::

:::{seealso}

- [](./geant4-geometry-pmt.md)
- [](./geant4-material-propertiestable.md)
- [](./geant4-constants.md)

:::
