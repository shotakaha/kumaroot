# 例外処理したい（`try...except...finally` / `raise`）

```python
try:
    例外が発生するかもしれない処理
except 例外の種類 as オブジェクト名:
    例外が発生したときの処理
except KeyboardInterrupt as e:
    print("中断しました")
    sys.exit(0)  # Ctrl-cを補足して正常終了
except Exception as e:
    基本的な例外が発生したときの処理
    print(f"Error: {e}")
    print(f"{e.args=}")
    sys.exit(1)  # 想定外のエラーで異常終了
finally:
    例外の有無に関係なく実行する処理
```

``try..except..finally``構文を使って例外処理（＝エラーハンドリング）できます。
`except`処理は複数回記述でき、`finally`処理は省略できます。

**例外の種類**には
Pythonにビルトインの例外クラス名、もしくはカスタムした例外クラス名を指定します。
また、発生した例外を**オブジェクト名**で受け取っておくと、
例外をさらにコントロールできます。
オブジェクト名には`e`や`err`を使うことが多いです。

例外処理は、親クラスの名前でも補足できます。
利用可能なビルトイン例外とその階層構造の詳細は
[exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
を参照してください。

:::{hint}

```python
def main():
    try:
        ...
    except Exception as e:
        基本的な例外が発生したときの処理
    except BaseException as e:
        KeyboardInteruptなどExceptionで捕捉できない例外が発生したときの処理
```

例外処理は、基本的に`main`関数に実装します。

:::

## 例外を送出したい（`raise`）

```python
if 条件確認:
    条件が正しいときの処理
else:
    raise 例外クラス名
```

`raise`を例外を送出（＝throw）できます。
例外クラス名は、ビルトインの例外クラスが使えます。
また、カスタムした例外クラスも作成できます。

自作パッケージを作成している場合、
適切な例外を発生させることで、ユーザー（自分自身を含む）に
優しいパッケージになります。

## `raise` or `sys.exit`

例外（＝エラー）が発生するとき、
`raise`するか、
`sys.exit`するかを考える必要があります。
一般的に、
ライブラリ（やサブ関数）の中では`raise`し、
CLI（やメイン関数）で例外をキャッチして`sys.exit`
すればよさそうです。

インポートして利用するパッケージの場合、
パッケージ内部で`sys.exit`されていると、
パッケージのユーザーはそこから先、どうすることもできません。
しかし、適切な例外が`raise`されていれば、
その例外処理をどうすべきか（キャッチして対処するのか、そのまま握り潰すのか、など）
ユーザーが判断できます。

```python
def func1():
    """サブ関数: 条件にマッチしない場合 ValueErrorを送出
    """
    if 条件:
        条件が正しいときの処理
        return
    else:
        # ここではsys.exitせずにraiseする
        msg = "値がおかしいよ"
        raise ValueError(msg)

def func2():
    ...
    if 条件:
        ...
    else:
        msg = "接続失敗"
        raise ConnectionError(msg)

def main():
    try:
        func1()
        func2()
    except ValueError as e:
        print(f"Error: {e}")
        print(f"{e.args=}")
        sys.exit()
    except ConnectionError as e:
        print(f"Error: {e}")
        print(f"{e.args=}")
        sys.exit()
    except KeyboardInterrupt as e:
        print(f"Error: {e}")
        print(f"{e.args=}")
        sys.exit()

if __name__ == "__main__":
    main()
```

このサンプルは、僕がスクリプトやパッケージを作成するときのテンプレ的なものです。
`raise`された例外は親の関数にも伝播します。
インポートした外部パッケージで例外が適切に送出されている場合、
サブ関数の中では`try...except`せずにそのままにしておけばOKです。

## よく遭遇する例外と確認事項

例外が発生した場合、まずエラーメッセージをきちんと確認することが大切です。
どの例外が、どのファイル（のどのあたり）で発生したかを把握することで、
その理由を考えたり、対応方法を考えたりできます。

以下に遭遇しがちなビルトイン例外と、そのときの確認事項を整理してみました。

:ImportError / ModuleNotFoundError:
モジュールのインポートが正しくない場合に発生します。
モジュール名が正しいか、モジュールがインストールされているか、Python実行環境のパスが正しいか、確認しましょう。

:AttributeError / KeyError / IndexError / ValueError:
オブジェクト操作が正しくない場合に発生します。
リストの長さをオーバーしていないか、辞書型にないキーを指定していないか、確認しましょう。

:NameError:
変数名が正しくないときに発生します。
変数の定義を忘れていないか、変数名にスペルミスがないか、確認しましょう。

:SyntaxError / IndentationError:
文法や構文が正しくないときに発生します。
インデントがずれていないか、条件文の末尾の`:`を忘れていないか、確認しましょう。

:FileExistsError / FileNotFoundError:
ファイル操作が正しくないときに発生します。
ファイル名が正しいか、既存のファイルが存在していないか、確認しましょう。

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
    response.raise_for_status()
except requests.exception.RequestException as e:
    print(f"Error: {e}")
```

外部パッケージによっては、パッケージ独自の例外クラスがあります。
上記サンプルは、[requests](./python-requests.md)パッケージの例外処理です。
このように、パッケージによっては、カスタムの例外クラスが定義されてます。
詳細はパッケージのドキュメントを確認してください。

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
