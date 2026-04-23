# ポアソン分布で乱数生成したい（`TRandomMixMax::Poisson`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 平均5のポアソン分布に従う乱数を生成
double randomValue = rng.Poisson(5);
```

`TRandomMixMax::Poisson`でポアソン分布にしたがう乱数を生成できます。
引数に平均値を指定することで、任意のポアソン分布の乱数を取得できます。

## ポアソン分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Poisson Distribution", 800, 600);
TH1D *h = new TH1D("h", "Poisson Distribution", 100, 0, 20);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Poisson(5));
}

h->Draw();
```

このサンプルでは、平均5のポアソン分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。
