# 石油を作りたい（`FindOrBuildElement`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *H = nm->FindOrBuildElement("G4_H");
G4Element *C = nm->FindOrBuildElement("G4_C");
G4Element *N = nm->FindOrBuildElement("G4_N");
G4Element *O = nm->FindOrBuildElement("G4_O");
G4Element *S = nm->FindOrBuildElement("G4_S");

// 密度を設定（産地によって異なる値）
G4double density = 0.85 * g/cm3;
G4Material *petroleum = new G4Material("Petroleum", density, 5);

// 質量比を設定
petroleum->AddElement(C, 85.*perCent);
petroleum->AddElement(H, 13.*perCent);
petroleum->AddElement(S, 1.5*perCent);
petroleum->AddElement(N, 0.2*perCent);
petroleum->AddElement(O, 0.3*perCent);
```

石油は産地によって組成が異なるため、Geant4のNISTデータには石油の材質がありません。
そのため、元素から作ります。
上のコードの組成は、以下の範囲に収まる例です。

石油の元素組成はおおよそ次のとおりです。

- 炭素C（83～87％）
- 水素H（11～14％）
- 硫黄S（5％以下）
- 窒素N（0.4％以下）
- 酸素O（0.5％以下）
- 金属（0.5％以下、上のコードでは省略）

:::{caution}

密度と組成は、対象とする原油の値に合わせて確認してください。
上のコードの値は範囲内の例です。

:::

## 石油を作りたい（`G4Element`）

```cpp
G4double z, a;
G4double density = 0.85 * g/cm3;

G4Element *H = new G4Element("Hydrogen", "H", z=1, a=1.008*g/mole);
G4Element *C = new G4Element("Carbon", "C", z=6, a=12.011*g/mole);
G4Element *N = new G4Element("Nitrogen", "N", z=7, a=14.007*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.999*g/mole);
G4Element *S = new G4Element("Sulfur", "S", z=16, a=32.06*g/mole);

G4Material *petroleum = new G4Material("Petroleum", density, 5);
petroleum->AddElement(C, 85.*perCent);
petroleum->AddElement(H, 13.*perCent);
petroleum->AddElement(S, 1.5*perCent);
petroleum->AddElement(N, 0.2*perCent);
petroleum->AddElement(O, 0.3*perCent);
```

`G4Element`で元素の原子番号（`z`）と質量数（`a`）を指定して作ります。
元素の性質はNISTの値で足りるので、通常は前の方法を使ってください。

## 石油を作りたい（`G4Material`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *C = nm->FindOrBuildElement("G4_C");
G4Element *H = nm->FindOrBuildElement("G4_H");

// 代表例として、n-ドデカン（C12H26）で作る
G4double density = 0.75 * g/cm3;
G4Material *petroleum = new G4Material("Petroleum", density, 2);

// 原子数で組成を設定（分子式 C12H26）
petroleum->AddElement(C, 12);
petroleum->AddElement(H, 26);
```

`G4Material`のコンストラクタで密度と元素数を指定し、`AddElement`に原子数を渡すと、分子式どおりの組成になります。
石油の組成そのものではなく、主要な炭化水素の一つで代用した例です。

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4Element](https://geant4.kek.jp/Reference/11.2.0/classG4Element.html)
- [geant4-material-element](geant4-material-element)

:::
