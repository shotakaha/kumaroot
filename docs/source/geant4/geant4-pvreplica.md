# 測定器を配置したい（``G4PVReplica``）

```cpp
new G4PVReplica(
    const G4String &pName,             // 名前
    G4LogicalVolume *pLogicalVolume,   // 子ボリューム
    G4LogicalVolume *pMotherVolume,    // 親ボリューム（物理ボリュームもOK）
    const EAxis pAxis,      // 並べる方向
    const G4int nReplicas,  // 並べる数
    const G4double width,   // 並べる方向の厚み
    const G4double offset   // 並べ始める場所の原点からのオフセット
)
```

[G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)で、複数の論理ボリュームを一度に配置できます。

## 並べる方向

```cpp
kXAis  // X方向
kZAis  // Z方向
kRho   // r方向（動径方向）
kPhi   // φ方向（極軸方向）
```
