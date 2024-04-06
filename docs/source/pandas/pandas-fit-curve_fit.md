# 任意の関数でフィットしたい（``scipy.optimize.curve_fit``）

```python
import numpy as np
from scipy.optimize import curve_fit

# func: 任意の関数； y = func(x, *params) の形
# x_data(array_like): X軸のデータ
# y_data(array_like): Y軸のデータ
# p_init(array_like): 初期パラメータ
popt, pcov = curve_fit(func, x_data, y_data, p_init)

# フィットのエラーを計算
perr = np.sqrt(np.diag(pcov))
```

[scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)で、任意の関数を使ってフィットできます。

``func``にはフィットに使う任意の関数を指定します。
具体例は[](./pandas-fit-gaussian.md)など、別ページに整理しました。

``x_data``、``y_data``は測定データの中でフィットに使う成分を指定します。
データフレーム形式（``pd.DataFrame``）を使っている場合、``pd.Series``を指定すればOKです
（NumPy配列（``nd.array``）に変換して渡しているサンプルもありますが必要ないはずです）。

``p_init``はフィットの初期パラメーターを指定します。
測定データの分布を確認し、近そうな値を指定します。
初期パラメーターが離れすぎていると、うまくフィットできない場合があります。

``curve_fit``した結果は、フィット関数のパラメーター数に応じた値が``popt``と``pcov``として返ってきます。
``pcov``の対角成分でフィットの誤差を計算できます。

:::{note}

実はフィットの中身をよく分かっていないことが分かったので、
もう少し調べてから追記します。

:::

## 具体例をしりたい

- [](./pandas-fit-gaussian.md)
- [](./pandas-fit-erfc.md)

## フィッティング

フィッティングは $n$ 個の測定データの組み合わせ
$(x_{i}^{\text{data}}, y_{i}^{\text{data}})$
に対して、できる限り正確にあてはまる関数
$y^{\text{fit}}=f(x)$
を探す作業です。

$x_{i}$を説明変数（独立変数）、
$y_{i}$を目的変数（従属変数）
と呼びます。

身近な例だと

- $x_{i}$：シンチレーターの光量（ADC値）、$y_{i}$：頻度
- $x_{i}$：検出器間の距離、$y_{i}$：TOF（Time of Flight）

のようなものです。

アルゴリズムの基本は **最小二乗法** です。
結果のよしあしは、その残差
$r_{i} = y_{i}^{\text{data}} - y_{i}^{\text{fit}}$
から判断します。

## 最小二乗法

1. パラメーター数が $k$ 個ある任意の**フィット関数**を考えます。

:::{math}

y_{i}^{\text{fit}} = f(x_{i} ; p_{1}, p_{2}, \cdots p_{k})

:::

2. 測定した各点 $x_{i}$ で、測定データとフィット関数の差を計算します。これを**残差（residual）** と呼びます。

:::{math}

r_{i} = y_{i}^{\text{data}} - y_{i}^{\text{fit}}

:::

3. これを2乗した値を**残差平方和（Residual Sum of Squares）** と呼びます。

:::{math}

\text{RSS} = \sum_{i=1}^{n} r^{2}

:::

4. 残差平方和が最小となるように、N個のパラメーターを計算します。

:::{math}

\min \text{RSS} = \min \left( \sum_{i=1}^{n} r^{2} \right)

:::

## 結果のよしあし（Goodness of Fit）

適切にフィットできたかどうか$\chi^{2}$値（ピアソンのカイ二乗検定）で判断します。

:::{math}

\chi^{2} = \sum_{i=1}^{n} \frac{(y_{i}^{\text{data}} - y_{i}^{\text{fit}})^{2}}{y_{i}^{fit}}

:::

これをフィットパラメーターの自由度（``degrees of freedom``）で割った値を reduced chi-squared と呼び、この値が1に近いほど、適切にフィットできていると判断します。

:::{math}

\text{reduced} \chi^{2} = \frac{\chi^{2}}{\text{dof}}

:::

## リファレンス

- [scipy.optimize.curve_fit - SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- [scipy.stats.goodness_of_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.goodness_of_fit.html)

