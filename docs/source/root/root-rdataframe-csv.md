# CSVファイルを読み込みたい（`ROOT::RDF::FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"

auto df = ROOT::RDF::FromCSV("data.csv");
auto cols = df.GetColumnNames();
auto hist = df.Histo1D({"h", "Data", 100, 0, 100}, "column_name");
```

`ROOT::RDF::FromCSV`を使用して、CSV形式のファイルをRDataFrameで読み込みます。
自動的に列名と列の型が推論され、すぐにデータ分析を開始できます。

```python
import ROOT

df = ROOT.RDF.FromCSV("data.csv")
cols = df.GetColumnNames()
hist = df.Histo1D(("h", "Data", 100, 0, 100), "column_name")
```

## メソッドのシグネチャ

```cpp
ROOT::RDataFrame ROOT::RDF::FromCSV(
    std::string_view fileName,
    bool readHeaders = true,
    char delimiter = ',',
    Long64_t linesChunkSize = -1LL,
    std::unordered_map<std::string, char> &&colTypes = {}
)
```

### 引数と戻り値

**引数**:

- **fileName** - CSVファイルのパス
- **readHeaders** - 最初の行をヘッダー（列名）として扱うか（デフォルト: `true`）
- **delimiter** - フィールド区切り文字（デフォルト: `','`）
- **linesChunkSize** - 処理チャンクサイズ（デフォルト: `-1`で自動）
- **colTypes** - 列の型を明示指定（空の場合は自動推論）

**戻り値**:

- RDataFrameオブジェクト

## ヘッダー付きCSVを読み込みたい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"
#include <iostream>

auto df = ROOT::RDF::FromCSV("measurements.csv");
auto filtered = df.Filter("temperature > 20.0 && humidity < 80.0");
auto mean = filtered.Mean("temperature");

std::cout << *mean << std::endl;
```

CSVファイルの最初の行にカラム名が含まれている場合、`readHeaders=true`（デフォルト）で読み込みます。

CSVファイルの例：

```csv
temperature,humidity,timestamp
20.5,65,2025-01-01T10:00:00
21.3,68,2025-01-01T10:15:00
19.8,72,2025-01-01T10:30:00
```

```python
import ROOT

df = ROOT.RDF.FromCSV("measurements.csv")
filtered = df.Filter("temperature > 20.0 and humidity < 80.0")
print(filtered.Mean("temperature").GetValue())
```

## ヘッダーなしCSVを読み込みたい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"

auto df = ROOT::RDF::FromCSV("plot_data.csv", false);
auto graph = df.Graph("Col0", "Col1");
graph->SetMarkerStyle(20);
graph->Draw("AP");
```

CSVファイルに列名がない場合は、`readHeaders=false`を指定します。
列は自動的に`Col0`、`Col1`、`Col2`……という名前で参照できます。

CSVファイルの例：

```csv
1.0,2.5
2.0,4.2
3.0,6.1
```

```python
import ROOT

df = ROOT.RDF.FromCSV("plot_data.csv", False)
print(df.GetColumnNames())
g = df.Graph("Col0", "Col1")
g.Draw("AP")
```

## 区切り文字を変更したい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"

// タブ区切り（TSV）
auto df_tsv = ROOT::RDF::FromCSV("data.tsv", true, '\t');

// セミコロン区切り
auto df_semi = ROOT::RDF::FromCSV("data.csv", true, ';');

// パイプ区切り
auto df_pipe = ROOT::RDF::FromCSV("data.txt", true, '|');
```

CSVファイルがタブやセミコロンなど異なる区切り文字を使用している場合、`delimiter`パラメーターで指定します。

## カラムの型を明示的に指定したい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"
#include <unordered_map>

auto df = ROOT::RDF::FromCSV(
    "sensor_data.csv",
    false,  // ヘッダーなし
    ',',
    -1,
    {{"Col0", 'D'}, {"Col1", 'D'}, {"Col2", 'L'}, {"Col3", 'T'}}
);

auto sum = df.Sum<Double_t>("Col0");
```

CSVファイルを読み込む際、デフォルトでは列の型が最初のデータ行から自動推論されます。
型の曖昧さがある場合や、明確な型指定が必要な場合は`colTypes`パラメーターで指定します。

### 型文字の一覧

- **`'L'`** - `Long64_t`（64-bit整数）
- **`'D'`** - `Double_t`（倍精度浮動小数点）
- **`'O'`** - `bool`（ブール値）
- **`'T'`** - `std::string`（文字列）

```python
import ROOT

