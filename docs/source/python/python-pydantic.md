# データクラスしたい（``pydantic``）

```python
from pydantic import BaseModel

class UserSettings(BaseModel):
    settings: str
    """（必須）設定ファイル名"""

    drive: str = ""
    """（オプション）設定ファイルのディレクトリ名（相対パス）"""

us = UserSettings("設定ファイル名")
print(us)
# UserSettings(settings='設定ファイル名', drive='')
```

``pydantic.BaseModel``を継承したクラスを作成します。
メンバー変数の型ヒントは必須で、この型を使って代入時にバリデーションしてくれます。
設定できる型は[Fields](https://docs.pydantic.dev/dev/api/fields/)を参照してください。

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
print(us)
# UserSettings(settings='設定ファイル名', drive='', data=Empty DataFrame)
```

``BaseModel``を継承したクラスの中の``model_config``でPydanticの設定を変更できます。
設定できる項目は [ConfigDict](https://docs.pydantic.dev/dev/api/config/)を参照してください。

上記サンプルでは、``pd.DataFrame``を設定できるようにしています。
``pd.DataFrame``はPythonのデフォルトの型ではないため、そのままでは使えませんが、
``arbitrary_types_allowed = True``にすると使えるようになります。

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

## リファレンス

- [Pydantic - docs.pydantic.dev](https://docs.pydantic.dev/latest/)
- [pydantic/pydantic - GitHub](https://github.com/pydantic/pydantic)
- [Configuration](https://docs.pydantic.dev/dev/concepts/config/)
- [Fields](https://docs.pydantic.dev/dev/concepts/fields/)
