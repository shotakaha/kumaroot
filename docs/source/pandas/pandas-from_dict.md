# 辞書型から作成したい（`pandas.DataFrame.from_dict`）

```python
pd.DataFrame(dict)
pd.DataFrame.from_dict()
```

## 辞書型から作成したい

```python
import random
import pandas as pd

n = 1000
samples = {
    "x": [random.gauss() for i in range(n)],
    "y": [random.uniform(4, 8) for i in range(n)],
    "z": [random.randint(0, 10) for i in range(n)],
}

data = pd.DataFrame(samples)
data
```

リスト型の値を持つ辞書型オブジェクト（``dict[str, list]型``）は、そのままデータフレームに変換できます。
辞書型オブジェクトのキーがカラム名になります。

## 辞書型を変換したい

```python
samples = {
    "x": [値11, 値21, 値31, 値41, ...],
    "y": [値12, 値22, 値32, 値42, ...],
    "z": [値13, 値23, 値33, 値43, ...],
}
pd.DaraFrame(samples)
```
