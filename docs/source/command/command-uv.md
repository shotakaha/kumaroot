# パッケージ管理したい（`uv`）

```console
$ uv add typer
$ uv add ruff --group dev
$ uv add zensical --group docs
```

`uv`は、Pythonのパッケージ管理コマンドです。
プロジェクト内に自動で仮想環境が作成され、パッケージはその中にインストールされます。

詳細は[](../python/python-uv.md)を参照してください。

## インストールしたい（`uv`）

```console
$ brew install uv

$ uv --version
uv 0.12.5 (Homebrew 2026-08-14 aarch64-apple-darwin)

$ uvx --version
uvx 0.12.5 (Homebrew 2026-08-14 aarch64-apple-darwin)
```

`uv`はHomebrewでインストールできます。
フォーミュラ名は`uv`です。
`uv`と`uvx`コマンドがインストールされます。
