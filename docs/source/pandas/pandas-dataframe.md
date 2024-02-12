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

## リスト型からデータフレームしたい

```python
import random
import pandas as pd

samples = [[random.gauss(), random.randint(3, 10), random.uniform(5, 20)] for i in range(100)]
data = pd.DataFrame(samples, columns=["x", "y", "z"])
```

リスト型オブジェクト（``list[list]型``）をデータフレームに変換できます。
``columns``オプションを使ってカラム名を変更できます。

## 辞書型からデータフレームしたい

```python
import random
import pandas as pd

samples = [{"x": random.gauss(), "y": random.randint(3, 10), "z": random.uniform(5, 20)} for i in range(100)]
data = pd.DataFrame(samples)
```

辞書型オブジェクト（``list[dict]型``）をデータフレームに変換できます。
辞書のキーがカラム名になります。


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
