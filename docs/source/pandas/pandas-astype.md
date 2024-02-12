# 型を変換したい（``pandas.DataFrame.astype``）

```python
data["カラム名"] = data["カラム名"].astype("型名")
data = data.astype({"カラム1": "int32", "カラム2": "int64"})
```

``DataFrame``や``Series``の型は``astype``で変換できます。
カラムを取り出して変換したり、辞書型``{"カラム名": "型名"}``で変換する内容を指定できます。
型名（``dtypes``）の一覧は[User's Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes)を参照してください。

## リファレンス

- [pandas.Series.astype](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)
- [pandas.DataFrame.astype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
- [pandas.DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
- [basic dtypes](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes)
