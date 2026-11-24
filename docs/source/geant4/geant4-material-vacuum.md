# 真空を作りたい（`G4_Galactic`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *vacuum = nm->FindOrBuildMaterial("G4_Galactic");
```

`G4_Galactic`でNISTデータにある真空（らしき状態）を生成できます。
密度は1.e-25 g/cm3、温度は2.73 K、圧力は3.e-18 Paで、水素のガスとして定義されています。

## 真空を作りたい（`FindOrBuildElement`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *H = nm->FindOrBuildElement("G4_H");

// 密度・温度・圧力を設定
G4double density = 1.e-25 * g/cm3;
G4Material *vacuum = new G4Material(
    "Vacuum",
    density,
    1,              // 成分の数
    kStateGas,      // G4State: 状態（ガス）
    2.73*kelvin,    // G4double: 温度
    3.e-18*pascal   // G4double: 気圧
);

// 原子数比を設定
vacuum->AddElement(H, 1);
```

NISTの元素から`G4Element`を取得し、水素だけで組成を指定します。
`G4_Galactic`と同じ組成と密度、温度、圧力です。

## 真空を作りたい（`G4Element`）

```cpp
G4Element *H = new G4Element("Hydrogen", "H", 1., 1.008*g/mole);

G4double density = 1.e-25 * g/cm3;
G4Material *vacuum = new G4Material(
    "Vacuum",
    density,
    1,
    kStateGas,
    2.73*kelvin,
    3.e-18*pascal
);
vacuum->AddElement(H, 1);
```

`G4Element`で元素の原子番号と質量数を指定して作ります。
元素の性質はNISTの値で足りるので、通常は前の方法を使ってください。

## 真空を作りたい（`G4Material`）

```cpp
G4Material *vacuum = new G4Material(
    "interGalactic",
    1.,            // 原子番号
    1.008*g/mole,  // 質量/モル
    1.e-25*g/cm3,  // 密度
    kStateGas,     // G4State: 状態（ガス）
    2.74*kelvin,   // G4double: 温度
    3.e-18*pascal  // G4double: 気圧
);
```

真空は「非常に密度が低いガス」として作ります。
ここの値はGeant4講習会の資料に掲載されていたものを使っています。
温度は`G4_Galactic`の2.73 Kと比べて0.01 Kの差があり、実用上は無視できる違いです。

:::{hint}

密度を1.e-25 g/cm3より小さくすると、Geant4は警告を出して1.e-25 g/cm3に置き換えます。
密度に0は指定できません。

:::

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.4.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.4.0/classG4NistManager.html)
- [G4Element](https://geant4.kek.jp/Reference/11.4.0/classG4Element.html)
- [geant4-material-element](geant4-material-element)

:::
