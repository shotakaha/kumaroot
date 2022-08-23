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

## 日付に変換したい

```python
pd.read_csv("ファイル名", parse_dates=["公開日", "更新日"])
```

日付のカラムがある場合、``parse_dates``を使って日付オブジェクトに変換できます。

データを読み込んだあとでも``pandas.to_datetime``で変換できます。
日付カラムのフォーマットが独特な場合に、ISO8601などの一般的な形に文字列への変換が必要な場合に便利です。

```python
data = pd.read_csv("ファイル名")
data["公開日"] = pd.to_datetime(data["公開日"])
data["更新日"] = pd.to_datetime(data["更新日"])
```

## リファレンス

- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [List of Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
