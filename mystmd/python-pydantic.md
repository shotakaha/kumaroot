---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# データクラスしたい（`pydantic`）

- https://docs.pydantic.dev/latest/

```{code-cell} ipython3
from pydantic import BaseModel


class UserSettings(BaseModel):
    settings: str
    """（位置引数）"""

    drive: str = ""
    """（オプション）"""


us = UserSettings(settings="設定ファイル名")
us
```

```{code-cell} ipython3
us.model_dump()
```

```{code-cell} ipython3
us.model_dump_json()
```

## ``pd.DataFrame``したい

- ``pd.DataFrame``はPydanticが標準で利用できる型ではない
- モデルの設定の変更が必要
- ``arbitrary_types_allowed=True``すると、該当のフィールドでバリデーションが効かなくなる

```{code-cell} ipython3
from pydantic import BaseModel, ConfigDict
import pandas as pd


class UserSettings(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    settings: str
    """（位置引数）"""

    drive: str = ""
    """（オプション）"""

    data: pd.DataFrame = pd.DataFrame()


us = UserSettings(settings="設定ファイル名")
us.model_dump()
```

``model_dump()``でシリアライズできる

```{code-cell} ipython3
us.drive = 1
us.model_dump()
```

- ``model_dump_json()``はできない
- ``PydanticSerializationError: Unable to serialize unknown type: <class 'pandas.core.frame.DataFrame'>``

```{code-cell} ipython3
# us.model_dump_json()
```

## カスタムバリデーターしたい

- ``pd.DataFrame``に対するバリデーションを自分で定義できる

```{code-cell} ipython3
from pydantic import BaseModel, field_validator
import pandas as pd
from typing import Any


class UserSettings(BaseModel):
    settings: str
    drive: str
    data: Any = pd.DataFrame({"timestamp": []})

    @field_validator("data")
    def check_dataframe(cls, field_value):
        if not isinstance(field_value, pd.DataFrame):
            raise ValueError("data must be a pandas.DataFrame")
        required_columns = ["timestamp"]
        if not all(col in field_value.columns for col in required_columns):
            raise ValueError(
                f"DataFrame must contain the following columns: {required_columns}"
            )

        return field_value
```

```{code-cell} ipython3
us = UserSettings(settings="設定ファイル名", drive=".")
# us = UserSettings(settings="設定ファイル名", drive=".", data=pd.DataFrame({"time": []}))
```

```{code-cell} ipython3
us.model_dump()
```

```{code-cell} ipython3
# us.model_dump_json()
```

## 設定ファイルしたい

- TOML形式の設定ファイル
- ``tomllib``で読み込み辞書型に変換
- ``**dict``で展開して、クラスを初期化

```{code-cell} ipython3
import tomllib
from pydantic import BaseModel


class UserSettings(BaseModel):
    device: str
    baudrate: int


settings_str = """
device="/dev/ttyUSB0"
baudrate=1000
"""

sd = tomllib.loads(settings_str)
UserSettings(**sd)
```

階層構造（セクション）を持つ設定

```{code-cell} ipython3
import tomllib
import datetime
from pydantic import BaseModel


class UserSettings(BaseModel):
    string: str
    integer: int
    number: float
    boolean: bool
    local_datetime: datetime.datetime
    local_date: datetime.date
    local_time: datetime.time
    array: list
    table: dict
    inline_table: dict
    array_table: list


settings_string = """
[basic]
string = "str"
integer = 10
number = 100.0
boolean = true

[datetime]
local_datetime = "2024-08-28 12:34:56"
local_date = "2024-08-28"
local_time = "12:34:56"

[arrays]
array = ["array1", "array2", 0]
inline_table = { k1 = "v1", k2 = "v2" }
[arrays.table]
k1 = "v1"
k2 = 10

[[arrays.array_table]]
key = "key1"
value = "value1"

[[arrays.array_table]]
key = "key2"
value = "value2"
"""

sd = tomllib.loads(settings_string)

args = {**sd.get("basic", {}), **sd.get("datetime", {}), **sd.get("arrays", {})}

UserSettings(**args)
```
