# クロス集計したい（``crosstab``）

```python
pd.crosstab(data["カラムA"], data["カラムB"])
```

[pandas.crosstab](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.crosstab.html)を使ってクロス集計できます。
指定した2つのカレゴリカルデータ（離散変数）の頻度を数えてくれます。
トップレベルのメソッドなので、引数にはデータフレーム（というか``pd.Series``）を指定します。
デフォルトで``dropna=True``となっていて、すべての値がNaNのカラムは除外されます。

:::{note}

同様のメソッドに[pandas.pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html)や[pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)があります。

どれも同じ様なことができますが、明確な使い分けの基準は分かっていません。
自分がやりたいことができればよしとしています。
:::

## 小計したい（``margins``）

```python
pd.crosstab(data["カラムA"], data["カラムB"], margins=True)
pd.crosstab(data["カラムA"], data["カラムB"], margins=True, margins_name="小計")
```

列と行の末尾にそれぞれの小計を追加できます。
``margins_name``で小計したカラムの名前を設定できます。デフォルトは``All``です。
人間が確認するためのデータの場合、追加しておくとよいと思います。

## 規格化したい（``normalize``）

```python
pd.crosstab(data["カラムA"], data["カラムB"], normalize=True)

# 行ごとの小計で規格化
pd.crosstab(data["カラムA"], data["カラムB"], normalize="index")

# 列ごとの小計で規格化
pd.crosstab(data["カラムA"], data["カラムB"], normalize="columns")
```

全体の合計値でクロス集計表を規格化できます。
また、列ごとの小計 or 行ごとの小計で規格化することもできます。

## 平均値したい（``aggfunc``）

```python
pd.crosstab(data["カラムA"], data["カラムB"], values=data["カラムC"], aggfunc="mean")
```

数値型のデータの場合、平均値で計算できます。
``values``と``aggfunc``をセットで指定します。
平均値の他にも合計値（``sum``）／最大値（``max``）／中央値（``median``）／最小値（``min``）などで集計できます。
