# 量子効率を設定したい（`EFFICIENCY`）

## QEのテーブルを用意したい（`PmtQETable`）

```cpp
#include <vector>

// 光電面の量子効率（QE）のテーブル
struct PmtQETable {
    std::vector<G4double> wavelength;  // 波長 [nm]（データシートの値）
    std::vector<G4double> qe;          // 各波長での量子効率 [-]
};

// データシートから読み取った量子効率
inline const PmtQETable kDefaultPmtQE = {
    // wavelength [nm]
    {
        280.0, 281.0, 285.0, 287.0, 291.0,
        293.0, 297.0, 302.0, 304.0, 308.0,
        311.0, 316.0, 318.0, 323.0, 325.0,
        331.0, 333.0, 339.0, 342.0, 344.0,
        350.0, 353.0, 356.0, 363.0, 366.0,
        369.0, 383.0, 386.0, 390.0, 397.0,
        401.0, 405.0, 409.0, 413.0, 418.0,
        426.0, 431.0, 435.0, 440.0, 444.0,
        449.0, 454.0, 459.0, 464.0, 470.0,
        475.0, 481.0, 486.0, 492.0, 498.0,
        504.0, 510.0, 517.0, 523.0, 530.0,
        537.0, 544.0, 551.0, 559.0, 566.0,
        574.0, 582.0, 590.0, 599.0, 608.0,
        617.0, 626.0, 636.0, 646.0, 656.0,
        667.0, 678.0, 689.0, 827.0, 830.0,
    },
    // qe [-]
    {
        0.0000, 0.0000, 0.0175, 0.0398, 0.0621,
        0.0792, 0.0963, 0.1116, 0.1269, 0.1415,
        0.1561, 0.1698, 0.1834, 0.1923, 0.2011,
        0.2134, 0.2256, 0.2365, 0.2474, 0.2532,
        0.2591, 0.2621, 0.2651, 0.2682, 0.2713,
        0.2744, 0.2776, 0.2770, 0.2763, 0.2744,
        0.2725, 0.2719, 0.2713, 0.2697, 0.2682,
        0.2663, 0.2645, 0.2603, 0.2561, 0.2518,
        0.2474, 0.2418, 0.2363, 0.2284, 0.2205,
        0.2108, 0.2011, 0.1933, 0.1855, 0.1784,
        0.1712, 0.1619, 0.1526, 0.1427, 0.1329,
        0.1243, 0.1071, 0.0985, 0.0912, 0.0838,
        0.0745, 0.0578, 0.0505, 0.0431, 0.0358,
        0.0253, 0.0205, 0.0156, 0.0106, 0.0081,
        0.0057, 0.0024, 0.0017, 0.0007, 0.0000,
    },
};
```

データシートの値を、そのまま`kDefaultPmtQE`に書き写します。
別の光電面に切り替えるときは、この構造体の値だけを差し替えます。

:::{hint}

上の値は、もとのエネルギー（`eV`）の表を`hc / λ`で`nm`に換算し、整数の`nm`に丸めたものです。
さらに、範囲を280〜830 nmに合わせるため、両端に0の点を加えています。これは説明用の架空の調整です。
実際のデータシートの値がある場合は、その値をそのまま入力してください。

:::

## 波長をエネルギーに変換したい（`WavelengthToEnergy`）

```cpp
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"

// 波長 [nm] を光子エネルギーに変換する（E = hc / λ）
inline G4double WavelengthToEnergy(G4double wavelengthNm)
{
    return (h_Planck * c_light) / (wavelengthNm * nm);
}
```

Geant4の`EFFICIENCY`はエネルギーで指定するため、波長`nm`からエネルギーに変換します。
Geant4の単位系で計算すると、戻り値はそのまま`eV`などの単位で使えます。

## EFFICIENCYのテーブルを作りたい（`MakeEfficiencyProperties`）

```cpp
#include "G4MaterialPropertiesTable.hh"

// QEテーブルをEFFICIENCYとして登録する（エネルギーは昇順）
inline G4MaterialPropertiesTable* MakeEfficiencyProperties(const PmtQETable& table)
{
    std::vector<G4double> energy;
    std::vector<G4double> qe;

    // 後ろから順に読むと、エネルギーの昇順になる
    for (std::size_t i = table.wavelength.size(); i-- > 0;) {
        energy.push_back(WavelengthToEnergy(table.wavelength[i]));
        qe.push_back(table.qe[i]);
    }

    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("EFFICIENCY", energy, qe);
    return mpt;
}
```

`EFFICIENCY`はエネルギーの昇順で登録する必要があるため、変換後に順序を逆にします。
データシートは波長の昇順に並んでいることが多いので、変換すると並びが逆になります。

## 光電面の光学表面にQEを設定したい（`AttachPhotocathodeSurface`）

```cpp
#include "G4LogicalSkinSurface.hh"
#include "G4LogicalVolume.hh"
#include "G4OpticalSurface.hh"

// 光電面の論理ボリュームに、QEを持つ光学表面を貼る
G4LogicalSkinSurface* AttachPhotocathodeSurface(
    G4LogicalVolume* photocathode,
    const PmtQETable& table = kDefaultPmtQE,
    const G4String& name = "PhotocathodeSurface")
{
    // 光電面の光学表面（金属として光子を吸収する簡易モデル）
    auto surface = new G4OpticalSurface(
        name, glisur, polished, dielectric_metal);
    surface->SetMaterialPropertiesTable(MakeEfficiencyProperties(table));

    return new G4LogicalSkinSurface(name, photocathode, surface);
}
```

`MakeEfficiencyProperties()`の結果を、光電面の`G4OpticalSurface`に登録します。
関数にしておくと、アプリが変わっても同じ関数を呼べます。

`BuildPmtPhotocathode()`を使うアプリでは、光電面の論理ボリュームを作った後に呼び出します。

```cpp
auto photocathode = BuildPmtPhotocathode(/* ... */);
AttachPhotocathodeSurface(photocathode);              // 既定のQEテーブル
// AttachPhotocathodeSurface(photocathode, myTable);  // 別のQEテーブル
```

## 注意

:::{caution}

- **範囲の外は端の値になります。** テーブルの範囲は280〜830 nmです。Geant4は範囲の外側で端の値を返します。両端の値を0にしてあるため、範囲の外のQEは0になります。データシートの範囲が狭い場合は、同じように両端に0の点を加えてください。
- **波長の単位を間違えないでください。** `wavelength`は`nm`で、`WavelengthToEnergy()`の中で`eV`に換算しています。`eV`の値を直接入れると結果が大きくずれます。
- **入射窓の透過は別に扱います。** 入射窓の透過は`RINDEX`と`ABSLENGTH`で表します（[](./geant4-geometry-pmt.md)を参照）。データシートのQEが窓の透過を含んでいる場合は、ここで透過率を掛けないでください。二重に減衰します。
- **旧コードとの違い。** 過去の実験で使ったコードは、区間の左端の値を使う階段状の計算でした。Geant4の`EFFICIENCY`は線形補間されるため、同じデータでも結果が少し変わります。
- **`EFFICIENCY`は検出確率として使われます。** `G4OpBoundaryProcess`は`G4BooleanRand(fEfficiency)`で判定し、成功した光子を`Detection`として扱います（`source/processes/optical/include/G4OpBoundaryProcess.hh`）。

:::

:::{seealso}

- [](./geant4-geometry-pmt.md)
- [](./geant4-material-propertiestable.md)
- [](./geant4-constants.md)

:::
