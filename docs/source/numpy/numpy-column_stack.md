# 列方向に結合したい（`np.column_stack`）

```python
# np.column_stack(tpl)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

np.column_stack(a, b)
# ==> array([
#       [1, 10],
#       [2, 20],
#       [3, 30],
#     ])
```

`np.column_stack`で、引数に指定したタプルを、
列方向に並べ直すことができます。
実験データの時刻と値をまとめたり、
複数の特徴量をまとめて1つのデータセットにするときなどに便利です。

## データフレームに変換したい

```python
import numpy as np
import pandas as pd

# データ数
n = 10

# 時刻（のサンプル）
time = np.arange(n)

# （ダミーの）センサーデータ
tmp = 20 + 5 * np.random.randn(n)
hmd = 60 + 10 * np.random.randn(n)
atm = 1013 + 5 * np.random.randn(n)

# 列方向に結合
data = np.column_stack((time, tmp, hmd, atm))

# データフレームに変換
names = ["time", "tmp", "hmd", "atm"]
df = pd.DataFrame(data, columns=names)
```

`np.column_stack`したNumPy配列は、
そのまま`pd.DataFrame`に渡すことができます。
