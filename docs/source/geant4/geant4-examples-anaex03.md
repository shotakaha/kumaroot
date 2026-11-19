# AnaEx03したい（`extended/analysis/AnaEx03/`）

Geant4 11.1で追加された`/analysis`コマンドのデモです。
ヒストグラムやntupleの作成、ファイルの管理を、C++ではなくマクロで操作できます。
詳しくは[G4AnalysisManager](geant4-analysismanager)を参照してください。

## ビルドしたい

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/extended/analysis/AnaEx03
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/AnaEx03

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する（マクロは位置引数で指定する）
$ cd build
$ ./AnaEx03 AnaEx03.in

// クリーンする
$ cd $G4WORK/AnaEx03
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`AnaEx03`という実行ファイルを作成します。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

実行すると、次のように出力ファイルが書き込まれ、閉じられます。

```console
... write file : e-.root - done
... close file : e-.root - done
... write file : proton.root - done
... close file : proton.root - done
```

## マクロの流れを確認したい

メインのマクロは`AnaEx03.in`です。
電子（`e-`）と陽子（`proton`）を、それぞれ別のファイルに保存します。

| ファイル | 入射粒子とエネルギー | イベント数 |
| --- | --- | --- |
| `e-` | 電子、100 MeV | 10 |
| `e-` | 電子、200 MeV | 20 |
| `e-` | 電子、300 MeV | 30 |
| `proton` | 陽子、400 MeV | 40 |
| `proton` | 陽子、500 MeV | 50 |

`/run/beamOn`の1回ごとに、1つのランになります。
ランが終わるたびに、`/analysis/write`で書き出し、`/analysis/reset`で初期化しています。

## 出力形式を変えたい

保存形式は、`AnaEx03.in`を読み込むラッパーのマクロで切り替えます。
ラッパーは、`/control/alias`で`defaultFileType`を設定してから、`AnaEx03.in`を実行します。

```console
// ROOT形式（既定）
$ ./AnaEx03 AnaEx03-root.in
e-.root
proton.root

// XML形式
$ ./AnaEx03 AnaEx03-xml.in
e-_nt*.xml
proton-_nt*.xml

// CSV形式
$ ./AnaEx03 AnaEx03-csv.in
./histo/e-_*.csv
./histo/proton_*.csv
./ntuple/e-_*.csv
./ntuple/proton_*.csv

// HDF5形式（失敗する）
$ ./AnaEx03 AnaEx03-hdf5.in
```

- ROOT形式とXML形式は、カレントディレクトリにファイルが作られました。
- CSV形式は、`histo/`と`ntuple/`のサブディレクトリにファイルが作られました。
- HDF5形式は、今回使ったGeant4のビルドでHDF5オプションが有効になっていなかったため、失敗しました。

:::{note}

`main()`は、マクロを読み込む前に`defaultFileType`を`root`に設定します。
そのため、`AnaEx03.in`を直接実行すると、ROOT形式で保存されます。

:::

## ファイルを開いて閉じたい（`/analysis/openFile`、`/analysis/closeFile`）

ファイルの開け閉めも、マクロで指定できます。
同じファイルに、ランを何回かに分けて書き込むこともできます。

```cfg
/analysis/openFile e-
/gun/particle e-
/gun/energy 100 MeV
/run/beamOn 10
/analysis/write
/analysis/reset
/gun/energy 200 MeV
/run/beamOn 20
/analysis/write
/analysis/reset
...
/analysis/closeFile
```

C++で`OpenFile()`、`Write()`、`CloseFile()`を呼ぶ代わりに、マクロでこれらを操作しています。

## ヒストグラムを途中で作り直したい・削除したい（`/analysis/h1/`）

ヒストグラムは、マクロの途中で作成や削除ができます。
ここでは、ランの途中で、新しいヒストグラムを作っています。

```cfg
/analysis/h1/delete 1
/analysis/h1/delete 3 true
/run/beamOn 20
/analysis/write
/analysis/reset
/gun/energy 300 MeV
/analysis/h1/create "EGap2" "Edep in gap (MeV) 2" 10 0. 100.
/analysis/h1/create "LGap2" "trackL in gap (mm) 2" 10 0. 500.
/run/beamOn 30
```

## ヒストグラムとntupleを作りたい（`RunAction`）

ヒストグラムとntupleは、`RunAction`のコンストラクタで作成します。
イベントごとの値は、`EventAction`から埋めます。

```cpp
// AnaEx03::RunAction::RunAction()（一部）
G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
analysisManager->SetDefaultFileType("root");

// ヒストグラムの番号は、0から自動的に振られる
analysisManager->CreateH1("EAbs", "Edep in absorber (MeV)", 100, 0., 800 * MeV);
analysisManager->CreateH1("EGap", "Edep in gap (MeV)", 100, 0., 100 * MeV);
analysisManager->CreateH1("LAbs", "trackL in absorber (mm)", 100, 0., 1 * m);

analysisManager->CreateNtuple("Ntuple1", "Edep");
analysisManager->CreateNtupleDColumn("Eabs");  // column Id = 0
analysisManager->CreateNtupleDColumn("Egap");  // column Id = 1
```

## 統計を表示したい（`/AnaEx03/runAction/printStatistic`）

`RunAction`は、`G4GenericMessenger`で、マクロから呼べるコマンドを用意しています。
`AnaEx03.in`では、各ランの後に`printStatistic`を実行しています。

```cpp
// AnaEx03::RunAction（一部）
fMessenger = new G4GenericMessenger(this, "/AnaEx03/runAction/", "Run action commands");

auto& printStatisticCmd = fMessenger->DeclareMethod("printStatistic", &RunAction::PrintStatistic, /* ... */);
printStatisticCmd.SetToBeBroadcasted(false);
```

## リファレンス

- [Example AnaEx03](https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/ExampleAnaEx03.html)
