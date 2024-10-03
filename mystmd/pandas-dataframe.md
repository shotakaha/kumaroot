---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

---
title: データフレームしたい（pd.DataFrame）
subject: pandasの使い方
keywords: [python, pandas]
authors:
  - Shota Takahashi
exports:
  - format: pdf  
---

```{code-cell} ipython3
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import hvplot.pandas

print(f"Pandas: {pd.__version__}")
# print(f"HvPlot: {hvplot.__version__}")
```

# 乱数を使ったサンプルデータしたい

- ``x``: ガウス分布
- ``y``: `(4, 8)`の一様分布
- ``z``: `(0, 10)`の整数の一様分布

```{code-cell} ipython3
rng = np.random.default_rng(511)  # シードを固定
n = 1000

x = rng.normal(size=n)
y = rng.uniform(4, 8, size=n)
z = rng.integers(0, 10, size=n)
```

# 辞書型を変換したい

```python
samples = {
    "x": [リスト],
    "y": [リスト],
    "z": [リスト],
}
```

- リスト型の値をもつ辞書型オブジェクトは、そのまま``pd.DataFrame`` に食べさせることができます。

```{code-cell} ipython3
rng = np.random.default_rng()
n = 1000

samples = {
    "x": rng.normal(size=n),
    "y": rng.uniform(4, 8, size=n),
    "z": rng.integers(0, 10, size=n),
}

data = pd.DataFrame(samples)
data
```

```{code-cell} ipython3
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
canvas = axs.ravel()
data.plot.scatter("x", "y", ax=canvas[0])
data.plot.scatter("z", "y", ax=canvas[1])
```

# 辞書型リストを変換したい

```python
samples = (
    {"x": 値1, "y": 値1, "z": 値1},
    {"x": 値2, "y": 値2, "z": 値2},
    ...,
    {"x": 値n, "y": 値n, "z": 値n},
)
```

- 辞書型リスト（``list[dict[str, Any]]``）、辞書型タプル（``tuple[dict[str, Any]]``）をデータフレームに変換できます
- 辞書のキーがカラム名になります

```{code-cell} ipython3
import random

samples = (
    {"x": random.gauss(), "y": random.uniform(4, 8), "z": random.randint(0, 10)}
    for i in range(1000)
)

data = pd.DataFrame(samples)
data
```

# リスト型リストを変換したい

```python
samples = [
    [リスト],    # x列
    [リスト],    # y列
    [リスト],    # z列
]
```

- リスト型リスト（``list[list]``）、タプル型リスト（``list[tuple]``）、リスト型タプル（``tuple[list]``）、タプル型タプル（``tuple[tuple]``）をデータフレームに変換します
- ``columns``オプションを使ってカラム名を変更できます

```{code-cell} ipython3
import random

samples = [
    (random.gauss(), random.uniform(4, 8), random.randint(0, 10)) for i in range(1000)
]
data = pd.DataFrame(samples, columns=["x", "y", "z"])
data
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
