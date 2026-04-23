# 一様分布で乱数生成したい（`TRandomMixMax::Uniform`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 0から1の一様乱数を生成
double randomValue = rng.Uniform(0, 1);
```

`TRandomMixMax::Uniform`で一様乱数を生成できます。
引数に下限と上限を指定することで、その範囲内の乱数を取得できます。

## 一様分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Uniform Distribution", 800, 600);
TH1D *h = new TH1D("h", "Uniform Distribution", 100, 0, 1);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.Uniform(0, 1));
}

h->Draw();
```

このサンプルでは、0から1の一様分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。
