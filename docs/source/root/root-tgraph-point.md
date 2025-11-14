# SetPointとSetPointErrorの実装例（`TGraph`/`TGraphErrors`）

```cpp
#include <TGraph.h>
#include <TGraphErrors.h>
#include <TTree.h>
#include <vector>

// 波形データを複数グラフに追加する実装例
void plotWaveformData() {
    // TreeからFADCデータを取得する場合の例
    TTree *t = new TTree("events", "Event data");
    std::vector<int> adc;
    t->Branch("adc", &adc);

    // イベント数分のグラフを作成
    const Int_t N = t->GetEntries();
    TGraph *gr[N];

    for (Int_t ientry = 0; ientry < N; ientry++) {
        t->GetEntry(ientry);

        // 各イベントについてグラフを初期化
        gr[ientry] = new TGraph();

        // SetPoint()でデータを追加
        Int_t Nsamp = (Int_t)adc.size();
        for (Int_t isamp = 0; isamp < Nsamp; isamp++) {
            gr[ientry]->SetPoint(isamp, isamp, adc[isamp]);
        }
    }
}
```

このドキュメントでは、`SetPoint()`と`SetPointError()`の実装パターンと、実際のデータ処理での応用例を示します。

## SetPoint()の基本パターン

```cpp
#include <TGraph.h>

TGraph *g = new TGraph();

// パターン1：インデックスを直接指定
g->SetPoint(0, 1.0, 2.0);
g->SetPoint(1, 2.0, 4.0);
g->SetPoint(2, 3.0, 6.0);

// パターン2：GetN()で現在の点数を取得（ループで便利）
for (Int_t i = 0; i < 10; i++) {
    Double_t x = i * 0.5;
    Double_t y = x * x;
    g->SetPoint(g->GetN(), x, y);
}

g->Draw("AP");
```

`SetPoint()`の第1引数はインデックス番号で、0から始まります。
ループで点を追加する場合、`GetN()`を使うと効率的です。

## SetPointError()の実装パターン

```cpp
#include <TGraphErrors.h>
#include <TMath.h>

TGraphErrors *g = new TGraphErrors();

// パターン1：SetPoint()の直後に同じインデックスで設定
g->SetPoint(0, 1.0, 2.0);
g->SetPointError(0, 0.1, 0.2);

g->SetPoint(1, 2.0, 4.0);
g->SetPointError(1, 0.15, 0.3);

// パターン2：インデックスを変数に保存（重要！）
Int_t npt = g->GetN();
g->SetPoint(npt, 3.0, 6.0);
g->SetPointError(npt, 0.2, 0.4);

// パターン3：ループでの追加
for (Int_t i = 0; i < 5; i++) {
    Double_t x = i + 1.0;
    Double_t y = x * 2.0;
    Double_t ex = TMath::Sqrt(x) * 0.1;
    Double_t ey = y * 0.05;

    Int_t n = g->GetN();
    g->SetPoint(n, x, y);
    g->SetPointError(n, ex, ey);
}

g->Draw("APE");
```

重要なポイント：

- `SetPoint()`と`SetPointError()`の**インデックスを一致させる**
- ループで追加する場合は、`GetN()`の結果を**変数に保存してから使用**

## 波形データをプロットする実装例

```cpp
#include <TGraph.h>
#include <TFile.h>
#include <TTree.h>
#include <vector>

void plotFADCWaveforms(const char *filename) {
    // ROOTファイルを開く
    TFile *f = new TFile(filename);
    TTree *t = (TTree*)f->Get("events");

    // FADCデータを読み込むためのブランチを設定
    std::vector<int> *adc = nullptr;
    t->SetBranchAddress("adc", &adc);

    const Int_t N = t->GetEntries();
    TGraph *gr[N];

    // 各イベントについて波形を処理
    for (Int_t ientry = 0; ientry < N; ientry++) {
        t->GetEntry(ientry);

        // 空のグラフを作成
        gr[ientry] = new TGraph();

        // 波形データを追加
        Int_t Nsamp = (Int_t)adc->size();
        for (Int_t isamp = 0; isamp < Nsamp; isamp++) {
            // SetPoint(index, x, y)
            // - index：点のインデックス
            // - x：サンプリング番号
            // - y：ADC値
            gr[ientry]->SetPoint(isamp, isamp, adc->at(isamp));
        }

        // グラフを描画（オプション）
        // gr[ientry]->Draw("AL");
    }

    f->Close();
}
```

