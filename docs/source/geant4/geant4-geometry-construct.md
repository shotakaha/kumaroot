# ジオメトリを構築したい（`Geometry::Construct`）

```cpp
G4VPhysicalVolume* Construct()
{
    // 実験室（World）を配置する
    auto world = SetupWorld();

    // 水タンクを実験室の中に配置する
    SetupTank(world);

    return world;
}
```

`Construct()`は、ジオメトリ（物理ボリュームの配置）を作る場所です。
`SetupWorld()`で最上位の実験室を配置し、その物理ボリュームを親として`SetupTank()`でタンクを配置します。
最後に、最上位の実験室の物理ボリュームを返します。

感度検出器（SD）や電磁場は、`ConstructSDandField()`で設定します。
ジオメトリの配置は`Construct()`で行うので、両者を混同しないようにしてください。

- [](./geant4-geometry-examples.md)
- [](./geant4-geometry-world.md)
- [](./geant4-geometry-tank.md)
