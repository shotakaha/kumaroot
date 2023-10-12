# 空白を削除したい（``pd.Series.str.replace``）

```python
data["名前"].str.replace("　", "")  # 全角スペースを削除する
data["名前"].str.replace("　", "").str.replace(" ", "")  # 全角スペースと半角スペースを削除する
```

[pandas.Series.str.replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)を使って、指定したカラムの値を置換できます。
上記のサンプルでは``名前``の表記揺れを修正するために、カラムのデータから全角スペース（と半角スペース）を削除しています。