FADCの波形データをプロットする場合、ループの中で`GetN()`を使わずに**インデックスを直接指定**するのが効率的です。

## エラーバー付きデータの追加パターン

```cpp
#include <TGraphErrors.h>
#include <TMath.h>
#include <vector>

void addMeasurementData(TGraphErrors *g,
                        const std::vector<Double_t> &x_values,
                        const std::vector<Double_t> &y_values,
                        const std::vector<Double_t> &y_errors) {
    // 既存のグラフに新しいデータを追加
    for (size_t i = 0; i < x_values.size(); i++) {
        // 現在の点数を取得してインデックスとする
        Int_t n = g->GetN();

        g->SetPoint(n, x_values[i], y_values[i]);
        g->SetPointError(n, 0.0, y_errors[i]);  // X誤差は0
    }
}

// 使用例
void example() {
    TGraphErrors *g = new TGraphErrors();

    // 測定データセット1
    std::vector<Double_t> x1 = {1.0, 2.0, 3.0};
    std::vector<Double_t> y1 = {1.5, 3.0, 4.5};
    std::vector<Double_t> ey1 = {0.1, 0.15, 0.2};
    addMeasurementData(g, x1, y1, ey1);

    // 測定データセット2を追加
    std::vector<Double_t> x2 = {4.0, 5.0, 6.0};
    std::vector<Double_t> y2 = {6.0, 7.5, 9.0};
    std::vector<Double_t> ey2 = {0.15, 0.2, 0.25};
    addMeasurementData(g, x2, y2, ey2);

    g->Draw("APE");
}
```

複数のデータセットを追加する場合、`GetN()`を使ってインデックスを動的に取得することで、データの順序を自動的に管理できます。

## よくある間違い

```cpp
#include <TGraphErrors.h>

TGraphErrors *g = new TGraphErrors();

// ❌ 間違い：SetPointの直後にGetN()を呼び出すと、値が増加してしまう
g->SetPoint(g->GetN(), 1.0, 2.0);
g->SetPointError(g->GetN(), 0.1, 0.2);
// 結果：SetPointは0を、SetPointErrorは1を参照
// エラーが異なる点に付加される

// ✅ 正しい：インデックスを保存してから使用
Int_t n = g->GetN();
g->SetPoint(n, 1.0, 2.0);
g->SetPointError(n, 0.1, 0.2);
// 結果：両方とも同じインデックスを参照
```

## パフォーマンスに関する注意

```cpp
#include <TGraph.h>

TGraph *g = new TGraph();

// パターン1：遅い（SetPoint()呼び出しが多い）
for (Int_t i = 0; i < 10000; i++) {
    g->SetPoint(g->GetN(), x[i], y[i]);
}

// パターン2：速い（配列をコンストラクタで渡す）
TGraph *g = new TGraph(10000, x, y);
```

大量のデータを追加する場合は、配列からグラフを作成する方が効率的です。

## 関連メソッド

- [TGraph](./root-tgraph.md) - 基本的な散布図
- [TGraphErrors](./root-tgrapherrors.md) - エラーバー付きグラフ
- TGraph::GetN() - グラフの点数を取得
- TGraph::GetPoint() - グラフの点座標を取得

## 参考資料

- [ROOT Documentation - TGraph::SetPoint](https://root.cern/doc/master/classTGraph.html#ac8f0e64c75e0a38d9d6aadc7f16aaf02)
- [ROOT Documentation - TGraphErrors::SetPointError](https://root.cern/doc/master/classTGraphErrors.html#ac9b1d0c0d7e3bd5f13a2d3b3d3d3d3d3)
