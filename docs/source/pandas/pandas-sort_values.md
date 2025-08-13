# ソートしたい（`pandas.DataFrame.sort_values`）

```python
data.sort_values(by="カラム名")
data.sort_values(by=["カラム1", "カラム2"])
```

[pandas.DataFrame.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)で、指定したカラムを基準にデータをソートできます。
デフォルトは昇順（ascending）です。
複数のカラムを基準にソートできます。

## 降順でソートしたい

```python
data.sort_values(by="カラム名", ascending=False)
data.sort_values(by=["カラム1", "カラム2"], ascending=[False, True])
```

降順（descending）でソートしたい場合は``ascending=False``にします。
``by``で複数のカラムを指定した場合、``ascending``に同じ個数のリストが必要です。
