# 磁場したい（``G4UniformMagField``）

```cpp
G4MagneticField *magnetic_field = new G4UniformMagField(G4ThreeVector(1.*Tesla, 0., 0.));
```

[G4UniformMagField](https://geant4.kek.jp/Reference/11.2.0/classG4UniformMagField.html)で一様磁場を作成できます。

## 空間全体に磁場したい

```cpp
G4FieldManager *global_field_manager = G4TransportationManager::GetTransportationManager()->GetFieldManager();
global_field_manager->SetDetectorField(magnetic_field);
global_field_manager->CreateChordFinder(magnetic_field);
```

作成した磁場は[G4FieldManager](https://geant4.kek.jp/Reference/11.2.0/classG4FieldManager.html)を使って、空間全体に適用できます。

## 局所的に磁場したい

```cpp
G4FieldManager *field_manager = new G4FieldManager(magnetic_field);
pLogicalVolume->SetFieldManager(field_manager, true);  // 子ボリュームにも磁場を伝搬させたい
```

論理ボリュームに対して磁場を与えることができます。
