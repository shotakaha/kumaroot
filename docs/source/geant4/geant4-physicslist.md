# 相互作用したい（``G4VModularPhysicsList``）

```cpp
G4VModularPhysicsList* physics_list = new FTFP_BERT;
runManager->SetUserInitialization(physics_list);
```

粒子と物質の相互作用モデルを定義して``G4RunManager``に設定します。

Geant4チームが用意した**Reference Physics List**を利用できます。
モデルの内容は[Gude for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。

モデル名は、利用している相互作用モデルを使った命名規則になっています。

| モデル名 | 電磁相互作用 | 低エネルギーハドロン | 高エネルギーハドロン | 中性子輸送 |
|---|---|---|---|---|
| FTFP_BERT | 標準 | Bertiniモデル | Fritiofモデル | - |
| FTFP_BERT_HP | 標準 | Bertiniモデル | Fritiofモデル | 高精度 |
| FTFP_BERT_LV | Livermoreモデル | Bertiniモデル | Fritiofモデル | - |
| QGSP_BERT | 標準 | Bertiniモデル | QGSモデル | - |

## カスタムしたい（``G4VUserPhysicsList``）

定義されていない相互作用が必要な場合は``G4VUserPhysicsList``を継承してカスタムできるようになっています。
