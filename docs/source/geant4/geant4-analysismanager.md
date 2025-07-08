# 解析マネージャーしたい（`G4VAnalysisManager`）

```cpp
auto am = G4AnalysisManager::Instance();
```

`G4AnalysisManager`は、Geant4のシミュレーションで得られた結果を管理するインスタンスです。
このクラスのおかげでROOT形式、CSV形式、XML形式への出力が標準機能として利用できます。

`G4AnalysisManager::Instance`は、
シングルトンとして設計されており、マルチスレッド環境にも対応しています。

:::{note}

`G4AnalysisManager`は Geant v10.0で導入されました。
このクラスは、抽象基底クラスである`G4VAnalysisManager`を継承した具体クラスであり、
ユーザーは通常この`G4AnalysisManager`を通じてヒストグラムやNtupleを操作します。

:::

## ラン情報を記録したい

```cpp
// include/RunAction.hh

#ifndef RUN_ACTION_HH
#define RUN_ACTION_HH

#include "G4UserRunAction.hh"
#include "G4String.hh"
#include "globals.hh"

class RunAction : public G4UserRunAction {
  public:
    RunAction();
    virtual ~RunAction();

    virtual void BeginOfRunAction(const G4Run* aRun) override;
    virtual void EndOfRunAction(const G4Run* aRun) override;

  private:
    // 必要に応じてメンバー変数を追加
    // - 値が一定（immutable）の変数
    // - 複数のメンバー関数で共有したい変数
    G4int fRunId = -1;
    G4double fStartTime = 0;
    G4String fSeedFileName;
};

#endif // RUN_ACTION_HH
```

ラン情報を記録するために、
`G4UserRunAction`を継承したユーザー定義の`RunAction`クラスを作成します。

このクラスの
コンストラクターに`G4AnalysisManager`の初期化
`BeginOfRunAction`にファイルを開く操作、
`EndOfRunAction`にデータ保存とファイルに書き出す操作を実装します。

### 初期化したい（`RunAction::RunAction`）

```cpp
void MyRunAction::RunAction() {
  auto am = G4AnalysisManager::Instance();

  // ログ詳細レベル（0-4）
  am->SetVerboseLevel(1);
  // 出力ファイル名
  am->SetFileName("my_output");
  // 出力形式（"root", "csv", "xml"）
  am->SetDefaultFileType("root");
  // ヒストグラム用ディレクトリ
  am->SetHistDirectoryName("hist");
  am->CreateH1("h1", "Edep in detector", 100, 0., 10.);

  // Ntuple用ディレクトリ
  am->SetNtupleDirectoryName("ntuple");
  am->SetNtupleMerging(true);  // マルチスレッド対応

  // ラン情報用Ntuple
  am->CreateNtuple("runinfo", "Run Metadata");
  am->CreateNtupleIColumn("runId");
  am->CreateNtupleIColumn("nEvents");
  am->CreateNtupleDColumn("startTime");  // unixtime
  am->CreateNtupleDColumn("endTime");
  am->CreateNtupleSColumn("fileName");
  am->CreateNtupleSColumn("seedFile");
  am->FinishNtuple();
}
```

出力するファイル名や形式、
必要なヒストグラムやNtupleの定義は、
RunActionクラスのコンストラクターの中で初期化します。

### ラン開始時の処理（`RunAction::BeginOfRunAction`）

```cpp
void MyRunAction::BeginOfRunAction(const G4Run* aRun) {
  fStartTime = std::time(nullptr);
  fRunId = run->GetRunID();

  // 出力ファイルを開く
  auto am = G4AnalysisManager::Instance();
  am->OpenFile();  // 出力ファイルを開く

    //
  fSeedFileName = "seed_run" + std::to_string(runId) + ".rndm";
  CLHEP::HepRandom::saveEngineStatus(seedFileName);

}
```

シミュレーションがはじまると、`BeginOfRunAction`が呼ばれます。
出力ファイルを開く操作（`OpenFile`）はここで実行します。

### ラン終了時の処理（`RunAction::EndOfRunAction`）

```cpp
void MyRunAction::EndOfRunAction(const G4Run* aRun) {
  G4int nEvents = aRun->GetNumberOfEvents();
  G4double endTime = std::time(nullptr);
  auto am = G4AnalysisManager::Instance();

  // 出力ファイル名を取得
  G4String outputFileName = am->GetFileName();

  // 保存
  am->FillNtupleIColumn(0, fRunId);
  am->FillNtupleIColumn(1, nEvents);
  am->FillNtupleDColumn(2, fStartTime);
  am->FillNtupleDColumn(3, endTime);
  am->FillNtupleSColumn(4, outputFileName);
  am->FillNtupleSColumn(5, fSeedFileName);
  am->AddNtupleRow();

  am->Write();
  am->CloseFile()
}
```

