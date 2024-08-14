# パッケージ管理したい（``pipx``）

```console
$ pipx install パッケージ名
$ pipx upgrade パッケージ名
$ pipx uninstall パッケージ名
```

仮想環境でパッケージを管理する場合は``pipx``コマンドを使います。
``pipx``は``Homebrew``を使ってインストールします。

```console
$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

``pipx``をインストールしたら、初回のみ``ensurepath``します。
シェルによらずこのコマンドで、PATHに``$HOME/.local/bin``が追加されます。

## シェル補完したい

```console
$ register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```

``pipx``コマンドのシェル補完が使えるようにすると便利です。

## パッケージを一覧したい（``list``）

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

``list``でインストールしたパッケージを一覧できます。
仮想環境（``venv``）のパスや、
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
$ pipx install poetry
$ pipx install commitizen
$ pipx install sphinx
$ pipx install sphinx-autobuild
$ pipx install mystmd
$ pipx install jupyter --include-deps
$ pipx install ruff
$ pipx install pytest

```

``jupyter``は、いろいろなサブパッケージに分割されているようです。
必要なサブパッケージがわかっていたら、そちらを直接指定すればよいです。
とりあえず全部でよい場合は``--include-deps``でインストールできます。
