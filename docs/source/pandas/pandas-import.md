# インポートしたい（``import pandas as pd``）

```python
import pandas as pd
```

公式ドキュメントは``pd``というエイリアスで読み込んでいました。
公式ドキュメントの[10分でPandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)にも書いてあります。

## 科学計算パッケージ

```python
import numpy as np
import scipy as sp
```

科学計算パッケージも``np``、``sp``というエイリアスで読み込みます。

## 可視化したい（``matplotlib``）

```python
import matplotlib.pyplot as plt
import japanize_matplotlib
```

図の作成に関係するモジュールを``plt``というエイリアスで読み込みます。

```python
import matplotlib as mpl
print(f"matplotlib: {mpl.__version__}")
```

公式ドキュメントは``mpl``というエイリアスで、パッケージを読み込んでいました。

## 可視化したい（``altair``）

```python
import altair as alt
```

公式ドキュメントは``alt``というエイリアスで読み込んでいました。
