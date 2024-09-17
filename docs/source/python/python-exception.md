# 例外処理したい（`try...except...`）

```python
try:
    例外が発生するかもしれない処理
except 例外クラス名 as オブジェクト名:
    例外が発生したときの処理
except Exception as e:
    基本的な例外が発生したときの処理
```

``try..except..``構文を使って例外処理できます。
**例外クラス名**にはPythonにビルトインの例外クラス名、もしくは
カスタムした例外クラス名を指定します。
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

## 中断処理したい（`KeyboardInterrupt`）

```python
try:
    例外が発生するかもしれない処理
except KeyboardInterrupt as e:
    中断処理
    # バッファーの内容をファイルに保存する、など
    sys.exit()
```

`KeyboardInterrupt`クラスで、中断処理（{kbd}`ctrl-c`）したときの例外処理ができます。
中断処理すると、そのときバッファーにあるデータなどは破棄されます。
長時間走らせるようなスクリプトや、CLIツールには必ず中断処理を書いて、
安全に終了できるようにしましょう。

## カスタム例外処理したい

```python
try:
    response = requests.get("https://httpbin.org/status/404")
except requests.exception.RequestException as e:
    print(e)
```

上記サンプルは、[requests](./python-requests.md)パッケージの例外処理です。
このように、パッケージによっては、カスタムの例外クラスが定義されてます。
詳細はパッケージのドキュメントを確認してください。

## 例外クラスを自作したい（``Exception``）

```python
class CustomError(Exception):
    """自作の例外クラス"""
```

例外クラスを自作する場合、`Exception`クラスを継承します。
小規模なスクリプトでは、ビルトインの例外クラスで十分対応できると思うので、
わざわざ例外クラスを自作する必要はありません。

もし、中規模〜大規模なパッケージを開発している場合には、
以下のようなユースケースで、自作を検討したほうがいいかもしれません。

1. 特定の例外シナリオに対処したい
2. 例外処理をカプセル化したい
3. 他の例外と区別したい

## リファレンス

- [Build-in Exceptions](https://docs.python.org/3/library/exceptions.html)