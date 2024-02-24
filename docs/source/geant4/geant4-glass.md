# ガラスを作りたい

```cpp
G4NistManager *nist = G4NistManager::Instance();
G4Material *pyrexGlass = nist->FindOrBuildMaterial("G4_Pyrex_Glass");
G4Material *plateGlass = nist->FindOrBuildMaterial("G4_GLASS_PLATE");
```

``G4_Pyrex_Glass``、``G4_GLASS_PLATE``でガラス材を生成できます。
構成元素と密度が異なるので、用途にあったほうを選択してください。

## カスタマイズしたい

```cpp
G4NistManager *nist = G4NistManager::Instance();
G4Material *SiO2 = nist->FindOrBuildMaterial("G4_SILICON_DIOXIDE");
G4Material *B2O3 = nist->FindOrBuildMaterial("G4_BORON_OXIDE");
G4Material *Na2O = nist->FindOrBuildMaterial("G4_SODIUM_MONOXIDE");
G4Material *Al2O3 = nist->FindOrBuildMaterial("G4_ALUMINUM_OXIDE");

G4Material *Glass = new G4Material("Glass", density=2.23*g/cm3, 4);
Glass->AddMaterial(SiO2, 80.6*perCent);
Glass->AddMaterial(B2O3, 13.0*perCent);
Glass->AddMaterial(Na2O, 4.0*perCent);
Glass->AddMaterial(Al2O3, 2.4*perCent);
```

過去に自分たちのプロジェクトではホウケイ酸ガラスを使っていました。
光電子増倍管の入射窓の材質に設定していました。
