# パッケージ管理したい（``pipx``）

```console
$ pipx install パッケージ名
$ pipx upgrade パッケージ名
$ pipx uninstall パッケージ名
```

`pipx`は実行ファイルをローカルな仮想環境にインストールするツールです。
`Homebrew`でインストールできます。

:::{caution}

`pipx`でインストールできるのはコマンドラインツールとして利用できるパッケージのみです。
`pandas`などライブラリとして利用するパッケージはインストールできません。

:::

## 設定したい（`ensurepath`）

```console
$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

`pipx`をインストールしたら、初回のみ、パスの設定が必要です。
`pipx ensurepath`で、シェルによらず、PATHに`$HOME/.local/bin`が追加されます。

:::{note}

`pipx`は「グローバルに使うCLI」なので、Homebrewでインストールすると管理が簡単です。
また、基本的に`pip`ではインストールしない方がよいと思います。

ただし、GitLab CIなど一時的な実行環境で使う場合は、`pip install pipx`がシンプルでよいです。

:::

## シェル補完したい

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

## 一括で更新したい（``upgrade-all``）

```console
$ pipx upgrade-all
upgraded package ruff from 0.1.4 to 0.1.5 (location: ~/.local/pipx/venvs/ruff)
upgraded package streamlit from 1.28.1 to 1.28.2 (location: ~/.local/pipx/venvs/streamlit)
upgraded package poetry from 1.7.0 to 1.7.1 (location: ~/.local/pipx/venvs/poetry)
upgraded package mypy from 1.6.1 to 1.7.0 (location: ~/.local/pipx/venvs/mypy)
upgraded package pyright from 1.1.335 to 1.1.336 (location: ~/.local/pipx/venvs/pyright)
```

``upgrade-all``オプションを使って、すべてのパッケージを更新できます。
定期的に実行しておくとよいと思います。

## 一括で再インストールしたい（``reinstall-all``）

```console
$ pipx reinstall-all
```

Python本体を更新した場合、パッケージの再インストールが必要です。
``reinstall-all``を使って、すべてのパッケージを再インストールできます。

## インストールしたパッケージ

```console
$ pipx install commitizen
$ pipx install jupyter --include-deps
$ pipx install jupytext
$ pipx install mystmd
$ pipx install poetry
$ pipx install pytest
$ pipx install ruff
$ pipx install sphinx
$ pipx install sphinx-autobuild
$ pipx install streamlit

```

``jupyter``は、いろいろなサブパッケージに分割されているようです。
必要なサブパッケージがわかっていたら、そちらを直接指定すればよいです。
とりあえず全部でよい場合は``--include-deps``でインストールできます。

## 環境変数をしりたい（``environment``）

```console
$ pipx environment
Environment variables (set by user):

PIPX_HOME=
PIPX_BIN_DIR=
PIPX_MAN_DIR=
PIPX_SHARED_LIBS=
PIPX_DEFAULT_PYTHON=
PIPX_FETCH_MISSING_PYTHON=
USE_EMOJI=

Derived values (computed by pipx):

PIPX_HOME=~/.local/pipx
PIPX_BIN_DIR=~/.local/bin
PIPX_MAN_DIR=~/.local/share/man
PIPX_SHARED_LIBS=~/.local/pipx/shared
PIPX_LOCAL_VENVS=~/.local/pipx/venvs
PIPX_LOG_DIR=~/.local/pipx/logs
PIPX_TRASH_DIR=~/.local/pipx/trash
PIPX_VENV_CACHEDIR=~/.local/pipx/.cache
PIPX_STANDALONE_PYTHON_CACHEDIR=~/.local/pipx/py
PIPX_DEFAULT_PYTHON=/opt/homebrew/opt/python@3.12/libexec/bin/python
USE_EMOJI=true
```

``environment``コマンドで、``pipx``で有効な環境変数を確認できます。
Python環境は、マシンによって異なる場合があります。
ツールがうまく動かない場合の確認作業に役立つかもしれません。
