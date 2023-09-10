# 円グラフしたい（``mark_arc``）

```python
x = "X軸にしたいカラム名"
v = "集計したいカラム名
data.groupby(x)[v].count().reset_index()

n = data[v].sum()
data["percentage"] = data[v] / n

alt.Chart(data).mark_arc().encode(
    alt.Theta("percentage"),
    alt.Color(x)
)
```

``mark_arc``を使って円グラフを作成できます。
データフレームは``pandas.DataFrame.groupby``などを使って、必要な要素を集計しておくことをオススメします。
