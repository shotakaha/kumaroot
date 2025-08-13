# 連結したい（``pandas.concat``）

```python3
pd.concat([data1, data2], ignore_index=True)
```

[pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)で、データを縦方向に連結できます。
``ignore_index=True``で、連結後のインデックスをリセットします。

## 複数ファイルを連結したい

```python3
from pathlib import Path
read_from = "ディレクトリ名"
search_pattern = "*.csv"
fnames = sorted(Path(read_from).glob(search_pattern))

dfs = []
for fname in fnames:
    df = read_csv(fname)
    dfs.append(df)
merged = pd.concat(dfs, ignore_index=True)
```

[pathlibモジュール](../python/python-pathlib.md)と組み合わせて、複数ファイルをひとつのデータフレームに変換できます。
手クセのように使っている書き方です。

## 連結できたか確認したい

```python3
merged = pd.concat([data1, data2], ignore_index=True)
len(data1) + len(data2) == len(merged)
```

縦方向に連結するため、連結したデータフレームの行数の和は、連結後のデータフレームの行数と一致するはずです。
