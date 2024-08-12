# パッケージ管理したい（``pipx``）

```console
$ pipx install パッケージ名
$ pipx upgrade パッケージ名
$ pipx uninstall パッケージ名
```

仮想環境でパッケージを管理すう場合は``pipx``コマンドを使います。
``pipx``は``Homebrew``を使ってインストールします。

```console
$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

## シェル補完したい

```console
$ register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```

``pipx``コマンドのシェル補完が使えるようにすると便利です。

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

Python本体を更新したあとは再インストールが必要です。
``reinstall-all``を使って、すべてのパッケージを再インストールできます。

## インストールしたパッケージ

```console
$ pipx install poetry
$ pipx install commitizen
$ pipx install jupyter --include-deps
```

``jupyter``は、いろいろなサブパッケージに分割されているようです。
必要なサブパッケージがわかっていたら、そちらを直接指定すればよいです。
とりあえず全部でよい場合は``--include-deps``でインストールできます。
