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
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"
#include "G4MaterialPropertiesTable.hh"

#include <vector>

// 光子の波長 [nm]
// 降順で定義
std::vector<G4double> wavelengths = {
    620.*nm,
    400.*nm, 390.*nm, 380.*nm, 370.*nm, 360.*nm,
    350.*nm, 340.*nm, 330.*nm, 320.*nm, 310.*nm,
    300.*nm, 290.*nm, 280.*nm, 270.*nm, 260.*nm,
    200.*nm,
};

// 吸収長
std::vector<G4double> absorption_lengths = {
    9.27*m,
    9.27*m, 3.86*m, 81.1*cm, 39.4*cm, 21.2*cm,
    15.7*cm, 13.6*cm, 11.58*cm, 9.81*cm, 7.71*cm,
    3.48*cm, 1.10*cm, 3.94*mm, 1.46*mm, 0.867*mm,
    0.867*mm,
};

// 波長をエネルギー [eV] に変換
std::vector<G4double> photon_energies;
photon_energies.reserve(wavelengths.size());  // メモリを先に確保

for (const auto& length : wavelengths) {
    // E = (2 * pi * hbar * c) / lambda
    photon_energies.push_back((CLHEP::twopi * CLHEP::hbarc) / length);
}

// 屈折率（波長によらず1.49）
std::vector<G4double> refractive_indices(photon_energies.size(), 1.49);

// 光学特性を定義
auto *mpt = new G4MaterialPropertiesTable();

// 屈折率を設定
mpt->AddProperty(
    "RINDEX",
    photon_energies.data(),
    refractive_indices.data(),
    photon_energies.size());

// 波長に依存する吸収長を設定
mpt->AddProperty(
    "ABSLENGTH",
    photon_energies.data(),
    absorption_lengths.data(),
    photon_energies.size());

// 光学特性を追加
pmma->SetMaterialPropertiesTable(mpt);
```

光学特性は`G4MaterialPropertiesTable`に登録して、材質に設定します。
`G4_PLEXIGLASS`で取得したアクリル材にも、同じ方法で設定できます。

屈折率は波長によらず1.49、
吸収長は波長ごとに値が変わるようにしました。
光子のエネルギーは波長の逆数に比例するため、波長を降順で並べると、エネルギーは昇順になります。

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4MaterialPropertiesTable](https://geant4.kek.jp/Reference/11.2.0/classG4MaterialPropertiesTable.html)

:::
