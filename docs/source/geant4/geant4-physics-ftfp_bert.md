# FTFP_BERTしたい（``FTFP_BERT``）

```cpp
#include "FTFP_BERT.hh"
#include "G4VModularPhysicsList.hh"

int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);
}
```

``FTFP_BERT``はGeant4.10から標準になった相互作用モデルです。
高エネルギー物理学分野のひとは、まず、このモデルから使ってみればよいそうです。

| モデル名 | 電磁相互作用 | 低エネルギーハドロン | 高エネルギーハドロン | 中性子輸送 |
|---|---|---|---|---|
| FTFP_BERT | 標準 | Bertiniモデル | Fritiofモデル | - |
| FTFP_BERT_HP | 標準 | Bertiniモデル | Fritiofモデル | 高精度 |
| FTFP_BERT_LV | Livermoreモデル | Bertiniモデル | Fritiofモデル | - |
| QGSP_BERT | 標準 | Bertiniモデル | QGSモデル | - |
