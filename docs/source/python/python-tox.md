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

## 複数の自動テストを組み合わせたい

```toml
env_list = ["py311", "py312", "lint"]

[env_run_base]
deps = ["pytest"]
commands = [["pytest"]]

[env.lint]
deps = ["ruff"]
commands = [["ruff", "check", "."]]
```

`env_list`に複数の環境名を並べると、`tox`コマンド1つでそれぞれが順番に実行されます。
`py311`、`py312`のような`py<バージョン>`という名前の環境は、
`[env_run_base]`の設定（共通の依存・コマンド）を使ってそのPythonバージョンで実行されます。
`lint`のような任意の名前の環境は、`[env.<環境名>]`で個別に依存やコマンドを上書きできます。
上記の例では、Python 3.11と3.12でそれぞれ`pytest`を実行しつつ、
`lint`環境で`ruff check .`を実行しています。

```console
$ tox
...
  py311: OK (3.25=setup[2.24]+cmd[1.01] seconds)
  py312: OK (1.83=setup[1.31]+cmd[0.52] seconds)
  lint: OK (1.86=setup[1.50]+cmd[0.36] seconds)
  congratulations :) (6.95 seconds)
```

すべての環境が成功すると、最後にサマリーが表示されます。
Pythonバージョンごとのユニットテストと、リンター・型チェックなど種類の異なるチェックを、
まとめて1コマンドで実行できるのが`tox`の強みです。

## リファレンス

- [tox](https://tox.wiki/)