シミュレーションの終了時に`EndOfRunAction`が呼ばれます。
出力したファイルに書き込む操作（`Write`）と、
閉じる操作（`CloseFile`）は、
この中で実行します。

マルチスレッド環境で実行した場合、
各スレッドで記録されたデータは、ランの終了時に
自動的にマスターで集約され、
ひとつのファイルにまとめて保存されます。

:::{note}

`CloseFile`だけでは結果が保存されません。
必ず`Write`を先に呼ぶ必要があります。

:::

## イベント情報したい

```cpp
// include/EventAction.hh

#ifndef EVENT_ACTION_HH
#define EVENT_ACTION_HH

#include "G4UserEventAction.hh"
#include "G4Event.hh"
#include "globals.hh"

class EventAction : public G4UserEventAction {
  public:
    EventAction();
    virtual ~EventAction();

    virtual void BeginOfEventAction(const G4Event* aEvent) override;
    virtual void EndOfEventAction(const G4Event* aEvent) override;

  private:
    G4int fEventId = -1;
    G4double fEnergyDeposit = 0;
};

#endif // EVENT_ACTION_HH
```

### イベント開始時の処理（`EventAction::BeginOfEventAction`）

```cpp
void EventAction::BeginOfEventAction(const G4Event* aEvent) {
  fEventId = event->GetEventID();
  fEnergyDeposit = 0;  // 初期化
}
```

```cpp
void EventAction::EndOfEventAction(const G4Event* aEvent) {
    auto am = G4AnalysisManager::Instance();
    am->FillNtupleIColumn(0, fEventId);
    am->FillNtupleDColumn(1, fEnergyDeposit);
    am->AddNtupleRow();
}
```

### イベント終了時の処理（`EventAction::EndOfEventAction`）

## ランアクションしたい

```cpp
void ActionInitialization::Build() const {
    SetUserAction(new MyRunAction{});
}
```

ユーザー定義した`MyRunAction`クラスは
`ActionInitialization`への登録が必要です。

## ファイル名を変更したい（``SetFileName``）

```cpp
auto am = G4AnalysisManager::Instance()
am->SetFileName("ファイル名.root");  // ROOT形式
am->SetFileName("ファイル名.csv");   // CSV形式
am->SetFileName("ファイル名");
```

ファイル名は拡張子をつけて設定できます。
拡張子がない場合は、``SetDefaultFileType``で指定した形式の拡張子が追加されます。

## ファイル形式を変更したい（``SetDefaultFileType``）

```cpp
auto am = G4AnalysisManager::Instance()
am->SetDefaultFileType("csv");  // CSV形式
am->SetDefaultFileType("root");  // ROOT形式
```

一般的なユーザーであればCSV形式で出力するとよいと思います。
CSV形式であれば、ユーザーが使い慣れているツールで解析できます。

HEP業界のユーザーであればROOT形式のほうが使いやすいと思います。
AnalysisManagerを使った付属サンプルのほとんどがROOTファイルで出力されるようになっています。

:::{seealso}

同様の設定はマクロコマンドでもできます。

```cfg
/analysis/setDefaultFileType csv
/analysis/setDefaultFileType root
```

:::

## サブディレクトリを作成したい（``SetHistoDirectoryName`` / ``SetNtupleDirectoryName``）

```cpp
am->SetHistoDirectoryName("histo");
am->SetNtupleDirectoryName("ntuple");
```

CSV形式のファイルを保存するディレクトリを設定できます。
ディレクトリはあらかじめ作成しておく必要があります。

## ヒストグラムを作成したい（``CreateH1`` / ``CreateH2`` / ``CreateH3``）

```cpp
auto am = G4AnalysisManager::Instance()
// 1Dヒストグラム
am->CreateH1(
    "name1",  // オブジェクト名
    "title",  // ヒストグラムのタイトル
    xbins,    // ビンの数
    xmin,     // ビンの最小値
    xmax      // ビンの最大値
);  // h1 Id = 0

am->CreateH1("name2", "title", xbins, xmin, xmax);  // h1 Id = 1

// 2Dヒストグラム
am->CreateH2("name3", "title", xbins, xmin, xmax, ybins, ymin, ymax);  // h2 Id = 0
am->CreateH2("name4", "title", xbins, xmin, xmax, ybins, ymin, ymax);  // h2 Id = 1
```

