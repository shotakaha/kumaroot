# 縦に並べたい（``alt.vconcat``）

```python
base = alt.Chart(data).encode(
    alt.X("x").title("X軸"),
    alt.Y("y").title("Y軸"),
)

mark1 = base.mark_bar()
mark2 = base.mark_line()

# mark1 & mark2
alt.vconcat(
    mark1,
    mark2,
)
```

``alt.vconcat``を使って、複数のグラフを縦に並べることができます。
``alt.vconcat``は``&``演算子で代替できます。
