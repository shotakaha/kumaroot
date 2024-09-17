# サブプロセスしたい（``subprocess``）

```python
import subprocess
subprocess.run(コマンド)
subprocess.run(["ls", "-l"])
```

Pythonのスクリプトの中でシェルコマンドなどを使う場合、[subprocess](https://docs.python.org/ja/3/library/subprocess.html)モジュールを使います。
実行するコマンドは引数やオプションも含めてリスト型で指定できます。

## 実行結果を確認したい

```python
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

type(result)  # CompletedProcess
result.args
result.returncode
result.stdout
result.stderr
```

``subprocess.run``の戻り値は``CompletedProcess``オブジェクトです。
戻り値を変数に代入すれば、このオブジェクトを通じて実行結果を確認できます。

`capture_output`オプション、`text`オプションを有効にすると、
標準出力や標準エラー出力に表示された内容を確認できます。

## 例外処理したい（``CalledProcessError``）

```python
import subprocess

try:
    result = subprocess.run(コマンド, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
```

`check`オプションを有効にすると、コマンドが失敗したときに例外を発生させることができます。
`subprocess`は`CalledProcessError`という例外クラスを持っています。
