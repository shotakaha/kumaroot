# Accumulableしたい（`G4VAccumulable`）

`G4VAccumulable`は、マルチスレッド環境で
スレッドセーフなデータ収集するための抽象基底クラスです。
Geant4では、この機能を使って
スレッドごとに独立してデータを蓄積し、
ラン終了時にマスタースレッドで統合（accumulate）できます。

この機能は、`G4VAccumulable`を継承した
`G4AccValue<T>`や、
`G4AccArray<T, N>`
といったテンプレートクラスとして実装されていて、
`G4AccumulablelManager`を通じて登録、初期化、集約、リセットできます。

詳細は[Accumulables](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Analysis/accumulables.html)を参照してください。

:::{hint}

**アキュムレーター** は並列処理における一般的な概念のようです。
スレッドごとに安全に隔離した変数を保持し、
マスタースレッドで最終的に合算するという仕組みです。

Geant4では`G4VAccumulable`クラスとして組み込み、
実際には`G4AccValue<T>`などのテンプレートクラスで実装されています。

:::

## 変数したい（`G4AccValue`）

```cpp
G4Accumulable<型> 変数名;
```

:::{note}

Geant4 11.3.0で、テンプレートクラス名が
`G4Accumlable`から`G4AccValue`に変更になりました。
新しくアプリを作成する場合は
`G4AccValue`を使う方がよさそうです。

:::

```cpp
// RunAction.hhのプライベート変数で定義
G4AccValue<G4double> energyEdeposit = 0;

// RunAction::RunAction()
// コンストラクタでAccumulableManagerを作成
auto* am = G4AccumulableManager::Instance()
am->Register(energyDeposit);

// RunAction::EndOfRunAction
// ランの終了時にデータをマージ
am->Merge();
```
