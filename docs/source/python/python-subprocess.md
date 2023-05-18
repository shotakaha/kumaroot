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
r = subprocess.run(["ls", "-l"], capture_output=True, text=True)

type(r)
r.args
r.returncode
r.stdout
r.stderr
```

``subprocess.run``の戻り値は``CompletedProcess``オブジェクトです。
戻り値を変数に代入すれば、このオブジェクトを通じて実行結果を確認できます。
