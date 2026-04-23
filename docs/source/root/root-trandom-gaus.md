# ガウス分布で乱数生成したい（`TRandomMixMax::Gaus`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 平均0、標準偏差1のガウス分布に従う乱数を生成
double randomValue = rng.Gaus(0, 1);
```

`TRandomMixMax::Gaus`でガウス分布にしたがう乱数を生成できます。
引数に平均値と標準偏差を指定することで、任意のガウス分布の乱数を取得できます。

## ガウス分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Gaussian Distribution", 800, 600);
TH1D *h = new TH1D("h", "Gaussian Distribution", 100, -5, 5);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Gaus(0, 1));
}

h->Draw();
```

このサンプルでは、平均0、標準偏差1のガウス分布に従う乱数を10000個生成し、その分布をヒストグラムで可視化しています。
