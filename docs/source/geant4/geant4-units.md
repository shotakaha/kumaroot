# 単位したい（`G4SystemOfUnits.hh`）

```cpp
#include "G4SystemOfUnits.hh"

G4double width = 3.5 * m;
G4double length = 10 * cm;
G4double density = 1.3 * g/cm3;
```

Geant4では、値に単位を掛けて書きます。
`m`、`g`、`eV`などの単位は、`G4SystemOfUnits.hh`で定義されています。
そのため、単位を使うには、このヘッダーを`#include`します。

Geant4は内部で単位をそろえて計算します。
たとえば長さの内部単位はmmなので、`3.5 * m`は`3500`として扱われます。

単位系の詳細は[System of units](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/unitSystem.html)で確認できます。

:::{note}

以前は``globals.hh``というヘッダーファイルで、
物理定数と物理単位を一括で読み込んでいました。

Geant4 11.4.0の`globals.hh`は、単位のヘッダーを読み込みません。
単位を使うときは、`G4SystemOfUnits.hh`を`#include`してください。

:::

## 単位を出力したい（`G4BestUnit`）

```cpp
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"    // G4BestUnit に必要

// KineticEnergy、StepSize、density は、すでに定義されている変数とする
G4cout << KineticEnergy/keV << " keV" << G4endl;
G4cout << density/(g/cm3)   << " g/cm3" << G4endl;
G4cout << G4BestUnit(StepSize, "Length") << G4endl;
```

値を単位で割ると、その単位での数値が得られます。
たとえば`density/(g/cm3)`は`1.3`になります。

`G4BestUnit`を使うと、値の大きさに合った単位を自動で選んで出力します。
第2引数には、カテゴリ名（`"Length"`など）を指定します。

## 利用できる単位を確認したい（`/units/list`）

```console
Idle> /units/list

          ----- The Table of Units -----

  category: Length
    parsec ( pc) = 3.08568e+19
millimeter ( mm) = 1
  angstrom (Ang) = 1e-07

  category: Surface
millimeter2 (   mm2) = 1
       barn (  barn) = 1e-22

  category: Volume
millimeter3 (mm3) = 1
      liter (  L) = 1e+06

  category: Angle
     radian ( rad) = 1
     degree ( deg) = 0.0174533

  category: Time
     second (  s) = 1e+09
 nanosecond ( ns) = 1
     minute (min) = 6e+10
       hour (  h) = 3.6e+12
        day (  d) = 8.64e+13
       year (  y) = 3.1536e+16

  category: Frequency
megahertz (MHz) = 0.001

  category: Electric charge
  eplus (e+) = 1
coulomb ( C) = 6.24151e+18

  category: Energy
 megaelectronvolt (MeV) = 1
            joule (  J) = 6.24151e+12

  category: Mass
 kilogram (kg) = 6.24151e+24

  category: Power
watt (W) = 6241.51

  category: Force
newton (N) = 6.24151e+09

  category: Pressure
    pascal ( Pa) = 6241.51
       bar (bar) = 6.24151e+08
atmosphere (atm) = 6.32421e+08

  category: Electric current
     ampere (  A) = 6.24151e+09

  category: Electric potential
megavolt (MV) = 1

  category: Temperature
kelvin (K) = 1

  category: Amount of substance
mole (mol) = 1

  category: Activity
becquerel (Bq) = 1e-09
    curie (Ci) = 37

  category: Dose
     gray (     Gy) = 1e-12
```

対話モードや、マクロで`/units/list`を実行すると、利用できる単位の一覧が表示されます。
上の表示は出力の例です。Geant4のバージョンによって、一覧の内容は変わることがあります。

各行の`= 数値`は、内部単位での値です。
たとえば`millimeter (mm) = 1`は、長さの内部単位が1 mmであることを表します。

## 単位を追加したい（`G4UnitDefinition`）

```cpp
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"

// 書式: new G4UnitDefinition(名前, 記号, カテゴリ名, 値);

new G4UnitDefinition("km/hour", "km/h", "Speed", km/(3600 * s));
new G4UnitDefinition("meter/ns", "m/ns", "Speed", m/ns);
```

`G4UnitDefinition`で、新しい単位を追加できます。
上の例では、`Speed`というカテゴリを作り、`km/h`と`m/ns`を追加しています。

単位の定義は、プログラムの中で保持されます。
同じ単位を何度も定義しないよう、`RunAction`のコンストラクタなど、初期化の時に1回だけ書いてください。

## リファレンス

- [G4UnitsTable.hh](https://geant4.kek.jp/Reference/11.4.0/G4UnitsTable_8hh_source.html)
