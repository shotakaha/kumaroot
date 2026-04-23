# ブライトウィグナー分布で乱数生成したい（`TRandomMixMax::BreitWigner`）

```cpp
#include <TRandomMixMax.h>
// 乱数生成器を初期化
TRandomMixMax rng;
// 平均0、幅1のブライトウィグナー分布に従う乱数を生成
double randomValue = rng.BreitWigner(0, 1);
```

`TRandomMixMax::BreitWigner`でブライトウィグナー分布にしたがう乱数を生成できます。
引数に平均値と幅を指定することで、任意のブライトウィグナー分布の乱数を取得できます。

## ブライトウィグナー分布のヒストグラムを作りたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandomMixMax.h>

TCanvas *c = new TCanvas("c", "Breit-Wigner Distribution", 800, 600);
TH1D *h = new TH1D("h", "Breit-Wigner Distribution", 100, -5, 5);

TRandomMixMax rng;
for (int i = 0; i < 10000; i++) {
    h->Fill(rng.BreitWigner(0, 1));
}
h->Draw();
```

このサンプルでは、平均0、幅1のブライトウィグナー分布にしたがう乱数を10000個生成し、その分布をヒストグラムで可視化しています。

:::{hint}

ブライトウィグナー分布は、共鳴粒子の質量分布などでよく使われる分布です。
平均値は共鳴の質量、幅は共鳴の寿命に関連しています。

:::
