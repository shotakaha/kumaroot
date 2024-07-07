# 単位したい（``G4SystemOfUnits.hh``）

```cpp
G4double width = 3.5 * m;
G4double length = 10 * cm;
G4double density = 1.3 g/cm3;
```

Geant4で使う物理量には単位をつける必要があります（**must**）。
単位系の詳細は[System of units](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/unitSystem.html)で確認できます。

## 利用できる単位を確認したい

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

よく使いそうな単位をピックアップしてみました。
対話モードで``/units/list``を実行して、利用できる単位の一覧を確認できます。

## 単位を出力したい

```cpp
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"

G4cout << KineticEnergy/keV << " keV";
G4cout << density/(g/cm3)   << " g/cm3";
G4cout << G4BestUnit(StepSize, "Length");
```

物理量を任意の単位で出力したい場合は、その単位名で割り算します。
また、``G4BestUnit``を使うと、適切な大きさの単位を計算して出力できます。

:::{note}

``g``や``eV``などの単位を扱う場合は``G4SystemOfUnit.hh``が必要です。
``G4BestUnit``を使う場合は``G4UnitsTable.hh``が必要です。

取得した値を確認するモジュールでは、
どちらもインクルードしておけばよいと思います。

:::

## 単位を追加したい（``G4UnitDefinition``）

```cpp
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"

new G4UnitDefinition ( "名前", "記号", "カテゴリ名", 値 )
new G4UnitDefinition ( "km/hour" , "km/h", "Speed", km/(3600*s) );
new G4UnitDefinition ( "meter/ns", "m/ns", "Speed", m/ns );
```

``G4UnitDefitinion``で新しい単位を追加できます。
上記のサンプルでは``Speed``カテゴリを新しく作成し、``km/h``と``m/ns``を追加しています。

:::{seealso}

- [System of Units](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/unitSystem.html)

:::
