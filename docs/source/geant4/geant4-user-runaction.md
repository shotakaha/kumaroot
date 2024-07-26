# ランアクションしたい（``G4UserRunAction``）

ランごとのデータを収集したい場合は、
``G4UserRunAction``クラスを継承したクラスを作成します。

## 親クラス

- [G4UserRunAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserRunAction.html)

```cpp
G4UserRunAction();
virtual ~G4UserRunAction() = default;
virtual void BeginOfRunAction(const G4Run* /*aRun*/) {};
virtual void EndOfRunAction(const G4Run* /*aRun*/) {}
```

親クラスのメンバー変数を確認しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``BeginOfRunAction()``は、ランの開始時に実行される関数です。
``EndOfRunAction()``は、ランの終了時に実行される関数です。

どちらも仮想関数になっているため、設定は必須ではありません。
必要に応じて自作クラスでoverrideします。

## RunActionクラス

```cpp
// include/RunAction.hh

#ifndef RunAction_h
#define RunAction_h 1

#include "G4UserRunAction.hh"
#include "G4Run.hh"

namespace ToyMC
{

class RunAction: public G4UserRunAction
{
  public:
    RunAction();
    ~RunAction() = default;

    void BeginOfRunAction(const G4Run *aRun) override;
    void EndOfRunAction(const G4Run *aRun) override;
};

};  // namespace ToyMC

#endif
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
