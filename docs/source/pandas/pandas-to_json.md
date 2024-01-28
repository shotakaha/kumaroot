# JSONを保存したい（``pd.DataFrame.to_json``）

```python
data.to_csv("ファイル名.json", orient="records")
# [
#     {"カラム1": "値11", "カラム2": "値11", "カラム3": "値13"},
#     {"カラム1": "値21", "カラム2": "値21", "カラム3": "値23"},
#     {"カラム1": "値31", "カラム2": "値31", "カラム3": "値33"},
#     {"カラム1": "値41", "カラム2": "値41", "カラム3": "値43"},
# ]
```

[pandas.DataFrame.to_json](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)を使って、JSON形式のファイルを作成できます。

[JSON形式](https://www.json.org/json-ja.html)はパースしやすいので、
異なる言語／アプリでデータをやりとりする場合には、重宝します。
``orient="records"``オプションで書き出すのが、人間にも読みやすくてよいと思います。

:::{seealso}

- [](./pandas-read_csv.md)
- [](./pandas-to_csv.md)

:::

## JSONLしたい

```python
data.to_csv("ファイル名.jsonl", orient="records", lines=True)
# {"カラム1": "値11", "カラム2": "値11", "カラム3": "値13"}
# {"カラム1": "値21", "カラム2": "値21", "カラム3": "値23"}
# {"カラム1": "値31", "カラム2": "値31", "カラム3": "値33"}
# {"カラム1": "値41", "カラム2": "値41", "カラム3": "値43"}
```

JSON形式のデータを1行ごとに改行したのが[JSONL（JSON Lines）](https://jsonlines.org/)形式です。
人間にも読みやすく、直接編集もしやすい形式のJSONです。
