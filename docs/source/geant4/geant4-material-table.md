# 材料を確認したい（``G4Material::GetMaterialTable``）

```cpp
G4NistManager *nistManager = G4NistManager::Instance();
nistManager->FindOrBuildMaterial("G4_AIR");
nistManager->FindOrBuildMaterial("G4_Pb");
nistManager->FindOrBuildMaterial("G4_Xe");
nistManager->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

G4cout << *(GetMaterial::GetMaterialTable()) << G4endl;
```

``GetMaterial::GetMaterialTable()``で、アプリケーションの中で定義された（＝``G4NistManager``で呼ばれた）材料を確認できます。
材料名のほかに、構成している元素の種類も確認できます。

また、材料が論理ボリュームで使われているかどうかも確認できます。

```console
***** Table : Nb of materials = 4 *****

 Material:   G4_AIR    density:  1.205 mg/cm3  RadL: 303.921 m    Nucl.Int.Length: 710.095 m
                       Imean:  85.700 eV   temperature: 293.15 K  pressure:   1.00 atm

   --->  Element: C (C)   Z =  6.0   N =    12   A = 12.011 g/mole
         --->  Isotope:   C12   Z =  6   N =  12   A =  12.00 g/mole   abundance: 98.930 %
         --->  Isotope:   C13   Z =  6   N =  13   A =  13.00 g/mole   abundance:  1.070 %
          ElmMassFraction:   0.01 %  ElmAbundance   0.02 %

   --->  Element: N (N)   Z =  7.0   N =    14   A = 14.007 g/mole
         --->  Isotope:   N14   Z =  7   N =  14   A =  14.00 g/mole   abundance: 99.632 %
         --->  Isotope:   N15   Z =  7   N =  15   A =  15.00 g/mole   abundance:  0.368 %
          ElmMassFraction:  75.53 %  ElmAbundance  78.44 %

   --->  Element: O (O)   Z =  8.0   N =    16   A = 15.999 g/mole
         --->  Isotope:   O16   Z =  8   N =  16   A =  15.99 g/mole   abundance: 99.757 %
         --->  Isotope:   O17   Z =  8   N =  17   A =  17.00 g/mole   abundance:  0.038 %
         --->  Isotope:   O18   Z =  8   N =  18   A =  18.00 g/mole   abundance:  0.205 %
          ElmMassFraction:  23.18 %  ElmAbundance  21.07 %

   --->  Element: Ar (Ar)   Z = 18.0   N =    40   A = 39.948 g/mole
         --->  Isotope:  Ar36   Z = 18   N =  36   A =  35.97 g/mole   abundance:  0.337 %
         --->  Isotope:  Ar38   Z = 18   N =  38   A =  37.96 g/mole   abundance:  0.063 %
         --->  Isotope:  Ar40   Z = 18   N =  40   A =  39.96 g/mole   abundance: 99.600 %
          ElmMassFraction:   1.28 %  ElmAbundance   0.47 %


 Material:    G4_Pb    density: 11.350 g/cm3   RadL:   5.613 mm   Nucl.Int.Length:  18.248 cm
                       Imean: 823.000 eV   temperature: 293.15 K  pressure:   1.00 atm

   --->  Element: Pb (Pb)   Z = 82.0   N =   207   A = 207.217 g/mole
         --->  Isotope: Pb204   Z = 82   N = 204   A = 203.97 g/mole   abundance:  1.400 %
         --->  Isotope: Pb206   Z = 82   N = 206   A = 205.97 g/mole   abundance: 24.100 %
         --->  Isotope: Pb207   Z = 82   N = 207   A = 206.98 g/mole   abundance: 22.100 %
         --->  Isotope: Pb208   Z = 82   N = 208   A = 207.98 g/mole   abundance: 52.400 %
          ElmMassFraction: 100.00 %  ElmAbundance 100.00 %


 Material:    G4_Xe    density:  5.485 mg/cm3  RadL:  15.462 m    Nucl.Int.Length: 324.297 m
                       Imean: 482.000 eV   temperature: 293.15 K  pressure:   1.00 atm

   --->  Element: Xe (Xe)   Z = 54.0   N =   131   A = 131.292 g/mole
         --->  Isotope: Xe124   Z = 54   N = 124   A = 123.91 g/mole   abundance:  0.090 %
         --->  Isotope: Xe126   Z = 54   N = 126   A = 125.90 g/mole   abundance:  0.090 %
         --->  Isotope: Xe128   Z = 54   N = 128   A = 127.90 g/mole   abundance:  1.920 %
         --->  Isotope: Xe129   Z = 54   N = 129   A = 128.91 g/mole   abundance: 26.440 %
         --->  Isotope: Xe130   Z = 54   N = 130   A = 129.90 g/mole   abundance:  4.080 %
         --->  Isotope: Xe131   Z = 54   N = 131   A = 130.91 g/mole   abundance: 21.180 %
         --->  Isotope: Xe132   Z = 54   N = 132   A = 131.90 g/mole   abundance: 26.890 %
         --->  Isotope: Xe134   Z = 54   N = 134   A = 133.91 g/mole   abundance: 10.440 %
         --->  Isotope: Xe136   Z = 54   N = 136   A = 135.91 g/mole   abundance:  8.870 %
          ElmMassFraction: 100.00 %  ElmAbundance 100.00 %


 Material: G4_PLASTIC_SC_VINYLTOLUENE    density:  1.032 g/cm3   RadL:  42.544 cm   Nucl.Int.Length:  69.969 cm
                       Imean:  64.700 eV   temperature: 293.15 K  pressure:   1.00 atm

   --->  Element: C (C)   Z =  6.0   N =    12   A = 12.011 g/mole
         --->  Isotope:   C12   Z =  6   N =  12   A =  12.00 g/mole   abundance: 98.930 %
         --->  Isotope:   C13   Z =  6   N =  13   A =  13.00 g/mole   abundance:  1.070 %
          ElmMassFraction:  91.47 %  ElmAbundance  47.37 %

   --->  Element: H (H)   Z =  1.0   N =     1   A =  1.008 g/mole
         --->  Isotope:    H1   Z =  1   N =   1   A =   1.01 g/mole   abundance: 99.989 %
         --->  Isotope:    H2   Z =  1   N =   2   A =   2.01 g/mole   abundance:  0.011 %
          ElmMassFraction:   8.53 %  ElmAbundance  52.63 %
```


## リファレンス

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
