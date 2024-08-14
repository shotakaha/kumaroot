# どこからでも論理ボリュームしたい（``G4LogicalVolumeStore``）

```cpp
auto lvs = G4LogicalVolumeStore::GetInstance();
G4LogicalVolume *lv = lvs->GetVolume("ボリューム名");
```

``G4LogicalVolumeStore``はシングルトンになっていて、``GetInstance``でどこからでもアクセスできます。

ジオメトリで作成されたすべての論理ボリュームの情報を持っており、``GetVolume``でボリューム名を指定して取得できます。

:::{note}

内部変数に
``std::map<G4String, std::vector<G4LogicalVolume*>>``を持っているため、
ボリューム名を指定する必要があります。

:::

## ワールドの大きさを取得したい

```cpp
G4LogicalVolume *world = G4LogicalVolumeStore::GetInstance()->GetVolume("World");

G4double solid_x{0.};
G4double solid_y{0.};
G4double solid_z{0.};

if (world) {
    // GetSolidで得られたオブジェクトをG4Boxにdynamic_castする
    // dynamic_castに失敗するとnullptrになる
    G4Box *box = dynamic_cast<G4Box*>(world->GetSolid())
    if (box) {
        solid_x = box->GetXHalfLength() * 2 / mm;
        solid_y = box->GetYHalfLength() * 2 / mm;
        solid_z = box->GetZHalfLength() * 2 / mm;
    } else {
        // dynamic_castできなかった場合
        G4err << "World volume of box not found." << G4endl;
    }
} else {
    // World が見つからなかった場合
    G4err << "world with the specified name not found." << G4endl;
}
```

上のサンプルは、``examples/B2/B2a/src/PrimaryGeneratorAction.cc``を参考にしました。
ここでは、ワールドの大きさを基準にして、
入射粒子の座標を設定するために使っていました。

``PrimaryGeneratorAction``クラスなど他のクラスからはジオメトリのクラスへの直接アクセスは基本的にできません。
そのような場合でも、``G4LogicalVolumeStore``のインスタンス（＝シングルトン）を経由して、論理ボリュームやソリッドにアクセスできます。

:::{note}

ジオメトリのクラスに、サイズを取得するためのpublicなゲッターを追加すれば、アクセスできます。
しかし、``G4LogicalVolumeStore``を経由したほうが、はるかに簡単だと思います。

:::

## リファレンス

- [G4LogicalVolumeStore](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolumeStore.html)
