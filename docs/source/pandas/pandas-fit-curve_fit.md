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

## リファレンス

- [scipy.optimize.curve_fit - SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)


