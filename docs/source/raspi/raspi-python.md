# Pythonしたい

```console
$ sudo apt install python3-pip
$ sudo apt install python3-venv
```

## pipxしたい

```console
$ sudo apt install pipx
$ pipx ensurepath
$ pipx --version
```

## uvしたい

```console
$ pipx install uv
$ uv --version
$ uvx --version
```

`uv`は`apt`パッケージが存在しないため、`pipx`を使ってインストールします。

## ruffしたい

```console
$ uv tool install ruff
$ ruff --version
```

## pre-commitしたい

```console
$ uv tool install pre-commit
$ pre-commit --version
```