``CreateH1``、``CreateH2``、``CreateH3``でヒストグラムを準備できます。

## ヒストグラムのIDを取得したい（``GetH1Id`` / ``GetH2Id`` / ``GetH3Id``）

```cpp
// ヒストグラムのIDを取得
G4int id1 = am->GetH1Id("name1");
G4int id2 = am->GetH1Id("name2");
G4int id3 = am->GetH2Id("name3");
G4int id4 = am->GetH2Id("name4");
```

ヒストグラムを作成したときの名前を使って、ヒストグラムのIDを取得できます。
``EventAction``クラスで、ヒストグラムに値をフィルするときに利用できます。

## ヒストグラムにフィルしたい（``FillH1`` / ``FillH2`` / ``FillH3``）

```cpp
am->FillH1(id, value, weight);
am->FillH2(id, xvalue, yvalue, weight);
am->FillH3(id, xvalue, yvalue, zvalue, weight);
```

ヒストグラムIDを指定して値をフィルできます。

## ヒストグラムを確認したい（``GetH1`` / ``GetH2`` / ``GetH3``）

```cpp
auto h1 = am->GetH1(id);
G4String name = am->GetH1Name(id);

G4double mean = h1->mean();
G4double rms = h1->rms();
```

ヒストグラムIDを指定して、ヒストグラムを取得できます。
取得したヒストグラムを使って、平均値などを取得できます。

```cpp
G4int nH1s = am->GetNofH1s;
for ( G4int i=0; i<nH1s; ++i) {
    auto h1 = am->GetH1(i);
    if (h1 == nullptr) continue;
    G4String name = am->GetH1Name(i);
    G4cout << "Name: " << name << G4endl;
    G4cout << "Mean: " << h1->mean() << G4endl;
    G4cout << "Rms: " << h1->rms() << G4endl;
}
```

``GetNofH1``でヒストグラムの数が取得できます。
その数だけループして確認できます。

## Ntupleを作成したい（``CreateNtuple`` / ``CreateNtupleDColumn`` / ``FinishNtuple``）

```cpp
am->CreateNtuple("Ntuple1", "title1");  // ntuple Id = 0
am->CreateNtupleIColumn("name1");  // column Id = 0
am->CreateNtupleDColumn("name2");  // column Id = 1
am->FinishNtuple();

am->CreateNtuple("Ntuple2", "title2");  // ntuple Id = 1
am->CreateNtupleIColumn("name3");  // column Id = 0
am->CreateNtupleDColumn("name4");  // column Id = 1
am->FinishNtuple();
```

``CreateNtuple``でNtupleを作成します。
``CreateNtupleDColumn``や
``CreateNtupleIColumn``でカラムを定義します。
``FinishNtuple``でNtupleを閉じます。

これを繰り返すことで複数のNtupleを作成できます。

## AnalysisManagerを使いたくない

``G4AnalysisManager``を使わなくてもファイルに出力できます。
その場合、C++の標準ライブラリを使い、
ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使います。

[G4VAnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)を使って、ファイルに出力できます。
Geant4は独自のデータベース形式を持たない代わりに、
ユーザー自身がいろいろなフォーマットに出力できるようになっています。

ファイル操作（設定／開く／閉じる）はランごとに実行すればよいため、``RunAction``の中で動作を定義します。
ユーザーが編集する必要があるユーザーフック関数は以下の3箇所です。

1. ``RunAction::RunAction``:
``RunAction``クラスのコンストラクターで、ファイル名や出力形式を設定します。
また、データを保存する「箱の形」を用意します。
2. ``RunAction::BeginOfRunAction``:
ラン開始時にファイルを開きます。
3. ``RunAction::BeginOfRunAction``:
ラン終了時にデータを保存し、ファイルを閉じます。

以下は、付属サンプルB4dとB5から該当箇所を抜粋して、説明を追加してみました。

```cpp
// //////////////////////////////////////////////////
// include/RunAction.hh
// //////////////////////////////////////////////////

#include "G4UserRunAction.hh"
#include "G4Run.hh"

class RunAction : public G4UserRunAction
{
    public:
      RunAction();
      ~RunAction() override = default;

      void BeginOfRunAction(const G4Run* aRun) override;
      void EndOfRunAction(const G4Run* aRun) override;

    private:
      // （オプション）
      // EventAction* fEventAction = nullptr;
}
```

