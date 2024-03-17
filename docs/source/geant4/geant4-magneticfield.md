# 磁場したい（``G4UniformMagField``）

```cpp
G4MagneticField *magnetic_field = new G4UniformMagField(G4ThreeVector(1.*Tesla, 0., 0.));
```

[G4UniformMagField](https://geant4.kek.jp/Reference/11.2.0/classG4UniformMagField.html)で一様磁場を作成できます。
