# 箱ひげ図したい（`pandas.DataFrame.plot.box`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame(...)

# 箱ひげ図を描く
data.plot.box(
  title="箱ひげ図",
  xlabel="X軸のタイトル",
  ylabel="Y軸のタイトル"
)
```

`pd.DataFrame.plot.box`で箱ひげ図を作成できます。
オプションでグラフのタイトルや軸のタイトルを変更できます。
