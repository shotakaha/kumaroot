# ランアクションしたい（``G4UserRunAction``）

ランごとのデータを収集したい場合は、
``G4UserRunAction``クラスを継承したクラスを作成します。

```cpp

#include "G4UserRunAction.hh"

class RunAction: public G4UserRunAction
{
    public:
        RunAction();
        ~RunAction() override = default;

        void BeginOfRunAction(const G4Run *aRun) override;
        void EndOfRunAction(const G4Run *aRun) override;
    private:
        fEnergyDeposit = -1;
}
```

:::{seealso}

- [](./geant4-run.md)
- [](./geant4-analysismanager.md)

:::

## 初期化したい（``RunAction``）

```cpp
RunAction::RunAction()
{
    auto am = G4AnalysisManager::Instance();
    am->SetFilename("ファイル名");
    am->SetDefaultFileType("csv");
}
```

## ラン開始したい（``BeginOfRunAction``）

```cpp
void RunAction::BeginOfRunAction(const G4Run *aRun)
{
    // G4Runに対する操作
    G4int run_id = aRun->GetRunID();
    G4int n_events = aRun->GetNumberOfEvents();
    auto events = aRun->GetEventVector();
    G4String random_status = aRun->GetRandomNumberStatus();

    // 保存ファイルの作成
    auto am = G4AnalysisManager::Instance();
    am->OpenFile();

    // 内部変数の初期化
    fEnergyDeposit = 0;

}
```

``BeginOfRunAction``はラン開始に実行されるメソッドです。
ランごとのデータを初期化したり、
保存先のファイルの設定をするとよいです。

## ラン終了したい（``EndOfRunAction``）

```cpp
void RunAction::EndOfRunAction(const G4Run *aRun)
{
    // G4Runに対する操作
    G4int run_id = aRun->GetRunID();
    G4int n_events = aRun->GetNumberOfEvents();
    auto events = aRun->GetEventVector();
    G4String random_status = aRun->GetRandomNumberStatus();

    auto am = G4AnalysisManager::Instance();
    am->Write();
    am->CloseFile();
}
```

``EndOfRunAction``はランの終わりに実行されるメソッドです。
すべてのイベントのデータを集計して、ランサマリーを表示できたりします。
