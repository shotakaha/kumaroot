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
