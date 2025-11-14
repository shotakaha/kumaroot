# 散布図を作りたい（`TGraph`）

```cpp
#include <TGraph.h>

// 散布図を作成
TGraph *g = new TGraph();
g->SetPoint(0, 1.0, 2.0);
g->SetPoint(1, 2.0, 4.0);
g->SetPoint(2, 3.0, 6.0);
g->Draw("AP");
```

`TGraph`は、XY平面に点をプロットして散布図を作成するクラスです。
方眼紙に点を順番に打つようなグラフを作成したい場合に活用します。
ヒストグラムと異なり、生データのままプロットするため、ビニング（ビン化）は行いません。

```python
from ROOT import TGraph

# 散布図を作成
g = TGraph()
g.SetPoint(0, 1.0, 2.0)
g.SetPoint(1, 2.0, 4.0)
g.SetPoint(2, 3.0, 6.0)
g.Draw("AP")
```

## コンストラクターのシグネチャ

```cpp
// 空のグラフを作成
TGraph();

// データ配列からグラフを作成
TGraph(Int_t n, Double_t *x, Double_t *y);

// ファイルから読み込み
TGraph(const char *filename);
```

### デフォルトコンストラクター（引数なし）

- 点を持たないグラフを作成
- `SetPoint()`を使って点を追加

### 配列コンストラクター

- `n`：点の個数
- `x`：X座標の配列
- `y`：Y座標の配列

### ファイル読み込みコンストラクター

- ファイルから直接グラフを読み込み

## 点を追加したい

```cpp
#include <TGraph.h>

TGraph *g = new TGraph();

// 単一の点を追加
g->SetPoint(0, 1.0, 2.0);
g->SetPoint(1, 2.0, 4.0);
g->SetPoint(2, 3.0, 6.0);

// GetN()で現在の点の数を取得して追加
g->SetPoint(g->GetN(), 4.0, 8.0);

g->Draw("AP");
```

`SetPoint()`メソッドで点を追加できます。第1引数は点のインデックス（0から始まる）、第2、第3引数はX、Y座標です。

`GetN()`を使うと現在のグラフに含まれる点の個数を取得できるため、常に最後に点を追加する場合に便利です。

## 配列からグラフを作成したい

```cpp
#include <TGraph.h>

const Int_t n = 5;
Double_t x[n] = {1, 2, 3, 4, 5};
Double_t y[n] = {2, 4, 6, 8, 10};

// 配列からグラフを作成
TGraph *g = new TGraph(n, x, y);

g->Draw("AP");
```

配列から直接グラフを作成することで、効率的にデータをプロットできます。

## 描画オプション

`Draw()`メソッドで異なる描画方法を指定できます。

| オプション | 説明 |
|---|---|
| `"A"` | 軸を描画（必ず含める） |
| `"P"` | 点を描画 |
| `"L"` | 直線で連結 |
| `"C"` | 曲線で連結 |
| `"*"` | アスタリスク記号で点を表示 |

```cpp
#include <TGraph.h>

TGraph *g = new TGraph();
g->SetPoint(0, 1.0, 2.0);
g->SetPoint(1, 2.0, 4.0);
g->SetPoint(2, 3.0, 6.0);

g->Draw("AP");     // 軸+点
g->Draw("APC");    // 軸+点+曲線
g->Draw("AL");     // 軸+直線
```

## 関連メソッド

- [TGraphErrors](./root-tgrapherrors.md) - エラーバー付きグラフ
- [TGraphAsymmErrors](./root-tgraph-asymmerrors.md) - 非対称エラーバー付きグラフ
- [TMultiGraph](./root-tmultigraph.md) - 複数グラフの重ね書き

## 参考資料

- [ROOT Documentation - TGraph](https://root.cern/doc/master/classTGraph.html)
