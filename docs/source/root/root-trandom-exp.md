# 指数関数で乱数生成したい（`TRandomMixMax::Exp`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 平均1の指数分布に従う乱数を生成
double randomValue = rng.Exp(1);
```

`TRandomMixMax::Exp`で指数分布にしたがう乱数を生成できます。
引数に平均値を指定することで、任意の指数分布の乱数を取得できます。

## 指数分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Exponential Distribution", 800, 600);
TH1D *h = new TH1D("h", "Exponential Distribution", 100, 0, 10);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Exp(1));
}
h->Draw();
```

このサンプルでは、平均1の指数分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。
