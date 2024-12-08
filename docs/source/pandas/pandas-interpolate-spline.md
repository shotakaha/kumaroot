# スプライン補間したい（`scipy.interpolate.interp1d`）

```python
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# サンプルデータを作成
points = {
    "x": [0, 1, 2, 3, 4, 5],
    "y": [0, np.nan, 2, np.nan, 4, 5]
}
data = pd.DataFrame(points)

# データ点から欠損値を除外
valid_data = data.dropna()
x_valid = valid_data["x"]
y_valid = valid_data["y"]

# スプライン補間
f_splined = interp1d(x_valid, y_valid, kind="cubic", fill_value="extrapolate");

# 欠損値を補間
x_data = data["x"]
data["y_splined"] = f_splined(x_data)
```

Pandas自体にはスプライン補間機能がありませんが、
`scipy.interpolate`モジュールの`interp1d`を使って、データをスプライン補間できます。

:::{note}

`interp1d`はレガシーなクラスとなっていて、将来的に削除される可能性があります。

:::

## 細分化したスプライン補間したい

```python
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# サンプルデータを作成
points = {
    "x": [0, 1, 2, 3, 4, 5],
    "y": [0, 1, 4, 9, 16, 25],
}
data = pd.DataFrame(points)

# データから欠損値を除外
valid_data = data.dropna()
x_valid = valid_data["x"]
y_valid = valid_data["y"]

# スプライン補間
f_splined = interp1d(x_valid, y_valid, kind="cubic", fill_value="extrapolate")

# X軸のデータ点を細分化
x_fine = np.linespace(x_valid.min(), x_valid.max(), 100)
y_fine = f_splined(x_fine)

splined = {
    "x": x_fine,
    "y": y_fine,
}
splined = pd.DataFrame(splined)
```

## リファレンス

- [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [scipy.interpolate.interp1d](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html)
- [scipy.interpolate.CubicSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html)
- [Interpolation - SciPy](https://docs.scipy.org/doc/scipy/tutorial/interpolate.html)
