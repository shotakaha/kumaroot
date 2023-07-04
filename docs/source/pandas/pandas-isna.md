# 欠損値を確認したい（``isna``）

```python
data.isna().any()    # 欠損値がある列にTrue
data.notna().all()   # 欠損値がある列にFalse
```
## 欠損値を削除したい

```python
data.dropna()
data.dropna(how="all")
data.dropna(subset=["カラム名"])
data.dropna(inplace=True)
data.dropna(thresh=2)
```

デフォルトだと欠損値を1つでも含む行が削除できます。
``how="all"``にすると、すべてが欠損値の行が削除できます。

## 欠損値を穴埋めしたい

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
