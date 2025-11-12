# 仮想環境したい（`venv`）

```console
# プロジェクトルートを作成する／移動する
$ mkdir -p path/to/your_project
$ cd path/to/your_project

# 仮想環境を作成する
$ python3 -m venv .venv

# 仮想環境を有効にする
$ source .venv/bin/activate
(.venv) $

# 仮想環境を無効にする
(.venv) $ deactivate
$
```

`venv`パッケージで、仮想環境を作成できます。
Python3.3以降に付属する標準モジュールです。
コマンドでは`python3 -m venv`の形でモジュールとして呼び出す必要があります。

:::{note}

**仮想環境が必要な理由：** Pythonパッケージ（ライブラリ）は通常、プロジェクトごとに異なるバージョンが必要です。システム全体にインストールすると、複数のプロジェクト間でバージョン競合が起きます。仮想環境を使うことで、各プロジェクトが独立した環境を持つことができます。

**現在の推奨方法：** 最近のPythonでは、システムグローバルにパッケージをインストールすることは非推奨です。すべてのパッケージを仮想環境にインストールする方法が推奨されています。これにより、プロジェクト間の依存関係の競合を防ぎ、環境を再現性よく管理できます。

:::

## 他ツールと比較したい

`venv`とその他の仮想環境パッケージとの比較を整理しました。

| ツール名 | 基本コマンド | 特長 |
|---|---|---|
| `venv` | `python3 -m venv .venv` | Python3.3以降の標準で軽量なパッケージ |
| `virtualenv` | `virtualenv venv` | `venv`より柔軟性があり、Python2系でも利用できるパッケージ |
| `pipenv` | `pipenv install` | `Pipfile`を使用し、仮想環境と依存関係の管理を統合できるパッケージ |
| `pyenv` | `pyenv install 3.11.4` | 複数のPython実行環境を管理できるパッケージ |
| `pyenv-virtualenv` | `pyenv virtualenv 3.11.4 venv` | `pyenv`を拡張子、実行環境ごとの仮想環境を作成できるパッケージ |

:::{tip}

`venv` はPythonの実行環境の切り替えはできません。
呼び出し時に
`python3.11 -m venv`、
`python3.12 -m venv`、
と実行環境を切り替えるか、
`pyenv`などと併用する必要があります。

最近では、これらの機能が統合された
[uvパッケージ](./python-uv.md)
を利用するのがオススメです。

:::
