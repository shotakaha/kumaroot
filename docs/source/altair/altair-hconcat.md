# 横に並べたい（``alt.hconcat``）

```python
base = alt.Chart(data).encode(
    alt.X("x").title("X軸"),
    alt.Y("y").title("Y軸"),
)

mark1 = base.mark_bar()
mark2 = base.mark_line()

# mark | mark2
alt.hconcat(
    mark1,
    mark2,
)
```

``alt.hconcat``を使って、複数のグラフを横に並べることができます。
``alt.hconcat``は``|``演算子で代替できます。
