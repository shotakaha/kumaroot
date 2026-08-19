# 仮想環境したい（``nodeenv``）

```console
$ pip3 install nodeenv
$ nodeenv node_env
$ source node_env/bin/activate
(node_env) $ node --version
(node_env) $ deactivate_node
```

Nodeの仮想環境を構築できます。
[MyST](../myst/myst-usage.md)のようにNode依存があるパッケージも、Pythonパッケージと同じように環境構築できます。
CI環境と組み合わせて使います。

:::{note}

無効化コマンドは`deactivate`ではなく`deactivate_node`です。
Pythonの`venv`と混同しないように注意してください。

:::

## 利用できるバージョンを確認したい

```console
$ nodeenv --list
```

## バージョンを指定したい（`-n` / `--node`）

```console
$ nodeenv -n 20.0.0 node_env  // 特定バージョンを指定
$ nodeenv -n lts node_env     // 最新のLTS版を指定
$ nodeenv -n system node_env  // システムのnodeを使う
```

`-n`（`--node`）オプションで、インストールするNode.jsのバージョンを指定できます。
省略した場合は最新版（`latest`）がインストールされますが、
プロジェクトによってはバージョンを固定しておきたい場合が多いので、
`-n lts`や具体的なバージョン番号を指定しておくのがオススメです。

## Python仮想環境と統合したい（`-p` / `--python-virtualenv`）

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ nodeenv -p
```

`-p`（`--python-virtualenv`）オプションで、
すでに有効化されているPythonの仮想環境（`venv`）に、Node.js環境を統合できます。
新しく仮想環境を作らず、既存の`.venv/bin/activate`（と`activate.fish`）にNode.js用の設定が追記されます。

これにより、`source .venv/bin/activate`を1回実行するだけで、
PythonとNode.jsの両方の環境を同時に有効化できます。
[MyST](../myst/myst-usage.md)のように、PythonパッケージとNode依存パッケージを両方使うプロジェクトで便利です。

:::{caution}

`-p`オプションは、現在有効化されている仮想環境の`activate`スクリプトを直接書き換えます。
間違った仮想環境を有効化した状態で実行しないように注意してください。

:::
