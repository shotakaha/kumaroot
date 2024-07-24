# 水タンクを作りたい（``SetupTankVolume``）

スーパーカミオカンデ（直径39.3m、高さ41.4m）サイズの水タンクを配置します。

```cpp
G4LogicalVolume *SetupWaterTank()
{
    // パラメーター設定
    G4String logical_name{"Tank"};
    G4String material_name{"G4_WATER"};
    G4double diameter{39.3 * m};
    G4double height{41.4 * m};

    // 形状を定義
    G4double r_min{0. * cm};         // 底面の内径
    G4double r_max{0.5 * diameter};  // 底面の外径
    G4double half_z{0.5 * height};   // 円柱の高さ（の半分）
    G4double s_phi{0. * deg};        // 円の角度（始点）
    G4double d_phi{360. * deg};      // 円の角度（終点）
    auto solid = new G4Tubs(
        "TankSolid",    // ソリッド名
        r_min,
        r_max,
        half_z,
        s_phi,
        d_phi
    );

    // 材料を定義
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuild(material_name);

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logical_name, // 名前
    )

    // （オプション）ワイヤーフレームを着色
    auto color = new G4VisAttributes(true, G4Colour(0., 0.5, 1.)); // 青系
    logical->SetVisAttributes(color);

    return logical;
}
```

``G4Tubs``で円柱を作成しました。
円柱の材料を``G4_WATER``にしました。
水タンクの論理ボリュームができました。

## 水タンクを配置したい

```cpp
G4VPhysicalVolume* SetVolumes()
{
    // Worldを準備する
    auto world = SetupWorldVolume();
    // Worldを配置する
    auto theWorld = new G4PVPlacement{...};

    // WaterTankを準備する
    auto tank = SetupWaterTankVolume();

    // タンクは縦置きにしたい
    G4RotationMatrix rotation = G4RotationMatrix(0., 90.*deg, 0.);
    G4ThreeVector direction = G4ThreeVector(0., 0., 0.);
    G4Transform3D origin = G4Transform3D(rotation, direction);

    new G4PVPlacement(
        origin,          // 子ボリュームの位置
        tank,            // 子ボリューム
        "TankPhysical",  // 名前
        theWorld,        // 親ボリューム
        false,           // no boolean operation
        0,               // G4int : copy number
        true,
    );

    return theWorld;
}
```

スーパーカミオカンデをイメージしているため、
水タンクを縦置きにしています。

``G4RotationMatrix``でY軸方向に90度回転させました。
縦置きにするために、どの引数を変更すればよいか、
よくわからなかったので、コンパイル＆実行して確認しながら調整しました。

ワールドの中心に配置したかったので、
``G4ThreeVector``は原点のままにしています。
