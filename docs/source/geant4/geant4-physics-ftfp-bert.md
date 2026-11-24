# 高エネルギー物理したい（`FTFP_BERT`）

```cpp
#include "G4RunManagerFactory.hh"
#include "FTFP_BERT.hh"

int main()
{
    auto* rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);
    auto* physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
}
```

`FTFP_BERT`はGeant4の標準的な物理リストです。
LHC実験などの高エネルギー物理学分野で広く使われています。
自作アプリの開発では、まず最初に使うとよい物理リストです。

## 標準的な物理リストの中身を見たい

```cpp
// FTFP_BERT.cc（一部を省略）
FTFP_BERT::FTFP_BERT(G4int ver)
{
  defaultCutValue = 0.7*CLHEP::mm;                      // デフォルトのカット値
  RegisterPhysics( new G4EmStandardPhysics(ver));       // 標準的な電磁相互作用
  RegisterPhysics( new G4EmExtraPhysics(ver) );         // 追加の電磁相互作用（シンクロトロン放射など）
  RegisterPhysics( new G4DecayPhysics(ver) );           // 粒子の崩壊
  RegisterPhysics( new G4HadronElasticPhysics(ver) );   // ハドロンの弾性散乱
  RegisterPhysics( new G4HadronPhysicsFTFP_BERT(ver));  // ハドロンの非弾性相互作用（FTFP + BERT）
  RegisterPhysics( new G4StoppingPhysics(ver) );        // 停止した負のハドロン
  RegisterPhysics( new G4IonPhysics(ver));              // イオンの物理過程
  RegisterPhysics( new G4NeutronTrackingCut(ver));      // 中性子の追跡の打ち切り
}
```

`FTFP_BERT`のコンストラクタは、次のモジュールを順に登録しています。

- `G4EmStandardPhysics`：標準的な電磁相互作用
- `G4EmExtraPhysics`：シンクロトロン放射などの追加の電磁相互作用
- `G4DecayPhysics`：粒子の崩壊
- `G4HadronElasticPhysics`：ハドロンの弾性散乱
- `G4HadronPhysicsFTFP_BERT`：ハドロンの非弾性相互作用（FTFPモデルとBERTモデル）
- `G4StoppingPhysics`：停止した負のハドロンの相互作用
- `G4IonPhysics`：イオンの物理過程
- `G4NeutronTrackingCut`：中性子の追跡の打ち切り

ハドロン相互作用では、高エネルギー側をFTFPモデル、低エネルギー側をBERTモデルが担当し、数GeV付近で切り替わります。
デフォルトのカット値は`0.7 mm`です。

## 高精度輸送したい（`FTFP_BERT_HP`）

```cpp
#include "FTFP_BERT_HP.hh"

auto* physics = new FTFP_BERT_HP{};
```

`FTFP_BERT_HP`は、`FTFP_BERT`に中性子の高精度輸送（HP）を追加した物理リストです。

20 MeV未満の中性子を、評価済み核データを使って高精度に扱います。
遮蔽計算など、中性子の振る舞いが重要な場合に向いています。
高精度になる分、計算時間が増加します。
また、中性子の核データファイル（環境変数`G4NEUTRONHPDATA`で指定）が必要です。

## 超高エネルギーしたい（`QGSP_BERT`）

```cpp
#include "QGSP_BERT.hh"

auto* physics = new QGSP_BERT{};
```

`QGSP_BERT`は、`FTFP_BERT`の高エネルギー側をQGS（Quark-Gluon String）モデルに置き換えた物理リストです。
超高エネルギーの粒子（宇宙線など）を扱う場合に使います。
Geant4 v10.0以前は`QGSP_BERT`が標準的な物理リストでした。
現在は`FTFP_BERT`が標準で、`QGSP_BERT`は用途に応じて選ぶものになっています。

## 他の物理リストを使いたい

`QBBC`などのリファレンス物理リストも、同じように`new`して使えます。

```cpp
auto* physics = new QBBC{};
```

| 物理リスト | 特徴 |
| --- | --- |
| [](./geant4-physics-qbbc.md) | 汎用的な物理リスト。附属サンプル B1 で使用 |
| `Shielding` | 遮蔽計算向け。中性子の高精度輸送を含む |
| `FTFP_INCLXX` | 核内カスケードに INCL++ モデルを使用 |
| `QGSP_BIC_HP` | 中性子の高精度輸送と Binary カスケードを使用 |

## 附属サンプルではどう使われているか見たい

附属サンプルB2では、`FTFP_BERT`に`G4StepLimiterPhysics`を追加しています。

```cpp
auto physicsList = new FTFP_BERT;
physicsList->RegisterPhysics(new G4StepLimiterPhysics());
runManager->SetUserInitialization(physicsList);
```

Geant4 11.4.0 の附属サンプルでの使用状況は次のとおりです。

- basic
  - [](./geant4-examples-b2.md)：`FTFP_BERT`に`G4StepLimiterPhysics`を追加
  - [](./geant4-examples-b4.md)：`FTFP_BERT`をそのまま使用
  - [](./geant4-examples-b5.md)：`FTFP_BERT`に`G4StepLimiterPhysics`を追加
  - [](./geant4-examples-b1.md)：`FTFP_BERT`ではなく`QBBC`を使用
- extended
  - [](./geant4-examples-anaex03.md)：`FTFP_BERT`をそのまま使用
  - [](./geant4-examples-lxe.md)、[](./geant4-examples-opnovice.md)、[](./geant4-examples-opnovice2.md)、[](./geant4-examples-wls.md)：`FTFP_BERT`の電磁過程を`G4EmStandardPhysics_option4`に置き換え、`G4OpticalPhysics`を追加

:::{seealso}

- [FTFP__BERT](https://geant4.kek.jp/Reference/11.4.0/classFTFP__BERT.html)
- [](./geant4-physics-opticalphysics.md)
- [](./geant4-user-physicslist.md)

:::
