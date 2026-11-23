# 化合物したい（``G4Material``）

```cpp
#include "G4NistManager.hh"
#include "G4SystemOfUnits.hh"

auto nm = G4NistManager::Instance();
G4Element *H = nm->FindOrBuildElement("H");
G4Element *O = nm->FindOrBuildElement("O");

// 名前、密度、構成元素の数
auto water = new G4Material("Water", 1.0 * g/cm3, 2);
water->AddElement(H, 2);  // 原子数で指定
water->AddElement(O, 1);
```

複数の元素（`G4Element`）を組み合わせて、化合物（`G4Material`）を作ります。
`AddElement()`の第2引数に原子数（`G4int`）を指定すると、分子の組成になります。
質量の割合（0〜1）を第2引数（`G4double`）に指定することもできます。

```cpp
// 質量の割合で作る場合（上の例とは別の材料）
auto water2 = new G4Material("Water2", 1.0 * g/cm3, 2);
water2->AddElement(H, 0.111898);  // 水素の質量割合
water2->AddElement(O, 0.888102);  // 酸素の質量割合
```

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4Element](https://geant4.kek.jp/Reference/11.2.0/classG4Element.html)

:::
