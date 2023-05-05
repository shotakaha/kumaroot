# 型ヒントしたい（``typing``）

```python
# 変数名: 型ヒント = 値
year: int = 2023
pi: float = 3.14
holiday: tuple[int, int, int, str] = (2023, 5, 5, "こどもの日")
```

[typing](https://docs.python.org/ja/3/library/typing.html)モジュールを使って、関数の引数などに型ヒント（＝型情報）を持たせることができます。
型ヒントを書いておくとVS Codeを使っているときに型情報がおかしい部分をハイライトしてくれたり、``mypy``などを使って型チェックできます。

型ヒントにはビルトインされている型（``int``、``float``、``bool``、``str``、``bytes``、``list``、``set``、``dict``、``tuple``）や
``typing``モジュールが提供している型があります。
すべてを暗記する必要はなく、[mypyのチートシート](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)を参照すれば大丈夫です。

:::{seealso}

最近はTypeScriptやRustに代表される静的型付けな言語がトレンドです（と思っています）。
その波はPythonにやってきて、関数アノテーションを利用した型ヒントが導入されました。
型がはっきりしていたほうが人々は安心するようです。

C/C++初心者のころ、型を宣言するのめんどくさいなと思っていたところでPythonを触り出し、型とか気にしなくても書けるの超便利じゃん！と感動したことがあったので、1周回ってしまった感じが強いです。

:::

## 複数の型ヒントしたい

```python
from typing import Union, Optional

x: Union[int, str]
x: int | str

y: Optional[str]
y: str | None
```

``typing.Union``を使って、複数の型ヒントを指定できます。
``None``を含む場合は``typing.Optional``を使います。
Python3.10+では ``|`` を使ってより簡潔に表現できるようになりました。
