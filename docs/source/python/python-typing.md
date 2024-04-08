# 型ヒントしたい（``typing``）

```python
# 変数名: 型ヒント = 値
year: int = 2023
pi: float = 3.14
holiday: tuple[int, int, int, str] = (2023, 5, 5, "こどもの日")
```

[typing](https://docs.python.org/ja/3/library/typing.html)で、関数の引数などに型ヒント（＝型情報）を追加できます。
Python3.5で追加された標準モジュールです。
型ヒントがあると、VS CodeなどのIDEで編集中に型チェックできるようになります。
入力時に補完候補を表示してくれたり、値がマッチしていない部分をハイライトしてくれたりします。

ビルトインされている型（``int``、``float``、``bool``、``str``、``bytes``、``list``、``set``、``dict``、``tuple``）や
``typing``モジュールが提供している型があります。
すべてを型ヒントを暗記する必要はなく、[mypyのチートシート](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)を参照すれば大丈夫です。

:::{seealso}

最近（2020年ころ）は、TypeScriptやRustに代表される静的型付けな言語がトレンドです。
その波はPythonにもやってきて、関数アノテーションを利用した型ヒントが導入されました。
型がはっきりしていたほうが、人々は安心するようです。

C/C++初心者のころ、型を宣言するのめんどくさいなと思っていたところでPythonに触れ、
型とか気にしなくても書けるの超便利じゃん！と感動したことがあったので、
1周回ってしまった感じが強いです。

:::

## ビルトインの型を使いたい

```python
# リスト型
x: list[int] = [1]
x: set[int] = {6, 7}

# 辞書型
x: dict[str, float] = {"field": 2.0}
```

## 複数の型ヒントしたい

```python
from typing import Union, Optional

x: Union[int, str]
x: int | str
x: list[int|str] = [3, 5, "test"]

y: Optional[str]
y: str | None
```

``typing.Union``を使って、複数の型ヒントを指定できます。
``None``を含む場合は``typing.Optional``を使います。
Python3.10以降では ``|`` を使ってより簡潔に表現できるようになりました。

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
