# CSVを読み込みたい（``pd.read_csv``）

```python
pd.read_csv("ファイル名")
```

[pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)でCSVファイルを読み込めます。
デフォルトの区切り文字は``,``（カンマ）です。

:::{seealso}

- [](./pandas-to_csv.md)
- [](./pandas-to_json.md)

:::

## 区切り文字を指定したい（``sep``）

```python
pd.read_csv("ファイル名", sep="\t")  # タブ区切り
pd.read_csv("ファイル名", sep=" ")   # スペース区切り
```

``sep``（または``delimiter``）オプションで区切り文字を指定して、任意の区切り文字のテキストファイルを読み込むことができます。

## エンコーディングを指定したい（``encoding``）

```python
pd.read_csv("ファイル名", encoding="shift_jis")  # シフトJIS
pd.read_csv("ファイル名", encoding="utf-16")     # UTF-16
```

``encoding``オプションを使って[Pythonの標準的なエンコーディング名](https://docs.python.org/3/library/codecs.html#standard-encodings))を指定できます。
デフォルトは``encoding="utf-8"``です。
``utf-8``と``utf_8``のように``-（ハイフン）``と``_（アンダースコア）``はエイリアスになっていて、どちらでも使えます。

読み込んだデータが文字化けしている場合はエンコーディングを指定する必要があります。
WindowsのExcelで作成されたCSVの場合、そのままでは文字化けすることが多く、だいたいシフトJIS（``shift_jis``）を指定すると解決します。

## 日付に変換したい

```python
pd.read_csv("ファイル名", parse_dates=["公開日", "更新日"])
```

日付のカラムがある場合、``parse_dates``を使って日付オブジェクトに変換できます。

```python
data = pd.read_csv("ファイル名")
data["公開日"] = pd.to_datetime(data["公開日"])
data["更新日"] = pd.to_datetime(data["更新日"])
```

データを読み込んだあとに、[pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)で変換できます。
日付カラムのフォーマットが独特な場合に、ISO8601などの一般的な形に文字列への変換が必要な場合に便利です。

```python
data["公開日"] = pd.to_datetime(data["公開日"])  # 日付オブジェクトに変換
data["公開年"] = data["公開日"].dt.year          # アクセサを使って「年」を取得
data["公開年月"] = data["公開日"].dt.format("%Y-%m") # アクセサを使って任意の文字列に変換
```

日付オブジェクトは[dt](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#api-series-dt)アクセサを使って日付に関する操作ができます。
[dt.strftime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.strftime.html)で任意の日付文字列に変換することもできます。

## コメント行をスキップしたい

```python
pd.read_csv("ファイル名", comment="1文字")  # コメント記号は1文字で指定
pd.read_csv("ファイル名", comment="#")      # '#'がコメント記号
```

``comment``オプションを使って、データをスキップできます。
シェルスクリプトで解析することを前提にしていたデータの場合、読み込みたくない行の先頭に``#``を書いたりします。
このようなデータも``Pandas``でそのまま再利用して分析できます。

コメント記号を指定して、その記号が先頭にある行をスキップできます。
