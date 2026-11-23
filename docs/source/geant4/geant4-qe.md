# 量子効率したい（`EFFICIENCY`）

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
        830.0, 827.0, 689.0, 678.0, 667.0,
        656.0, 646.0, 636.0, 626.0, 617.0,
        608.0, 599.0, 590.0, 582.0, 574.0,
        566.0, 559.0, 551.0, 544.0, 537.0,
        530.0, 523.0, 517.0, 510.0, 504.0,
        498.0, 492.0, 486.0, 481.0, 475.0,
        470.0, 464.0, 459.0, 454.0, 449.0,
        444.0, 440.0, 435.0, 431.0, 426.0,
        418.0, 413.0, 409.0, 405.0, 401.0,
        397.0, 390.0, 386.0, 383.0, 369.0,
        366.0, 363.0, 356.0, 353.0, 350.0,
        344.0, 342.0, 339.0, 333.0, 331.0,
        325.0, 323.0, 318.0, 316.0, 311.0,
        308.0, 304.0, 302.0, 297.0, 293.0,
        291.0, 287.0, 285.0, 281.0, 280.0,
    },
    // qe [-]
    {
        0.0000, 0.0007, 0.0017, 0.0024, 0.0057,
        0.0081, 0.0106, 0.0156, 0.0205, 0.0253,
        0.0358, 0.0431, 0.0505, 0.0578, 0.0745,
        0.0838, 0.0912, 0.0985, 0.1071, 0.1243,
        0.1329, 0.1427, 0.1526, 0.1619, 0.1712,
        0.1784, 0.1855, 0.1933, 0.2011, 0.2108,
        0.2205, 0.2284, 0.2363, 0.2418, 0.2474,
        0.2518, 0.2561, 0.2603, 0.2645, 0.2663,
        0.2682, 0.2697, 0.2713, 0.2719, 0.2725,
        0.2744, 0.2763, 0.2770, 0.2776, 0.2744,
        0.2713, 0.2682, 0.2651, 0.2621, 0.2591,
        0.2532, 0.2474, 0.2365, 0.2256, 0.2134,
        0.2011, 0.1923, 0.1834, 0.1698, 0.1561,
        0.1415, 0.1269, 0.1116, 0.0963, 0.0792,
        0.0621, 0.0398, 0.0175, 0.0000, 0.0000,
    },
};
```

`PmtQETable`は、データシートの波長と量子効率の値をそのまま格納する構造体です。
波長（`wavelength`）の単位は`nm`、量子効率（`qe`）は`[0, 1]`の範囲の値です。
それぞれ`std::vector<G4double>`型の可変長配列です。

`kDefaultPmtQE`は、データシートの値をそのまま書き写した例です。
要素ごとの間隔は、等間隔でなくても構いませんが、波長は **降順（長→短）** に並べてください。
また、波長と量子効率の要素数は同じにしてください。

:::{hint}

テーブルの両端の量子効率を0にしておくと、範囲外の波長の光子は検出されません。

:::

:::{caution}

データシートの量子効率が、純粋な量子効率の値か、入射窓の透過率を含んだ値か、必ず確認して書き写してください。
多くの場合、後者（入射窓の透過率を含んだ値）であることが多いと思います。

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

`WavelengthToEnergy`は、波長`nm`を光子のエネルギー`eV`に変換する関数です。
Geant4の`EFFICIENCY`はエネルギーで指定する必要があります。
一方で、PMTのデータシートには波長に対する量子効率のグラフが載っていることが多いので、変換する関数を用意しておくと便利です。
Geant4の単位系で計算すると、戻り値はそのまま`eV`などの単位で使えます。

:::{seealso}

- [](./geant4-constants.md)

:::

## 量子効率を登録したい（`MakeEfficiencyProperties`）

```cpp
#include "G4MaterialPropertiesTable.hh"

// QEテーブルをEFFICIENCYとして登録する（エネルギーは昇順）
inline G4MaterialPropertiesTable* MakeEfficiencyProperties(const PmtQETable& table)
{
    std::vector<G4double> energy;
    std::vector<G4double> qe;

    // 波長は降順なので、前から読むとエネルギーは昇順になる
    for (std::size_t i = 0; i < table.wavelength.size(); ++i) {
        energy.push_back(WavelengthToEnergy(table.wavelength[i]));
        qe.push_back(table.qe[i]);
    }

    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("EFFICIENCY", energy, qe);
    return mpt;
}
```

`MakeEfficiencyProperties`は、量子効率のテーブル（`PmtQETable`）を`G4MaterialPropertiesTable`に登録する関数です。
内部で波長をエネルギーに変換し、`AddProperty("EFFICIENCY", ...)`で登録しています。

:::{hint}

`EFFICIENCY`は、光学表面で吸収された光子が検出される確率として使われます。
光電面では、この値を量子効率に近似できます。
`G4OpBoundaryProcess`では、反射されずに吸収された光子に対して`G4BooleanRand(fEfficiency)`で判定します。
trueとなった光子が`Detection`として扱われます。

:::

:::{caution}

また、`EFFICIENCY`はエネルギーの昇順で登録する必要があります。
そのため、量子効率のテーブルの波長は降順にしておく必要があります。

:::

:::{seealso}

- [](./geant4-material-propertiestable.md)

:::

## 光電面に量子効率を設定したい（`AttachPhotocathodeSurface`）

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

`AttachPhotocathodeSurface`は、光電面の論理ボリュームに量子効率を持つ光学表面を適用する関数です。
`MakeEfficiencyProperties()`の結果を、光電面の`G4OpticalSurface`に登録しています。

```cpp
auto photocathode = BuildPmtPhotocathode(/* ... */);
AttachPhotocathodeSurface(photocathode);              // 既定のQEテーブル
// AttachPhotocathodeSurface(photocathode, myTable);  // 別のQEテーブル
```

前のページで作成した`BuildPmtPhotocathode()`を使う場合は、光電面の論理ボリュームを作った後に呼び出してください。

:::{seealso}

- [](./geant4-geometry-pmt.md)

:::
