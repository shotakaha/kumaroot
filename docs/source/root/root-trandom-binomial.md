# 二項分布で乱数生成したい（`TRandomMixMax::Binomial`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 試行回数10、成功確率0.5の二項分布に従う乱数を生成
double randomValue = rng.Binomial(10, 0.5);
```

`TRandomMixMax::Binomial`で二項分布にしたがう乱数を生成できます。
引数に試行回数と成功確率を指定することで、任意の二項分布の乱数を取得できます。

## 二項分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Binomial Distribution", 800, 600);
TH1D *h = new TH1D("h", "Binomial Distribution", 11, -0.5, 10.5);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Binomial(10, 0.5));
}
h->Draw();
```

このサンプルでは、試行回数10、成功確率0.5の二項分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。
