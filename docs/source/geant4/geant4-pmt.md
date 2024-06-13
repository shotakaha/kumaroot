# PMTを作りたい

```cpp
G4LogicalVolume *DefinePmtWindow(const G4String &name){

    // 材料を準備
    G4NistManager *nm = new G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_PLEXIGLASS")

    // 形状を定義
    // PMTの入射窓を、平たい円柱で作成
    auto solid = new G4Tubs(
        "windowSolid",
        0.,          // G4double: 内径
        3.81 * cm,   // G4double: 外径 （3in.管）
        1 * cm,      // G4double: 高さ（厚み）
        0. * deg,    // G4double sphi,
        360. * deg,  // G4double dphi,
    )

    auto logical = new G4LogicalVolume(
        solid,      // G4VSolid
        material,   // G4Material
        name,      // 名前（引数で指定）
    )

    return logical;
}
```

光電子増倍管（PMT）の入射窓だけを作成しました。
PMTに入射した光子の数を知りたい場合は、``G4SensitiveDetector``を追加し、データを残す必要があります（あとで追加する）
