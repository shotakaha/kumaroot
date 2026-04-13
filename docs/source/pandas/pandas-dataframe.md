# データフレームしたい（`pandas.DataFrame`）

```python
import pandas as pd

# values: list[dict]
data = pd.DataFrame(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
)

# values: dict[str, list]
data = pd.DataFrame(
    {
        "name": ["Alice", "Bob"],
        "age": [30, 25]
    }
)

data.display()
#   name  age
# 0  Alice   30
# 1  Bob     25
```

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)でデータフレームを作成できます。
`pandas`の中核となる、行（インデックス）と列（カラム）で構成される表形式のデータ構造で、データの操作や分析に便利です。
リスト型（`list[dict]`）や辞書型（`dict[str, list]`）など、さまざまな形式のデータからデータフレームを作成できます。

:::{hint}

基本的には、スプレッドシートのような表形式の構造を頭に思い浮かべればOKです。
それに対してまず
「行に対して操作」したいのか、
「列に対して操作」したいのか、
を考えると、
やりたいことが整理され、
目的の結果が得られるはずです。

:::

## 2次元配列したい（`pandas.DataFrame`）

```python
values: list[list] = [
    ["name", "age"],
    ["Alice", 30],
    ["Bob", 25]
]

data = pd.DataFrame(values)
```

2次元配列（`list[list]`）からデータフレームを作成できます。
最初の行はカラム名として扱われます。

```python
import numpy as np

values: np.ndarray = np.array([
    ["Alice", 30],
    ["Bob", 25],
])

data = pd.DataFrame(
    values,
    columns=["name", "age"],
)
```

2次元配列には`numpy.ndarray`を使う方が便利です。
データにカラム名が含まれていない場合は、`columns`オプションで列の名前を指定してください。

## 空のデータフレームしたい（`pandas.DataFrame`）

```python
data = pd.DataFrame()
data = pd.DataFrame(columns=[])
data = pd.DataFrame(index=[], columns=[])

print(data.empty)  # True
```

`pd.DataFrame()`で空のデータフレームを作成できます。
`columns`オプションで列の名前を指定したり、`index`オプションで行のインデックスを指定したりできます。
`empty`属性で、データフレームが空かどうかを確認できます。

## カラムの値を取得したい（`pandas.DataFrame`）

```python
# "カラム名"の値を取得
data["カラム名"]

# "カラム名"の値を行方向にスライス
data["カラム名"][開始:終了]
```

`[]`アクセサで、カラムの値を取得できます。
取得した値は`pandas.Series`オブジェクトになっていて、
さらに`[開始:終了]`で行方向にスライスできます。
