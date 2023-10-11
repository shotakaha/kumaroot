# 重複を確認したい（``pd.DataFrame.duplicated``）

```python
data.duplicated().sum()
data.duplicated(subset=["カラム1", "カラム2"])
data.duplicated(subset=["カラム1", "カラム2"], keep="last")
```

[pd.DataFrame.duplicated]で重複している行を判定できます。
デフォルトは、すべてのカラムの値が重複している行が対象です。
また``keep="first"``となっているため、2番目以降の重複データが``True``（=重複している）と判定されます。

``subset``でカラム名（のリスト）を指定して、範囲を絞ることができます。

## 重複したデータを削除したい（）

```python
data.drop_duplicates()
data.drop_duplicated(subset=["カラム1", "カラム2"])
data.drop_duplicated(subset=["カラム1", "カラム2"], keep="last")
```

[pd.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)で重複したデータを削除できます。
``pd.DataFrame.duplicate``で``True``と判定されたデータが削除されます。
オプションもほぼ同じです。
