# ファイル出力したい（``G4VAnalysisManager``）

```cpp
G4AnalysisManager *analysis_manager = new G4AnalysisManager::Instance();

// RunAction::BeginOfRunActionで設定する
analysis_manager->SetDefaultFileType("csv");
analysis_manager->SetFileName("ファイル名");
analysis_manager->OpenFile();

// EventActionで設定する
analysis_manager->Write();

// RunAction::EndOfRunActionで設定する
analysis_manager->Close();
```

Geant4は独自のデータベース形式を持っていません。
その代わりに、ユーザー自身がいろいろなフォーマットに出力できるように[G4VAnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)というインターフェース的なクラスが用意されています。

## CSV形式にしたい

```cfg
/analysis/setDefaultFileType csv
```

```cpp
analysis_manager->SetDefaultFileType("csv");
```

一般的なユーザーであればCSV形式で出力するとよいと思います。
CSV形式であれば、ユーザーが使い慣れているツールで解析できます。

## ROOT形式にしたい

```cfg
/analysis/setDefaultFileType root
```

```cpp
analysis_manager->SetDefaultFileType("root");
```

HEP業界のユーザーであればROOT形式のほうが使いやすいと思います。
付属サンプルROOTファイルで出力されるようになっています。

## AnalysisManagerを使いたくない

ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使って、
ファイルに出力すればOKだそうです。
