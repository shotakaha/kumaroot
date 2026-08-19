# フォーマッター／リンターしたい（`ruff`）

```console
$ ruff --version
ruff 0.16.3

$ ruff format
$ ruff check
$ ruff check --statistics
```

``ruff``はRustで書かれたPython用のリンター&フォーマッタです。
これまで``black``、``isort``、``flake8``を組み合わせてできたことをすべて``ruff``に集約できます。
``pyproject.toml``に設定を記述できるため、既存のPythonプロジェクトにも導入しやすいです。

:::{note}

Pythonのリンター＆フォーマッタの変遷は闇が深そうです。
時代とともにベストプラクティスが移り変わっている感じで、
これを使っておけばOKみたいな標準的なモジュールが存在しませんでした。
``ruff``は、そのような悩みを解決してくれるツールです。

:::

## インストールしたい（`ruff`）

- pipでインストール

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install ruff
```

- pipxでインストール

```console
$ pipx install ruff
```

- uv toolでインストール

```console
$ uv tool install ruff
```

- poetryでプロジェクトに追加

```console
$ poetry add ruff --group=dev
```

- uvでプロジェクトに追加

```console
$ uv add ruff --group dev
```

`ruff`はCLIツールなので、`pipx`や`uv tool`でグローバルにインストールできます。
プロジェクトに追加する場合は `--group dev` オプションで追加するとよいです。

## 設定したい（`[tool.ruff]`）

```toml
# pyproject.toml

[tool.ruff]
# 対象となるPythonのバージョン
target-version = "py311"

# 1行あたりの最大文字数
# デフォルトは88。100くらいにしてもよい説がある
line-length = 88

# 未使用importの自動削除
# fix = true

# ruff check の設定
[tool.ruff.lint]
# チェックするルールセット
select = [
    "E",    # pycodestyle (PEP8)
    "F",    # pyflakes（未使用変数・未定義参照など）
    "I",    # import order（importの順序）
    "B",    # bugbear（潜在的なバグ）
    "UP",   # pyupgrade（新しい構文へ自動更新）
    "N",    # pep8-naming（命名規則）
    "C4",   # flake8-comprehensions（内包表記の改善）
    "SIM",  # flake8-simplify（冗長な構文の簡略化）
    "RUF",  # Ruff独自の拡張
]

# チェックしないルールセット
ignore = [
    "E501",    # 行の長さ
]

# 自動修正するルールセット
fixable = ["ALL"]
unfixable = []


# import orderの設定
[tool.ruff.lint.isort]
combine-as-imports = true
known-first-party = ["自作したパッケージ名"]

# ruff formatの設定
[tool.ruff.format]
quote-style = "double"    # ["double" | "single"]
indent-style = "space"    # ["space" | "tab"]
line-ending = "lf"        # ["lf", "crlf", "native"]
skip-magic-trailing-comma = false  # 末尾のカンマを残す（false） | 残さない（true）
docstring-code-format = true  # docstringも整形する（true） | 整形しない（false）
```

Ruffの設定は`pyproject.toml`の`[tool.ruff]`セクションに記述できます。
また、`ruff.toml`、`.ruff.toml`に個別設定として保存することもできます。

## フォーマットしたい（``ruff format``）

```console
$ ruff format
$ ruff format --check
$ ruff format --diff
$ ruff format ファイル名
```

``format``コマンドでフォーマッターとして利用できます。
引数にファイル名を指定したり、確認したいディレクトリで``ruff format .``を指定して実行します。

```toml
[tool.ruff]
line-length = 100

[tool.ruff.format]
quote-style = "double"
```

## リンターしたい（``ruff check``）

```console
$ ruff check .
$ ruff check ファイル名
```

`ruff check`コマンドでリンターを実行します。
引数にファイル名やディレクトリを指定できます。
`ruff check .`でプロジェクト内のすべての該当するファイルを指定できます。

```console
$ ruff check --show-fixes
$ ruff check --fix
```

`--show-fixes`で修正が必要な箇所を表示します。
`--fix`で軽微な修正を自動修正できます。
修正された箇所はターミナルに出力されます。

```console
$ ruff check ファイル名 --select カテゴリ記号
$ ruff check . --select ALL
$ ruff check . --select E,F,W,I,D
```

`--select`オプションを使って、チェックしたいカテゴリーやエラー番号などを指定できます。

```console
$ ruff check --statistics
$ ruff check --statistics --select ALL
```

`--statistics`オプションと`--select ALL`を使って、
どのルールを有効にすればよいか確認できます。

## ルールを確認したい（``ruff rule``）

```console
$ ruff rule ルールID
```

``select``や``ignore``で設定できるカテゴリ記号は[公式ドキュメントの「ルール」](https://docs.astral.sh/ruff/rules/)に書いてあります。
`ruff linter`コマンドでも、インストールされているバージョンのカテゴリ記号一覧を確認できます。
バージョンが上がるたびに追加・変更されるため（記号が短縮されたり、新しいカテゴリーが増えたりします）、
最新の一覧はコマンドか公式ドキュメントで確認するのが確実です。

```console
$ ruff linter
```

よく使われる代表的なカテゴリーは次の通りです。

- ``E``, ``W``: ``pycodestyle``
- ``F``: ``Pyflakes``
- ``I``: ``isort``
- ``N``: ``pep8-naming``
- ``UP``: ``pyupgrade``
- ``B``: ``flake8-bugbear``
- ``C4``: ``flake8-comprehensions``
- ``SIM``: ``flake8-simplify``
- ``RUF``: Ruff-specific rules

## コミットフックしたい（`ruff-pre-commit`）

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.15.12
  hooks:
  # ruff check
  - id: ruff
  # ruff format
  - id: ruff-format
```

`ruff`用のフックがあるので、[pre-commit](./python-pre-commit.md)と連携させることができます。

`id: ruff`を有効にすると
`ruff check .`が実行されます。
ファイルは修正されません。

`id: ruff-format`を有効にすると
`ruff format .`が実行されます。
ファイルは修正されます。

## リファレンス

- [Ruff - docs.astral.sh](https://docs.astral.sh/ruff/)
- [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
