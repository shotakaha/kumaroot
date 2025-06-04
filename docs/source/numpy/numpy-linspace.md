# 多次元配列したい（`np.linspace`）

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

`np.linspace`で**要素数**を指定して等間隔のNumPy配列を生成できます。
`開始点`、`終了点`、`要素数`を指定できるため、
`np.arange`より制御しやすく、ダミーデータ（のX軸）を生成したい場合に便利です。
