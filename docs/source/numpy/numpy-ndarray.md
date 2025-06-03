# 多次元配列したい（`np.array`）

```python
# 1次元配列
a = np.array([1, 2, 3])
# => array([1, 2, 3])

# 2次元配列
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    ])
# => array([[1, 2, 3],
#           [4, 5, 6]])

# 2次元配列（型を明示）
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    ],
    dtype=np.float64)
# => array([[1., 2., 3.],
#           [4., 5., 6.]])
```

`np.array`でNumPy配列（`numpy.ndarray`型）を作成できます。
`dtype`オプションで要素の型を指定できます。

`dtype`にはPython標準のビルトイン型（`int`、`float`、`complex`、`bool`、`str`、`bytes`、`object`）が使えます。
精度を明示したい場合はNumPy型（`np.int64`、`np.float64`、`np.complex128`など）を使います。

:::{note}

NumPyのベクトル演算を有効利用するためには、
NumPy配列の要素の型（`dtype`）を揃えることが重要です。

異なる型を混在させると `dtype=object` となり、
Pythonのリストと同じような動作になりますが、
演算速度は遅くなります。

型を混在させたい場合は、
素直にPythonのリストを使えばよいです。

:::

## リストから多次元配列したい

```python
# 1次元配列
seq = [1, 2, 3, 4]
a = np.array(seq)

# 2次元配列
seq = [[1, 2, 3], [4, 5, 6]]
a = np.array(seq)
```

## タプルから多次元配列したい

```python
# 1次元配列
seq = (1, 2, 3, 4)
a = np.array(seq)

# 2次元配列
seq = ((1, 2, 3), (4, 5, 6))
a = np.array(seq)
```

## 辞書から多次元配列したい

```python
d = {"a": 1, "b": 2, "c": 3}

# 値を変換
a = np.array(list(d.values()))

# キーを変換
a = np.array(list(d.keys()), dtype=object)

# キーと値を変換
a = np.array(list(d.items()), dtype=object)
```

辞書型を`np.array`に渡しても意図した通りには動きません。
キーと値をどのように処理するかを明記する必要があります。

## データフレームから多次元配列したい

```python
import pandas as pd
import numpy as np

d = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
}
df = pd.DataFrame(d)
a = df.to_numpy()
# ==> array([
#       [1, 4],
#       [2, 5],
#       [3, 6]
#     ])
```

`pandas.DataFrame`が持っている`to_numpy`メソッドで、
NumPy配列に変換できます。
列方向に定義したデータを、行方向のデータにできます。
