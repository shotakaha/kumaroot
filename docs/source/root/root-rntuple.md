# RNTupleしたい

```cpp
#include <ROOT/RNTuple.hxx>
#include <memory>

using RNTupleWriter = ROOT::Experimental::RNTupleWriter;
using RNTupleReader = ROOT::Experimental::RNTupleReader;

// データを書き込む
auto writer = RNTupleWriter::Recreate("ntuple", "output.root");
auto pt = writer->MakeField<float>("pt");
auto eta = writer->MakeField<float>("eta");

for (int i = 0; i < 100; i++) {
    *pt = 10.0 + i * 0.1;
    *eta = -2.5 + i * 0.05;
    writer->Fill();
}
writer->Commit();
```

`RNTuple`は`TTree`の後継となるクラスです。ただし、互換性はありません。

`TTree`は1995年にROOTがリリースされたときから、フレームワークの主要クラスでした。しかし、30年前と比べて、データ解析周辺の環境は様変わりしています。それに対応するために、これまでの高エネルギー物理学での知見を活かしつつ、新しいクラスの開発が行われています。

```python
import ROOT
from ROOT.Experimental import RNTupleWriter, RNTupleReader

# データを書き込む
writer = RNTupleWriter.Recreate("ntuple", "output.root")
pt = writer.MakeField("pt", "float")
eta = writer.MakeField("eta", "float")

for i in range(100):
    pt[0] = 10.0 + i * 0.1
    eta[0] = -2.5 + i * 0.05
    writer.Fill()
writer.Commit()
```

## RNTupleについて

### TTreeとの比較

| 項目 | TTree | RNTuple |
|------|-------|---------|
| リリース年 | 1995年 | 2018年（実験的） |
| バージョン | 安定 | 実験的 |
| パフォーマンス | 良好 | 最適化済み |
| 互換性 | あり | なし |
| 圧縮 | オプション | デフォルト |
| 並列読み書き | 限定的 | 高速 |

## データを書き込みたい（`RNTupleWriter::Recreate`）

```cpp
#include <ROOT/RNTuple.hxx>

using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

auto writer = RNTupleWriter::Recreate("ntuple", "data.root");
auto event_id = writer->MakeField<int>("event_id");
auto pt = writer->MakeField<float>("pt");
auto eta = writer->MakeField<float>("eta");

for (int i = 0; i < 1000; i++) {
    *event_id = i;
    *pt = 10.0 + i * 0.01;
    *eta = -2.5 + i * 0.005;
    writer->Fill();
}

writer->Commit();
```

`RNTupleWriter::Recreate()`でNTupleを新規作成します。フィールドを定義してから`Fill()`でデータを記録します。

## データを読み込みたい（`RNTupleReader::Open`）

```cpp
#include <ROOT/RNTuple.hxx>

using RNTupleReader = ROOT::Experimental::RNTupleReader;

auto reader = RNTupleReader::Open("ntuple", "data.root");
auto view = reader->GetView<int, float, float>({"event_id", "pt", "eta"});

for (auto entry : view) {
    int event_id = std::get<0>(entry);
    float pt = std::get<1>(entry);
    float eta = std::get<2>(entry);
    std::cout << "Event: " << event_id << ", pt: " << pt << ", eta: " << eta << std::endl;
}
```

`RNTupleReader::Open()`でNTupleから読み込みます。`GetView()`でフィールドを指定してアクセスできます。

## 複数のフィールドを定義したい（`MakeField`）

```cpp
#include <ROOT/RNTuple.hxx>

using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

auto writer = RNTupleWriter::Recreate("events", "output.root");

auto run_number = writer->MakeField<int>("run");
auto event_number = writer->MakeField<int>("event");
auto energy = writer->MakeField<double>("energy");
auto charge = writer->MakeField<int>("charge");

for (int i = 0; i < 100; i++) {
    *run_number = 2025;
    *event_number = i;
    *energy = 100.0 + i;
    *charge = (i % 2 == 0) ? 1 : -1;
    writer->Fill();
}

writer->Commit();
```

各データ型に応じて`MakeField<T>()`でフィールドを定義します。複数のフィールドを定義して、`Fill()`で全フィールドを同時に記録します。

## 参考情報

### RNTupleの特徴

- **高速な読み書き**: 最適化されたバイナリ形式
- **デフォルト圧縮**: ディスク容量を効率的に利用
- **スケーラビリティ**: 大規模データセットに対応
- **モダン設計**: 並列処理に最適化

### 実験的ステータス

RNTupleはまだ実験的なクラスです。本番環境での使用は、ROOT開発チームの最新情報を確認してから判断してください。

## 関連メソッド

- [TTree::Branch](./root-ttree-branch.md) - TTreeでのブランチ作成
- [TTree::Fill](./root-ttree-fill.md) - TTreeでのデータ追加
- [TTree::Write](./root-ttree-write.md) - TTreeでのファイル保存

## 参考リンク

- [ROOT RNTuple Documentation](https://root.cern/doc/master/namespacesROOT_1_1Experimental.html)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
- [ROOT Release Notes](https://root.cern/release-notes/)
