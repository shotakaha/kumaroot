# 型チェックしたい（`pyright`）

```console
$ pyright --version
pyright 1.1.383

$ pyright ファイル名 or ディレクトリ名
```

`pyright`はMicrosoftが開発しているPython用の型チェッカーです。
`Pylance`でも使用されているためVS Codeでも利用できます。

## インストールしたい（`pyright`）

- `pipx`でインストール

```console
$ pipx install pyright
```

- `poetry`でインストール

```console
$ poetry add pyright --dev test
```

- `uv`でインストール

```console
$ uv tool install pyright
```

## リファレンス

- [Pyright](https://microsoft.github.io/pyright/#/)
