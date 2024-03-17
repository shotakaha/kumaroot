# Accumulableしたい（``G4Accumulable``）

```cpp
G4Accumulable<型> 変数名;

// RunAction.hhのプライベート変数で定義
G4Accumulable<G4double> energy_deposit = 0;

// RunAction::RunAction()
// コンストラクタでAccumulableManagerを作成
G4AccumulableManager *accumulableManager = G4AccumulableManager::Instance()
accumulableManager->RegisterAccumulable(energy_deposit);

// RunAction::EndOfRunAction
// ランの終了時にデータをマージ
accumulableManager->Merge();
```

``G4Accumulable``は、ユーザーのデータ収集を簡単にするために追加された型（みたいなもの）です。
``G4AccumulableManager``を使って、変数の代入／追加ができます。
また、マルチスレッド環境で実行した場合、``Merge``を使ってそれぞれのWorkerノードで取得したデータをまとめることができます。

詳細は[Accumulables](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Analysis/accumulables.html)を参照してください。

:::{note}

まったく調べてないですが、おそらく``std::vector``のような可変長リストなんだと思います。

:::
