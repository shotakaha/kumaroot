# 重複を確認したい（``pandas.DataFrame.duplicated``）

```python
data.duplicated()
data.duplicated(subset=["カラム1", "カラム2"])
data.duplicated(subset=["カラム1", "カラム2"], keep="last")
```

[pandas.DataFrame.duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html)で重複している行を確認できます。
デフォルトは、**すべてのカラムの値**が重複している行が対象です。
また``keep="first"``となっているため、2番目以降の重複データが``True``（=重複している）と判定されます。

``subset``でカラム名（のリスト）を指定して、範囲を絞ることができます。

```python
dupes = data.duplicated().sum()
if dupes == 0:
    logger.info("No dupes")
```

重複している行が``True``となるため、その合計を計算して重複している数を確認できます。

## 重複したデータを削除したい（``pandas.DataFrame.drop_duplicates``）

```python
data.drop_duplicates()
data.drop_duplicated(subset=["カラム1", "カラム2"])
data.drop_duplicated(subset=["カラム1", "カラム2"], keep="last")
```

[pd.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)で重複したデータを削除できます。
``pd.DataFrame.duplicate``で``True``と判定されたデータが削除されます。
オプションもほぼ同じです。
