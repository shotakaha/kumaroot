# クロス集計したい（``pandas.crosstab``）

```python
pd.crosstab(data["カラムA"], data["カラムB"])
```

`pd.crosstab`で使ってクロス集計できます。
クロス集計すると、指定した2つのカテゴリカルデータ（離散変数）の頻度を確認できます。
トップレベルのメソッドなので、引数にはデータフレーム（というか``pd.Series``）を指定します。
デフォルトで``dropna=True``となっていて、すべての値がNaNのカラムは除外されます。

```python
table = pd.crosstab(data["q01"], data["q02"])

print(table)
q02	Male	Female
q01
20s	67	35
30s	52	34
40s	26	11
50s	25	5
60s	16	3
70s	5	0
80s	2	0
```

上記はアンケート結果を集計したときのサンプルです。
回答者の年代（``q01``）と性別（``q02``）で集計しています。

:::{note}

``pd.crosstab``で得られたデータフレームの並びを確認すると、
行方向が``q02``、列方向が``q01``となっています。
与えた引数の順番と逆になるので、クロス集計結果からヒートマップにする時は転置（``.T``）する必要があります。

:::

## 小計したい（``margins`` / ``margins_name``）

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
また、列ごとの小計（``columns``）もしくは行ごとの小計（``index``）でも規格化できます。
規格化したい基準が合っているかどうかは``margins=True``オプションで確認できます。

## 平均値したい（``aggfunc``）

```python
# カラムA: 離散変数
# カラムB: 離散変数
# カラムC: 連続変数（数値）
pd.crosstab(data["カラムA"], data["カラムB"], values=data["カラムC"], aggfunc="mean")
```

数値型のデータを集計したい場合は、``values``と``aggfunc``をセットで指定します。
平均値の他に、合計値（``sum``）／最大値（``max``）／中央値（``median``）／最小値（``min``）などで集計できます。

## リファレンス

- [pandas.crosstab](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.crosstab.html)
- [pandas.pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html)- [pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
