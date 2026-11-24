# 汎用的な物理リストしたい（`QBBC`）

```cpp
#include "G4RunManagerFactory.hh"
#include "QBBC.hh"

int main()
{
    auto* rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);
    auto* physics = new QBBC{};
    rm->SetUserInitialization(physics);
}
```

`QBBC`は、Geant4標準のモジュール型物理リスト（`G4VModularPhysicsList`）の1つです。
電磁相互作用、ハドロン相互作用、崩壊過程などを含みます。
附属サンプルの`basic/B1`で使われています。
迷ったら`FTFP_BERT`でよいですが、`QBBC`も汎用的で安全な物理リストです。

## 標準的な物理リストの中身を見たい

```cpp
// QBBC.cc（一部を省略）
QBBC::QBBC(G4int ver, const G4String&)
{
  defaultCutValue = 0.7*CLHEP::mm;                             // デフォルトのカット値
  RegisterPhysics( new G4EmStandardPhysics(ver) );             // 標準的な電磁相互作用
  RegisterPhysics( new G4EmExtraPhysics(ver) );                // 追加の電磁相互作用（シンクロトロン放射など）
  RegisterPhysics( new G4DecayPhysics(ver) );                  // 粒子の崩壊
  RegisterPhysics( new G4HadronElasticPhysicsXS(ver) );        // ハドロンの弾性散乱（断面積データセット版）
  RegisterPhysics( new G4StoppingPhysics(ver) );               // 停止した負のハドロン
  RegisterPhysics( new G4IonPhysicsXS(ver) );                  // イオンの物理過程（断面積データセット版）
  RegisterPhysics( new G4IonElasticPhysics(ver) );             // イオンの弾性散乱
  RegisterPhysics( new G4HadronInelasticQBBC(ver));            // ハドロンの非弾性相互作用（FTFP・BERT・BIC）
  RegisterPhysics( new G4ChargeExchangePhysics(ver) );         // 荷電交換
  RegisterPhysics( new G4NeutronTrackingCut(ver) );            // 中性子の追跡の打ち切り
}
```

`QBBC`のコンストラクタは上のモジュールを順に登録しています。
`FTFP_BERT`をベースにしていますが、次のモジュールが異なります。

- `G4HadronElasticPhysicsXS`: 断面積データセット（XS）版のハドロン弾性散乱
- `G4IonPhysicsXS`: 断面積データセット（XS）版のイオン物理
- `G4IonElasticPhysics`: イオンの弾性散乱
- `G4ChargeExchangePhysics`: 荷電交換
- `G4HadronInelasticQBBC`: ハドロンの非弾性相互作用（FTFP・BERT・BIC）

ハドロンの非弾性相互作用では、核子のエネルギーに応じて次のようにモデルが分かれます。

- BIC：0〜1.5 GeV
- BERT：1 GeV から、FTFモデルとの遷移エネルギーまで。π中間子は12 GeVまで
- FTFP：高エネルギー側

## 附属サンプルではどう使われているか見たい

附属サンプルB1では、`QBBC`を使い、詳細度を1に設定しています。

```cpp
auto physicsList = new QBBC;
physicsList->SetVerboseLevel(1);
runManager->SetUserInitialization(physicsList);
```

`QBBC`を使っている附属サンプルは、`basic/B1`です。
ほかの多くの例題は`FTFP_BERT`を使っています（[](./geant4-physics-ftfp-bert.md)を参照）。

:::{seealso}

- [](./geant4-physics-ftfp-bert.md)
- [](./geant4-examples-b1.md)
- [](./geant4-user-physicslist.md)

:::