```cpp
// //////////////////////////////////////////////////
// src/RunAction.cc
// //////////////////////////////////////////////////

// RunActionのコンストラクタ（初期化）
RunAction::RunAction()
{
    // G4AnalysisManagerのインスタンスを作成する
    // このインスタンスはシングルトンになっている
    auto am = G4AnalysisManager::Instance();

    // 表示レベルを設定する（オプション）
    am->SetVerboseLevel(1);

    // ファイル名を設定する（オプション）
    // マクロファイルで変更可能
    am->SetFileName("ファイル名");

    // ファイル形式を指定する（オプション）
    // ファイル名に拡張子がない場合はROOT形式になる
    am->SetDefaultFileType("csv");
    // am->SetDefaultFileType("root");

    // /////////////////////////
    // ユーザー独自の設定
    // 目的に合わせて自分で考える部分
    ///////////////////////////

    // 1Dヒストグラムを作成する
    // am->CreateH1("name", "title", nbins, xmin, xmax);
    am->CreateH1("Chamber1", "Drift Chamber 1 # Hits", 50, 0., 50); // h1 Id = 0
    am->CreateH1("Chamber2", "Drift Chamber 2 # Hits", 50, 0., 50); // h1 Id = 2

    // 2Dヒストグラムを作成する
    // am->CreateH2("name", "title", nxbins, xmin, xmax, nybins, ymin, ymax);
    am->CreateH2("Chamber1 XY", "Drift Chamber 1 X vx Y", 50, -1000., 1000., 50, -300., 300.);  // h2 Id = 0
    am->CreateH2("Chamber2 XY", "Drift Chamber 2 X vx Y", 50, -1000., 1000., 50, -300., 300.);  // h2 Id = 1

    // Ntupleを作成する
    // am->CreateNtuple("name", "title);
    am->CreateNtuple("B5", "Hits");
    // am->CreateNtupleIColumn("name");
    am->CreateNtupleIColumn("Dc1Hits");  // column Id = 0
    am->CreateNtupleIColumn("Dc2Hits");  // column Id = 1
    // am->CreateNtupleDColumn("name");
    am->CreateNtupleDColumn("ECEnergy");  // column Id = 2
    am->CreateNtupleDColumn("HCEnergy");  // column Id = 3
    am->CreateNtupleDColumn("Time1");     // column Id = 4
    am->CreateNtupleDColumn("Time2");     // column Id = 5
    // am->CreateNtupleDColumn("name", vector);
    am->CreateNtupleDcolumn("ECEnergyVector", fEventAction->GetEmCalEdep());  // column Id = 6
    am->CreateNtupleDcolumn("HCEnergyVector", fEventAction->GetHadCalEdep());  // column Id = 7
    am->FinishNtuple();

    // Ntupleのファイル名を設定する
    // am->SetNtupleFileName(id, "fileName");
    am->SetNtupleFileName(0, "B5ntuple");
}
```

```cpp
// //////////////////////////////////////////////////
// src/RunAction.cc
// //////////////////////////////////////////////////

// ラン開始時の処理
void RunAction::BeginOfRunAction(const G4Run* aRun)
{
    // ラン番号を表示する
    G4cout << "Run started: " << run->GetRunID() << G4endl;

    // AnalysisManagerのインスタンスを取得する
    // AMがシングルトンなので、作成済みのインスタンスが取得できる
    auto am = G4AnalysisManager::Instance()

    // 前のランの結果をリセットする
    // 付属サンプルB5は、ラン終了時に自動リセットせず、
    // ラン開始時にリセットしている
    am->Reset();

    // ファイルを開く
    // ファイル名はコンストラクタで設定済み
    am->OpenFile();
    G4cout << "File opened: " << am->GetFileName() << G4endl;
}
```

```cpp
// //////////////////////////////////////////////////
// src/RunAction.cc
// //////////////////////////////////////////////////

// ラン終了時の処理
void RunAction::EndOfRunAction(const G4Run* aRun)
{
    // AnalysisManagerのインスタンスを取得する
    // AMがシングルトンなので、作成済みのインスタンスが取得できる
    auto am = G4AnalysisManager::Instance()

    // 取得したデータをファイルに出力する
    am->Write();

    // ファイルを閉じる
    am->CloseFile(false);
    // サンプルB5では、ラン終了時にデータ（ヒストグラム）を
    // 保持したままにしている
    // デフォルトは自動リセットされる
    // am->CloseFile(reset=true);
    G4cout << "File closed: " << am->GetFileName() << G4endl;
}
```

:::{hint}

データ取得はイベントごとやステップごとに値を取得するため、
``EventAction``クラスや``SteppingAction``クラスで定義します。

:::

## リファレンス

- [G4AnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)
- [G4UserRunAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserRunAction.html)
- [examples/extended/analysis/AnaEx03](https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/ExampleAnaEx03.html)
