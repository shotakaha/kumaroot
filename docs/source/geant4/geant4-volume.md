# 構造体の作り方

```cpp
G4Material *fMaterial = new G4Material(...)
G4VSolid *fDetectorS = new G4Box(...)
G4LogicalVolume *fDetectorL = new G4LogicalVolume(...)
G4VPhysicalVolume *fDetectorP = new G4PVPlacement(...)
```

構造体は4つのステップで作成できます。

1. 材料を作る（``G4Material``）
2. 形を作る（``G4VSolid``）
3. 測定装置を組み立てる（``G4LogicalVolume``）
4. 測定装置を並べる（``G4VPhysicalVolume``）

これはとても分かりやすいオブジェクト指向な設計になっていると思います。

現実の実験と同じように、材料と形を決めて測定装置を作り、
実験室に配置します。

測定装置を作った段階では「論理ボリューム」として扱います。
論理ボリュームは複製して使い回すこともできます。
論理ボリュームを実験室内の座標に配置すると「物理ボリューム」になります。

## 材料の作り方

```cpp
G4NistManager *fNist = new G4NistManager::Instance();
G4Material *fWater = fNist->FindOrBuildMaterial("G4_WATER");
```

現実と同じように物質（``G4Material``）は元素（``G4Element``）の組み合わせ、
元素は同位体（``G4Isotope``）の組み合わせで作ることができます。
また、``G4NistManager``を使ってNISTのデータベースにある物質や元素を参照して使うこともできます。

## 形の作り方

```cpp
G4double fDiameter = 39.3*m;
G4double fHeight = 41.4*m;
G4double rmin, rmax, z, sphi, dphi;
G4Tubs *fTankS = G4Tubs("TankS", rmin=0., rmax=0.5*fDiameter, z=0.5*fHeight, sphi=0., dphi=0.);
```

``G4VSolid``を継承したクラスを使って、形を作ります。
箱型（``G4Box``）、円柱型（``G4Tubs``）など基本的な立体のクラスを使います。
これらのクラスのオブジェクトをブーリアン演算して、より複雑な形を作ることもできるみたいです。

## 測定装置の作り方

```cpp
G4LogicalVolume *fTankL = new G4LogicalVolume(
    fTankS,
    fWater,
    "Super Kamiokande",
)
```

形（``G4VSolid``）と材料（``G4Material``）を指定して、
``G4LogicalVolume``オブジェクトを作成します。
これが測定装置です。

## 実験室の作り方

すべての測定装置を配置する空間も作成する必要があります。
この空間は通常``world``と呼ばれます。

地球上の実験室は空気で満たしておけばよいので、次のように作ることができます。

```cpp
G4NistManager *fNist = new G4NistManager::Instance();
G4Material *fAir = fNist->FindOrBuilldMaterial("G4_AIR");

G4double fWorldX = 50*m;
G4double fWorldY = 50*m;
G4double fWorldZ = 50*m;
G4Box *fWorldS = new G4Box("worldS", 0.5*fWorldX, 0.5*fWorldY, 0.5*fWorldZ);
G4LogicalVolume *fWorldL = new G4LogicalVolume(fWorldS, fAir, "Kamioka Mine");

G4RotationMatrix fRotation = G4RotationMatrix();    // no rotation
G4ThreeVector fDirection = G4ThreeVector();         // at (0, 0, 0)
G4Transform3D fLocation = G4Ttransform3D(fRotation, fDirection)
G4VPhysicalVolume *fWorldP = new G4PVPlacement(
    fLocation,
    fWorldL,
    "WorldP",
    nullptr,    // mother volume = none
    false,      // boolean operation = false
    0,          // copy number
    True        // check overlaps
    )
```

## 測定器の並べ方

```cpp
G4RotationMatrix fRotation = G4RotationMatrix();  // no rotation
G4ThreeVector fDirection = G4ThreeVector();       // at (0, 0, 0)
G4Transform3D fLocation = G4Ttransform3D(fRotation, fDirection)
G4VPhysicalVolume *fTankP = new G4PVPlacement(
    fLocation,
    fTankL,
    "TankP",
    fWorldL,    // mother volume
    false,      // boolean operation
    0,          // copy number
    True,       // check overlaps
)
```

測定器を配置するには、
親ボリュームの実験室の原点に対して、
どこにあるかを指定します。
