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

以下は、付属サンプルB5の該当箇所を抜粋して、説明を追加してみました。

```cpp
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
// ラン開始時の処理
void RunAction::BeginOfRunAction()
{
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
}
```

```cpp
// ラン終了時の処理
void RunAction::EndOfRunAction()
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
}
```


このときに、データを保存する「箱の形」も``CreateH1``や``CreateNtuple``で作成します。

- ``RunAction::RunAction`` - コンストラクター
- ``RunAction::BeginOfRunAction`` - ラン開始時の動作
- ``RunAction::EndOfRunAction`` - ラン終了時の動作



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

## AnalysisManagerを使いたくない

``G4AnalysisManager``を使わなくてもファイルに出力できます。
その場合、C++の標準ライブラリを使い、
ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使います。


## リファレンス

- [G4AnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)
