# 仮想環境したい（``nodeenv``）

```console
$ pip3 install nodeenv
$ nodeenv node_env
$ source node_env/bin/activate
(node_env) $ # 仮想環境
```

Nodeの仮想環境を構築できます。
[MyST](../myst/myst-usage.md)のようにNode依存があるパッケージも、Pythonパッケージと同じように環境構築できます。
CI環境と組み合わせて使います。

## 利用できるバージョンを確認したい

```console
$ nodeenv --list
```
