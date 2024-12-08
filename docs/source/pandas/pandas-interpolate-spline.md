# スプライン補間したい（`scipy.interpolate.CubicSpline`）

```python
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

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
f_splined = CubicSpline(x_valid, y_valid)

# 欠損値を補間
x_data = data["x"]
data["y_splined"] = f_splined(x_data)
```

`scipy.interpolate.CubicSpline`を使って、データをスプライン補間できます。

## スプライン補間したい（`scipy.interpolate.interp1d`）

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
f_splined = interp1d(x_valid, y_valid, kind="cubic", fill_value="extrapolate")

# 欠損値を補間
x_data = data["x"]
data["y_splined"] = f_splined(x_data)
```

`scipy.interpolate.interp1d`を使って、データをスプライン補間できます。

:::{note}

`interp1d`はレガシーなクラスとなっています。
将来的に削除される可能性があるので、別のクラスに移行した方がよさそうです。

:::

## リファレンス

- [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [scipy.interpolate.interp1d](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html)
- [scipy.interpolate.CubicSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html)
- [Interpolation - SciPy](https://docs.scipy.org/doc/scipy/tutorial/interpolate.html)
