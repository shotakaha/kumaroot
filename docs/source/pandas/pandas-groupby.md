# グループ集計したい（``groupby``）

```python
g = ["グループ化したいカラム名"]
v = ["集計したいカラム名"]

data.groupby(g)[v].sum().reset_index()
```

``グループ化したいカラム名``（のリスト）と``集計したいカラム名``（のリスト）を指定して、データを集計できます。
``groupby``で返ってくるオブジェクトは（型名を確認して追記する）型になっています。
そのままでは扱いづらいので``reset_index``して普通のデータフレームに変換しています。

## パーセンテージを計算したい

```python
g = "グループ化したいカラム名"
v = "集計したいカラム名"
grouped = data.groupby(g)[v].count().reset_index()

n = grouped[v].sum()
grouped["percentage"] = grouped[v] / n
```

## 複数のカラムを別々に集計（``agg_func``）したい

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

``pageview``と``session``のカラムは合計値（``sum``）、
``uvisitor``のカラムはカウント数（``count``）したい場合は、
まず別々に``groupby``したデータフレームを作成し、
``グループ化したいカラム名``を基準にしてマージさせます。
