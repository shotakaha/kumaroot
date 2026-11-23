# アクリルを作りたい（`G4_PLEXIGLASS`）

```cpp
auto *nm = G4NistManager::Instance();
auto *acrylic = nm->FindOrBuildMaterial("G4_PLEXIGLASS");
```

`G4_PLEXIGLASS`でアクリル材（アクリル樹脂）を生成できます。

アクリル樹脂の化学組成はPMMA（ポリメタクリル酸メチル）ですが、Geant4では工業名の「プレキシガラス」で登録されています。

:::{note}

プレキシガラスという呼び方を知らなかったため、データシートなどからアクリル材を検索できず、自分で作るしかないと思っていました。

:::

## 元素からアクリルを作りたい（`G4Element`）

```cpp
// 名称: ポリメタクリル酸メチル樹脂（polymethyl methacrylate）
// 略称: PMMA
// 化学式: (C5 H8 O2)n
auto *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
auto *H = nm->FindOrBuildElement("G4_H");
auto *C = nm->FindOrBuildElement("G4_C");
auto *O = nm->FindOrBuildElement("G4_O");

// 密度を設定
G4double density = 1.19 * g/cm3;
auto *pmma = new G4Material("PMMA", density, 3);

// 原子数比を設定
pmma->AddElement(C, 5);
pmma->AddElement(H, 8);
pmma->AddElement(O, 2);
```

プレキシガラスという呼び方を知らなかったころに、自分で作ってみたサンプルです。
元素記号で`G4Element`を取得し、原子数比で組成を指定します。
`G4_PLEXIGLASS`と同じ組成（C5H8O2）と密度（1.19 g/cm3）です。

## アクリルの光学特性を設定したい（`G4MaterialPropertiesTable`）

```cpp
#include "G4MaterialPropertiesTable.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"

#include <vector>

// 波長 [nm] を光子エネルギーに変換する（E = hc / λ）
inline G4double WavelengthToEnergy(G4double wavelengthNm)
{
    return (h_Planck * c_light) / (wavelengthNm * nm);
}

// 光子の波長 [nm]（降順で定義）
std::vector<G4double> wavelengths = {
    620.0,
    400.0, 390.0, 380.0, 370.0, 360.0,
    350.0, 340.0, 330.0, 320.0, 310.0,
    300.0, 290.0, 280.0, 270.0, 260.0,
    200.0,
};

// 吸収長
std::vector<G4double> absorptionLengths = {
    9.27*m,
    9.27*m, 3.86*m, 81.1*cm, 39.4*cm, 21.2*cm,
    15.7*cm, 13.6*cm, 11.58*cm, 9.81*cm, 7.71*cm,
    3.48*cm, 1.10*cm, 3.94*mm, 1.46*mm, 0.867*mm,
    0.867*mm,
};

// 波長をエネルギー [eV] に変換（昇順になる）
std::vector<G4double> energies;
energies.reserve(wavelengths.size());
for (const auto& w : wavelengths) {
    energies.push_back(WavelengthToEnergy(w));
}

// 屈折率（波長によらず1.49）
std::vector<G4double> refractiveIndices(energies.size(), 1.49);

// 光学特性を登録
auto *mpt = new G4MaterialPropertiesTable();
mpt->AddProperty("RINDEX", energies, refractiveIndices);
mpt->AddProperty("ABSLENGTH", energies, absorptionLengths);

// 材質に設定
pmma->SetMaterialPropertiesTable(mpt);
```

光学特性は`G4MaterialPropertiesTable`に登録して、材質に設定します。
`geant4-qe`と同じく、波長は`nm`で書いて`WavelengthToEnergy`でエネルギーに変換してから登録します。
`AddProperty`には`std::vector`を渡すので、エネルギーと値の要素数がずれる心配がありません。

屈折率は波長によらず1.49、
吸収長は波長ごとに値が変わるようにしました。
波長は降順で並べているので、エネルギーは昇順になります。

:::{caution}

`AddProperty`に渡すエネルギーは昇順である必要があります。
波長を昇順で並べると、そのまま登録できないので注意してください。

:::

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4MaterialPropertiesTable](https://geant4.kek.jp/Reference/11.2.0/classG4MaterialPropertiesTable.html)
- [geant4-constants](geant4-constants)
- [geant4-material-propertiestable](geant4-material-propertiestable)

:::
