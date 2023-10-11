# カラムを削除したい（``pd.DataFrame.drop``）

```python
data.drop(columns="カラム名")  # カラム名を指定して列を削除する
data.drop(columns=["カラム1", "カラム2"])  # カラム名をリストで指定
data.drop(index="インデックス名")  # インデックス名を指定して行を削除する
```

[pandas.DataFrame.drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)を使ってカラムを削除できます。
``columns``オプションでカラム、``index``オプションで行を削除できます。
