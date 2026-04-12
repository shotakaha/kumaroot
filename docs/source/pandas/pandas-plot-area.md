# 面グラフしたい（`pandas.DataFrame.plot.area`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame(...)

# 面グラフを描く
data.plot.area(
  x = "X軸のカラム名",
  y = "Y軸のカラム名",
  stacked = True,  # 積み上げグラフにするかどうか
  title = "面グラフ",
  xlabel = "X軸のタイトル",
  ylabel = "Y軸のタイトル",
)
```

`pd.DataFrame.plot.area`で面グラフを作成できます。
`x`、`y`でX軸とY軸に使うカラム名を指定します。
`stacked`オプションで、積み上げグラフにするかどうかを指定できます。
オプションでグラフのタイトルや軸のタイトルを変更できます。
