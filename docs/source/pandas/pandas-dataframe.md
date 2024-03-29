# データフレームしたい（``pandas.DataFrame``）

```python
data = pd.DataFrame(リスト型オブジェクト)
data = pd.DataFrame(辞書型オブジェクト)
```

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)でデータフレームを作成できます。

データフレームは``Pandas``の基本的なデータ構造で、
行（インデックス）と列（カラム）で構成されています。

スプレッドシートのような表構造を頭に思い浮かべて、
行に対する操作なのか、列に対する操作なのか、
を意識すると扱いやすいと思います。

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

## 辞書型を変換したい

```python
samples = {
    "x": [値11, 値21, 値31, 値41, ...],
    "y": [値12, 値22, 値32, 値42, ...],
    "z": [値13, 値23, 値33, 値43, ...],
}
pd.DaraFrame(samples)
```

## データを確認したい

```python
data.head()
data.tail()
```

## カラムを取り出したい

```python
data["カラム名"]
data["カラム名"][開始:終了]
```

``[]``アクセサを使って、カラムを取り出せます。
さらに``[開始:終了]``で行方向にスライスできます。

## 行を取り出したい

```python
data.loc[開始:終了]
data.loc[開始:終了, "カラム名"]
```

[pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)を使って、データフレームを行方向にスライスできます。

また``.loc``を使うと、取り出した行の値を変更できます。
たとえば、ある閾値を越えた測定値を取り出したい場合、次のように書きます。

```python
name = "有効値"
data[name] = 0
isT = data["測定値"] > 閾値
data.loc[isT, name] = data["測定値"]
```
