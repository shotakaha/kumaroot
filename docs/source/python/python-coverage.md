# カバレッジしたい（`coverage`）

```console
$ coverage run -m pytest  # pytestと併用
$ coverage run report     # ターミナルに出力
$ coverage html           # HTMLを生成

$ pytest --cov=パッケージ名 --cov-report=term --cov-report=html
```

`coverage`パッケージもしくは`pytest-cov`パッケージで
テストコードのカバレッジを確認できます。

**カバレッジ**とは、テストを実行したときに、
ソースコードのどこ部分が実際に実行されたかを示す指標です。
よく使われるのは **行カバレッジ（Line Coverate）** で
「全体の行数のうち、何行が実行されたか」をパーセンテージで示します。

:::{note}

カバレッジは、書かれたコードに対して、どれだけテストが通っているかという値です。
常に100%にするするというものでもなく、
100%だからバグがないというわけでもない、
ということに留意が必要です。

:::

## 設定ファイルしたい（`pyproject.toml`）

```toml
[tool.coverage.run]
branch = true
source = ["パッケージ名"]

[tool.coverage.report]
# 除外対象のファイル
# - ユニットテストのコード
# - __init__.py
omit = [
    "tests/*",
    "**/__init__.py",
]
# 除外対象の行
# - 明示的に除外した行
# - 実行用のエントリーポイント（__main__）
exclude_lines = [
    "pragma: no cover",
    "if __name__ == .__main__.:",
]

show_missing = true
skip_covered = true

[tool.pytest.ini_options]
addopts = "--cov=パッケージ名 --cov-report=term --cov-report=html"
```

`pyproject.toml`に
`coverage`と`pytest`の設定をまとめて整理できます。
カバレッジ測定から除外するファイルや行を設定できます。

`branch = false`は「各行のコードが実行されたかどうか」だけですが、
`branch = true`では「if文や論理演算の各分岐も実行されたかどうか」まで確認できます。

## 設定ファイルしたい（`.coveragerc`）

```ini
[run]
branch = True
source = パッケージ名

[report]
omit =
    tests/*
    */__init__.py
exclude_lines =
    pragma: no cover
    if __name__ == "__main__":

show_missing = True
skip_covered = True
```

`coverage`専用のオプションは
`.coveragerc`にINI形式で設定できます。
