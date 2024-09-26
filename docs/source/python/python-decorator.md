# デコレーターしたい（`@decorator`）

```python
@デコレーター名
def 関数名(引数):
    ...
```

`@デコレーター名`で、関数やクラス本体の処理は変更せずに、補足処理を追加できます。

## デコレーターを書きたい

```python
from functools import wraps

def decorator_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs)
        ...前処理
        result = f(*args, **kwargs)  # 元の関数を実行
        ...処理
        return result  # 元の関数の実行結果
    return wrapper
```

デコレータを自作するときのテンプレートのようなものを用意しました。

デコレーターの正体は **高階関数** で、引数が関数オブジェクトになっていて、返り値も内部処理した関数オブジェクトになっています。

まず、デコレーター関数（`decorator_name`）の引数を任意の関数（`f`）とします。
そして、デコレーター関数の中に、
ラッパー関数（`wrapper`）を作成します。
ラッパー関数の引数は可変長配列（`(*args, **kwargs)`）にし、
元の関数の引数を受け取れるようにします。
また、ラッパー関数の返り値は、元の関数の実行値にします。
最後に、ラッパー関数オブジェクトを、デコレーター関数の返り値とします。

このデコレーター関数（`decorator_name`）の返り値を
ラッパー関数（`wrapper`）オブジェクトにするのがポイントです。

:::{hint}

ラッパー関数には`@functools.wraps`デコレーターを使っています。
このデコレーターを使うことで、
元の関数のメタデータ情報（`__name__`、`__doc__`など）を
引き継ぐ（残す？）ことができます。

:::

以下では、作っておくとちょっと便利になるデコレーターを考えてみました。
動作確認していないものもあります。動かなかった場合は、教えてください。

## ストップウォッチしたい

```python
import time
from functools import wraps

def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = f(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{f.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

@timer
def some_function(...):
    ...
    return ...
```

関数の実行時間を計測したい場合のデコレーターです。
`@timer`デコレーターで、任意の関数の実行時間を標準出力で確認できます。

`time.perf_counter`を使うことで、より高精度な実行時間を取得できます。
また、CPUの実行時間だけを取得したい場合は`time.process_time`に置き換えればOKです。

## リトライしたい

```python
import time
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    time.sleep(delay)
            raise Exception(f"Function {f.__name__} failed after {max_retries} retries.")
        return wrapper
    return decorator

@retry
def some_function(引数):
    ...
    return
```

例外が発生する可能性がある処理に対して、リトライ機能を追加するデコレーターです。

## リファレンス

- [functools - docs.python.org](https://docs.python.org/3/library/functools.html)
- [関数定義 - docs.python.org](https://docs.python.org/ja/3/reference/compound_stmts.html#function)
- [クラス定義 - docs.python.org](https://docs.python.org/ja/3/reference/compound_stmts.html#class)
- [PEP318 - peps.python.org](https://peps.python.org/pep-0318/)
