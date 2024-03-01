# 構造体の作成手順

```cpp
G4Material *fMaterial = new G4Material(...)
G4VSolid *fSolidBox = new G4Box(...)
G4LogicalVolume *fLogicalVolume = new G4LogicalVolume(...)
G4VPhysicalVolume *fPhysicalVolume = new G4PVPlacement(...)
```

構造体は4つのステップで作成できます。

1. 材料を作成する（``G4Material``）
2. 形状を作成する（``G4VSolid``の派系クラス）
3. 論理ボリュームを作成する（``G4LogicalVolume``）
4. 配置する（``G4VPhysicalVolume``の派系クラス）
