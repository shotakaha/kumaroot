# データクラスしたい（``dataclass``）

```python
from dataclasses import dataclass

@dataclass
class クラス名:
    変数名: 型          # 位置引数（必須）
    変数名: 型 = 初期値  # オプション引数
```

C/C++の構造体のように、データ構造を保持するためのクラスを作成する場合に便利なモジュールです。
使い方も簡単で、これまでのクラス定義に``@dataclass``をデコレータとして追加するだけです。

通常のクラス定義では、``__init__``でメンバー変数を初期化する必要がありますが、それらを省略できます。
引数が多い場合はとても便利です。

:::{note}
`@dataclass`はゆるめのデータクラスを作るのに適しています。変数のバリデーションはなく、あとからメンバー変数を追加することもできます。

設定ファイルを読み込む場合など、変数のバリデーションをしたい場合は[pydantic.BaseModel](./python-pydantic.md)が適しています。
:::

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
fnames
```

上記のサンプルは、データを読み込むための設定用クラスを作るときに、よく使っている例です。

## 初期化したい（``__post_init__``）

```python
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    read_from: str
    search_pattern: str

    def __post_init__(self):
        self.fnames = self.get_fnames()

    def get_fnames(self):
        fnames = sorted(Path(self.read_from).glob(self.search_pattern))
        return fnames
```

``__post_init__``でインスタンスを作成したときの挙動を定義できます。

```python
c = Config(
    read_from=".",
    search_pattern="*.csv"
)

# すでに get_fnames されているので
# fnames = c.get_fnames() は必要ない
c.fnames
```


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
    z: float

q = Quantity(
    timestamp="測定時刻",
    x="Xの値",
    y="Yの値",
    z="Zの値",
)

data = pd.DataFrame(asdict(q))
```

``asdict``で``@dataclass``クラスを辞書型に変換できます。
[pandas.DataFrame](../pandas/pandas-dataframe.md)として読み込みたいときに便利です。

## リファレンス

- [dataclasses - Python3](https://docs.python.org/3/library/dataclasses.html)
