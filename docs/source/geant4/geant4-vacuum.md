# 真空を作りたい（``G4_Galactic``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *vacuum = nm->FindOrBuildMaterial("G4_Galactic")
```

``G4_Galactic``で真空（らしき状態）を生成できます。

## カスタイマイズしたい

```cpp
G4Material *vacuum = new G4Material(
    "interGalactic",
    1.,            // 原子番号
    1.008*g/mole,  // 質量/モル
    1.e-25*g/cm3,  // 密度
    kStateGas,     // G4State: 状態（ガス）
    2.74*kelvin,   // G4double: 温度
    3.e-18*pascal  // G4double: 気圧
)
```

真空は「非常に密度が低いガス」として作ります。
ここの値はGeant4講習会の資料に掲載されていたものを使っています。
