# 空気を作りたい（`G4_AIR`）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *air = nm->FindOrBuildMaterial("G4_AIR");
```

`G4_AIR`でNISTデータにある空気を生成できます。
炭素C（0.000124）、窒素N（0.755268）、酸素O（0.231781）、アルゴンAr（0.012827）が含まれています。

## 空気を作りたい（`FindOrBuildElement`）

```cpp
G4NistManager *nm = G4NistManager::Instance();

// 元素を取得（NISTの元素名を指定）
G4Element *N = nm->FindOrBuildElement("G4_N");
G4Element *O = nm->FindOrBuildElement("G4_O");

// 密度を設定
G4double density = 1.290 * mg/cm3;
G4Material *air = new G4Material("Air", density, 2);

// 質量比を設定
air->AddElement(N, 70.*perCent);
air->AddElement(O, 30.*perCent);
```

NISTの元素から`G4Element`を取得し、窒素Nと酸素Oだけで組成を指定します。
密度は`G4_AIR`（1.205 mg/cm3）より大きい値にしています。

## 空気を作りたい（`G4Element`）

```cpp
G4double a, z, density;
G4int nelements;

G4Element *N = new G4Element("Nitrogen", "N", z=7, a=14.01*g/mole);
G4Element *O = new G4Element("Oxygen", "O", z=8, a=16.00*g/mole);
G4Material *Air = new G4Material("Air", density=1.290*mg/cm3, nelements=2);
Air->AddElement(N, 70.*perCent);
Air->AddElement(O, 30.*perCent);
```

自分のプロジェクトで使っていた空気です。
``G4Element``と``G4Material``を使って、窒素Nと酸素Oだけで作ってありました。

:::{note}

この空気の組成はユーザーガイドの[Define a Mixture by Fractional Mass](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/materialDef.html#define-a-mixture-by-fractional-mass)から取ってきたもののようです。

:::

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.4.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.4.0/classG4NistManager.html)
- [G4Element](https://geant4.kek.jp/Reference/11.4.0/classG4Element.html)
- [geant4-material-element](geant4-material-element)

:::
