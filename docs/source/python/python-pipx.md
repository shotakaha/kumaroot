# パッケージ管理したい（`pipx`）

```console
$ pipx install パッケージ名
$ pipx upgrade パッケージ名
$ pipx uninstall パッケージ名
```

`pipx`は実行ファイルをローカルな仮想環境にインストールするツールです。
最近の`pipx`は、仮想環境の管理に[uv](./python-uv.md)を使っています。
`uv`がインストールされていない場合は、`pip`が使われます。

:::{caution}

`pipx`でインストールできるのはコマンドラインツールとして利用できるパッケージのみです。
`pandas`などライブラリとして利用するパッケージはインストールできません。

:::

## インストールしたい（`pipx`）

```console
$ brew install pipx
$ pipx ensurepath
```

`pipx`はHomebrewでインストールできます。
インストールした後は一度だけ`pipx ensurepath`を実行し、パスを設定する必要があります。
利用しているシェルを自動判別し、PATHに`$HOME/.local/bin`が追加されます。

:::{note}

`pipx`は「グローバルに使うCLI」なので、Homebrewでインストールすると管理が簡単です。
また、基本的に`pip`ではインストールしない方がよいと思います。

ただし、GitLab CIなど一時的な実行環境で使う場合は、`pip install pipx`がシンプルでよいです。

:::

## シェル補完したい（`completions`）

```console
$ pipx completions
```

`pipx completions`コマンドで、使っているシェルに応じたシェル補完の設定方法を確認できます。
案内された通りにコマンドを実行するか、シェルの設定ファイルに追記します。

fishの場合は、次のコマンドを一度だけ実行すればOKです。

```console
$ register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```

`register-python-argcomplete`でシェル補完機能を追加できます。
シェル上で`pipx`コマンドが補完されるようになるのでとても便利です。

## パッケージを一覧したい（`list`）

```console
$ pipx list
venvs are in ~/.local/pipx/venvs
apps are exposed on your $PATH at ~/.local/bin
manual pages are exposed at ~/.local/share/man
shell completions are exposed at ~/.local/share
   package commitizen 3.29.0, installed using Python 3.12.2
    - cz
    - git-cz
   package mystmd 1.3.4, installed using Python 3.12.5
    - myst
   package poetry 1.8.3, installed using Python 3.12.3
    - poetry
```

`pipx list`でインストールしたパッケージを一覧できます。
仮想環境（`venv`）のパスや、
インストールに使ったPythonのバージョン、
一緒にインストールされた依存パッケージの名前なども確認できます。

## 一括で更新したい（`upgrade-all`）

```console
$ pipx upgrade-all
upgraded package ruff from 0.1.4 to 0.1.5 (location: ~/.local/pipx/venvs/ruff)
upgraded package streamlit from 1.28.1 to 1.28.2 (location: ~/.local/pipx/venvs/streamlit)
upgraded package poetry from 1.7.0 to 1.7.1 (location: ~/.local/pipx/venvs/poetry)
upgraded package mypy from 1.6.1 to 1.7.0 (location: ~/.local/pipx/venvs/mypy)
upgraded package pyright from 1.1.335 to 1.1.336 (location: ~/.local/pipx/venvs/pyright)
```

`pipx upgrade-all`で、すべてのパッケージを更新できます。
定期的に実行しておくとよいと思います。

## 一括で再インストールしたい（`reinstall-all`）

```console
$ pipx reinstall-all
```

`pipx reinstall-all`コマンドで、すべてのパッケージを再インストールできます。
Python本体を更新した場合、パッケージの再インストールが必要です。


## 環境変数をしりたい（`environment`）

```console
$ pipx environment
Environment variables (set by user):

PIPX_HOME=
PIPX_GLOBAL_HOME=
PIPX_BIN_DIR=
PIPX_GLOBAL_BIN_DIR=
PIPX_MAN_DIR=
PIPX_COMPLETION_DIR=
PIPX_GLOBAL_MAN_DIR=
PIPX_GLOBAL_COMPLETION_DIR=
PIPX_SHARED_LIBS=
PIPX_DEFAULT_PYTHON=
PIPX_DEFAULT_BACKEND=
PIPX_COOLDOWN=
PIPX_FETCH_MISSING_PYTHON=
PIPX_FETCH_PYTHON=
PIPX_DISABLE_SHARED_LIBS_AUTO_UPGRADE=
PIPX_USE_EMOJI=
PIPX_MAX_LOGS=

Derived values (computed by pipx):

PIPX_HOME=~/.local/pipx
PIPX_BIN_DIR=~/.local/bin
PIPX_MAN_DIR=~/.local/share/man
PIPX_COMPLETION_DIR=~/.local/share
PIPX_SHARED_LIBS=~/.local/pipx/shared
PIPX_LOCAL_VENVS=~/.local/pipx/venvs
PIPX_LOG_DIR=~/Library/Logs/pipx
PIPX_TRASH_DIR=~/.local/pipx/.trash
PIPX_VENV_CACHEDIR=~/.cache/pipx
PIPX_STANDALONE_PYTHON_CACHEDIR=~/.local/pipx/py
PIPX_DEFAULT_PYTHON=/opt/homebrew/opt/python@3.15/bin/python3.15
PIPX_RESOLVED_BACKEND=uv
PIPX_BACKEND_SOURCE=auto-path
PIPX_UV_BINARY=~/.local/share/mise/shims/uv
UV_CACHE_DIR=
PIPX_DISABLE_SHARED_LIBS_AUTO_UPGRADE=false
PIPX_USE_EMOJI=true
```

`pipx environment`コマンドで、`pipx`で有効な環境変数を確認できます。
Python環境は、マシンによって異なる場合があります。
`PIPX_RESOLVED_BACKEND`が`uv`になっている場合は、
`PIPX_UV_BINARY`の実行パスの`uv`を使ってパッケージを管理していることを意味します。
ツールがうまく動かない場合の確認作業に役立つかもしれません。

## リファレンス

- [pipx](https://pipx.pypa.io/)
- [pipx - GitHub](https://github.com/pypa/pipx)
- [pipx - PyPI](https://pypi.org/project/pipx/)
