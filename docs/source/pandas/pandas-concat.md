# データを連結したい（``pd.concat``）

```python3
pd.concat([data1, data2], ignore_index=True)
```

[pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)で、データを縦方向に連結できます。

```python3
from pathlib import Path
read_from = "データディレクトリ"
fnames = sorted(Path(read_from).glob("*.csv"))

tmp = []
for fname in fnames:
    data = read_csv(fname)
    tmp.append(data)
merged = pd.concat(_tmp, ignore_index)
```

## 連結できたか確認したい

```python3
merged = pd.concat([data1, data2], ignore_index=True)
len(data1) + len(data2) == len(merged)
```

縦方向に連結するため、連結したデータフレームの行数の和は、連結後のデータフレームの行数と一致するはずです。
