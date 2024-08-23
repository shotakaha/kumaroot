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

## モデルの設定したい（``Model Config``）

```python
class UserSettings(BaseModel):
    settings: str
    drive: str = ""
    data: pd.DataFrame = pd.DataFrame()

    class Config:
        arbitrary_types_allowed = True

us = UserSettings("設定ファイル名")
print(us)
# UserSettings(settings='設定ファイル名', drive='', data=Empty DataFrame)
```

``BaseModel``を継承したクラスの中に``class Config:``を作りモデルの設定を変更できます。
``pd.DataFrame``はPythonのデフォルトの型ではないため、そのままでは使えませんが、
``arbitrary_types_allowed = True``にすると使えるようになります。

設定できる項目は [Model Config](https://docs.pydantic.dev/1.10/usage/model_config/)を参照してください。

## プライベート変数したい

```python
from pydantic import BaseModel, PrivateAttr


class UserSettings(BaseModel):
    settings: str
    drive: str = ""
    _data: pd.DataFrame = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

us = UserSettings("設定ファイル名")
print(us)
# UserSettings(settings='設定ファイル', drive='')
```

初期化のときに`PrivateAttr()`を設定すると、メンバー変数を非表示にできます。
変数名は、`_変数名`のように`sunder (single underscore)`する必要があります。

## リファレンス

- [Pydantic - docs.pydantic.dev](https://docs.pydantic.dev/latest/)
- [pydantic/pydantic - GitHub](https://github.com/pydantic/pydantic)
