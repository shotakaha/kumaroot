# Pythonパッケージしたい（``rye``）

```console
$ rye add pandas
$ rye add --dev ipykernel
$ rye add --dev sphinx
$ rye sync
```

```console
$ rye add polars
$ rye add --dev ipykernel
$ rye add --dev mystmd
$ rye sync
```

## インストールしたい（``rye``）

```console
$ brew install rye

$ which rye
/opt/homebrew/bin/rye

$ rye --version
rye 0.31.0
commit: 0.31.0 (2024-03-22)
platform: macos (aarch64)
self-python: cpython@3.12.2
symlink support: true
uv enabled: true
```

## 初期化したい（``init``）

```console
$ rye init .
success: Initialized project in プロジェクトのパス.
  Run `rye sync` to get started

$ ls -1a
.git/
.gitignore
.python-version
README.md
pyproject.toml
src/
```

``rye init .``でプロジェクトを``rye``で管理できるようにします。
``pyproject.toml``をはじめ、必要なファイルが生成されます。
Pythonのバージョンは``.python-version``に保存されます。

:::{caution}

すでに``pyproject.toml``が存在している場合は、初期化に失敗します。
``poetry``からの移行を考えているプロジェクトで、一時的に共存させたかったのですが、簡単にはできないみたいです。

:::

## Pythonのバージョンを固定する（``pin``）

```console
$ rye pin 3.11
$ rye run python3 --version
Python 3.11.8
```
