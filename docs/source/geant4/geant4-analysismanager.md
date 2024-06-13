# ファイル出力したい（``G4VAnalysisManager``）

```cpp
G4AnalysisManager *am = new G4AnalysisManager::Instance();

// RunAction::BeginOfRunActionで設定する
am->SetDefaultFileType("csv");
am->SetFileName("ファイル名");
am->OpenFile();

// EventActionで設定する
am->Write();

// RunAction::EndOfRunActionで設定する
am->CloseFile();
```

[G4VAnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)を使って、ファイルに出力できます。

Geant4は独自のデータベース形式を持たない代わりに、
ユーザー自身がいろいろなフォーマットに出力できるようになっています。

## CSV形式にしたい

```cpp
am->SetDefaultFileType("csv");
```

一般的なユーザーであればCSV形式で出力するとよいと思います。
CSV形式であれば、ユーザーが使い慣れているツールで解析できます。

```cfg
/analysis/setDefaultFileType csv
```

同様の設定はマクロコマンドでもできます。

## ROOT形式にしたい

```cpp
am->SetDefaultFileType("root");
```

HEP業界のユーザーであればROOT形式のほうが使いやすいと思います。
付属サンプルROOTファイルで出力されるようになっています。

```cfg
/analysis/setDefaultFileType root
```

同様の設定はマクロコマンドでもできます。

## AnalysisManagerを使いたくない

``G4AnalysisManager``を使わなくてもファイルに出力できます。
その場合、C++の標準ライブラリを使い、
ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使います。
