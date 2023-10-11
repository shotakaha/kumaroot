# カラム名を変更したい（``pd.DataFrame.rename``）

```python
rename_columns = {
    "カラム名1": "変更後1",
    "カラム名2": "変更後2",
    "カラム名3": "変更後2",
}
data.rename(columns=rename_columns)
```

[pandas.DataFrame.rename](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html)でカラム名を変更できます。
現在と変更後のカラム名を辞書型で定義しておくとよいです。
