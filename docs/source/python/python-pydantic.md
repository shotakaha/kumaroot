# データクラスしたい（``pydantic``）

```python
from pydantic import BaseModel

class UserSettings(BaseModel):
    settings: str
    """（必須）設定ファイル名"""

    drive: str = ""
    """（オプション）設定ファイルのディレクトリ名（相対パス）"""

us = UserSettings(settings="設定ファイル名")
print(us)
# UserSettings(settings='設定ファイル名', drive='')
```

``pydantic``はPythonの型ヒントを利用したデータクラスです。
``pydantic.BaseModel``を継承したクラスを作成し、すべてのメンバー変数に型ヒントを与えます。
クラスをインスタンス化する時に、型ヒントにしたがってバリデーションしてくれます。
設定できる型は[Fields](https://docs.pydantic.dev/dev/api/fields/)を参照してください。

:::{caution}

デフォルトでは、クラスをインスタンス化するときと、シリアライズするときにバリデーションが実行されるようです。
メンバー変数に値を代入しただけでは、バリデーションは実行されないことに留意してください。
（おそらくモデルやメンバー変数の設定で変更できると思います）

:::

:::{seealso}

Pydantic v1.10の過去ドキュメントの[Field Types](https://docs.pydantic.dev/1.10/usage/types/)も参考になると思います。

:::

## 設定したい（``model_config``）

```python
from pydantic import BaseModel, ConfigDict

class UserSettings(BaseModel):
    model_config = ConfigDic(arbitrary_types_allowed = True)

    settings: str
    drive: str = ""
    data: pd.DataFrame = pd.DataFrame()


us = UserSettings("設定ファイル名")
us
# UserSettings(settings='設定ファイル名', drive='', data=Empty DataFrame)

```

``model_config``でPydanticのモデル設定を変更できます。
値は``ConfigDict``で設定します。
設定できる項目は [ConfigDict](https://docs.pydantic.dev/dev/api/config/)を参照してください。

上記サンプルでは、``pd.DataFrame``を設定できるようにしました。
``pd.DataFrame``はPythonのデフォルトの型ではないため、そのままでは使えませんが、
``arbitrary_types_allowed = True``にすると使えるようになります。

## カスタムバリデーターしたい（``field_validator``）

```python
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

us = UserSettings(settings="設定ファイル名", drive=".")
# => OK

us = UserSettings(settings="設定ファイル名", drive=".", data=pd.DataFrame({"time": []}))
# => ValidationError
```

``arbitrary_types_allowed = True``にすると、そのフィールドのバリデーションがスキップされます。
型安全を（ある程度）保ちたい場合は、``field_validator``で自分でバリデーターを定義できます。

上記のサンプルでは、``data``に対してカスタムバリデーターを定義しています。
``data``が``pd.DataFrame``であることと、必要なカラム名が存在することを確認しています。
確認に失敗した場合は、``raise ValueError``を発生させ、説明を出力しています。

## データクラスを出力したい（``model_dump`` / ``model_dump_json``）

```python
us.model_dump()
# {'settings': '設定ファイル名', 'drive': ''}

us.model_dump_json()
# '{"settings":"設定ファイル名","drive":""}'
```

``model_dump``で、データクラスの中身を出力（＝シリアライズ）できます。
シリアライズするときに型ヒントを使ったバリデーションが実行されます。
型ヒントと異なる値を代入していた場合は`UserWarning`が表示されます。

:::{note}

`arbitrary_types_allowed = True`としていたら
``pd.DataFrame``はJSON形式にシリアライズできませんでした。
モデル設定を変更した場合は、注意が必要かもしれません。

:::

## プライベート変数したい

```python
from pydantic import BaseModel, ConfigDict, PrivateAttr


class UserSettings(BaseModel):
    model_config = ConfigDic(arbitrary_types_allowed = True)

    settings: str
    drive: str = ""
    _data: pd.DataFrame = PrivateAttr()

us = UserSettings("設定ファイル名")
print(us)
# UserSettings(settings='設定ファイル', drive='')
```

`PrivateAttr()`を初期値に設定すると、メンバー変数を非表示にできます。
変数名は、`_変数名`のように`sunder (single underscore)`する必要があります。

## 設定ファイルしたい

```python
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

# 設定ファイルはTOML形式
# ここではTOMLのシンタックスを模した文字列

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

# TOMLファイルを読み込む → dict型
sd = tomllib.loads(settings_string)

# 読み込んだ内容をフラットにする
args = {**sd.get("basic", {}), **sd.get("datetime", {}), **sd.get("arrays", {})}

# インスタンス化
UserSettings(**args)
```

設定ファイルを読み込んで、クラスを初期化するケースはよくあります。
このサンプルでは、``pydantic.BaseModel``を継承したクラスを使うことで、
設定ファイルのバリデーションを実行しています。

## リファレンス

- [Pydantic - docs.pydantic.dev](https://docs.pydantic.dev/latest/)
- [pydantic/pydantic - GitHub](https://github.com/pydantic/pydantic)
- [Configuration](https://docs.pydantic.dev/dev/concepts/config/)
- [Fields](https://docs.pydantic.dev/dev/concepts/fields/)
- [field_validator](https://docs.pydantic.dev/dev/api/functional_validators/)
