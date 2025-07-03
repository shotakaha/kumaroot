# プラスチックシンチレータを作りたい

```cpp
G4Material* MakeEJ200() {
    // Eljen Technologies社のEJ-200

    // シンチレーターのベース材
    auto nm = G4NistManager::Instance();
    G4Material *material = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

    // 波長 [nm] -> エネルギー [eV] に変換
    auto e = [](double wavelength_nm) {
        return 1240.0 / wavelength_nm * eV;
    };

    // 光子のエネルギー（例として3点）
    const G4int n = 3;
    G4double energy[n] = {
        e(500.0),  // 赤 - 緑
        e(420.0),  // 青; POPOPピーク
        e(350.0)   // 紫; PPOピーク
    };

    // 光学特性テーブルを作成
    auto mpt = new G4MaterialPropertiesTable();

    // 屈折率
    // -> Refractive Indexを参照
    G4double rindex[n] = { 1.58, 1.58, 1.58 };
    mpt->AddProperty("RINDEX", energy, rindex, n);

    // 吸収長
    // -> ???
    G4double abslength[n] = { 100 * cm, 100 * cm, 10 * cm };
    mpt->AddProperty("ABSLENGTH", energy, abslength, n);

    // 発光スペクトル
    // -> Emission Spectrumを参照
    // 横軸は 波長 [nm] をエネルギーに変換して指定する
    G4double emission[n] = { 0.1, 1.0, 0.1 };
    mpt->AddProperty("SCINTILLATIONCOMPONENT1", energy, emission, n);

    // その他の発光特性
    // 単位エネルギーあたりの発光量
    // -> Scintillation Efficiency (photons/1MeV e-) を参照
    mpt->AddConstProperty("SCINTILLATIONYIELD", 10000. / MeV);
    // 発光量の統の的揺らぎ（＝エネルギー分解能）
    mpt->AddConstProperty("RESOLUTIONSCALE", 1.0);
    // シンチレーション光の減衰時間
    // -> Decay Time (ns) を参照
    mpt->AddConstProperty("FASTTIMECONSTANT", 2.1 * ns);
    // 発光成分の比率：fast / (fast+slow)
    mpt->AddConstProperty("YIELDRATIO", 1.0);

    // テーブルを材料に登録
    material->SetMaterialPropertiesTable(mpt);

    return material;
}
```

