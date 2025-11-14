# エラーバー付きグラフを作りたい（`TGraphErrors`）

```cpp
#include <TGraphErrors.h>

// エラーバー付きグラフを作成
TGraphErrors *g = new TGraphErrors();
g->SetPoint(0, 1.0, 2.0);
g->SetPointError(0, 0.1, 0.2);
g->SetPoint(1, 2.0, 4.0);
g->SetPointError(1, 0.15, 0.3);
g->Draw("AP");
```

`TGraphErrors`は、各データ点に誤差（エラーバー）を付与できるグラフクラスです。
測定値の不確かさやばらつきを可視化する際に活用します。
[TGraph](./root-tgraph.md)と同じように点をプロットしますが、X軸とY軸の両方に誤差を指定できます。

```python
from ROOT import TGraphErrors

# エラーバー付きグラフを作成
g = TGraphErrors()
g.SetPoint(0, 1.0, 2.0)
g.SetPointError(0, 0.1, 0.2)
g.SetPoint(1, 2.0, 4.0)
g.SetPointError(1, 0.15, 0.3)
g.Draw("AP")
```

## コンストラクターのシグネチャ

```cpp
// 空のグラフを作成
TGraphErrors();

// データ配列からグラフを作成
TGraphErrors(Int_t n,
             Double_t *x,
             Double_t *y,
             Double_t *ex,
             Double_t *ey);
```

### デフォルトコンストラクター（引数なし）

- 点を持たないグラフを作成
- `SetPoint()`と`SetPointError()`を使って点とエラーを追加

### 配列コンストラクター

- `n`：点の個数
- `x`：X座標の配列
- `y`：Y座標の配列
- `ex`：X軸の誤差の配列
- `ey`：Y軸の誤差の配列

## 点とエラーを追加したい

```cpp
#include <TGraphErrors.h>

TGraphErrors *g = new TGraphErrors();

// 方法1：SetPoint()とSetPointError()を個別に呼び出す
g->SetPoint(0, 1.0, 2.0);
g->SetPointError(0, 0.1, 0.2);

// 方法2：GetN()を使って最後に追加する場合
Int_t n = g->GetN();
g->SetPoint(n, 2.0, 4.0);
g->SetPointError(n, 0.15, 0.3);

g->Draw("AP");
```

`SetPoint()`で点を追加し、`SetPointError()`で対応するインデックスにエラー情報を追加します。

重要な点は、`SetPoint()`と`SetPointError()`の第1引数（インデックス）を一致させることです。

## 配列からグラフを作成したい

```cpp
#include <TGraphErrors.h>

const Int_t n = 3;
Double_t x[n] = {1.0, 2.0, 3.0};
Double_t y[n] = {2.0, 4.0, 6.0};
Double_t ex[n] = {0.1, 0.15, 0.2};
Double_t ey[n] = {0.2, 0.3, 0.4};

// 配列からグラフを作成
TGraphErrors *g = new TGraphErrors(n, x, y, ex, ey);

g->Draw("AP");
```

配列から直接グラフを作成することで、効率的にデータをプロットできます。

## SetPointErrorの注意点

```cpp
#include <TGraphErrors.h>

TGraphErrors *g = new TGraphErrors();

// ❌ 間違い：GetN()が呼ぶたびに増加するため、エラーが正しい位置に付かない
g->SetPoint(g->GetN(), 1.0, 2.0);
g->SetPointError(g->GetN(), 0.1, 0.2);  // GetN()が1を返すが、点は0のままになる

// ✅ 正しい：インデックスを保存してから使用
Int_t npt = g->GetN();
g->SetPoint(npt, 1.0, 2.0);
g->SetPointError(npt, 0.1, 0.2);  // 同じインデックスを使用
```

`SetPoint()`と`SetPointError()`を続けて呼び出す際、`GetN()`は呼び出しのたびに値が変わるため、必ずインデックスを変数に保存してから使用してください。

## 描画オプション

`Draw()`メソッドで異なる描画方法を指定できます。

| オプション | 説明 |
|---|---|
| `"A"` | 軸を描画（必ず含める） |
| `"P"` | 点を描画 |
| `"E"` | エラーバーを描画 |
| `"L"` | 直線で連結 |
| `"C"` | 曲線で連結 |

```cpp
#include <TGraphErrors.h>

TGraphErrors *g = new TGraphErrors();
g->SetPoint(0, 1.0, 2.0);
g->SetPointError(0, 0.1, 0.2);
g->SetPoint(1, 2.0, 4.0);
g->SetPointError(1, 0.15, 0.3);

g->Draw("AP");      // 軸+点
g->Draw("APE");     // 軸+点+エラーバー（推奨）
g->Draw("APEL");    // 軸+点+エラーバー+直線
```

## 関連メソッド

- [TGraph](./root-tgraph.md) - 基本的な散布図
- [TGraphAsymmErrors](./root-tgraph-asymmerrors.md) - 非対称エラーバー付きグラフ
- [TMultiGraph](./root-tmultigraph.md) - 複数グラフの重ね書き

## 参考資料

- [ROOT Documentation - TGraphErrors](https://root.cern/doc/master/classTGraphErrors.html)
