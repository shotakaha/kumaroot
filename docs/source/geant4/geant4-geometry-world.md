# 実験室を作りたい（``SetupWorldVolume``）

```cpp
G4LogicalVolume *SetupWorldVolume(){

    // パラメーターの設定
    G4String logical_volume = "World";
    G4String material_name = "G4_AIR";
    G4String length_x = 1. * m;
    G4String length_y = 1. * m;
    G4String length_z = 1. * m;

    // 形状を定義
    G4double halfX = 0.5 * length_x;
    G4double halfY = 0.5 * length_y;
    G4double halfZ = 0.5 * length_z;

    auto solid = new G4Box{
        "solid",    // 名前
        halfX,
        halfY,
        halfZ,
    };

    // 実験室の素材を決める
    G4NistManager *nm = new G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial(material_name);

    // 実験室
    auto logical = new G4LogicalVolume{
        solid,         // G4VSolid
        material,      // G4Material
        logical_name,  // 名前
        nullptr,       // G4FieldManager
        nullptr,       // G4VSensitiveDetector
        nullptr,       // G4UserLimits
    };
    return logical;
}
```

Geant4で通常**World**（ワールド）と呼ばれるシミュレーション用の実験室を作成します。
このボリュームは親ボリュームを持たず、
すべての測定装置はこの空間の中に収まるように配置する必要があります。

ここでは形状を``G4Box``（箱型）、
素材を``G4_AIR``（空気）に設定した
論理ボリュームを作成しています。

ワールドの論理物体を返す関数を作成します。
引数で論理物体の名前を設定できるようになっています。
これを``DetectorConstruction::Construct``の中で呼び出して、物理物体として配置します。

## 実験室を配置したい

```cpp
G4VPhysicalVolume* SetupVolumes()
{
    // 実験室の論理物体を取得する
    auto world = SetupWorldVolume();

    // 実験室の置き場所を決める
    G4RotationMatrix rotation = G4RotationMatrix{};       // 回転 : なし
    G4ThreeVector position = G4ThreeVector{0., 0., 0.};  // 方向 :  (0, 0, 0)
    G4Transform3D origin = G4Transform3D{rotation, position}  // 座標

    // 実験室を配置する
    G4VPhysicalVolume *theWorld = new G4PVPlacement(
        location,    // G4Transform3D : 論理ボリュームを配置する座標
        world,       // G4LogicalVolume : 配置する論理ボリューム
        "theWorld",  // G4String : この物理ボリュームの名前
        0,           // G4LogicalVolume: 親ボリュームはなし
        false,       // G4bool pMany（廃止）
        0,           // G4int pCopyNo : コピー番号
        true         // G4bool check overlaps
    )

    return theWorld;
}
```

測定器シミュレーションを実行する実験室（通称：World）を作成しました。
実験室は50m立方の箱型としました。
どうしてこの大きさにしたかというと、この中にスーパーカミオカンデを配置してみたいからです。

まず、実験室の形を決めます。
箱型の実験室なので``G4Box``を使いました。
``G4Box``のサイズに関係する引数はすべて**半分の長さ**で指定することになっているので0.5倍してあります。

次に実験室の材質を決めます。
地球にある実験室なので空気で満たしました。

最後に、置き場所を決めます。
これで、最上位の親ボリュームである実験室の完成です。
あとは、測定装置をこの中に納まるように並べるだけです。

:::{note}

Geant4では生成された粒子が「実験室の外側に飛び出す」か「運動量がゼロになる」まで、素粒子反応が繰り返されます。なので、ある程度の外枠を定義しておかないと、必要のない計算にまで時間をかけてしまうことになります。

:::

## 非表示にしたい

```cpp
pWorldLogical->SetVisAttributes(G4VisAttributes::GetInvisible());
```
