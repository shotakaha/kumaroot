# PMTを作りたい（``BuildPMT``）

```cpp
G4LogicalVolume *BuildPMT()
{
    // パラメーター設定
    G4String logical_name{"PMTWindow"};
    G4String material_name{"G4_PLEXIGLASS"};
    G4double radius{3.81 * cm};  // 3in.管
    G4double thickness{1.0 * mm};

    // 形状を定義
    // PMTの入射窓を、平たい円柱で作成
    G4double r_min{0. * cm};
    G4double r_max{radius};
    G4double half_z{0.5 * thickness};
    G4double s_phi{0. * deg};
    G4double d_phi{360. * deg};

    auto solid = new G4Tubs{
        "pmtSolid",
        r_min,    // 内径
        r_max,    // 外径
        half_z,   // 高さ（厚み）
        s_phi,    // 開始角度
        d_phi,    // 回転角
    };

    // 材料を定義
    // 入射窓はプレキシガラス（アクリル）に設定
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_PLEXIGLASS");

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logical_name  // 名前
    );

    return logical;
}
```

光電子増倍管（PMT）の入射窓だけを作成しました。
PMTに入射した光子の数を知りたい場合は、``G4SensitiveDetector``を追加し、データを残す必要があります（あとで追加する）

## PMTを配置したい

```cpp
G4LogicalVolume* SetupPmtArray()
{
    // 親ボリューム（別途作成済みのものを使う）
    auto container = BuildWorld();

    // 子ボリューム = PMTを準備する
    auto element = BuildPMT();

    // PMTを5本並べる
    std::vector<int> elements{101, 102, 103, 104, 105};
    for (G4int id: elements) {
        auto rotation = G4RotationMatrix{};
        auto direction = G4ThreeVector{};
        auto origin = G4Transform3D{rotation, direction};
        new G4PVPlacement(
            origin,
            element,
            "Container",
            container,
            false,
            id,  // copy_number
            true
        );
    }

    return container;
}
```

複数本のPMTを配置したいケースは多いと思います。
ここでは横一列に並べようとしています。
