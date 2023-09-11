# 重ね書きしたい（``alt.layer``）

```python
base = alt.Chart(data).encode(
    alt.X("x").title("X軸"),
    alt.Y("y").title("Y軸"),
)

mark = base.mark_bar()
text = base.mark_text().encode(
    alt.Text("y")
)

# mark + text
alt.layer(
    mark,
    text
)
```

``alt.layer``を使って、複数のグラフを重ね書きできます。
サンプルでは、ヒストグラム（``mark_bar``）にエントリー数をテキスト（``mark_text``）表示しています。
``alt.layer``は``+``演算子で代替できます。
