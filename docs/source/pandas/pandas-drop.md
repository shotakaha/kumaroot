# データを削除したい（``pd.DataFrame.drop``）

```python
data.drop(columns="カラム名")
data.drop(columns=["カラム1", "カラム2"])
```

[pandas.DataFrame.drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)を使ってカラムを削除できます。
``columns``オプションでカラムを指定します。
カラムはリスト形式で複数していできます。

## 行を削除したい

```python
data.drop(index="インデックス名")  # インデックス名を指定して行を削除する
```

``index``オプションで行を削除できます。

## 欠損値を削除したい（``pd.DataFrame.dropna``）

```python
data.dropna()            # 欠損値を含む行を削除する
data.dropna(how="all")   # すべての値が欠損値である行を削除する
data.dropna(axis="columns")    # 欠損値を含む列（カラム）を削除する
data.dropna(thresh=2)    # 欠損値を2個以上含む行を削除する
data.dropna(subset=["カラム名"])    # カラムを指定して、欠損値を含む行を削除する
```

``pd.DataFrame.drpna``を使って欠損値を含む行を削除できます。
デフォルトは欠損値をひとつでも含む行を削除します（``how=any``、``axis="index"``）

``how="all"``にすると、すべての値が欠損値の行だけを削除できます。
``how``の代わりに``thresh``を指定して、任意の個以上の欠損値を含む行を削除できます。
``subset``でカラムを指定して、欠損値を含む行を削除できます。

また、``axis="columns"``を指定して、欠損値を含む列を削除できます。
