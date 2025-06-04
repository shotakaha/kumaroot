# 等間隔で配列したい（`np.arange`）

```python
# np.arange(start, stop, step)
np.arange(5)
# ==> array([0, 1, 2, 3, 4])

np.arange(1, 5)
# ==> array([1, 2, 3, 4])

np.arange(1, 10, 2)
# ==> array([1, 3, 5, 7, 9])

np.arange(0, 1, 0.1)
# ==> array([0., 0.1, 0.2, ..., 0.9])
```

`np.arange`で範囲を指定して等間隔のNumPy配列を生成できます。
`start`オプションで開始値を変更できます。
`step`オプションでステップ間隔を変更できます。

## 精密に等間隔で配列したい（`np.linspace`）

```python
# np.linspace(start, stop, num])
np.linspace(0, 4, 5)
# ==> array([0, 1, 2, 3, 4])

np.linspace(1, 4, 4)
# ==> array([1, 2, 3, 4])

np.arange(1, 9, 5)
# ==> array([1, 3, 5, 7, 9])

np.arange(0, 0.9, 10)
# ==> array([0., 0.1, 0.2, ..., 0.9])
```

`np.linspace`で範囲を指定して等間隔のNumPy配列を生成できます。
`np.arange`と異なり`(開始点、終了点、要素数)`を指定できるので制御しやすく、ダミーデータ（のX軸）を作成したい場合に便利です。

## 対数スケールで分割したい

```python
np.logspace(start, stop, num)
```

## 初期化したい

```python
# すべて 0 で初期化
# np.zeros(shape)
np.zeros(100)
np.zeros((3, 5))  # 3x5行列

# すべて 1 で初期化
# np.ones(shape)
np.ones(100)
np.ones((3, 5))  # 3x5行列

# 任意の値（fill_value）で初期化
# np.full(shape, fill_value)
np.full(100, 3.14)
np.full((3, 5), 3.14)  # 3x5行列
```

`np.zeros`はすべて`0`、
`np.ones`はすべて`1`、
`np.full`はすべて任意の値で初期化した
任意のサイズのNumPy配列を生成できます。

```python
np.empty(shape)    # 初期化してない配列
```

`np.empty`で任意のサイズの配列を生成できます。

## 単位行列したい（`np.identity`）

```python
# NxNの単位行列
# np.identity(N)
np.identity(3)
```

`np.identity`で任意のサイズの単位行列を生成できます。

```python
# 対角成分が [v1, v2, v3] の対角行列
# np.diag([v1, v2, v3])
np.diag([1., 1., 1.])
```

`np.diag`で、任意の対角成分を持つ対角行列を生成できます。
