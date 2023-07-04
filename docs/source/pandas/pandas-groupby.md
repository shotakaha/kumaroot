# グループ集計したい（``groupby``）

```python
# 集計項目
v = ["pageview", "session"]
u = "uvisitor"

# 1次集計
g = group = [u]
grouped = data.groupby(g)[v].sum().reset_index()

# 2次集計
_left = grouped.groupby(group)[v].sum().reset_index()
_right = grouped.groupby(group)[u].count().reset_index()
insight = pd.merge(_left, _right, on=group)
```

あとできちんと書きます。
