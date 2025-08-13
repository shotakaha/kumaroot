# グループ化したい（`pandas.DataFrame.groupby`）

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

# 集計したカラムの総計を計算
n = grouped[v].sum()
grouped["percentage"] = grouped[v] / n
```

集計した値の割合を計算しています。
集計したカラムの総計で、グループごとの集計値を割り算しています。

## 平均値と標準偏差したい（``pandas.DataFrame.agg``）

```python
grouped = data.groupby(g)[v].agg(["mean", "std"]).reset_index()
```

``pd.DataFrame.agg``の引数にはリスト（や辞書）も設定できます。
``mean``と``std``を与えると平均値と標準偏差をまとめて取得できます。

## 複数の方法で集計したい

```python
# グループ化したいカラム
group: list[str] = ["グループ化したいカラム"]

# 集計項目
# ページビュー数, セッション数
v = ["pageview", "session"]
# ユニークビジター数（＝同一IPアドレスの数）
u = "uvisitor"

# あとのデータ処理のためwカラム名を変更する
data.rename(columns={"ipaddress": u}, inplace=True)

# 1次集計
g = group + [u]
grouped = data.groupby(group)[v].sum().reset_index()

# 2次集計
_left = grouped.groupby(group)[v].sum().reset_index()
_right = grouped.groupby(group)[u].count().reset_index()
insight = pd.merge(_left, _right, on=group)
```

あるカラム（のリスト）は合計値、
別のカラム（のリスト）はカウント値、のように、
複数の方法で集計したい場合です。

1回の操作で完結させることができないので、
まず``グループ化したいカラム名``ごとに``groupby``して集計したデータフレームを作成し、それから、``グループ化したいカラム名``を基準にしてマージ（``pandas.merge``）しています。

上のサンプルでは、``pageview``と``session``のカラムは合計値（``sum``）、
``uvisitor``のカラムはカウント数（``count``）で集計しています。

:::{note}

このコードを書いたときは、``pd.DataFrame.agg``の引数に辞書を指定できることを認識していませんでした。
もしかしたら、こんな回りくどいことをせずに計算できるかもしれません。

:::

## リファレンス

- [Group by: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
