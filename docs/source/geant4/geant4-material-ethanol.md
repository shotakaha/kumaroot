# エタノールを作りたい（`G4_ETHYL_ALCOHOL`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *ethanol = nm->FindOrBuildMaterial("G4_ETHYL_ALCOHOL");
```

`G4_ETHYL_ALCOHOL`でNISTデータにあるエタノールを生成できます。
化学式はC2H5OH（C2H6O）です。

## エタノールを作りたい（`FindOrBuildElement`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *C = nm->FindOrBuildElement("G4_C");
G4Element *H = nm->FindOrBuildElement("G4_H");
G4Element *O = nm->FindOrBuildElement("G4_O");

// 密度を設定
G4double density = 0.7893 * g/cm3;
G4Material *ethanol = new G4Material("Ethanol", density, 3);

// 原子数比を設定（C2H6O）
ethanol->AddElement(C, 2);
ethanol->AddElement(H, 6);
ethanol->AddElement(O, 1);
```

NISTの元素から`G4Element`を取得し、原子数比で組成を指定します。
`G4_ETHYL_ALCOHOL`と同じ組成（C2H6O）と密度（0.7893 g/cm3）です。

## エタノールを作りたい（`G4Element`）

```cpp
G4double a, z, density;

G4Element *C = new G4Element("Carbon", "C", z=6, a=12.011*g/mole);
G4Element *H = new G4Element("Hydrogen", "H", z=1, a=1.008*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=15.999*g/mole);

G4Material *ethanol = new G4Material("Ethanol", density=0.7893*g/cm3, 3);
ethanol->AddElement(C, 2);
ethanol->AddElement(H, 6);
ethanol->AddElement(O, 1);
```

`G4Element`で元素の原子番号（`z`）と質量数（`a`）を指定して作ります。
元素の性質はNISTの値で足りるので、通常は前の方法を使ってください。

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4Element](https://geant4.kek.jp/Reference/11.2.0/classG4Element.html)
- [geant4-material-element](geant4-material-element)

:::
