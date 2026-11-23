# 実験室を作りたい（`BuildWorld`）

```cpp
G4LogicalVolume* BuildWorld(
    const G4String& logicalName = "World",
    const G4String& materialName = "G4_AIR",
    G4double lengthX = 50. * m,
    G4double lengthY = 50. * m,
    G4double lengthZ = 50. * m)
{
    // 形状を定義（G4Box は半分の長さで指定する）
    auto solid = new G4Box(
        logicalName + "Solid",  // solid 名（論理名から導く）
        0.5 * lengthX,
        0.5 * lengthY,
        0.5 * lengthZ
    );

    // 実験室の素材を決める
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial(materialName);

    // 論理ボリューム（実験室）
    return new G4LogicalVolume(
        solid,         // G4VSolid
        material,      // G4Material
        logicalName,   // 名前
        nullptr,       // G4FieldManager（未使用）
        nullptr,       // G4VSensitiveDetector（未使用）
        nullptr        // G4UserLimits（未使用）
    );
}
```

Geant4で通常**World**（ワールド）と呼ばれるシミュレーション用の実験室を作成します。
このボリュームは親ボリュームを持たず、
すべての測定装置はこの空間の中に収まるように配置する必要があります。

ここでは形状を``G4Box``（箱型）、
素材を``G4_AIR``（空気）、
大きさを50m立方に設定した論理ボリュームを作成しています。

関数の引数はすべて既定値を持つので、引数を省略すると上の値が使われます。
素材や大きさを変えたいときは、その引数を指定します。
論理ボリューム名を変える場合は、``G4LogicalVolumeStore::GetVolume("World")``や可視化マクロの指定も合わせて変更してください。

引数の``G4Box``のサイズは**全長**で指定しますが、``G4Box``の引数は**半分の長さ**を要求するので、0.5倍してから渡しています。

ワールドの論理物体を返す関数を作成します。
これを``SetupWorld``の中で呼び出して、物理物体として配置します。

## 実験室を配置したい

```cpp
G4VPhysicalVolume* SetupWorld(const G4String& physicalName = "World")
{
    // 実験室の論理物体を取得する
    auto logical = BuildWorld();

    // 実験室を配置する（回転なし・原点・親ボリュームなしに固定）
    return new G4PVPlacement(
        nullptr,          // G4RotationMatrix*（回転なし）
        G4ThreeVector(),  // 位置（原点）
        logical,          // G4LogicalVolume : 配置する論理ボリューム
        physicalName,     // G4String : この物理ボリュームの名前
        nullptr,          // G4LogicalVolume : 親ボリュームはなし
        false,            // G4bool pMany（未使用）
        0,                // G4int pCopyNo : コピー番号
        true              // G4bool check overlaps
    );
}
```

``G4PVPlacement``に渡す引数のうち、World は回転・位置・親ボリュームを持ちません。
そのため、これらは``nullptr``や原点で固定しています。

``SetupWorld``の中で``BuildWorld``を呼び出し、その戻り値を配置しています。
これで、最上位の親ボリュームである実験室の完成です。
あとは、測定装置をこの中に納まるように並べるだけです。

測定器シミュレーションを実行する実験室（通称：World）を作成しました。
実験室は50m立方の箱型としました。
どうしてこの大きさにしたかというと、この中にスーパーカミオカンデを配置してみたいからです。
スーパーカミオカンデの高さ41.4mに余裕を持たせて、約1.2倍の大きさにしています。

:::{note}

Geant4では生成された粒子が「実験室の外側に飛び出す」か「運動量がゼロになる」まで、素粒子反応が繰り返されます。なので、ある程度の外枠を定義しておかないと、必要のない計算にまで時間をかけてしまうことになります。

:::

## 非表示にしたい

```cpp
world->SetVisAttributes(G4VisAttributes::GetInvisible());
```

``world``は``G4LogicalVolume``（論理ボリューム）なので、``BuildWorld``が返した値に対して設定します。
可視化の詳細は[G4VisAttributes](geant4-logicalvolume-visattributes)を参照してください。
