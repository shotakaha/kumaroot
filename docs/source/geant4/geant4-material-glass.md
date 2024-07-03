# ホウケイ酸ガラスを作りたい

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *SiO2 = nm->FindOrBuildMaterial("G4_SILICON_DIOXIDE");
G4Material *B2O3 = nm->FindOrBuildMaterial("G4_BORON_OXIDE");
G4Material *Na2O = nm->FindOrBuildMaterial("G4_SODIUM_MONOXIDE");
G4Material *Al2O3 = nm->FindOrBuildMaterial("G4_ALUMINUM_OXIDE");

G4Material *glass = new G4Material("Glass", density=2.23*g/cm3, 4);
glass->AddMaterial(SiO2, 80.6*perCent);
glass->AddMaterial(B2O3, 13.0*perCent);
glass->AddMaterial(Na2O, 4.0*perCent);
glass->AddMaterial(Al2O3, 2.4*perCent);
```

過去に自分たちのプロジェクトではホウケイ酸ガラスを使っていました。
光電子増倍管の入射窓の材質に設定していました。

## 鉛ガラスを作りたい（``G4_GLASS_PLATE``）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *glass = nm->FindOrBuildMaterial("G4_GLASS_LEAD");
```

``G4_GLASS_LEAD``で鉛ガラスを生成できます。

## ガラスを作りたい（``G4_GLASS_PLATE``）

```cpp
G4NistManager *nm = G4NistManager::Instance();
G4Material *pyrexGlass = nm->FindOrBuildMaterial("G4_Pyrex_Glass");
G4Material *plateGlass = nm->FindOrBuildMaterial("G4_GLASS_PLATE");
```

``G4_Pyrex_Glass``、``G4_GLASS_PLATE``でガラス材を生成できます。
構成元素と密度が異なるので、用途にあったほうを選択してください。
