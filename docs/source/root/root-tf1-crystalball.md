# クリスタルボール関数でフィットしたい（`TF1` with `"crystalball"`）

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <cmath>

TH1D *h = new TH1D("h", "Crystal Ball Distribution", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 10000; i++) {
    double u = random.Gaus(0, 1);
    double x = u;
    // 負側の裾を強調
    if (u < -2) {
        x = -2 - pow(1 - random.Uniform(), -1.0 / 3.0) * 1.5;
    }
    h->Fill(x);
}

TF1 *f = new TF1("crystalball", "crystalball", -5, 5);
h->Fit(f);
```

クリスタルボール関数は、中心がガウス分布で、片側に指数関数的な裾を持つ関数です。
高エネルギー物理での粒子検出効率の非対称性をモデル化するのに用いられます。

## クリスタルボール関数

クリスタルボール関数は以下の2つの領域で定義されます：

**中心部**（$|x - \mu| < \alpha \sigma$）：

:::{math}
f(x) = N \cdot \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
:::

**裾部**（$|x - \mu| \ge \alpha \sigma$）：

:::{math}
f(x) = N \cdot \left( \frac{n}{\alpha} \right)^n \cdot \exp\left( -\frac{\alpha^2}{2} \right) \cdot \left( \frac{n}{\alpha} - |x - \mu|/\sigma \right)^{-n}
:::

中心部はガウス分布、裾部は冪乗関数で表現される非対称な分布です。

## パラメーター

クリスタルボール関数`"crystalball"`は以下の5つのパラメーターで定義されます。

| パラメーター | インデックス | 説明 | デフォルト値 |
|----------|------|------|---------|
| $N$ : 正規化係数（Normalization） | [0] | 関数の高さ | ヒストグラムから自動設定 |
| $\mu$ : 平均値（Mean） | [1] | 分布の中心 | ヒストグラムから自動設定 |
| $\sigma$ : 標準偏差（Sigma） | [2] | ガウス部分の幅 | ヒストグラムから自動設定 |
| $\alpha$ : テール開始点 | [3] | ガウス部分から裾部への遷移点（標準偏差単位） | ヒストグラムから自動設定 |
| $n$ : テール減衰指数 | [4] | 裾部の減衰の急峻さ（大きいほど急峻） | ヒストグラムから自動設定 |

## 関連メソッド

- [TF1](./root-tf1.md) - 関数を定義
- [TGraphErrors::Fit](./root-tgraph-fit.md) - グラフをフィット
- [GetParameter](./root-tf1-getparameter.md) - パラメーター値を取得
- [SetParameter](./root-tf1-setparameter.md) - パラメーター値を設定

## 参考リンク

- [ROOT TF1 Documentation](https://root.cern/doc/master/classTF1.html)
