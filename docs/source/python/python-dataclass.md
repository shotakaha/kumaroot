# データクラスしたい（``dataclass``）

```python
from dataclasses import dataclass
```

C/C++の構造体のように、データ構造を保持するためのクラスを作成する場合に便利なモジュールです。
使い方も簡単で、これまでのクラス定義に``@dataclass``をデコレータとして追加するだけです。

```python
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    read_from: str
    search_pattern: str

    def get_fnames(self):
        fnames = sorted(Path(self.read_from).glob(self.search_pattern))
        return fnames
```

```python
c = Config(
    read_from=".",
    search_pattern="*.csv"
)
fnames = c.get_fnames()
```

上記のサンプルは、データを読み込むための設定用クラスを作るときに、よく使っている例です。

## 辞書型にしたい（``asdict``）

```python
from dataclasses import dataclass, asdict
import pendulum
import pandas as pd

@dataclass
class Quantity:
    timestamp: pendulum.datetime
    x: float
    y: float

q = Quantity(
    timestampe="測定時刻時",
    x="Xの値",
    y="Yの値"
)

data = pd.DataFrame(asdict(q))
```

``asdict``で``@dataclass``クラスを辞書型に変換できます。
[pandas.DataFrame](../pandas/pandas-dataframe.md)として読み込みたいときに便利です。

## リファレンス

- [dataclasses - Python3](https://docs.python.org/3/library/dataclasses.html)
