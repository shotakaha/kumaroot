# FTFP_BERTしたい（`FTFP_BERT`）

```cpp
#include "FTFP_BERT.hh"

int main()
{
    auto* physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
}
```

メイン関数で物理モデルを設定する部分を抜粋しました。

`FTFP_BERT`はv10.0以降で標準の物理モデルとして採用された相互作用モデルです。
とくに高エネルギー物理のシミュレーションでは、まずこのモデルから使うのが推奨されています。

## その他の標準的な物理モデル

| モデル名 | 電磁相互作用 | 低エネルギーハドロン | 高エネルギーハドロン | 中性子輸送 |
|---|---|---|---|---|
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
