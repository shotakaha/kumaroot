# ガウス関数でフィットしたい

```python
import pandas as pd
import numpy as np
from scipy.optimize from curve_fit

def gaus_function(x, amp, mu, sigma):
    """ガウス関数
    Args:
        x(array-like): データ
        a(float): 振幅
        mu(float): 平均
        sigma(float): 標準偏差
    Returns:
        f(ndarray): ガウス関数
    """
    # 分子と分母に分けて計算
    n = (x - mu)**2
    d = 2 * sigma**2
    f = amp * np.exp(-n/d)
    return f

def fit(data: pd.DataFrame, x: str, y: str) :
    """
    Args:
        data(pd.DataFrame): 測定データ
        x(str): X軸に使うカラム名
        y(str): Y軸に使うカラム名
    """

    copied = data.copy()

    func = gaus_function
    x_data = copied[x]
    y_data = copied[y]
    p_init = [a0, mu0, sigma0]

    popt, pcov = curve_fit(func, x_data, y_data, p_init)
    perr = np.sqrt(np.diag(pcov))

    amp, mu, sigma = popt
    amp_error, mu_error, sigma_error = perr

    print(f"Amplitude: {amp} +/- {amp_error}")
    print(f"Mean: {mu} +/- {mu_error}")
    print(f"Sigma: {sigma} +/- {sigma_error}")

    xmin = x_data.min()
    xmax = x_data.max()
    x_fit = np.arange(xmin, xmax, 0.1)
    y_fit = func(x_fit, mu, sigma)

    return popt, perr, x_fit, y_fit
```
