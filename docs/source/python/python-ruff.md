# フォーマッター／リンターしたい（`ruff`）

```console
$ ruff --version
ruff 0.6.1

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

```console
// グローバルに追加
$ pipx install ruff
```

```console
// プロジェクトに追加（dev）
$ poetry add ruff --group=dev
```

```console
// プロジェクトに追加する場合（dev）
$ uv add ruff --group dev

// グローバルに追加
$ uv tool install ruff
```

`ruff`はCLIツールなので`pipx`や`uv tool`なのでグローバルにインストールできます。
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

# 並列実行数
# threads = 4

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
[tool.ruff.isort]
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
また、`ruff.tomll`、`.ruff.toml`に個別設定として保存することもできます。

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
$ ruff check . --select E F W I D
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
どんなものがあるかなと思って書き写してみたら、なんと58種類もありました。

1. ``E``, ``W``: ``pycodestyle``
2. ``F``: ``Pyflakes``
3. ``C90``: ``mccabe``
4. ``I``: ``isort``
5. ``N``: ``pep8-naming``
6. ``D``: ``pydocstyle``
7. ``UP``: ``pyupgrade``
8. ``YTT``: ``flake8-2020``
9. ``ANN``: ``flake8-annotations``
10. ``ASYNC``: ``flake8-async``
11. ``TRIO``: ``flake8-trio``
12. ``S``: ``flake8-bandit``
13. ``BLE``: ``flake8-blind-except``
14. ``FBT``: ``flake8-boolean-tra``
15. ``B``: ``flake8-bugbear``
16. ``A``: ``flake8-builtins``
17. ``COM``: ``flake8-commas``
18. ``CPY``: ``flake8-copyright``
19. ``C4``: ``flake8-comprehensions``
20. ``DTZ``: ``flake8-datetimez``
21. ``T10``: ``flake8-debugger``
22. ``DJ``: ``flake8-django``
23. ``EM``: ``flake8-errmsg``
24. ``EXE``: ``flake8-executable``
25. ``FA``: ``flake8-future-annotations``
26. ``ISC``: ``flake8-implicit-str-concat``
27. ``ICN``: ``flake8-import-conventions``
28. ``G``: ``flake8-logging-format``
29. ``INP``: ``flake8-no-pep420``
30. ``PIE``: ``flake8-pie``
31. ``T20``: ``flake8-print``
32. ``PYI``: ``flake8-pyi``
33. ``PT``: ``flake8-pytest-style``
34. ``Q``: ``flake8-quotes``
35. ``RSE``: ``flake8-raise``
36. ``RET``: ``flake8-return``
37. ``SLF``: ``flake8-self``
38. ``SLT``: ``flake8-slots``
39. ``SIM``: ``flake8-simplify``
40. ``TID``: ``flake8-tidy-imports``
41. ``TCH``: ``flake8-type-checking``
42. ``INT``: ``flake8-gettext``
43. ``ARG``: ``flake8-unused-arguments``
44. ``PTH``: ``flake8-use-pathlib``
45. ``TD``: ``flake8-todos``
46. ``FIX``: ``flake8-fixme``
47. ``ERA``: ``eradicate``
48. ``PD``: ``pandas-vet``
49. ``PGH``: ``pygrep-hooks``
50. ``PL``: ``pylint``
51. ``TRY``: ``tryceratops``
52. ``FLY``: ``flynt``
53. ``NPY``: NumPy-specific rules
54. ``AIR``: ``Airflow``
55. ``PERF``: ``Perflint``
56. ``FURB``: ``refurb``
57. ``LOG``: ``flake8-logging``
58. ``RUF``: Ruff-specific rules

## コミットフックしたい（`ruff-pre-commit`）

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.6.7
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
