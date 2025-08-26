# 型ヒントしたい（`typing`）

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

具体的な使い方は
[mypyのチートシート](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
がとても参考になります。

:::{note}

Python3.12+であれば`typing`モジュールでOK。
3.8から3.11もサポートするならば`typing_extensions`（後方互換性＋新機能テスト）も併用すると安全です。

:::

## 変数したい

```python
変数名: 型ヒント = 初期値
変数名: 型ヒント # 初期値なし
```

`変数名: 型ヒント`のように、変数名の後に`: 型ヒント`をつけて型ヒントを定義できます。

```python
x: int = 42          # int型
x: float = 42.0      # float型
x: bool = True       # bool型
x: str = "test"      # str型
x: bytes = b"test"   # bytes型
```

Python3.9+であれば、ビルトイン型で型ヒントできます。

```python
# 自作クラスをインポート
from .config import RsyncTaskConfig

task: RsyncTaskConfig | None = RsyncTaskConfig(...)
```

型ヒントの名前には自作クラスも利用できます。

## リスト型したい（`list` / `set` / `typing.Iterable` / `typing.Sequence`）

```python
# str型のリスト
x: list[str] = ["test"]

# int型の集合
x: set[int] = {2, 3, 5, 7, 11}
```

`list[値の型ヒント]`、
`set[値の型ヒント]`で
リスト型（コレクション型）の型ヒントを定義できます。

```python
from typing import List, Set
x: List[str] = ["test"]
x: Set[int] = {2, 3, 5, 7, 11}
```

Python3.8以前では、ビルトイン型が使えないので`typing.List`などを使う必要がありました。

```python
from typing import Iterable, Sequence

# list-likeな集まり
x: Iterable[str] = ["test"]
x: Iterable[int] = {2, 3, 5, 7, 11}

# 読み取り専用のlist-likeな集まり
x: Sequence[str] = ["test"]
x: Sequence[int] = {2, 3, 5, 7, 11}
```

`typing.Iterable`と`typing.Sequence`は`typing`モジュールが提供している型ヒントです。
`for`ループできたり、`len`や`__getitem__`が利用できるオブジェクトに対する
汎用的なリスト型（`list-like`）の型ヒントとして利用できます。

:::{note}

「汎用的な型ヒント」はPythonのDuck Typingに基づいています。
Duck Typingとは、「あひるはガーガー鳴く」という知識から、
「ガーガー鳴いているものはあひる（のようなもの）だ」と推定する考え方です。

この仕組みにより、Pythonではオブジェクトの詳細なクラス設計を知らなくても、
特定のメソッドやプロトコルを持っているかどうかだけで型ヒントを適用できます。

:::

## 辞書型したい（`dict` / `typing.Mapping` / `typing.MutableMapping`）

```python
x: dict[str, float] = {
    "field1": 2.0,
    "field2": 3.0,
    "field3": 5.0,
}
```

`dict[キーの型ヒント, 値の型ヒント]`で辞書型の型ヒントを定義できます。

```python
from typing import Mapping

# map-likeな集まり
x: Mapping[str, float] = [
    "field1": 2.0,
    "field2": 3.0,
    "field3": 5.0,
]

# mutableなmap-likeな集まり
x: MutableMapping[str, float] = [
    "field1": 2.0,
    "field2": 3.0,
    "field3": 5.0,
]
```

`typing.Mapping`と`typing.MutableMapping`は`typing`モジュールが提供している型ヒントです。
`__getitem__`や`__setitem__`が利用できるオブジェクトに対する
汎用的な辞書型（`dict-like`）の型ヒントとして利用できます。

## タプル型したい（`tuple`）

```python
# 固定長
x: tuple[int, str, float] = (3, "yes", 7.5)

# 可変長
x: tuple[int, ...] = (1, 2, 3, 4, 5)
```

`tuple[値の型ヒント, 値の型ヒント, 値の型ヒント]`でタプル型の型ヒントを定義できます。
固定長の場合は、要素数とそれぞれの型ヒントが必要です。
`tuple[値の型ヒント, ...]`で、同じ型の可変長のタプルを定義できます。

## `Any`型したい（`typing.Any`）

```python
from typing import Any

x: Any = 42.0
x: Any = "test"
```

`typing.Any`は「なんでもOK」な特殊型です。
プロトタイピングでとりあえず動かしたいときには便利ですが、
型チェックが無効になるため、長期的に運用する場合は乱用禁止です。

:::{note}

`pyright`には独自拡張の`Unknown`型があります。
`Unknown`も任意の型を表しますが、
これは`Any`の「なんでもあり」と違い、
「ここは型がわからない」という安全側のコンセプトです。

`pyright`はTypeScriptをベースにしているためです。

:::

## 複数の型ヒントしたい（`typing.Union`）

```python
# Python3.9まで
from typing import Union
x: Union[int, str]

# Python3.10以降
x: int | str
x: list[int|str] = [3, 5, "test"]
```

`typing.Union`を使って、複数の型ヒントを組み合わせて指定できます。
Python3.10以降ではOR記号（ ``|`` ）を使ってより簡単に表現できるようになりました。

## `None`したい（`typing.Optional`）

```python
# Python3.9まで
typing import Optional
x: Optional[str]

# Python3.10以降
x: str | None
```

`None`を含む場合は`typing.Optional`を使います。
`Optional[X]`は`Union[X, None]`のシンタックスシュガーです。
Python3.10以降ではOR記号（ ``|`` ） を使って直感的に表現できるようになりました。

## 関数したい

```python
# 引数なし
def 関数名() -> 型ヒント:
    ...

# 引数あり
def 関数名(引数: 型ヒント) -> 型ヒント:
    ...

# 引数とオプション引数あり
def 関数名(引数: 型ヒント, 引数: 型ヒント = デフォルト値) -> 型ヒント:
    ...
```

関数の戻り値に型ヒントを定義できます。
変数の型ヒントと同様に、ビルトイン型、`typing`モジュールが提供する型、自作クラスの型など設定できます。

## 前方参照したい（`__future__.annotations`）

```python
from __future__ import annotations

def f(foo: A) -> int:
    ...
```

`__future__.annotations`をインポートすると、クラス名を前方参照を利用できます。

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import bar

def listify(arg: "bar.BarClass") -> "list[bar.BarClass]":
    return [arg]
```

`typing.TYPE_CHECKING`を使えば、型ヒントだけに自作クラスを適用できます。
循環参照を回避したい場合に利用します。

## 型ヒントあれこれ

Pythonの「型ヒント」は、あくまでも"注釈（annotation）"として導入された機能です。
これらの型ヒントには強制力がなく、開発支援のための仕組みです。
型チェッカー（`mypy`、`pyright`）やIDE（`VS Code`など）が利用する情報であり、
実行時（ランタイム）には基本的に影響しません。
そのため、既存の関数やクラスの動作を変えることなく、後から型ヒントを追加できます。

より厳密な型チェックやバリデーションを行いたい場合は
[Pydantic](https://docs.pydantic.dev/latest/)
などのパッケージを利用するとよいでしょう。

:::{note}

最近（2020年）は、TypeScriptやRustに代表されるように静的型付けできる言語がトレンドです。
その波がPythonにもやってきて、関数アノテーションを利用した型ヒントが導入されました。

C/C++初心者のころ（2010年代）、型を宣言するのめんどくさいなとつまずいていたときに、
型とか気にしなくても書けるPython超便利じゃん！と感動し、Pythonでの開発に流れたのに、
1周回ってきてしまった感があります。

:::

## リファレンス

- [typing](https://docs.python.org/ja/3/library/typing.html)
- [Type hints cheat sheet - mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Built-in types - mypy](https://mypy.readthedocs.io/en/stable/builtin_types.html)
