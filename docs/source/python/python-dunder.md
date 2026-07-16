# 特殊メソッドしたい（`__dunder__`）

Pythonで書かれたソースコードを読んでいると、`__`で囲まれたメソッド名が目に入ってきます。
これは`__特殊メソッド__`を意味していて、ふたつのアンダースコアが連なるため**ダンダー（dunder）**と呼ばれてます。

また、ひとつのアンダースコアを変数名の前につけて内部変数を意味したり、
変数名の後ろにつけて仮変数とする慣習もあります。

## 初期化したい（`__init__`）

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
```

`__init__`は、インスタンスを生成するときに自動的に呼ばれる特殊メソッドです。
`Point(1, 2)`のようにクラスを呼び出すと、
内部で`__init__`が呼ばれ、`self.x`・`self.y`に値が設定されます。
C++やJavaでいう「コンストラクタ」に相当します。

## 文字列にしたい（`__str__` / `__repr__`）

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"

p1 = Point(1, 2)
print(p1)   # Point(1, 2)          <- __str__が呼ばれる
p1          # Point(x=1, y=2)      <- 対話モードでは__repr__が呼ばれる
```

`__str__`と`__repr__`を実装すると、
`str()`や`print()`で自作クラスを文字列として表示できるようになります。
役割は似ていますが、意図が異なります。

- `__str__`：人間が読みやすい表示を意図する
- `__repr__`：開発者向けの、できれば`eval()`で再現できるような表示を意図する

:::{hint}

`__str__`が定義されていない場合は、`__repr__`が代わりに使われます。

:::

## 比較演算子したい（`__eq__` / `__lt__` / `__gt__`）

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)   # True   <- __eq__が呼ばれる
print(p1 < p3)     # True   <- __lt__が呼ばれる
```

比較演算子にも、それぞれ対応する特殊メソッドがあります。

| 演算子 | 特殊メソッド |
| --- | --- |
| `==` | `__eq__` |
| `!=` | `__ne__` |
| `<` | `__lt__` |
| `<=` | `__le__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |

:::{note}

`__eq__`を定義すると、デフォルトのハッシュ値が使えなくなり、
そのままでは`set`や辞書のキーとして使えなくなります（``TypeError: unhashable type``）。
必要であれば`__hash__`も一緒に定義してください。

:::

## 四則演算したい（`__add__` / `__sub__`）

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)   # Point(4, 6)   <- __add__が呼ばれる
print(p1 - p2)   # Point(-2, -2) <- __sub__が呼ばれる
print(p1 * 2)     # Point(2, 4)   <- __mul__が呼ばれる
```

四則演算にも、それぞれ対応する特殊メソッドがあります。

| 演算子 | 特殊メソッド |
| --- | --- |
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |

## 長さしたい（`__len__`）

```python
class Group:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

group = Group(["Alice", "Bob", "Carol"])
print(len(group))   # 3   <- __len__が呼ばれる
```

`__len__`を実装すると、`len()`で自作クラスの「長さ」を取得できるようになります。
戻り値は0以上の整数（`int`）である必要があります。

:::{hint}

`__len__`を実装すると、そのクラスのインスタンスは`bool()`や`if`文で
`len() == 0`のときに`False`と判定されるようになります
（``__bool__``が定義されていない場合）。

:::

## プライベート変数したい（`_変数名` / `_関数名()`）

```python
def _internal_function(引数):
    pass
```

変数名や関数名の先頭に`_`をつけて、プライベートであることを表します。

:::{caution}

Pythonの仕組み的に、C++のようなプライベート変数はありません。
先頭に`_`をつけても、言語レベルでのアクセス制限は一切かかっておらず、
`モジュール名._変数名`のようにふつうにアクセスできてしまいます。
ヒトの目に「触れてはいけない」と伝えるための、あくまで慣習上の印です。

呼び方と実装が一致していないので、C++などから来たひとは戸惑うかもしれませんが、
個人的には、セッター／ゲッターを書かなくてもいいので便利だなと感じます。

:::

## 一時変数したい（`_`）

```python
for i in range(10):
    time.sleep(1)

# i を使わないので、次のように書いてもOK
for _ in range(10):
    time.sleep(1)
```

返り値を受け取る必要がない場合、`_`で代用できます。

## 仮変数したい（`変数名_`）

```python
type_ = type(変数)
```

使いたい変数名が、Pythonの予約語と重なってしまう場合は、変数名のあとに`_`をつける慣習があります。
できるかぎり命名規則に沿った変数名を考えるべきですが、
スコープの範囲が狭かったり、一時的な変数の場合には、このようにしてもよいと思います。
