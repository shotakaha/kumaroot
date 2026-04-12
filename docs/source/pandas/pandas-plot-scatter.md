# 散布図したい（`pandas.DataFrame.plot.scatter`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame(...)

# 散布図を描く
data.plot.scatter(
  x="X軸のカラム名",
  y="Y軸のカラム名",
)
```

`pd.DataFrame.plot.scatter`で散布図を作成できます。
`x`、`y`でX軸とY軸に使うカラム名を指定します。

:::{seealso}

- [](../altair/altair-scatter.md)
- [](../hvplot/hvplot-scatter.md)
- [](../plotly/plotly-scatter.md)

:::

## カラーマップしたい（`c` / `cmap`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame(...)

# 散布図を描く
data.plot.scatter(
    x="X軸のカラム名",
    y="Y軸のカラム名",
    c="色に使うカラム名",
    cmap="viridis",
)
```

`c`オプションで、マーカー色に使うカラム名を指定できます。
`cmap`オプションで、カラーマップのパターンを指定できます。
指定できるカラーマップのパターンは[colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)を参照してください。

## バブル図したい（`s`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame(...)

# バブル図を描く
data.plot.scatter(
    x="X軸のカラム名",
    y="Y軸のカラム名",
    s="マーカーの大きさに使うカラム名",
)
```

`s`オプションで、マーカーの大きさに使うカラム名を指定できます。
