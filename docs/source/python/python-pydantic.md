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

`pydantic`でPythonの型ヒントをデータクラスのバリデーションができます。
`pydantic.BaseModel`を継承するだけで、そのデータクラスをインスタンス化する時に、
型ヒントにしたがってバリデーションしてくれます。
また、データクラスの変数は[Fields](https://docs.pydantic.dev/dev/api/fields/)で詳細に設定できます。





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

## 再代入したい（`validate_assignment`）

```python
from pydantic import BaseModel, ConfigDict

class UserSettings(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    settings: str
```

`validate_assignment=True`で、インスタンスに再代入したときにもバリデーションを追加できます。

:::{caution}

デフォルトでは、クラスをインスタンス化するときと、シリアライズするときにバリデーションが実行されます。
メンバー変数に値を再代入しただけでは、バリデーションは実行されないことに留意してください。

:::

## リスト型したい（`list`）

```python
from pydantic import BaseModel, Field

class UserSettings(BaseModel):
    items: list[int] = Field(
        default_factory=list,
        min_items=1,
        max_items=10,
        description="整数のリスト",
    )
```

`list[int]`の型ヒントを設定したあとで、`Field`で詳細に設定できます。

:::{note}

Python3.8以前では`typing`モジュールの`List[int]`を使う必要がありました。
Python3.9以降では組み込みのジェネリック型である`list[int]`が推奨されています。

:::

## 例外処理したい（`ValidationError`）

```python
from pydantic import BaseModel, ValidationError

class UserSettings(BaseModel):
    name: str

if __name__ == "__main__":
    try:
        us = UserSettings(name=100)
        print(us)
    except ValidationError as e:
        print(e.errors())
```

`pydantic.ValidationError`でバリデーションエラーの場合に例外処理できます。
`errors()`メソッドで、エラーになった理由などの詳細が確認できます。

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

## 設定クラス

ツールの設定を操作するクラスの作り方を整理します。

1. 設定ファイルを定義する
   1. `config.toml`のようなファイル
   2. サポートするファイル形式を選択する: `TOML` / `YAML` / `JSON` / `CSV` などなど
   3. 設定項目を決定する: `label` / `summary` / ...
2. 設定のデータクラスを定義する
   1. `class Config`のようなクラス
   2. クラス内のデータ構造のみを定義する
   3. ここで`Pydantic.BaseModel`を継承すると便利
3. 設定の操作クラスを定義する
   1. `class ConfigLoader`のようなクラス
   2. 単一のデータクラスに、設定ファイルの値を読み込ませる
   3. `BaseModel`を継承していると読み込み値が検証できる
4. 設定の管理クラスを定義する
   1. `class ConfigReader`、`class ConfigWriter`のようなクラス
   2. 設定ファイルの検索や設定項目の表示などをまかせるクラス

```python
class RsyncTask(BaseModel):
    """A single configuration

    Attributes:
        label (str): Unique identifier of the task.
        summary (str): Short description of the task.
        host (str): Remove host (e.g., "user@host.example.com") or "none" for local.
        source (str): Source path of rsync.
        target (str): Target path of rsync.
        options (List[str]): List of rsync options.
        enabled (bool): Whether the task is enabled
    """

    label: str
    summary: str
    host: str
    source: str
    target: str
    options: list[str]
    enabled: bool = True

    @property
    def is_remote(self) -> bool:
        return self.host.lower() != "none"

    @property
    def rsync_source(self) -> str:
        return f"{self.host}:{self.source}" if self.is_remote else self.source

    @property
    def rsync_target(self) -> str:
        return self.target


class ConfigLoader(BaseModel):
    """Configuration loader

    This class loads and parsed configuration files
    """

    fetch: dict[str, RsyncTask] = {}
    backup: dict[str, RsyncTask] = {}

    def get_enabled_task(self, kind: Literal["fetch", "backup"]) -> list[RsyncTask]:
        settings = getattr(self)
        return [setting for setting in settings.values() if setting.enabled]

    def get_task_by_label




## リファレンス

- [Pydantic - docs.pydantic.dev](https://docs.pydantic.dev/latest/)
- [pydantic/pydantic - GitHub](https://github.com/pydantic/pydantic)
- [Configuration](https://docs.pydantic.dev/dev/concepts/config/)
- [Fields](https://docs.pydantic.dev/dev/concepts/fields/)
- [field_validator](https://docs.pydantic.dev/dev/api/functional_validators/)
