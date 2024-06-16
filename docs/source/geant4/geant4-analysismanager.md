# ファイル出力したい（``G4VAnalysisManager``）

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
am->CreateH1("name1", "title", xbins, xmin, xmax);  // h1 Id = 0
am->CreateH1("name2", "title", xbins, xmin, xmax);  // h1 Id = 1

// 2Dヒストグラム
am->CreateH2("name3", "title", xbins, xmin, xmax, ybins, ymin, ymax);  // h2 Id = 0
am->CreateH2("name4", "title", xbins, xmin, xmax, ybins, ymin, ymax);  // h2 Id = 1
```

``CreateH1``、``CreateH2``、``CreateH3``でヒストグラムを準備できます。

### ヒストグラムIDを取得したい（``GetH1Id`` / ``GetH2Id`` / ``GetH3Id``）

```cpp
// ヒストグラムのIDを取得
G4int id1 = am->GetH1Id("name1");
G4int id2 = am->GetH1Id("name2");
G4int id3 = am->GetH2Id("name3");
G4int id4 = am->GetH2Id("name4");
```

ヒストグラムを作成したときの名前を使って、ヒストグラムのIDを取得できます。
``EventAction``クラスで、ヒストグラムに値をフィルするときに利用できます。

### ヒストグラムにフィルしたい（``FillH1`` / ``FillH2`` / ``FillH3``）

```cpp
am->FillH1(id, value, weight);
am->FillH2(id, xvalue, yvalue, weight);
am->FillH3(id, xvalue, yvalue, zvalue, weight);
```

ヒストグラムIDを指定して値をフィルできます。

:::{note}

このメソッドは基本的に``EventAction``クラスで使うメソッドです。
``RunAction``クラスで使うことはないと思います。

:::

### ヒストグラムを確認したい（``GetH1`` / ``GetH2`` / ``GetH3``）

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

``CreateNtuple``でNtupleを作成し
``CreateNtupleDColumn``でカラムを作成します。
``FinishNtuple``することで複数のNtupleを作成できます。

## AnalysisManagerを使いたくない

``G4AnalysisManager``を使わなくてもファイルに出力できます。
その場合、C++の標準ライブラリを使い、
ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使います。

## リファレンス

- [G4AnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)
- [G4UserRunAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserRunAction.html)
