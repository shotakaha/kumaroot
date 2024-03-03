# 相互作用したい（``G4VModularPhysicsList``）

```cpp
G4VModularPhysicsList* physicsList = new FTFP_BERT;
runManager->SetUserInitialization(physicsList);
```

粒子と物質の相互作用モデルを定義して``G4RunManager``に設定します。

## 定義済みの相互作用モデルしたい（``G4VModularPhysicsList``）

``G4VModularPhysicsList``でGeant4で定義された相互作用モデルを設定できます。
定義済みのモデルの内容は[Gude for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。

Geant4の相互作用モデルは``FTFP_BERT``をデフォルトとして採用しています。
以前のバージョンでは``QGSP_BERT``が採用されていました。
医療や宇宙開発関係は``QBBC``を採用するのがよいようです。

## カスタムしたい（``G4VUserPhysicsList``）

定義されていない相互作用が必要な場合は``G4VUserPhysicsList``を継承してカスタムできるようになっています。
