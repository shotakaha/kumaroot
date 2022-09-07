# dataclass

```python
from dataclasses import dataclass
```

クラスを作成する場合に便利なモジュールです。
使い方も簡単で、これまでのクラス定義に``@dataclass``をデコレータとして追加するだけです。

```python
@dataclass
class Config:
    path: str
```
