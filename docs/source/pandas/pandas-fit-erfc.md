# 相補誤差関数でフィットしたい（``scipy.special.erfc``）

```python
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import erfc

def erfc_function(x, amp, mu, sigma, offset):
    """相補誤差補正関数
    Args:
        x(array-like): 測定データ
        amp(float): 振幅
        mu(float): 平均
        sigma(float): 標準偏差
        offset(float): 切片
    Returns:
        f(array-like): 誤差補正関数
    """
    f = amp * erfc((x - mu) / sigma) + offset
    return f

def fit(data: pd.DataFrame, x: str, y: str):
    """
    Args:
        data(pd.DataFrame): 測定データ
        x(str): X軸のカラム名
        y(str): Y軸のカラム名
    Returns:
        popt(array_like): フィット値
        perr(array_like): フィット値の誤差
        x_fit(array_like): フィットした結果のX軸の値
        y_fit(array_like): フィットした結果のY軸の値
    """

    copied = data.copy()
    func = erfc_function
    x_data = copied[x]
    y_data = copied[y]
    p_init = [初期パラメータ]

    popt, pcov = curve_fit(func, x_data, y_data, p_init)
    perr = np.sqrt(np.diag(pcov))

    xmin = x_data.min()
    xmax = x_data.max()

    amp, mu, sigma, offset = popt
    amp_e, mu_e, sigma_e, offset_e = perr

    print(f"Amplitute: {amp} +/- {amp_e}")
    print(f"Mean: {mu} +/- {mu_e}")
    print(f"Sigma: {sigma} +/- {sigma_e}")
    print(f"Offset: {offset} +/- {offset_e}")

    x_fit = np.arange(xmin, xmax, 0.1)
    y_fit = func(x_fit, amp, mu, sigma, offset)

    return popt, perr, x_fit, y_fit
```

宇宙線測定時のスレッショルドを決定したときのサンプルです。
スレッショルド値をスライドさせ、得られた検出率の曲線に対して、
相補誤差関数でフィッティングしました。

## 誤差関数

:::{math}

\text{erf}(x) = \frac{2}{\sqrt(\pi)} \int_{t=0}^{x} \exp(-t^{2}) \text{d}t

:::

誤差関数は、ガウス分布（正規分布）の累積分布関数です。
宇宙線測定時の信号に乗るノイズはガウス分布にしたがうと仮定できます。
あるスレッショルド値 $T$ に対して、信号の大きさ $x$ が $x < T$
（$T$より小さい）となる確率を算出できます。

## 相補誤差関数

:::{math}

\text{erfc}(x) = 1 - \text{erf}(x)

:::

あるスレッショルド値 $T$ に対して、信号の大きさ $x$ が $T < x$
（$T$より大きい）となる確率を算出できます。

## リファレンス

- [scipy.special.erfc](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.erfc.html)
- [scipy.special.erf](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.erf.html#scipy.special.erf)
