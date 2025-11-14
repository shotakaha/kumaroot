# キャンバスを作成したい（`TCanvas`）

```cpp
#include <TCanvas.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c1", "Canvas Title", 800, 600);
c->Draw();
```

`TCanvas`はROOTで図形やグラフを描画するための描画領域（キャンバス）を提供するクラスです。
ヒストグラムやグラフなどのオブジェクトはTCanvas上に描画されます。



```python
from ROOT import TCanvas

# キャンバスを作成
c = TCanvas("c1", "Canvas Title", 800, 600)
c.Draw()
```

## コンストラクターのシグネチャ

```cpp
// デフォルトコンストラクター
TCanvas();

// 基本的なコンストラクター
TCanvas(const char *name,
        const char *title = "",
        Int_t ww = 0,
        Int_t wh = 0);

// 詳細なコンストラクター（位置とサイズを指定）
TCanvas(const char *name,
        const char *title,
        Int_t wtopx,
        Int_t wtopy,
        Int_t ww,
        Int_t wh);
```

## コンストラクターのパラメーター

### 基本的なコンストラクター

**name** - キャンバスの識別名

- オブジェクト識別用
- ROOTファイルでの保存
- 同じディレクトリ内では一意

**title** - キャンバスのタイトル

- ウィンドウのタイトルバーに表示

**ww** - キャンバスの幅（ピクセル）

- デフォルト値：0（自動決定）
- 0の場合は約700ピクセル

**wh** - キャンバスの高さ（ピクセル）

- デフォルト値：0（自動決定）
- 0の場合は約600ピクセル

### 詳細なコンストラクター（位置とサイズ指定）

**wtopx** - ウィンドウの左端のX座標

**wtopy** - ウィンドウの上端のY座標

**ww** - キャンバスの幅（ピクセル）

**wh** - キャンバスの高さ（ピクセル）

## newで作成すべきか、スタック変数で作成すべきか

ROOTではキャンバスは**`new`で動的確保することが推奨されます。**

```cpp
#include <TCanvas.h>

// ❌ 推奨されない：スタック変数として作成
{
    TCanvas c("c", "Canvas");  // スコープを抜けるとメモリが解放される
    // ここで描画
}  // キャンバスのメモリが自動解放される

// ✅ 推奨：newで動的確保
TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
// ここで描画
// 手動でdelete c;する必要はない（ROOTが管理）
```

### newを推奨する理由

1. **キャンバスがROOTに登録される**
   - `new`で作成したキャンバスはROOTのメモリ管理下に入る
   - `gROOT->GetListOfCanvases()`で参照できる

2. **対話モードとマクロの動作が一貫する**
   - 対話モードで`new`を使う場合と同じ動作が保証される
   - スタック変数だとスコープを抜けた時に予期しない動作が発生する可能性

3. **メモリ管理はROOTが行う**
   - ROOTはキャンバスのメモリを自動管理する
   - 明示的な`delete`は通常不要

4. **ウィンドウが消えない**
   - スタック変数ではスコープ終了時にウィンドウが消えてしまう
   - `new`で作成すればプログラム終了まで表示される

## グラフやヒストグラムを描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c", "Histogram Canvas", 800, 600);

// ヒストグラムを作成
TH1D *h = new TH1D("h", "Gaussian Distribution", 100, -3, 3);

// データを入力
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// キャンバスに描画
h->Draw();
```

```{note}
ROOTの対話モードで`h->Draw()`を実行した場合、キャンバスが存在しなければ自動的に生成されます。
ただし、マクロやスクリプトではキャンバスを明示的に作成することが推奨されます。
```



## 関連メソッド

- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::Draw](./root-tcanvas-draw.md) - グラフを描画する
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - ファイルに保存する
- [TCanvas::cd](./root-tcanvas-cd.md) - 領域を選択する
- [TLegend](./root-tlegend.md) - 凡例を追加する

## 参考資料

- [ROOT Documentation - TCanvas](https://root.cern/doc/master/classTCanvas.html)
