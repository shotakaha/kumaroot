# 複数のデータを結合したい（``pd.concat``）

```python3
pd.concat([data1, data2], ignore_index=True)
```

[pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)で、データを縦方向に結合できます。

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

## データの結合を確認したい

```python3
merged = pd.concat([data1, data2], ignore_index=True)
len(data1) + len(data2) == len(merged)
```
