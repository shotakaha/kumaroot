# タイトルと軸ラベルを変更したい（`SetTitle`、`SetXTitle`）

ヒストグラムを作成後に、タイトルや軸ラベルを変更できます。コンストラクターで指定する方法と異なり、動的にタイトルを更新できます。

## クイックリファレンス

### C++

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Initial Title", 100, 0, 10);

// タイトルを変更
h->SetTitle("Updated Title");

// タイトルと軸ラベルをセミコロン区切りで設定
h->SetTitle("Title;X axis;Y axis");

// 個別に軸ラベルを設定
h->SetXTitle("X axis");
h->SetYTitle("Y axis");
h->SetZTitle("Z axis");

// タイトルを取得
const char* title = h->GetTitle();

// 軸ラベルを取得
const char* xtitle = h->GetXaxis()->GetTitle();
const char* ytitle = h->GetYaxis()->GetTitle();
```

### Python

```python
from ROOT import TH1D

h = TH1D("h", "Initial Title", 100, 0, 10)

# タイトルを変更
h.SetTitle("Updated Title")

# タイトルと軸ラベルをセミコロン区切りで設定
h.SetTitle("Title;X axis;Y axis")

# 個別に軸ラベルを設定
h.SetXTitle("X axis")
h.SetYTitle("Y axis")

# タイトルを取得
title = h.GetTitle()

# 軸ラベルを取得
xtitle = h.GetXaxis().GetTitle()
ytitle = h.GetYaxis().GetTitle()
```

## タイトル全体を変更したい（`SetTitle`）

`SetTitle`メソッドでヒストグラムのタイトル全体を変更できます。

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Initial Title", 100, 0, 10);

// タイトルのみを変更
h->SetTitle("New Histogram Title");

// タイトルと軸ラベルをセミコロン区切りで同時に指定
h->SetTitle("Histogram;X-axis;Y-axis");

// 現在のタイトルを取得
printf("Title: %s\n", h->GetTitle());
```

セミコロン（`;`）で区切ることで、タイトル、X軸ラベル、Y軸ラベルを同時に指定できます。

## 軸ラベルを個別に変更したい（`SetXTitle`、`SetYTitle`、`SetZTitle`）

個別に軸ラベルを設定したい場合は、`SetXTitle`、`SetYTitle`、`SetZTitle`メソッドを使用します。

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Histogram", 100, 0, 10);

// X軸のラベルを設定
h->SetXTitle("Measurement Value");

// Y軸のラベルを設定
h->SetYTitle("Frequency");

// 3次元ヒストグラム（TH3）の場合、Z軸も設定可能
// h->SetZTitle("Z-axis Label");
```

## 軸ラベルを取得したい（`GetXaxis()->GetTitle()`）

軸ラベルを取得する場合は、`GetXTitle`メソッドではなく、軸オブジェクトを経由して取得する必要があります。

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Histogram", 100, 0, 10);
h->SetXTitle("X Value");
h->SetYTitle("Y Value");

// 軸オブジェクトを取得してラベルを確認
const char* xtitle = h->GetXaxis()->GetTitle();
const char* ytitle = h->GetYaxis()->GetTitle();

printf("X-axis: %s\n", xtitle);
printf("Y-axis: %s\n", ytitle);

// このように直接呼び出すと、期待した結果が得られません
// const char* xtitle2 = h->GetXTitle();  // 存在しないメソッド
```

**重要**：軸ラベルを取得する際は、`GetXaxis()`や`GetYaxis()`メソッドで軸オブジェクトを取得してから、その軸オブジェクトの`GetTitle()`メソッドを呼び出してください。

## 実践例：複数のヒストグラムのタイトルを動的に設定したい

```cpp
#include <TH1D.h>
#include <TString.h>

// 複数のヒストグラムを生成
TH1D *histograms[5];
for (Int_t i = 0; i < 5; i++) {
    TString name;
    name.Form("h%d", i);

    histograms[i] = new TH1D(name.Data(), "", 100, 0, 10);

    // 動的にタイトルと軸ラベルを設定
    TString title;
    title.Form("Dataset %d;Measurement;Count", i + 1);
    histograms[i]->SetTitle(title.Data());
}
```

このサンプルでは、ループ内で複数のヒストグラムを生成し、各ヒストグラムに異なるタイトルを動的に設定しています。`TString::Form`を使用することで、タイトルに番号やパラメーターを含めることができます。

## 関連メソッド

- [TH1::GetTitle](https://root.cern/doc/master/classTH1.html#a3c6e35a38b8a6a00d6d1f3f6f0c5b5f5) - タイトルを取得
- [TH1::GetXaxis](https://root.cern/doc/master/classTH1.html#a3c2f8b6c5a7b9d1e3f5g7h9i1j3k5m7) - X軸オブジェクトを取得
- [TH1::GetYaxis](https://root.cern/doc/master/classTH1.html#a3c2f8b6c5a7b9d1e3f5g7h9i1j3k5m8) - Y軸オブジェクトを取得
- [TAxis::GetTitle](https://root.cern/doc/master/classTAxis.html#a3c6e35a38b8a6a00d6d1f3f6f0c5b5f5) - 軸のタイトルを取得

## 参考資料

- [ROOT Documentation - TH1::SetTitle](https://root.cern/doc/master/classTH1.html#a3c6e35a38b8a6a00d6d1f3f6f0c5b5f5)
- [ROOT Documentation - TAxis](https://root.cern/doc/master/classTAxis.html)
