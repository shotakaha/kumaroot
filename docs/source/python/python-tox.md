# 自動テストしたい（`tox`）

```console
$ tox --version
4.21.2 from [PATH]

$ tox
```

`tox`は複数のテストを組み合わせて自動化できるツールです。
`tox.ini`もしくは`pyproject.toml`で設定します。

Pythonのランタイムごとに仮想環境を作成し、
フォーマッター＆リンター、
型チェック、
ユニットテストのすべてを`tox`コマンドひとつで実行できるようになります。

## インストールしたい（`tox`）

- `pipx`でインストール

```console
$ pipx install tox
```

- `poetry`でインストール

```console
$ poetry add tox --group test
```

- `uv`でインストール

```console
$ uv tool install tox
```

## リファレンス

- [tox](https://tox.wiki/)
