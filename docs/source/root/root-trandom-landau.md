# ランダウ分布で乱数生成したい（`TRandomMixMax::Landau`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 平均0、スケール1のランドウ分布に従う乱数を生成
double randomValue = rng.Landau(0, 1);
```

`TRandomMixMax::Landau`でランダウ分布にしたがう乱数を生成できます。
引数に平均値とスケールを指定することで、任意のランダウ分布の乱数を取得できます。

## ランダウ分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Landau Distribution", 800, 600);
TH1D *h = new TH1D("h", "Landau Distribution", 100, -5, 5);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Landau(0, 1));
}
h->Draw();
```

このサンプルでは、平均0、スケール1のランドウ分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。
