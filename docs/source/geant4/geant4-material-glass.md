# ガラスを作りたい（`G4_GLASS_PLATE`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *plateGlass = nm->FindOrBuildMaterial("G4_GLASS_PLATE");
```

`G4_GLASS_PLATE`でNISTデータにある板ガラスを生成できます。
密度は2.4 g/cm3で、酸素O、ナトリウムNa、ケイ素Si、カルシウムCaから構成されています。

`G4_GLASS_PLATE`と後述の`G4_Pyrex_Glass`は構成元素と密度が異なるので、用途にあったほうを選択してください。

## ガラスを作りたい（`FindOrBuildElement`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *O = nm->FindOrBuildElement("G4_O");
G4Element *Na = nm->FindOrBuildElement("G4_Na");
G4Element *Si = nm->FindOrBuildElement("G4_Si");
G4Element *Ca = nm->FindOrBuildElement("G4_Ca");

// 密度を設定
G4double density = 2.4 * g/cm3;
G4Material *glass = new G4Material("PlateGlass", density, 4);

// 質量比を設定
glass->AddElement(O, 45.98*perCent);
glass->AddElement(Na, 9.6441*perCent);
glass->AddElement(Si, 33.6553*perCent);
glass->AddElement(Ca, 10.7205*perCent);
```

NISTの元素から`G4Element`を取得し、質量比で組成を指定します。
`G4_GLASS_PLATE`と同じ組成と密度（2.4 g/cm3）です。

## ガラスを作りたい（`G4Element`）

```cpp
G4double z, a;
G4double density = 2.4 * g/cm3;

G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.999*g/mole);
G4Element *Na = new G4Element("Sodium", "Na", z=11, a=22.990*g/mole);
G4Element *Si = new G4Element("Silicon", "Si", z=14, a=28.086*g/mole);
G4Element *Ca = new G4Element("Calcium", "Ca", z=20, a=40.078*g/mole);

G4Material *glass = new G4Material("PlateGlass", density, 4);
glass->AddElement(O, 45.98*perCent);
glass->AddElement(Na, 9.6441*perCent);
glass->AddElement(Si, 33.6553*perCent);
glass->AddElement(Ca, 10.7205*perCent);
```

`G4Element`で原子番号（`z`）と質量数（`a`）を指定して作ります。
元素の性質はNISTの値で足りるので、通常は前の方法を使ってください。

## 耐熱ガラスを作りたい（`G4_Pyrex_Glass`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *pyrexGlass = nm->FindOrBuildMaterial("G4_Pyrex_Glass");
```

`G4_Pyrex_Glass`で耐熱ガラス（パイレックス）を生成できます。
密度は2.23 g/cm3で、ホウ素B、酸素O、ナトリウムNa、アルミニウムAl、ケイ素Si、カリウムKから構成されています。

## 鉛ガラスを作りたい（`G4_GLASS_LEAD`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *leadGlass = nm->FindOrBuildMaterial("G4_GLASS_LEAD");
```

`G4_GLASS_LEAD`で鉛ガラスを生成できます。
密度は6.22 g/cm3で、鉛Pbの質量比は約75%です。

## ホウケイ酸ガラスを作りたい（`FindOrBuildMaterial`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *SiO2 = nm->FindOrBuildMaterial("G4_SILICON_DIOXIDE");
G4Material *B2O3 = nm->FindOrBuildMaterial("G4_BORON_OXIDE");
G4Material *Na2O = nm->FindOrBuildMaterial("G4_SODIUM_MONOXIDE");
G4Material *Al2O3 = nm->FindOrBuildMaterial("G4_ALUMINUM_OXIDE");

// 密度を設定
G4double density = 2.23 * g/cm3;
G4Material *glass = new G4Material("BorosilicateGlass", density, 4);

// 質量比を設定
glass->AddMaterial(SiO2, 80.6*perCent);
glass->AddMaterial(B2O3, 13.0*perCent);
glass->AddMaterial(Na2O, 4.0*perCent);
glass->AddMaterial(Al2O3, 2.4*perCent);
```

過去に自分たちのプロジェクトではホウケイ酸ガラスを使っていました。
光電子増倍管の入射窓の材質に設定していました。

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.4.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.4.0/classG4NistManager.html)
- [G4Element](https://geant4.kek.jp/Reference/11.4.0/classG4Element.html)
- [geant4-material-element](geant4-material-element)

:::