df = ROOT.RDF.FromCSV(
    "sensor_data.csv",
    False,
    ",",
    -1,
    {
        "Col0": 0x44,  # Double（'D'の ASCII コード）
        "Col1": 0x44,  # Double
        "Col2": 0x4c,  # Long64_t（'L'の ASCII コード）
        "Col3": 0x54   # String（'T'の ASCII コード）
    }
)
```

## フィルタリングと新規カラムを定義をしたい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"

auto df = ROOT::RDF::FromCSV("physics_data.csv");

auto filtered = df.Filter("charge1 * charge2 == -1");
auto with_mass = filtered.Define(
    "invariant_mass",
    "sqrt(pow(E1 + E2, 2) - pow(px1 + px2, 2) - pow(py1 + py2, 2) - pow(pz1 + pz2, 2))"
);

auto mass_window = with_mass.Filter("invariant_mass > 80 && invariant_mass < 100");
auto hist = mass_window.Histo1D({"h", "Mass", 50, 80, 100}, "invariant_mass");
hist->Draw();
```

RDataFrameを使用して、CSVデータに対して複雑なフィルタリングと列の演算を実行できます。

```python
import ROOT

df = ROOT.RDF.FromCSV("physics_data.csv")

filtered = df.Filter("charge1 * charge2 == -1")
with_mass = filtered.Define(
    "invariant_mass",
    "sqrt(pow(E1 + E2, 2) - pow(px1 + px2, 2) - pow(py1 + py2, 2) - pow(pz1 + pz2, 2))"
)
mass_window = with_mass.Filter("invariant_mass > 80 and invariant_mass < 100")
hist = mass_window.Histo1D(("h", "Mass", 50, 80, 100), "invariant_mass")
hist.Draw()
```

## CSV を ROOT ファイルに変換したい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"

auto df = ROOT::RDF::FromCSV("input.csv");
df.Snapshot("tree", "output.root");
```

CSVファイルを一度だけ変換してROOT形式に保存することで、繰り返し読み込み時のパフォーマンスが向上します。

```python
import ROOT

df = ROOT.RDF.FromCSV("input.csv")
df.Snapshot("tree", "output.root")

# 次回以降は高速で読み込める
df2 = ROOT.RDataFrame("tree", "output.root")
```

## 複数列の統計情報を取得したい（`FromCSV`）

```cpp
#include "ROOT/RDataFrame.hxx"
#include <iostream>

auto df = ROOT::RDF::FromCSV("data.csv");

auto mean_x = df.Mean("x");
auto mean_y = df.Mean("y");
auto std_x = df.StdDev("x");
auto std_y = df.StdDev("y");

std::cout << "X: " << *mean_x << " ± " << *std_x << std::endl;
std::cout << "Y: " << *mean_y << " ± " << *std_y << std::endl;
```

RDataFrameを使用して、複数の列について同時に統計情報を取得できます。

```python
import ROOT

df = ROOT.RDF.FromCSV("data.csv")

print(f"X mean: {df.Mean('x').GetValue():.3f}")
print(f"X std: {df.StdDev('x').GetValue():.3f}")
print(f"Y mean: {df.Mean('y').GetValue():.3f}")
print(f"Y std: {df.StdDev('y').GetValue():.3f}")
```

## CSVファイルの形式要件

FromCSVで読み込めるCSVファイルの形式：

```csv
# コメント行（# で始まる）
col1,col2,col3
10,20,text1
15,25,text2
20,30,text3

25,35,text4
```

### 形式の規則

- **コメント行**：`#`で始まる行はスキップされます
- **空行**：自動的にスキップされます
- **フィールド数**：すべての行で同じ列数である必要があります
- **クォート処理**：区切り文字を含むフィールドは`"`でクォートします
- **エスケープ**：クォート内のクォートは二重化（`"He said ""Hello"""`）

### 注意事項

- スペースは有効です（前後のスペースは削除されません）
- 埋め込まれた改行はサポートされていません
- 先頭ゼロ（`00123`）は数値と推論される可能性があります。ZIPコードの場合は型を明示指定してください

## 制限事項

### メモリ制限

FromCSVはCSVファイル全体をメモリに読み込みます。
非常に大きなファイルの場合は、CSVをROOTフォーマットに変換して保存することをオススメします。

### 型推論の落とし穴

型は最初の「データ行」（ヘッダーではなく）から推論されます。
先頭ゼロを含む値（`00123`）の場合、整数型と推論される可能性があります。
このような場合は、`colTypes`パラメーターで型を明示指定してください。

## 関連するメソッド

- [RDataFrame の基本](./root-rdataframe.md)
- [TTree::ReadFile](./root-ttree.md)

## 参考資料

- [ROOT::RDataFrame クラスリファレンス](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
- [ROOT::RDF::RCsvDS クラスリファレンス](https://root.cern/doc/master/classROOT_1_1RDF_1_1RCsvDS.html)
- [RDataFrame チュートリアル](https://root.cern.ch/doc/master/group__tutorial__dataframe.html)
- [CSV データソースチュートリアル](https://root.cern/doc/v632/df014__CSVDataSource_8C.html)
