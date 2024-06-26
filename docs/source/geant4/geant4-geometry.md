# ジオメトリ作成の流れ

```cpp
// 1. 素材（マテリアル）を用意する
G4Material *pMaterial = new G4Material(...)

// 2. 形状（ソリッド）を作成する
G4VSolid *pDetectorSolid = new G4Box(...)

// 3. 測定器（論理物体）を組み立てる
G4LogicalVolume *pDetectorLogical = new G4LogicalVolume(...)

// 4. 測定器（物理物体）を配置する
G4VPhysicalVolume *pDetectorPhysical = new G4PVPlacement(...)
```

Geant4空間に配置する構造体を**ジオメトリ**と呼びます。
ジオメトリは次の4つのステップで作成できます。

1. 素材（マテリアル）を用意する（``G4Material``）
2. 形状（ソリッド）を作成する（``G4VSolid``）
3. 測定器（論理物体）を組み立てる（``G4LogicalVolume``）
4. 測定器（物理物体）を配置する（``G4VPhysicalVolume``）

とても分かりやすいオブジェクト指向な設計になっていて、
現実世界の実験と同じように、素材と形状を決めて測定装置を作り、実験室に配置します。

測定装置を作成した段階は「論理ボリューム」と呼びます。
論理ボリュームは複製して使い回すことができます。

論理ボリュームを実験室内の座標に配置すると「物理ボリューム」になります。

## 素材（マテリアル）の作り方

```cpp
G4NistManager *nm = new G4NistManager::Instance();
G4Material *pWater = nm->FindOrBuildMaterial("G4_WATER");
```

``G4Material``を使って素材を作成します。

現実世界と同じように、Geant4の世界でも
物質（``G4Material``）は元素（``G4Element``）の組み合わせ、
元素は同位体（``G4Isotope``）の組み合わせで合成できるようになっています。

標準的な素材の場合、``G4NistManager``を使ってNISTのデータベースにある物質や元素を参照して使うのが簡単です。

## 形状（ソリッド）の作り方

```cpp
G4double diameter = 39.3*m;
G4double height = 41.4*m;
G4double rmin, rmax, z, sphi, dphi;
G4Tubs *pTankSolid = G4Tubs("TankSolid", rmin=0., rmax=0.5*diameter, z=0.5*height, sphi=0.*deg, dphi=360.*deg);
```

``G4VSolid``を継承したクラスを使って形状を作ります。
箱型（``G4Box``）、円柱型（``G4Tubs``）など基本的な立体クラスは用意されています。
これらのクラスから作ったオブジェクトをブーリアン演算して、より複雑な形を作ることもできるようです。

## 測定装置の作り方

```cpp
G4LogicalVolume *pTankLogical = new G4LogicalVolume(
    pTankSolid,
    pWater,
    "Super Kamiokande",
)
```

素材（``G4Material``）と形状（``G4VSolid``）を指定して、
論理ボリューム（``G4LogicalVolume``オブジェクト）を作成します。

:::{seealso}

- [](./geant4-nistmanager.md)
- [](./geant4-pvplacement.md)
- [](./geant4-pvreplica.md)
- [](./geant4-world.md)

:::
