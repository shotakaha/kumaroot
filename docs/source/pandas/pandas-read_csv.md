# CSVを読み込みたい（``pd.read_csv``）

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

読み込んだデータが文字化けしている場合はエンコーディングを指定する必要があります。
``encoding``を使って[Pythonの標準的なエンコーディング名](https://docs.python.org/3/library/codecs.html#standard-encodings))を指定できます。
``utf-8``と``utf_8``のように``-（ハイフン）``と``_（アンダースコア）``はエイリアスになっていて、どちらでも使えます。

WindowsのExcelで作成されたCSVの場合、そのままでは文字化けすることが多いです。
だいたいシフトJIS（``shift_jis``）sを指定すると解決します。

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

## コメント行をスキップしたい

```python
pd.read_csv("ファイル名", comment="1文字")  # コメント記号は1文字で指定
pd.read_csv("ファイル名", comment="#")      # '#'がコメント記号
```

データの先頭にコメントが書かれていることがあります。
コメント記号があれば、その記号を指定することでスキップできます。

## リファレンス

- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [List of Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
