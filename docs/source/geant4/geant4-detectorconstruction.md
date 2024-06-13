# 測定器を作りたい（``G4VUserDetectorConstruction``）

```cpp

// ローカル関数（でもクラスの中の関数にしてもよい）
DefineWorldVolume(const G4String &name){...};
DefineDetectorVolume(const G4String &name){...};
DefineSubDetectorVolume(const G4String &name){...};

// 測定器の建設に必要なメイン関数
G4VPhysicalVolume *DetectorConstruction::Construct()
{
    // 論理物体を取得する
    auto worldLogical = DefineWorldVolume("world");
    auto detectorLogical = DefineDetectorVolume("detector");

    // ワールドを配置する
    G4Transform3D location = G4Transform3D(nullptr, nullptr);
    G4VPhysicalVolume *world = new G4PVPlacement(
        location,
        worldLogical,    // G4LogicalVolume: 配置する論理物体
        "worldPhysical",
        nullptr,         // G4LogicalVolume: 親となる論理物体
        ...);

    // 測定器を配置する
    G4Transform3D location = G4Transform3D(nullptr, nullptr);
    new G4PVPlacement(
        location,
        detectorLogical,  // G4LogicalVolume: 配置する論理物体
        "detectorP",
        worldLogical,     // G4LogicalVolume: 親となる論理物体
        ...);

    return world;
}
```

測定器を構築するクラスは、``G4VUserDetectorConstruction``を継承して作成します。
その中の``DetectorConstruction::Construct()``をオーバーライドして実装します。

附属サンプルを眺めると、``Construct()``関数の中で、ワールドも測定器も一緒くたに定義しているのですが、個人的には測定器のパーツ単位でモジュール化するとよいと思います。

:::{note}

測定器のサイズがすでに決まっている場合は、
ワールドや測定器のサイズはハードコードしてしまっても
問題ないと思います。

:::
