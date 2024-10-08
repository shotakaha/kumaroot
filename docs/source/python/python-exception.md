# 例外処理したい（`try...except...`）

```python
try:
    例外が発生するかもしれない処理
except 例外の種類 as オブジェクト名:
    例外が発生したときの処理
except Exception as e:
    基本的な例外が発生したときの処理
    print(f"Error: {e}")
    print(f"{e.args=}")
```

``try..except..``構文を使って例外処理（＝エラーハンドリング）できます。
**例外の種類**には
Pythonにビルトインの例外クラス名、もしくはカスタムした例外クラス名を指定します。
また、発生した例外を**オブジェクト名**で受け取っておくと、
例外をさらにコントロールできます。
オブジェクト名には`e`や`err`を使うことが多いです。

`except`処理は複数記述できます。
例外処理は、親クラスの名前でも補足できます。
利用可能なビルトイン例外とその階層構造の詳細は
[exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
を参照してください。

:::{hint}

```python
except Exception as e:
    基本的な例外が発生したときの処理
```

ビルトイン例外クラスは基本的に`Exception`クラスから派生したクラスになっています。
なので`Exception`を指定すれば、どんな例外も補足できます。

:::

## よくある例外と確認事項

エラーが発生した場合、まずエラーメッセージをきちんと確認することが大切です。
どのファイル（のどのあたり）で例外が発生したかが特定できれば、
その理由を考えたり、対応方法を考えたりできます。

以下に出会いがちなビルトイン例外と、そのときの確認事項を整理してみました。

:ImportError / ModuleNotFoundError:
モジュールのインポートが正しくない場合に発生します。
モジュールがインポートされているか、Python実行環境のパスが正しいか、確認しましょう。

:AttributeError / KeyError / IndexError / ValueError:
オブジェクト操作が正しくない場合に発生します。
リストの長さをオーバーしていないか、辞書型にないキーを指定していないか、確認しましょう。

:NameError:
変数名が正しくないときに発生します。
変数が宣言されているか、変数名にスペルミスがないか、確認しましょう。

:SyntaxError / IndentationError:
文法が正しくないときに発生します。
インデントが正しいか、条件文の末尾の`:`を忘れていないか、確認しましょう。

:FileExistsError / FileNotFoundError:
ファイル操作が正しくないときに発生します。
ファイル名が正しいかどうか、既存のファイルが存在していないか、確認しましょう。

## 中断処理したい（`KeyboardInterrupt`）

```python
try:
    例外が発生するかもしれない処理
except KeyboardInterrupt as e:
    中断処理
    # バッファーの内容をファイルに保存する、など
    print(f"Error: {e}")
    sys.exit()
```

`KeyboardInterrupt`クラスで、中断処理（{kbd}`ctrl-c`）したときの例外処理ができます。
中断処理すると、そのときバッファーにあるデータなどは破棄されます。
長時間走らせるようなスクリプトや、CLIツールには必ず中断処理を書いて、
安全に終了できるようにしましょう。

## パッケージの例外処理したい

```python
try:
    response = requests.get("https://httpbin.org/status/404")
except requests.exception.RequestException as e:
    print(f"Error: {e}")
```

上記サンプルは、[requests](./python-requests.md)パッケージの例外処理です。
このように、パッケージによっては、カスタムの例外クラスが定義されてます。
詳細はパッケージのドキュメントを確認してください。

## 例外したい（`raise`）

```python
if 条件確認:
    条件が正しいときの処理
else:
    raise 例外クラス名
```

`raise`で例外を発生できます。
例外クラス名は、ビルトインの例外クラスが使えます。
また、カスタムした例外クラスも作成できます。

自作のパッケージをライブラリとして作成している場合、
適切な例外を発生させることで、ユーザー（自分自身を含む）に優しくなります。

:::{note}

条件に合わないとき、`sys.exit`などで終了させることもできます。
スクリプトの場合は、この挙動が正しいです。

```python
if 条件確認:
    条件が正しいときの処理
else:
    sys.exit()
```

ライブラリは、スクリプトからインポートして使われます。
ライブラリ内部で強制終了するような処理があると、そのライブラリのユーザーはその後どうすることもできません。
例外を`raise`することで、その後の処理をユーザーに委ねることができます。
（例外をキャッチして対処するのか、そのまま握り潰すか、ユーザーが自由にできます）

:::

## 例外クラスをカスタムしたい（``Exception``）

```python
# MODULE_NAME.py
class CustomError(Exception):
    """CustomError: 最小構成（何もしない）"""
    pass

def CustomFunction(...):
    if 条件:
        正常処理
    else:
        raise CustomError("エラー発生!"):
```

`Exception`クラスを継承して、例外クラスをカスタムできます。
小規模なスクリプトでは、ビルトインの例外クラスで十分対応できると思うので、
わざわざ例外クラスを自作する必要はありません。

上記のサンプルは、例外クラス名だけを変更しています。
公開されている有名なパッケージでもよく使われている気がします。

```python
# exceptions.py
class CustomError(Exception):
    """CustomError: 自作の例外クラス"""
    def __init__(self,
                message: str = "デフォルトのエラーメッセージ",
                error_code: int | None = None
        ):
        """CustomErrorを初期化

        Args:
            message (str): エラーメッセージ
            error_code (int): エラーコード
        """
        super().__init__(message)    # 親クラスのExceptionクラスの初期化
        self.message = message
        self.error_code = error_code

    def __str__(self):
        """例外の文字列表現

        Returns:
            str: [エラーコード] エラーメッセージ
        """
        if self.error_code is not None:
            return f"{[{self.error_code}] {self.message}}"
        return self.message
```

以下のようなユースケースで、自作を検討したほうがいいかもしれません。

1. 特定の例外シナリオに対処したい
2. 例外処理をカプセル化したい
3. 他の例外と区別したい

中規模〜大規模なパッケージを開発している場合には、複数の例外クラスが必要になるかもしれません。
その場合は、`exceptions.py`のようなファイルに整理するのが一般的なようです。

カスタムした例外クラスの作成は``@dataclass``デコレーターを使って簡略化できます。

```python
# exceptions.py
from dataclasses import dataclass

@dataclass
class CustomError(Exception):
    """CustomError: 自作の例外クラス

    dataclassを使って簡略化
    """
    message: str = "デフォルトのエラーメッセージ"
    error_code: int | None = None

    def __str__(self):
        """例外の文字列表現"""
        if self.error_code is not None:
            return f"[{self.error_code}] {self.message}"
        return self.message
```

```python
from .exceptions import CustomError

def custom_function(...):
    if 条件:
        正常処理
    else:
        raise CustomError("エラー発生!", 101)

try:
    custom_function(...)
except CustomError as e:
    print(e)
    # => "[101] エラー発生!"
```

## リファレンス

- [Build-in Exceptions - docs.python.org](https://docs.python.org/3/library/exceptions.html)
- [try文 - docs.python.org](https://docs.python.org/ja/3/reference/compound_stmts.html#the-try-statement)