[Elijen Technologies社のEJ-200](https://eljentechnology.com/products/plastic-scintillators/ej-200-ej-204-ej-208-ej-212)のデータシートを参考にプラスチックシンチレーターを作成しました。

## シンチレーターバーを作りたい

```cpp
G4LogicalVolume *DefineDetectorVolume(const G4String &name){

    // 材料を作成
    auto* material = MakeEJ200();

    // 形状を定義する（OSECHI: 幅5cm x 長さ10cm x 厚み1cm
    G4double halfX = 2.5 * cm;  // 半幅
    G4double halfY = 5.0 * cm;  // 半長
    G4double halfZ = 0.5 * cm;  // 半厚

    auto* solid = new G4Box(
        "detectorSolid",
        halfX,    // 幅
        halfY,    // 長さ
        halfZ     // 厚み
    );

    // 論理物体を定義する
    auto* logical = new G4LogicalVolume(
        solid,     // G4VSolid
        material,  // G4Material
        name       // 名前（引数で指定）
    );

    // ワイヤフレームの色を変更（オプション）
    auto* color = new G4VisAttribute(G4Colour(0.8888, 0.0, 0.0));
    logical->SetVisAttributes(color);

    return logical;

    // 物理物体の配置は別にする
}
```

小型宇宙線検出器OSECHIでは幅5cm、長さ10cm、厚み1cmのプラシンを3枚重ねて使っています。
このサイズのシンチレーター1枚を想定して論理ボリュームを作成しました。

## 有感領域を追加したい

```cpp
void AttachSensitiveDetector(
    G4LogicalVolume* logical,
    const G4String& name
) {
    auto* sdm = G4SDManager::GetSDMpointer();

    // 重複登録を確認
    auto* sd = sdm->FindSensitiveDetector(name);

    // 登録されていない場合は新規に追加
    if (!sd) {
        auto* d = new DetectorSD(name);  // ユーザー定義のSDクラス
        sdm->AddNewDetector(d);
        logical->SetSensitiveDetector(d);
    } else {
        // 既存のSDを再利用
        logical->SetSensitiveDetector(sd);
    }
}

// SDを設定
auto* lv = DefineDetectorVolume("osechi");
AttachSensitiveDetector(lv, "/detector");
```

OSECHIで利用するプラスチックシンチレーターのバーを、
SensitiveDetectorに設定しました。
`AttachSensitiveDetector`という関数を作成し、
同じ論理ボリュームに、同じ（名前の）SDの重複登録をしないようにしました。

## プラスチックシンチレーター

プラスチックシンチレーターは、有機蛍光体（シンチレータ）を高分子樹脂に溶解・重合して作られた固体シンチレーターです。
ベース材料としてボリビニルトルエン（PVT）やポリメチルメタアクリレート（PMMA、アクリル樹脂）が使われることが多く、蛍光体としては、
一次蛍光材にPPO（2,5-Diphenyloxazole）、
二次蛍光材にPOPOP（1,4-Bis(5-phenyloxazol-2-yl)benzene）が添加されるのが一般的です。

安価で加工性がよいため、大型かつ自由な形状のシンチレーターが必要な用途に適しており、宇宙線観測や放射線検出、教育用装置などに広く使われています。

シンチレーション光の波長はおよそ400nm前後で、
その立ち上がりは1ns以下、減衰時間も数ns程度と
時間応答性がよいため、荷電粒子の個数の計数や、
複数セットを並べて飛跡検出器として使われることが多いです。

## 市販のプラスチックシンチレーター

市販されているプラスチックシンチレーターのひとつに[Ejen Technology社のEJ-200](https://eljentechnology.com/products/plastic-scintillators/ej-200-ej-204-ej-208-ej-212)があります。
EJ-200は、
ベース材にポリビニルトルエン（PVT）を使用し、
一次蛍光材としてPPO、
二次蛍光材としてPOPOPを添加した構成となっています。

Geant4でこのような材料を実装する場合は、PPOやPOPOPを個別のマテリアルとして定義せず、ベース材に対してG4MaterialPropertiesTableを使って、屈折率、吸収長、発光スペクトルなどの光学特性を設定するのが一般的です。

## シンチレーション光の原理と特徴

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

## Birksの式と発光量

「Birksの式」は経験則に基づく関係式で、
単位飛程長あたりのエネルギー損失（$dE/dx$）と、
そこから得られる発光量（$dL/dx$）の関係を説明できます。

```{math}
\frac{dL}{dx} = \frac{S \frac{dE}{dx}}{1 + kB\frac{dE}{dx}}
```

ここで、
$S$はシンチレーション効率、
$kB$はquenching係数で、光子が消光（quench）する確率を表します。

この式から、アルファ粒子のように$dE/dx$の大きな荷電粒子では、光の出力が抑制（quench）されることが分かります。
同じエネルギーを持つアルファ粒子と電子で発光量が異なる現象は「アルファ対ベータ比（alpha-to-beta ratio）」と呼ばれるパラメーターで表されます。

これらの値は、実験データに合わせて調整が必要なパラメーターです。
Geant4では、
$S$（シンチレーション効率）は`SCINTILLATIONYIELD`、
$kB$（quenching係数）は`BIRKSCONSTANT`
の定数名を使って、G4MaterialPropertiesTableに光学特性として設定できます。

## リファレンス

- Glenn F. Knoll著、神野郁夫・木村逸郎・阪井英次共訳、放射線計測ハンドブック（第4版）「第8章 シンチレーション検出器の原理」
