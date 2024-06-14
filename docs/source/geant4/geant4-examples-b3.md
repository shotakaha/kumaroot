# B3したい（``examples/basic/B3``）

![](./fig/exampleB3.png)

B3の題材はPETです。
患者の頭を円柱とし、その周りをLSO結晶で作ったガンマ線検出器で取り囲んでいます。

## ビルドしたい

```console
$ cd examples/basic/B3/B3a
(B3/B3a/) $ mkdir build
(B3/B3a/) $ cd build
(B3/B3a/build/) $ cmake ..
(B3/B3a/build/) $ make -j8
(B3/B3a/build/) $ ./exampleB3a
```

``examples/basic/B3/``の中には``B3a``と``B3b``のディレクトリがあります。

## 患者の頭部を作成する

```cpp
G4LogicalVolume* DefinePatientVolume(const G4String &aName)
{
    // 脳の組織を取得する
    G4NistManager *nm = new G4NistManager::Instance()
    auto material = nm->FindOrBuildMaterial("G4_BRAIN_ICMP");

    // 円柱を作成する
    // 半径 : 8 cm
    // 長さ : 10cm
    auto solid = new G4Tubs(
        "Patient",
        0.,
        8 * cm,    // 半径
        5 * cm,    // 長さ
        0. * deg,
        360. * deg
    )

    // 論理物体を作成する
    auto logical = new G4LogicalVolume(
        solid,
        material,
        aName,
    )

    return logical;
}
```

```cpp
// 物理物体を配置する
auto logicPatient = DefinePatientVolume("PatientLV");
new G4PVPlacement(
    nullptr,
    G4ThreeVector(),
    logicPatient,
    "Patient",
    logicWorld,
    false,
    0,
    fCheckOverlaps,
)
```

## 結晶を作成する

```cpp
void DefineMaterials()
{
    G4NistManager *nm = new G4NistManager::Instance();
    G4bool isotopes = false;

    G4Element* O = nm->FindOrBuildElement("O", isotopes);
    G4Element* Si = nm->FindOrBuildElement("Si", isotopes);
    G4Element* Lu = nm->FindOrBuildElement("Lu", isotopes);

    auto LSO = new G4Material("Lu2SiO5", 7.4 * g / cm3, 3);
    LSO->AddElement(Lu, 2);
    LSO->AddElement(Si, 1);
    LSO->AddElement(O, 5);
}
```

```cpp
G4LogicalVolume* DefineCrystalVolume(const G4String &aName)
{
    // 材料を準備する
    G4NistManager *nm = new G4NistManager::Instance()
    auto material = nm->FindOrBuildMaterial("Lu2SiO5")

    // 結晶の形を作成する
    // 外形の寸法
    G4double fullX = 6.0 * cm;
    G4double fullY = 6.0 * cm;
    G4double fullZ = 3.0 * cm;
    // 容器の厚み
    G4double gap = 0.5 * mm;

    // 内形の寸法（の半分）
    G4double halfX = 0.5 * (fullX - gap);
    G4double halfY = 0.5 * (fullY - gap);
    G4double halfZ = 0.5 * (fullZ - gap);

    auto solid = new G4Box(
        "crystalSolid",
        halfX,
        halfY,
        halfZ
    )

    G4LogicalVolume* logical = new G4LogicalVolume(
        solid,
        material,
        aName
    )

    return logical;
}
```

```cpp
G4VPhysicalVolume* DefineDetectorVolume(const G4String &aName)
{
    auto logicCrystal = DefineCrystalVolume("CrystalLV");

    G4int numberOfCrystals = 32;
    G4int numberOfRings = 9;

    G4double dPhi = twopi / numberOfCrystals
    G4double half_dPhi = 0.5 * dPhi;
    G4double cos_dPhi = std::cos(half_dPhi);
    G4double tan_dPhi = std::tan(half_dPhi);

    G4double ring_R1 = 0.5 * fullY / tan_dPhi;
    G4double ring_R2 = (ring_R1 + fullZ) / cos_dPhi;
    G4double dZ = numberOfRings * fullX;

    for (G4int icrystal = 0; icrystal < n_crystals; icrystal++) {
        G4double phi = icrystal * dPhi;
        G4RotationMatrix rotation = G4RotationMatrix();
        rotation.rotateY(90 * deg);
        rotation.rotateZ(dphi);
        G4ThreeVector uz = G4ThreeVector(std::cos(phi), std::sin(phi), 0.);
        G4ThreeVector position = (ring_R1 + 0.5 * dZ) * uz;
        G4Transform3D transform = G4Transform3D(rotation, position);

        new G4PVPlacement(
            transform,
            logicCrystal,
            aName,
            logicRing,
            icrystal,
            fCheckOverlaps
        );
    }
}
```

