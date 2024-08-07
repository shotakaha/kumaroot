# プラスチックシンチレータを作りたい

```cpp
// シンチレーター
G4NistManager *nm = new G4NistManager::Instance()
G4Material *scintillator = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");
```

[付属サンプルB5のDetectorConstruction.cc](https://github.com/Geant4/geant4/blob/master/examples/basic/B5/src/DetectorConstruction.cc)を参考にプラスチックシンチレーターを作成しました。

:::{note}

付属サンプルB5では、シンチレーターの材料にビニルトルエン（C9H10）を指定していました。
もしかしたら、実験によっては別の材料を使っているかもしれません。

:::

## シンチレーターバーを作りたい

```cpp
G4LogicalVolume *DefineDetectorVolume(const G4String &name){

    // 材料を調達する
    G4NistManager *nm = new G4NistManager::Instance()
    auto material = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

    // 形状を定義する
    G4double halfX = 2.5 * cm;
    G4double halfY = 5.0 * cm;
    G4double halfZ = 0.5 * cm;

    auto solid = new G4Box(
        "detectorSolid",
        halfX,    // 幅
        halfY,    // 長さ
        halfZ,   // 厚み
    )

    // 論理物体を定義する
    auto logical = new G4LogicalVolume(
        solid,     // G4VSolid
        material,  // G4Material
        name,      // 名前（引数で指定）
    )

    // ワイヤフレームの色を変更（オプション）
    auto color = new G4VisAttribute(G4Colour(0.8888, 0.0, 0.0));
    logical->SetVisAttributes(color);

    return logical;

    // 物理物体の配置は別にする
}
```

小型宇宙線検出器OSECHIで使っているプラスチックシンチレーターを想定して作成しました。
OSECHIでは幅5cm、長さ10cm、厚み1cmのプラシンを3枚重ねて使っています。

## 有感領域を追加したい

```cpp
auto sdManager = G4SDManager::GetSDMpointer();
G4String SDname;
auto detector = new DetectorSD(SDname="/detector");
fDetectorLogical->SetSensitiveDetector(detector);
```

## プラスチックシンチレーター

プラスチックシンチレーターは、有機シンチレータを溶媒に溶かしてから、高分子化した固体プラスチックです。
材料としてボリビニールトルエンやポリメチルメタアクリレート（アクリル樹脂）がよく使用されるようです。
安価で成形加工が容易なため、大体積の固体シンチレーターが必要な場面で使われます。

プラスチックシンチレーターが発するシンチレーション光の波長は400nmくらいで、
その立ち上がりはns以下、減衰時間も数ns程度です。
時間応答性がよいため、荷電粒子の個数の計数や、
複数セットを並べて飛跡検出器として使われることが多いです。

### シンチレーション光の原理と特徴

入射した荷電粒子がシンチレーターの中で失ったエネルギーの一部が、
シンチレーターを構成する分子を励起したあと、
ふたたび基底状態に戻るときに可視光を放出します。

発光するタイミングや発光時間により、
即発蛍光（prompt fluorescence）、
遅発蛍光（delayed fluorescence）、
燐光（phosphorescence）
とよばれる成分に区別されます。
プラスチックシンチレーターの場合、その主成分は即発蛍光です。

発光量は通過した荷電粒子のエネルギー損失に（ほぼ）比例と近似してよいですが、
厳密には、粒子の種類とそのエネルギーに依存していて「Birksの式」で表すことができます。

### Birksの式と発光量

「Birksの式」は経験則から得られた式で、
単位飛程長あたりのエネルギー損失（$dE/dx$）と発光量（$dL/dx$）の関係を説明できます。

```{math}
\frac{dL}{dx} = \frac{S \frac{dE}{dx}}{1 + kB\frac{dE}{dx}}
```

$S$はシンチレーション効率、
$kB$は消光（quench）する確率で、実験データに合わせて調整するパラメーターです。
また、同じエネルギーを持つ電子と重荷電粒子に対する発光量の違いは
「アルファ対ベータ比（alpha-to-beta ratio）」というパラメーターが使われます。



## リファレンス


- Glenn F. Knoll著、神野郁夫・木村逸郎・阪井英次共訳、放射線計測ハンドブック（第4版）「第8章 シンチレーション検出器の原理」
