# 構造体を作りたい

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
4. 配置して物理ボリュームを作成する（``G4VPhysicalVolume``の派系クラス）

これはとても分かりやすいオブジェクト指向な設計になっていると思います。

現実の実験と同じように、
材料をどうするか、形をどうするか、を考えて測定装置を用意します。
論理ボリュームはまさに「測定装置」です。

測定をするためには、測定装置を組み上げて実験室に配置しないといけません。
論理ボリュームをある座標に配置すると、物理ボリュームになります。
物理ボリュームは「実験室に設置した測定装置」そのものです。
