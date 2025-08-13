# リスト型から作成したい（`pandas.DataFrame`）

```python
pd.DataFrame(list_of_lists)
pd.DataFrame(list_of_dicts)
pd.DataFrame(list, columns=[])
```

## 辞書型リストを変換したい

```python
import random
import pandas as pd

# 100行 x 3列のデータ
# [
#    {"x": 値11, "y": 値12, "z": 値13},
#    {"x": 値21, "y": 値22, "z": 値23},
#    {"x": 値31, "y": 値32, "z": 値33},
#    {"x": 値41, "y": 値42, "z": 値43},
#    ...
# ]
samples = [{"x": random.gauss(), "y": random.randint(3, 10), "z": random.uniform(5, 20)} for i in range(100)]
data = pd.DataFrame(samples)
```

**測定データが辞書型**でまとめてある辞書型リスト（``list[dict]型``）は簡単にデータフレームに変換できます。
辞書のキーがカラム名になります。

:::{hint}

一般的に、``pd.Series``型／``pd.DataFrame``型への変換は時間がかかります。
複数のイベントを連続で処理する場合は、個々のステップの返り値は辞書型で返し、最後に変換するとよいです。

:::

## リスト型リストを変換したい

```python
import random
import pandas as pd

# 100行 x 3列 のデータ
# [
#    [値11, 値12, 値13],
#    [値21, 値22, 値23],
#    [値31, 値32, 値33],
#    [値41, 値42, 値43],
#    ...,
# ]
samples = [[random.gauss(), random.randint(3, 10), random.uniform(5, 20)] for i in range(100)]
data = pd.DataFrame(samples, columns=["x", "y", "z"])
```

**測定データがリスト型**でまとめてあるリスト型リスト（``list[list]型``）は簡単にデータフレームに変換できます。
``columns``オプションを使ってカラム名を変更できます。
