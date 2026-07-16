# サブプロセスしたい（`subprocess`）

```python
import subprocess
subprocess.run(コマンド)
subprocess.run(["ls", "-l"])
```

Pythonのスクリプトの中でシェルコマンドなどを使う場合、[subprocess](https://docs.python.org/ja/3/library/subprocess.html)モジュールを使います。
実行するコマンドは引数やオプションも含めてリスト型で指定できます。

:::{note}

古い`os.system`や`subprocess.call`、`subprocess.Popen`を直接使う書き方も存在しますが、
現在は`subprocess.run`を使うのが推奨されています。
戻り値のオブジェクトを通じて、実行結果、標準出力、エラーなどをまとめて扱えます。

:::

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

:::{note}

`text=True`を指定しないと、`result.stdout`、`result.stderr`は`bytes`型で返ってきます。
文字列（`str`）として扱いたい場合は`text=True`を指定してください

:::

## 例外処理したい（`CalledProcessError`）

```python
import subprocess

try:
    result = subprocess.run(コマンド, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
```

`check`オプションを有効にすると、コマンドが失敗したときに例外を発生させることができます。
`subprocess`は`CalledProcessError`という例外クラスを持っています。

## シェル経由で実行したい（`shell=True`）

```python
subprocess.run("ls -l | grep py", shell=True)
```

`shell=True`を指定すると、パイプ（``|``）やリダイレクト（``>``）のような
シェル機能を含む文字列コマンドをそのまま実行できます。

:::{caution}

`shell=True`は、コマンドの一部にユーザー入力をそのまま含めると、
**シェルインジェクション**の脆弱性につながります
（例：``f"ls {user_input}"``のような組み立て方）。
ユーザー入力を扱う場合は、`shell=True`を避け、
冒頭のようにコマンドをリスト型で渡す書き方を使ってください。

:::

## 標準入力したい（`input`）

```python
result = subprocess.run(["grep", "py"], input="foo.py\nbar.txt\n", text=True, capture_output=True)
result.stdout
```

`input`オプションで、コマンドの標準入力にデータを渡せます。
`text=True`と組み合わせることで、文字列のまま渡せます。

## タイムアウトしたい（`timeout`）

```python
import subprocess

try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired as e:
    print(f"Timeout: {e}")
```

`timeout`オプションで、コマンドの実行時間の上限を秒数で指定できます。
上限を超えると`TimeoutExpired`例外が発生し、プロセスは自動的に終了させられます。
ハングする可能性のある外部コマンドを呼び出す場合は、設定しておくと安全です。
