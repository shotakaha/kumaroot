# 物理ボリュームを複製したい（``G4PVReplica``）

```cpp
auto physical_volume = new G4PVReplica{
    const G4String &pName,             // 名前
    G4LogicalVolume *pLogicalVolume,   // 子ボリューム
    G4LogicalVolume *pMotherVolume,    // 親ボリューム（物理ボリュームもOK）
    const EAxis pAxis,      // 複製する方向
    const G4int nReplicas,  // 複製する数
    const G4double width,   // 複製する方向の厚み
    const G4double offset   // 複製を開始する座標（原点からのオフセット）
};
```

[G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)で、繰り返し構造を持つ、複数の論理物体を一度に配置できます。
論理物体の数が多い場合は、メモリ節約になるそうです。

## 物理ボリュームを確認したい

```cpp
auto name = physical_volume->GetName();
auto current_volume = physical_volume->GetLogicalVolume();
auto mother_volume = physical_volume->GetMotherLogical();
G4int copy_number = physical_volume->GetCopyNo();
G4bool overlaps = physical_volume->CheckOverlaps();
```


## 並べる方向

```cpp
kXAis  // X方向
kZAis  // Z方向
kRho   // r方向（動径方向）
kPhi   // φ方向（極軸方向）
```

:::{seealso}

- [G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)
- [G4VPhysicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4VPhysicalVolume.html)

:::
