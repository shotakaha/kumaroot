# 実行パスを確認したい（``which``）

```console
$ which コマンド名
$ which python3
/opt/homebrew/bin/python3
```

``which``でコマンドの実行パスを確認できます。
コマンドが見つからないときや、思った挙動をしないときは、実行パスが正しいか確認しましょう。

## すべての実行パスを確認したい（``-a``）

```console
$ which -a コマンド名
$ which -a python3
/opt/homebrew/bin/python3    # HomebrewでインストールしたPython3
/usr/bin/python3             # macOSデフォルトのPython3
```

``-a``オプションで、すべてのパスを表示できます。
コマンドは優先順位の高い順に表示されます。

Homebrewやその他のツールでコマンドを追加した場合に、
コマンドの実行パスを確認したいときに使います。
