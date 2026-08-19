# 自動テストしたい（`tox`）

```console
$ tox --version
4.60.0 from [PATH]

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

## 設定したい（`tox.toml`）

```toml
env_list = ["py312"]

[env_run_base]
deps = ["pytest"]
commands = [["pytest"]]
```

プロジェクトルートに`tox.toml`を配置すると、TOML形式で設定を書けます。
`env_list`でテストするPython環境（`envlist`のTOML版）を指定します。
`[env_run_base]`（`[testenv]`のTOML版）に、各環境で共通のインストールパッケージや実行コマンドを書きます。
`commands`は、1つのコマンドを文字列の配列として書き、それをさらに配列で囲みます。

:::{note}

従来の`tox.ini`（INI形式）も引き続き使えます。
`pyproject.toml`の`[tool.tox]`セクションに、
`legacy_tox_ini`というキーで`tox.ini`の内容を文字列としてまるごと埋め込むこともできますが、
TOMLの中にINIを文字列として書く形になるため、素直に`tox.toml`を使う方がわかりやすいです。

:::

## リファレンス

- [tox](https://tox.wiki/)
