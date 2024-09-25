# デコレーターしたい（`@decorator`）

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

デコレーターは、関数本体の処理は変更せずに、補足処理を追加できる機能です。
その正体は「高階関数」で、関数の中で関数を実行しています。

上のサンプルは、デコレータを自作するときのテンプレートです。
デコレーター関数（`decorator_name`）の中にで、
ラッパー関数（`wrapper`）を定義していて、
デコレーター関数（`decoretor_name`）の返り値が
ラッパー関数（`wrapper`）になっているのがポイントです。

また、`@functools.wraps`を使うことで、元の関数のメタデータ情報（`__name__`、`__doc__`など）を引き継ぐことができます。
（内部処理は確認していませんが、とりあえず使っておけばOKです）

ラッパー関数（`wrapper`）の引数は`(*args, **kwargs)`の可変長配列にすることで、任意の関数をデコレートできるようになります。

ここでは、作っておくとちょっと便利になるデコレーターを考えてみました。
動作確認していないものもあります。
動かなかった場合は、教えてください。

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

関数の実行時間を計測したいケースはよくあると思います。
`@timer`デコレーターで、任意の関数の実行時間を標準出力で確認できます。
`time.perf_counter`を使うことで、より高精度な実行時間を取得できます。
また、CPUの実行時間だけを取得したい場合は`time.process_time`を使うとよいらしいです。

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

## リファレンス

- [functools](https://docs.python.org/3/library/functools.html)
