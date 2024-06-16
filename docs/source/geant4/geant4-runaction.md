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
    // 内部変数（プライベート変数など）の初期化など
    fEnergyDeposit = 0;
    auto am = G4AnalysisManager::Instance();
    am->OpenFile();
}
```

``BeginOfRunAction``はラン開始に実行されるメソッドです。
ランごとのデータを初期化したり、
保存先のファイルの設定をするとよいです。

## ラン終了したい（``EndOfRunAction``）

```cpp
void RunAction::EndOfRunAction(const G4Run *aRun)
{

    auto am = G4AnalysisManager::Instance();
    am->Write();
    am->CloseFile();

}
```

``EndOfRunAction``はランの終わりに実行されるメソッドです。
すべてのイベントのデータを集計して、ランサマリーを表示できたりします。
