# ジオメトリ作成の流れ

```cpp
// 1. 形状を定義する
G4VSolid *solid = new G4Box(...)  // 四角柱
G4VSolid *solid = new G4Tubs(...)  // 円柱

// 2. 材料を定義する
auto nm = G4NistManager::Instance();
auto material = nm->FindOrBuildMaterial("材料名");
auto material = nm->FindOrBuildMaterial("G4_AIR");
auto material = nm->FindOrBuildMaterial("G4_WATER");

// 3. 測定器（論理ボリューム）を定義する
G4LogicalVolume *logical = new G4LogicalVolume(...)

// 4. 測定器（物理ボリューム）を配置する
G4VPhysicalVolume *theDetector = new G4PVPlacement(...)
```

Geant4空間に配置する構造体を**ジオメトリ**と呼びます。
ジオメトリは次の4つのステップで作成できます。

1. 形状（ソリッド）を作成する（``G4VSolid``）
2. 素材（マテリアル）を用意する（``G4Material``）
3. 測定器（論理物体）を組み立てる（``G4LogicalVolume``）
4. 測定器（物理物体）を配置する（``G4VPhysicalVolume``）

現実世界の実験と同じように、形状と材料を決めて測定装置を作り、実験室に配置するという、とても分かりやすいオブジェクト指向な設計になっています。

## 形状を作成したい（``G4VSolid``）

```cpp
G4Box("name", half_x, half_y, half_z);
G4Tubs("name", r_min, r_max, half_z, s_phi, d_phi);
```

[](./geant4-geometry-solid.md)に整理しました。

## 素材を作成したい（``G4NistManager``）

```cpp
auto nm = G4NistManager::Instance();
auto nm->FindOrBuildMaterial("G4_WATER");
```

[](./geant4-material.md)に整理しました。

## 測定器を作成したい（``G4LogicalVolume``）

```cpp
G4LogicalVolume(
    G4VSolid *pSolid,
    G4Material *pMaterial ,
    const G4String &name,
    G4FieldManager *pFieldManager=nullptr,
    G4VSensitiveDetector* pSDetector=nullptr,
    G4UserLimits* pUserLimits=nullptr,
    G4bool optimise=true
);
```

``G4LogicalVolume``で論理ボリュームを作成できます。
引数からわかるように、形状（``G4VSolid``）と素材（``G4Material``）の設定が必要です。

論理ボリュームは複製して使い回すことができます。
詳しくは[](./geant4-logicalvolume.md)に整理しました。

:::{hint}

磁場などの外場（``G4FieldManager``）や、
有感検出器（``G4VSensitiveDetector``）の設定などもできますが、
論理ボリュームを作成したあとで、設定を追加することが多いようです。

:::

## 測定器を配置する

```cpp
G4PVPlacement(...);
G4PVReplica(...);
```

``G4PVPlacement``などの配置用クラスを使って論理ボリュームを実験室（ワールド）内に配置することで、物理ボリューム（``G4VPhysicalVolume``）になります。

また、これらの配置用クラスを使って、論理ボリュームを入れ子構造にできます。
詳しくは、[](./geant4-physicalvolume-pvplacement.md)や
[](./geant4-physicalvolume-pvreplica.md)に
整理しました

## リファレンス

- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)
- [G4VSolid](https://geant4.kek.jp/Reference/11.2.0/classG4VSolid.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)
- [G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)

:::
