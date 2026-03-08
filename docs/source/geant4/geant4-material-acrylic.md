# アクリルを作りたい（`G4_PLEXIGLASS`）

```cpp
auto *nm = G4NistManager::Instance();
auto *acrylic = nm->FindOrBuildMaterial("G4_PLEXIGLASS");
```

`G4_PLEXIGLASS`でアクリル材（アクリル樹脂）を生成できます。

アクリル樹脂の化学組成はPMMA（ポリメタクリル酸メチル）ですが、
Geant4では工業名の「プレキシガラス」で登録されています。

:::{note}

プレキシガラスという呼び方を知らなかったため、データシートなどからアクリル材を検索できず、自分で作るしかないと思っていました。

:::

## カスタマイズしたい

```cpp
// 名称: ポリメタクリル酸メチル樹脂（polymethyl methacrylate)
// 略称: PMMA
// 化学式: (C5 H8 O2)n
auto* nm = G4NistManager::Instance();

// 元素を取得
auto* H = nm->FindOrBuildElement("G4_H");
auto* C = nm->FindOrBuildElement("G4_C");
auto* O = nm->FindOrBuildElement("G4_O");

// 密度を設定
G4double density = 1.19 * g/cm3;
auto* pmma = new G4Material("PMMA", density, 3);

// 原子数比を設定
pmma->AddElement(C, 5);
pmma->AddElement(H, 8);
pmma->AddElement(O, 2);
```

プレキシガラスという呼び方を知らなかったころに、自分で作ってみたサンプルです。
PMMAの化学式は`(C5 H8 O2)n`で、密度は`1.19 g/cm3`として作成しています。

## 光学特性したい

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
}

// 吸収長
std::vector<G4double> absorption_lengths = {
    9.27*m,
    9.27*m, 3.86*m, 81.1*cm, 39.4*cm, 21.2*cm,
    15.7*cm, 13.6*cm, 11.58*cm, 9.81*cm, 7.71*cm,
    3.48*cm, 1.10*cm, 3.94*mm, 1.46*mm, 0.867*mm,
    0.867*mm,
}

// 波長をエネルギー [eV] に変換
std::vector<G4double> photon_energies;
photon_energies.reserve(wavelengths.size());  // メモリを先に確保

for (const auto& length : wavelengths) {
    // E = (2 * pi * hbar * c) / lambda
    photon_energies.push_back((CLHEP::twopi * CLHEP::hbarc) / length);
}

// 光学特性を定義
auto* mpt = new G4MaterialPropertiesTable();

// 波長によらない屈折率を設定
mpt->AddConstProperty("RINDEX", 1.49);
// 波長に依存する吸収長を設定
mpt->AddProperty(
    "ABSLENGTH",
    photon_energies.data(),
    absorption_lengths.data(),
    wavelengths.size(),
);

// 光学特性を追加
pmma->SetMaterialPropertiesTable(mpt);
```

アクリル材の光学特性を設定するサンプルです。
波長に依らない特性は`AddConstProperty`、
波長に依存する特性は`AddProperty`で設定できます。

屈折率は波長によらず1.49、
吸収長は波長ごとに値が変わるようにしました。
