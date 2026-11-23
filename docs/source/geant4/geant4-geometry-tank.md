# 水タンクを作りたい（`BuildTank`）

```cpp
G4LogicalVolume* BuildTank(
    const G4String& logicalName = "Tank",
    const G4String& materialName = "G4_WATER",
    G4double diameter = 39.3 * m,
    G4double height = 41.4 * m)
{
    // 形状を定義
    G4double rMin = 0. * cm;          // 底面の内径
    G4double rMax = 0.5 * diameter;   // 底面の外径
    G4double halfZ = 0.5 * height;    // 円柱の高さ（の半分）
    G4double sPhi = 0. * deg;         // 円の角度（始点）
    G4double dPhi = 360. * deg;       // 円の角度（終点）
    auto solid = new G4Tubs(
        logicalName + "Solid",  // solid 名
        rMin,
        rMax,
        halfZ,
        sPhi,
        dPhi
    );

    // 材料を定義
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial(materialName);

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,         // G4VSolid
        material,      // G4Material
        logicalName,   // 名前
        nullptr,       // G4FieldManager（未使用）
        nullptr,       // G4VSensitiveDetector（未使用）
        nullptr        // G4UserLimits（未使用）
    );

    // （オプション）ワイヤーフレームを着色
    auto color = new G4VisAttributes(true, G4Colour(0., 0.5, 1.)); // 青系
    logical->SetVisAttributes(color);

    return logical;
}
```

`BuildTank`関数は、円柱形の論理ボリュームを1つ作成する関数です。
`G4Tubs`で円柱を作成しています。
円柱の軸はZ軸方向で、引数は半径と高さの半分を指定します。

初期値はスーパーカミオカンデを参考に、材質を水（`G4_Water`）として、サイズを直径39.3m、高さ41.4mとしました。

## 水タンクを配置したい

```cpp
G4VPhysicalVolume* SetupTank(
    G4VPhysicalVolume* parent,
    const G4String& physicalName = "Tank")
{
    // タンクの論理ボリュームを準備する
    auto logical = BuildTank();

    // タンクは縦置きにしたい（X軸まわりに90度回転）
    G4RotationMatrix rotation;
    rotation.rotateX(90. * deg);

    // 原点に配置する
    G4ThreeVector position{0., 0., 0.};

    // タンクを配置する
    return new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        logical,                            // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        0,                                  // コピー番号
        true                                // 重なりチェック
    );
}
```

`SetupTank`関数は、`BuildTank`で作成した円柱状の論理ボリュームを、親ボリューム（`parent`）の中に物理ボリュームとして配置する関数です。

`G4Tubs`で作成した円柱の軸はZ軸方向になっているため、タンクは横置きになっています。
スーパーカミオカンデのように縦置きにしたいため、`G4RotationMatrix`でX軸まわりに90度回転させています。
これで回転後はY軸方向を向くようになります。

ワールドの中心に配置したかったので`G4ThreeVector`は原点のままにしています。
引数`parent`には、`SetupWorld`が返した実験室の物理ボリュームを渡します。
