# ジオメトリ作成の流れ

```cpp
G4Material *pMaterial = new G4Material(...)
G4VSolid *pDetectorSolid = new G4Box(...)
G4LogicalVolume *pDetectorLogical = new G4LogicalVolume(...)
G4VPhysicalVolume *pDetectorPhysical = new G4PVPlacement(...)
```

Geant4空間に配置する構造体を**ジオメトリ**と呼びます。
ジオメトリは次の4つのステップで作成できます。

1. 素材（マテリアル）を用意する（``G4Material``）
2. 形状（ソリッド）を作成する（``G4VSolid``）
3. 測定器を組み立てる（``G4LogicalVolume``）
4. 測定器を配置する（``G4VPhysicalVolume``）

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

## 測定器の並べ方

```cpp
G4RotationMatrix rotation = G4RotationMatrix();  // no rotation
G4ThreeVector direction = G4ThreeVector();       // at (0, 0, 0)
G4Transform3D location = G4Ttransform3D(fRotation, fDirection)
G4VPhysicalVolume *pTankPhysical = new G4PVPlacement(
    location,
    pTankLogical,     // この論理ボリューム
    "TankPhysical",
    pWorldLogical,    // 親となる論理ボリューム
    false,      // boolean operation
    0,          // copy number
    True,       // check overlaps
)
```

``G4PVPlacement``を使って、測定器を配置します。
測定器の場所は、次に書いた**World**の原点に対して座標を指定します。

## 実験室の作り方

```cpp
G4NistManager *nm = new G4NistManager::Instance();
G4Material *pAir = nm->FindOrBuilldMaterial("G4_AIR");

G4double world_x = 50.*m;
G4double world_y = 50.*m;
G4double world_z = 50.*m;
G4Box *pWorldSolid = new G4Box("WorldSolid", 0.5*world_x, 0.5*world_y, 0.5*world_z);
G4LogicalVolume *pWorldLogical = new G4LogicalVolume(pWorldSolid, pAir, "Kamioka Mine");

G4RotationMatrix rotation = G4RotationMatrix();    // no rotation
G4ThreeVector direction = G4ThreeVector();         // at (0, 0, 0)
G4Transform3D location = G4Ttransform3D(location, direction)
G4VPhysicalVolume *pWorldPhysical = new G4PVPlacement(
    location,
    pWorldLogical,
    "WorldPhysical",
    nullptr,    // mother volume = none
    false,      // boolean operation = false
    0,          // copy number
    True        // check overlaps
    )
```

通常**World**と呼ばれる実験室の空間を作成します。
地球上の実験室を想定して空気で満たしておきました。

このボリュームは親ボリュームを持ちません。
すべての測定装置はこの空間の中に収まるように配置する必要があります。
