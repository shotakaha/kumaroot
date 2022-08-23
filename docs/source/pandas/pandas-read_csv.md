# CSVデータを読み込みたい

```python
pd.read_csv("ファイル名")
```

## 区切り文字を指定したい

```python
pd.read_csv("ファイル名", sep="\t")  # タブ区切り
pd.read_csv("ファイル名", sep=" ")   # スペース区切り
```

カンマ区切りでない場合、``sep``（または``delimiter``）で区切り文字を指定できます。

## エンコーディングを指定したい

```python
pd.read_csv("ファイル名", encoding="shift_jis")  # シフトJIS
pd.read_csv("ファイル名", encoding="utf-16")     # UTF-16
```

エンコーディングを指定して読み込むことができます。
WindowsのExcelで作成されたCSVの場合、シフトJISになっていることが多く、そのままでは文字化けしてしまいます。
``utf_8``でも``utf-8``のどちらも使えます。

## リファレンス

- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [List of Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
