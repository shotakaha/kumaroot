# 論理ボリュームしたい（``G4LogicalVolume``）

```cpp

// 準備
auto solid = new G4Box{...};
auto nm = G4NistManager::Instance();
auto material = nm->FindOrBuildMaterial("G4_AIR");

// 論理ボリュームを作成
G4String logical_name = "LogicalVolume"
auto logical_volume = G4LogicalVolume{
    solid,        // G4VSolid*
    material,     // G4Material*
    logical_name, // G4String,
    nullptr,      // G4FieldManager*
    nullptr,      // G4VSensitiveDetector*
    nullptr,      // G4UserLimits
    true          // G4bool
};
```

``G4LogicalVolume``で論理ボリュームを作成できます。
論理ボリュームは、Geant4空間の中に**配置する前の状態**のボリュームです。
このボリュームにかかる力場（電磁場、重力場）を追加したり、
有感検出器（SensitiveDetector）を追加したりできます。
とても大事な概念のボリュームです。

論理ボリュームの作成には、
形状（``G4VSolid``）と素材（``G4Material``）の設定が必要です。
また、ボリュームの名前には、あとからアクセスする可能性を考えて、
認識しやすいものをつけておくとよいと思います。

:::{hint}

あとのページで紹介していますが、
論理ボリュームの名前を使って、
有感検出器の一括設定ができます。

:::

```{toctree}
---
maxdepth: 1
---
geant4-logicalvolume-mass
geant4-logicalvolume-visattributes
geant4-logicalvolume-sensitivedetector
geant4-logicalvolume-fieldmanager
```

## リファレンス

- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
