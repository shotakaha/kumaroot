# ジオメトリを作成したい

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

## 形状を作成したい（`G4VSolid`）

```cpp
G4Box("name", half_x, half_y, half_z);
G4Tubs("name", r_min, r_max, half_z, s_phi, d_phi);
```

直方体（`G4Box`）や円筒（`G4Tubs`）など、`G4VSolid`を継承したクラスを使って、
測定器の形状を定義します。

:::{seealso}

詳しくは
[](./geant4-geometry-solid.md)
に整理しました。

:::

## 素材を作成したい（`G4Material`）

```cpp
auto nm = G4NistManager::Instance();
G4Material *pWater = nm->FindOrBuildMaterial("G4_WATER");
```

測定器に使う素材（`G4Material`）を定義します。
`G4NistManager`を使ってNISTのデータベースに準拠した
元素や物質の情報を簡単に取得できます。

:::{seealso}

詳しくは
[](./geant4-material.md)
に整理しました。

:::

## 測定器を作成したい（`G4LogicalVolume`）

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

`G4LogicalVolume`で論理ボリュームを作成します。
引数からわかるように、形状（`G4VSolid`）と素材（`G4Material`）の設定が必要です。
論理ボリュームは複製して使い回すことができます。

:::{seealso}
詳しくは
[](./geant4-logicalvolume.md)
に整理しました。
:::

:::{hint}

`G4LogicalVolume`の引数を確認すると、
磁場などの外場（`G4FieldManager`）や、
有感検出器（`G4VSensitiveDetector`）も設定できます。

しかし、最近のユーザーアプリケーションでは、
`Construct`の中で論理ボリュームを作成したあとに、
`ConstructSDandField`の中で設定を追加することが多いようです。

:::

## 測定器を配置する（`G4PVPlacement`）

```cpp
new G4PVPlacement(
    nullptr,                  // 回転；なし
    G4ThreeVector(0, 0, 0),   // 配置；原点に配置
    logicDetector,            // 論理ボリューム
    "Detector",               // 物理ボリュームの名前； "Detector"
    logicWorld,               // 親・論理ボリューム
    false,                    // 多重配置； しない
    0,                        // コピー番号
    false                     // 物理ボリュームの重なり確認； しない
```

`G4PVPlacement`で論理ボリューム（`G4LogicalVolume`）を、
物理ボリューム（`G4VPhysicalVolume`）として配置します。
配置したボリュームは自動的に`G4PhysicalVolumeStore`にも追加されます。

:::{seealso}

詳しくは
[](./geant4-physicalvolume-pvplacement.md)
に整理しました。

:::

```cpp
G4PVReplica(...);
```

繰り返し構造をもつ測定器（や検出器）の場合は
`G4PVReplica`で効率的に配置できます。

:::{seealso}

詳しくは
[](./geant4-physicalvolume-pvreplica.md)
に整理しました

:::

:::{hint}

`G4VPhysicalVolume`は物理ボリュームの抽象基底クラスであり、ユーザーが直接インスタンスを呼び出すことはできません。

ユーザーのアプリケーションでは、
`G4PVPlacement`（単体配置）、
`G4PVReplica`（等間隔配置）、
`G4PVParameterised`（反復配置）
といった派生クラスを通じて利用します。

ただし、`G4VPhysicalVolume* MyGeometry::Construct`のように
関数の戻り値の型として使うことはあります。

:::

## リファレンス

- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)
- [G4VSolid](https://geant4.kek.jp/Reference/11.2.0/classG4VSolid.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)
- [G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)
- [G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)
