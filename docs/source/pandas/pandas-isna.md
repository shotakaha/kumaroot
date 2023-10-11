# 欠損値を確認したい（``pd.DataFrame.isna``）

```python
data.isna().sum()
```

データフレームに含まれるカラムごとの欠損値の数が確認できます。
[isnull](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html)と
[isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)は同じです。
``pd.DataFrame.isna``を使うことが推奨されています。

データに欠損値があるとうまく集計できない場合があります。
前処理の段階で除外するか、補完するかの処理が必要です。

```python
data.isna().any()    # 欠損値がある列にTrue
data.notna().all()   # 欠損値がある列にFalse
```

## 欠損値を削除したい（``pd.DataFrame.dropna``）

```python
data.dropna()            # 欠損値を含む行を削除する
data.dropna(how="all")   # すべての値が欠損値である行を削除する
data.dropna(axis="columns")    # 欠損値を含む列（カラム）を削除する
data.dropna(thresh=2)    # 欠損値を2個以上含む行を削除する
data.dropna(subset=["カラム名"])    # カラムを指定して、欠損値を含む行を削除する
```

``pd.DataFrame.drpna``を使って欠損値を含む行を削除できます。

デフォルトは``how=any``、``axis="index"``で、欠損値を1つでも含む行を削除します。

``how="all"``にすると、すべての値が欠損値の行だけを削除できます。
``how``の代わりに``thresh``を指定して、任意の個以上の欠損値を含む行を削除できます。
``subset``でカラムを指定して、欠損値を含む行を削除できます。

また、``axis="columns``を指定して、欠損値を含む列を削除できます。

## 欠損値を補完したい（``pd.DataFrame.fillna``）

```python
data.fillna(0)
data.fillna(method="ffill")
data.fillna(method="bfill")
data.fillna(data.mean())
```

## リファレンス

- [pandas.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html)
- [pandas.DataFrame.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)
- [pandas.DataFrame.notna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.notna.html)
- [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
- [pandas.DataFrame.any](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.any.html)
- [pandas.DataFrame.all](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.all.html)
