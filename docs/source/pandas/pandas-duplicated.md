# データに重複があるかを調べたい（``duplicated``）

```python
data.duplicated(subset=None, keep="first")
data.duplicated(["カラム1", "カラム2"])
```

データが重複しているか調べることができます。
デフォルトで、すべてのカラムの内容が確認対象になっています。
確認対象のカラムを限定したい場合は``subset``で指定できます。
これはリストも指定できます。

デフォルトは``keiip="first"``となっているため、2番目以降の重複データが``True``（=重複している）と表示されます。

## 重複しているデータの数を知りたい

```python
data.duplicated("カラム").sum()
```

重複しているデータの数は``True``の合計として求めることができます。

## リファレンス

- [pandas.DataFrame.duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html)
- [pandas.Series.duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.duplicated.html)
- [pandas.Index.duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.duplicated.html)
