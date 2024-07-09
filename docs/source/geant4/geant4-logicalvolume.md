# 論理ボリュームしたい（``G4LogicalVolume``）

```cpp
auto nm = G4NistManager::Instance();
auto material = nm->FindOrBuildMaterial("G4_AIR");

auto solid = new G4Box{...};
auto logical_volume = G4LogicalVolume{
    solid,
    material,
    "solid",
};
```

``G4LogicalVolume``はGeant4空間の中に配置する前の状態のボリュームです。
形と材質を設定して定義します。
また、ボリュームにかかる力場（電磁場、重力場）を追加したり、
SensitiveDetectorを追加したりできます。

```{toctree}
---
maxdepth: 1
---
geant4-logicalvolume-mass
geant4-logicalvolume-visattributes
geant4-logicalvolume-sensitivedetector
geant4-logicalvolume-fieldmanager
```

:::{seealso}

- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4VSolid](https://geant4.kek.jp/Reference/11.2.0/classG4VSolid.html)
- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4FieldManager](https://geant4.kek.jp/Reference/11.2.0/classG4FieldManager.html)
- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)
- [G4UserLimits](https://geant4.kek.jp/Reference/11.2.0/classG4UserLimits.html)

:::
