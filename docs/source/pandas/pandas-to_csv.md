# CSVを保存したい（``pd.DataFrame.to_csv``）

```python
data.to_csv("ファイル名", index=False)
```

[pandas.DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)で、CSVファイルに出力できます。
デフォルトではインデックス番号のカラムも保存されるため、``index=False``オプションをつけることが多いです。

:::{seealso}

- [](./pandas-read_csv.md)
- [](./pandas-to_json.md)

:::

## 追記したい

```python
data.to_csv("ファイル名", index=False, mode="a", header=None)
```

``mode="a"``オプションでファイルに追記できます。
ヘッダー行も出力されるため``header=None``と合わせて使うことが多いです。

## タブ／スペース区切りしたい

```python
data.to_csv("ファイル名", index=False, sep="\t")
data.to_csv("ファイル名", index=False, sep=" ")
```

``sep``オプションを使って区切り文字を変更できます。

## カラムを指定したい

```python
names = ["カラム1", "カラム2"]
data.to_csv("ファイル名", index=False, columns=names)
```

``columns``オプションで保存するカラム名を指定できます。

以下のようにカラムを絞ったデータフレームを保存しても、同じことができます。（こちらのほうがよく使います。）

```python
names = ["カラム1", "カラム2"]
data[names].to_csv("ファイル名", index=False)
```
