# ダミー信号したい

```cpp
// 乱数生成器を使って、実験データを模倣したダミー信号を生成する例
#include <TRandom.h>
#include <TH1D.h>
#include <TCanvas.h>

// 1次元ヒストグラムを作成
TH1D *h = new TH1D("h", "Dummy Signal;X axis;Counts", 100, -5, 5);

// signal: ガウス分布に従うデータを生成してヒストグラムに入力
// background: 一様分布に従うデータを生成してヒストグラムに入力
for (int i = 0; i < 10000; i++) {
    if (gRandom->Uniform() < 0.7) {
        // 70%の確率でsignalを生成
        h->Fill(gRandom->Gaus(0, 1));
    } else {
        // 30%の確率でbackgroundを生成
        h->Fill(gRandom->Uniform(-5, 5));
    }
}

// ヒストグラムを描画
TCanvas *c = new TCanvas("c", "Dummy Signal", 800, 600);
h->Draw();
```

乱数生成器を組み合わせて、実験で得られるデータの特徴を模倣したダミー信号を生成できます。
この例では、ガウス分布に従う信号と一様分布に従う背景を組み合わせて、ヒストグラムに入力しています。

測定器やMCシミュレーションがない場合に、
データ取得ツールの動作確認や、
解析ツールの設計の方向性を検討することに役立ちます。
