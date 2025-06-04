# 等間隔で配列したい（`np.arange`）

```python
# np.arange([start,] stop[, step])
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
