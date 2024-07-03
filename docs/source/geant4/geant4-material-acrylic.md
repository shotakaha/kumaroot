# アクリルを作りたい（``G4_PLEXIGLASS``）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *acrylic = nm->FindOrBuildMaterial("G4_PLEXIGLASS");
```

``G4_PLEXIGLASS``でアクリル材（アクリル樹脂）を生成できます。

:::{note}

アクリル樹脂で作ったガラスのことを「プレキシガラス」（商標名）と呼ぶそうです。
この呼び方を知らなかったのでデータシートから検索できず、自分で作るしかないと思っていました。
構成する元素も密度も同じなので、代用してOKと思います。

:::

## カスタマイズしたい

```cpp
// 名称: ポリメタクリル酸メチル樹脂（polymethyl methacrylate)
// 略称: PMMA
// 化学式: C5H8O2
G4NistManager *nist = G4NistManager::Instance();
G4Element H = nist->FindOrBuildElement("G4_H");
G4Element C = nist->FindOrBuildElement("G4_C");
G4Element O = nist->FindOrBuildElement("G4_O");

G4Material *fAcrylic = new G4Material("Acrylic", density=1.19*g/cm3, nelements=3);
fAcrylic->AddElement(C, 5);
fAcrylic->AddElement(H, 8);
fAcrylic->AddElement(O, 2);
```

プレキシガラスという呼び方を知らなかったので、自分で作ってみました。
構成する元素の情報はNISTデータを参照しています。

:::{note}

``G4Element``オブジェクトを取得する場合は``FindOrBuildElement``を使います。

:::

## 光学特性したい

```cpp
const G4int entries = 17;

// 光子の波長 [nm]
G4double photon_wavelength[entries] = {
    200.*nm,
    260.*nm, 270.*nm, 280.*nm, 290.*nm, 300.*nm,
    310.*nm, 320.*nm, 330.*nm, 340.*nm, 350.*nm,
    360.*nm, 370.*nm, 380.*nm, 390.*nm, 400.*nm,
    620.*nm
};

// 吸収長
G4double absorption_length[entries] = {
    0.867*mm,
    0.867*mm, 1.46*mm, 3.94*mm, 1.10*cm, 3.48*cm,
    7.71*cm, 9.81*cm, 11.58*cm, 13.6*cm, 15.7*cm,
    21.2*cm, 39.4*cm, 81.1*cm, 3.86*m, 9.27*m,
    9.27*m
    };

// 波長[nm]をエネルギー[eV]に変換
// E[J] = hv[m] = hc/L[m]
// E[eV] ~ 1240./L[nm]
G4double photon_energy[entries];
for(int i = 0; i<entries; i++) {
    photon_energy[i] = 1240./photon_wavelength[i] * eV;
}

// 光学特性を定義
G4MaterialPropertiesTable *mpt = new G4MaterialPropertiesTable();
mpt->AddConstProperty("RINDEX", 1.49);
mpt->AddPropertry("ABSLENGTH", photon_energy, absorption_length, entries);

// 光学特性を追加
fAcrylic->SetMaterialPropertiesTable(mpt);
```

アクリルの光学特性を追加しました。
屈折率は``AddConstProperty``を使って、波長によらず1.49にしました。
吸収長は``AddProperty``を使って、波長ごとに値が変わるようにしました。
