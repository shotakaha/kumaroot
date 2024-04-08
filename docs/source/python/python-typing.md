# 型ヒントしたい（``typing``）

```python
# 変数名: 型ヒント = 値
year: int = 2023
pi: float = 3.14
holiday: tuple[int, int, int, str] = (2023, 5, 5, "こどもの日")
```

[typing](https://docs.python.org/ja/3/library/typing.html)で、関数の引数などに型ヒント（＝型情報）を追加できます。
Python3.5で追加された標準モジュールです。
型ヒントがあると、VS CodeなどのIDEで編集中に型チェックしてくれるようになります。
入力時に補完候補を表示してくれたり、値がマッチしていない部分をハイライトしてくれたりします。

:::{note}

最近（2020年）は、TypeScriptやRustに代表される静的型付けな言語がトレンドです。
その波がPythonにもやってきて、関数アノテーションを利用した型ヒントが導入されました。

C/C++初心者のころ、型を宣言するのめんどくさいなと思っていたところでPythonに触れ、
型とか気にしなくても書けるの超便利じゃん！と感動したことがあったので、1周回ってきた感があります。

:::

:::{note}

デフォルトの型ヒントには強制力はありません。
より厳しく型ヒント／型チェックしたい場合は[Pydantic](https://docs.pydantic.dev/latest/)などのパッケージを利用してください。

:::

## ビルトインの型を使いたい

```python
# リスト型
x: list[int] = [1]
x: set[int] = {6, 7}

# 辞書型
x: dict[str, float] = {"field": 2.0}
```

Python3.9以降であれば、ビルトインされている型で型ヒントできます。

| 型 | 内容 |
|---|---|
| ``int`` | 整数値 |
| ``float`` | 浮動小数点 |
| ``bool`` | 真偽値 |
| ``str`` | 文字列 |
| ``bytes`` | 8ビット文字列 |
| ``object`` | 任意のオブジェクト |
| ``list[str]`` | （文字列の）リスト |
| ``tuple[int, int]`` | 2要素のタプル |
| ``tuple[int, ...]`` | 任意の要素数のタプル |
| ``dict[str, int]`` | ``{文字列: 整数値}``の辞書 |

## 追加の型を使いたい

```python
from typing import Any, Iterable, Sequence, Mapping
```

``typing``モジュールが提供している型もあります。

| 型 | 内容 |
|---|---|
| ``Any`` | なんでも |
| ``Iterable[int]`` | 整数値の``list-like``な集まり |
| ``Sequence[int]`` | 読み込み専用の``list-like``な集まり |
| ``Mapping[str, int]`` | ``dict-like``な集まり |

[mypyのチートシート](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)がとても参考になります。

## 複数の型ヒントしたい

```python
# Python3.9まで
from typing import Union
x: Union[int, str]

# Python3.10以降
x: int | str
x: list[int|str] = [3, 5, "test"]
```

``typing.Union``を使って、複数の型ヒントを組み合わせて指定できます。
Python3.10以降ではOR記号（ ``|`` ） を使ってより簡単に表現できるようになりました。

## ``None``したい

```python
# Python3.9まで
typing import Optional
x: Optional[str]

# Python3.10以降
x: str | None
```

``None``を含む場合は``typing.Optional``を使います。
Python3.10以降ではOR記号（ ``|`` ） を使って直感的に表現できるようになりました。

## Duck Typeしたい

```python
# 関数の list-like な引数
from typing import Iterable
def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]
```

```python
# 関数の dict-like な引数
from typing import Mapping
def f(mapping: Mapping[int, str]) -> list[int]:
    mapping[5] = "maybe"
    return list(mapping.keys())

def f(mapping: MutableMapping[int, str]) -> set[str]:
    mapping[5] = "maybe"
    return set(mapping.values())
```

## リファレンス

- [typing](https://docs.python.org/ja/3/library/typing.html)
- [Type hints cheat sheet - mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Built-in types - mypy](https://mypy.readthedocs.io/en/stable/builtin_types.html)
