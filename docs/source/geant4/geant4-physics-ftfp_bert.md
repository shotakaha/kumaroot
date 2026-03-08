# 高エネルギー物理したい（`FTFP_BERT`）

```cpp
#include "FTFP_BERT.hh"

int main()
{
    auto* physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
}
```

`FTFP_BERT`は、LHC実験などの高エネルギー物理学分野で利用されている物理モジュールです。
この物理モジュールは、
標準的な電磁相互作用（`G4EmStandardPhysics`）、
ハドロン相互作用（FTFPモデルとBERTモデル）、
粒子の崩壊（`G4DecayPhysics`）
で構成されています。

## その他の標準的な物理モデル

高エネルギー物理の相互作用モデルには、いくつか種類があります。
どのモデルを採用しているか、モデル名である程度判別できるようになっています。

| モデル名 | 電磁相互作用 | 低エネルギーハドロン | 高エネルギーハドロン | 中性子輸送 |
| --- | --- | --- | --- | --- |
| FTFP_BERT | 標準 | Bertiniモデル | Fritiofモデル | - |
| FTFP_BERT_HP | 標準 | Bertiniモデル | Fritiofモデル | 高精度 |
| FTFP_BERT_LV | Livermoreモデル | Bertiniモデル | Fritiofモデル | - |
| QGSP_BERT | 標準 | Bertiniモデル | QGSモデル | - |

モデル名に使われている用語の補足です。

- `FTFP` : Fritiof（高エネルギー） + Precompound（前平衡モデル）
- `BERT` : Bertini Cascade（低エネルギーの核内カスケード）
- `HP` : High Precision（熱中性子などの高精度輸送モデル）
- `LV` : Livermore（低エネルギーの電磁相互作用に対応したモデル）
- `QGS` : Quark-Gluon String Model（超高エネルギー領域に対応したモデル）

Geant4 v10.0以前は`QGSP_BERT`、以降は`FTFP_BERT`が
Geant4の標準的なモデルとして採用されています。
まずは、`FTFP_BERT`を採用しておけばよいはずです。
