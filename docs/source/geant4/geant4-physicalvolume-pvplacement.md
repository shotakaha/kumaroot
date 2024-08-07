# 物理ボリュームを配置したい（``G4PVPlacement``）

```cpp
auto physical_volume = new G4PVPlacement{
    const G4Transrom3D &Transform3D,
    G4LogicalVolume *pLogicalVolume,  // 子ボリューム
    const G4String &pName,            // 名前
    G4LogicalVolume *pMotherVolume,   // 親ボリューム,
    G4bool bMany,                     // ブーリアン演算,
    G4int aCopyID,                    // コピー番号,
    G4bool bCheckOverlaps             // 重なり確認
};
```

[G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)は``G4VPhysicalVolume``を具象化したクラスです。
論理物体（logical volume）を物理物体（physical volume）として配置できます。

## 物理ボリュームを確認したい

```cpp
auto name = physical_volume->GetName();
auto current_volume = physical_volume->GetLogicalVolume();
auto mother_volume = physical_volume->GetMotherLogical();
G4int copy_number = physical_volume->GetCopyNo();
G4bool overlaps = physical_volume->CheckOverlaps();
```

## 複数の測定器を配置したい

```cpp
const G4int n_detectors = 10;
G4RotationMatrix rotation = G4RotationMatrix();
G4ThreeVector direction = G4ThreeVector(0.*m, 0.*m, 0.*m);
G4Transform3D location = G4Transform3D(rotation, direction);

G4int z = 0;
for (int i = 0; i < n_detectors; i++) {
    z = i * 10 * cm;
    direction = G4ThreeVector(0.*cm, 0.*cm, z);
    location = G4Transform3D(rotation, direction);
    new G4PVPlacement(
        location,
        pDetectorLogical,
        "Detector Logical",
        pWorldLogical,
        false,
        i,    // copy number
        true
    )
}
```

複数の測定器を配置する場合は、コピー番号（``copyNo``）を変更することで、異なる物理物体としてアクセスできます。
区別する必要がない場合は、同じ値でOKです。

:::{seealso}

- [G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)

:::
