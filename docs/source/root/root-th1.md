# ヒストグラムしたい（`TH1D` / `TH1F`）

```cpp
#include <TH1D.h>

// ヒストグラムを作成
TH1D *h = new TH1D(
    "h1",    // ヒストグラムの名前
    "Histogram;X axis;Y axis",    // タイトルと軸ラベル（セミコロン区切り）
    200,  // nbinsx - ビン数
    -2,   // xlow - X軸の最小値
    2     // xup - X軸の最大値
);

// ランダムなデータをヒストグラムに入力
for (int i = 0; i < 100000; i++) {
    // 平均0、標準偏差1のガウス分布に従うデータを入力
    h->Fill(gRandom->Gaus(0, 1));
}

// 統計情報を表示
std::cout << "Mean: " << h->GetMean() << std::endl;
std::cout << "RMS: " << h->GetRMS() << std::endl;
std::cout << "Entries: " << h->GetEntries() << std::endl;

// ヒストグラムを描画
h->SetStats();  // 統計ボックスを表示
h->Draw();
```

`TH1`はROOTで1次元ヒストグラムを扱う基底クラスです。
分布の精度に合わせて
`TH1D`（倍精度浮動小数点）や
`TH1F`（単精度浮動小数点）などの派生クラスを使用します。

`name`はヒストグラムの識別子です。
プログラム内でヒストグラムを参照する際に使用します。
他のオブジェクトと重複しないように、ユニークな名前を付けることが推奨されます。

`title`でグラフのタイトルを設定できます。
セミコロン（`;`）で区切ることでX軸とY軸のタイトルを同時に設定できます。

`nbinsx`でビンの数を指定し、`xlow`と`xup`でX軸の範囲を指定します。
ヒストグラムにデータを入力するには、`Fill`メソッドを使用します。
`Fill`したデータの値がビンの範囲内にある場合は、そのビンのカウントが増加します。
ビンの範囲外のデータポイントは、
`Underflow`（`xlow`より小さい）または
`Overflow`（`xup`より大きい）としてカウントされます。

データを解析する際に、データの分布を視覚化して分析するために使用します。
データ型に応じた派生クラスを選択することで、メモリ使用量と精度のバランスを最適化できます。

## 保存したい（`TH1::Write`）

```cpp
#include <TFile.h>

// ヒストグラムを作成
// ...（前のコードと同様）

// ヒストグラムをファイルに保存
TFile *file = new TFile("histogram.root", "RECREATE");
h->Write();  // ヒストグラムをファイルに書き込む
file->Close();  // ファイルを閉じる
```

ROOTのヒストグラムは`TFile`に保存します。
`TH1->Write`メソッドでヒストグラムを書き込みます。
複数のヒストグラムを作成した場合は、ヒストグラムごとに`Write`することで、同じファイルに保存できます。

## エラー（統計誤差）を管理したい

ヒストグラムの各ビンには、統計誤差（エラー）が関連付けられています。通常、エラーは自動的に計算されますが、明示的に設定することもできます。

### 重みとエラーの違い

| 項目 | 重み（Weight） | エラー（Error） |
|---|---|---|
| 指定方法 | `Fill`の第2引数 | `SetBinError`で個別設定、または`Sumw2`で追跡 |
| 役割 | データポイントの統計的重要度 | 各ビンの統計誤差（不確かさ） |
| フィッティング | 重みが統計的重要度として考慮される | エラーは重みとして使用される場合がある |
| 自動計算 | 指定しない場合は重み=1 | `Sumw2()`後は重みから自動計算、通常は√N |

## 実践例：ガウス分布のデータを解析したい

```cpp
#include <TH1D.h>
#include <TRandom.h>
#include <cstdio>

// ヒストグラムを作成
TH1D *h = new TH1D("gauss",
                   "Gaussian Distribution;Value;Frequency",
                   200, -5, 5);

// ガウス分布に従うデータを生成
for (Int_t i = 0; i < 100000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// 統計情報を表示
printf("Mean: %f\n", h->GetMean());
printf("RMS: %f\n", h->GetRMS());
printf("Entries: %lld\n", h->GetEntries());

// 統計ボックスを表示して描画
h->SetStats();
h->Draw();
```

このサンプルでは、平均0、標準偏差1のガウス分布に従う100000個のデータポイントをヒストグラムに入力し、その統計情報を表示しています。

## 関連メソッド

- [TH1::GetEntries](https://root.cern/doc/master/classTH1.html#a3e1dce4da0d3de6f9e5175c4a4da5589) - エントリー数を取得
- [TH1::GetBinContent](https://root.cern/doc/master/classTH1.html#a2f88d66e1e7fb2c6a872d50c4e5f5efb) - ビンの内容を取得
- [TH1::GetBinError](https://root.cern/doc/master/classTH1.html#a72e5df3acb63a960cdaebc3e18f47bfd) - ビンの誤差を取得
- [TH1::Integral](https://root.cern/doc/master/classTH1.html#ae49a9a1d996e4f8f30b2d12a09e6e034) - ヒストグラムの積分値を計算
- [TH1::Fit](https://root.cern/doc/master/classTH1.html#a5bc5a5f4f48285d8d41ce37d82e7a8ea) - 関数をフィットする

## リファレンス

- [TH1 - ROOT Documentation](https://root.cern/doc/master/classTH1.html)
- [TH1D - ROOT Documentation](https://root.cern/doc/master/classTH1D.html)
- [TH1F - ROOT Documentation](https://root.cern/doc/master/classTH1F.html)
- [TH1I - ROOT Documentation](https://root.cern/doc/master/classTH1I.html)
