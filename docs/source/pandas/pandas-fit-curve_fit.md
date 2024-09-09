# 曲線フィットしたい（``scipy.optimize.curve_fit``）

```python
import numpy as np
from scipy.optimize import curve_fit

# func: 任意の関数； y = func(x, *params) の形
# x_data(array_like): X軸のデータ
# y_data(array_like): Y軸のデータ
# p0(array_like): 初期パラメータ
popt, pcov = curve_fit(func, x_data, y_data, p0)

# フィットのエラーを計算
perr = np.sqrt(np.diag(pcov))
```

`scipy.optimize.curve_fit`で、任意の関数を使って曲線フィットできます。

引数には実験で得られたデータ点と、フィットしたい関数を用意すればOKです。
具体例は[](./pandas-fit-gaussian.md)など、別ページに整理しました。

``func``にはフィットしたい関数を指定し、
``x_data``、``y_data``は測定データの中でフィットに使う成分を指定します。
データフレーム形式（``pd.DataFrame``）を使っている場合、``pd.Series``を指定すればOKです
NumPy配列（``nd.array``）に変換して渡しているサンプルもありますが必要ないはずです。

``p0``はフィットの初期パラメーターを指定します。
初期パラメーターがまちがっていると、うまくフィットできない場合があります。
測定データの分布を確認し、近そうな値を指定します。

``curve_fit``の結果は、フィット関数のパラメーター数に応じた値が
``popt``と``pcov``として返ってきます。
``pcov``の対角成分でフィットの誤差を計算できます。

## 最適化したい（``method``）

```python
curve_fit(func, x_data, y_data, p0, method="lm")
curve_fit(func, x_data, y_data, p0, method="trf")
curve_fit(func, x_data, y_data, p0, method="dogbox")
```

``method``オプションで、フィッティングを最適化するアルゴリズムを変更できます。
アルゴリズムは`lm`、`trf`、`dogbox`から選択します。
デフォルトは`None`になっていて、
制約条件がない場合（＝`bounds=(-np.inf, np.inf)`）は`lm`、
制約条件がある場合は`trf`を使うことになっています。

`curve_fit`のフィッティングの基本は非線形の最小二乗法ですが、
その計算アルゴリズムはいろいろあるようです。
その中でもLevenberg-Marguardt法が広く使われているそうです。


:lm:
Levenberg-Marquardt アルゴリズム。
MINPACKで実装されているものと同等。
制約があるsparse Jacobianな場合は扱うことができない。
制約条件がない場合に効率的な手法。

:trf:
Trust Region Reflective アルゴリズム。
制約ががあるlarge sparse bounds に適している。
一般的にロバストな手法。

:dogbox:
dogleg アルゴリズム。
ランクが不足しているJacobianでは非推奨。

:::{note}

[curve_fitのソースコード](https://github.com/scipy/scipy/blob/v1.14.1/scipy/optimize/_minpack_py.py#L591-L1060)を確認すると、
`method="lm"`の場合、[leastsq]()、
それ以外の場合、[least_squares]()、を使っています。

どちらも非線形最小二乗法を使ってパラメーターをフィッティングしますが、
`leastsq`はレガシーな関数で、ユーザーが新しく作成するスクリプトでの利用は推奨されていません。

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

## 共分散行列

`pcov`は共分散行列（covariance matrix）を表すk行k列の2次元配列です。
`k`はフィッティングのパラメーター数です。

:::{math}

\text{cov} = \pmatrix{
    \sigma_{11}^{2} & \sigma_{12}^{2} & \cdots & \sigma_{1k}^{2} \\
    \sigma_{21}^{2} & \sigma_{22}^{2} & \cdots & \sigma_{2k}^{2} \\
    \vdots & \vdots & \ddots & \vdots \\
    \sigma_{k1}^{2} & \sigma_{k2}^{2} & \cdots & \sigma_{kk}^{2}
    }

:::

上記の`curve_fit`で求めた最適値（`popt`）の要素を使って、
対角成分（``i=j``の成分）は分散、
それ以外の成分（``i≠j``の成分）は共分散の値が入っています。

対角成分を使って、フィッティング全体の標準誤差を計算できます。

:::{math}

\text{err}
& = \sqrt{\sigma_{11}^{2} + \sigma_{22}^{2} + \dots + \sigma_{kk}^{2}} \\
& = \sqrt{\sum_{i=1}^{k}\sigma_{ii}^{2}}

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
- [scipy.optimize.leastsq - SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html)
- [scipy.optimize.least_squares - SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)
- [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- [scipy.stats.goodness_of_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.goodness_of_fit.html)

