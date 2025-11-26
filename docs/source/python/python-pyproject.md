# プロジェクト設定したい（`pyproject.toml`）

`pyproject.toml`はPythonプロジェクトの定義ファイルです。
これまでの`setup.py`などに代わる新しいPython標準です。

最近では、ほとんどのツールが`pyproject.toml`を認識できます。
また、`uv`や`hatch`などPEP621に準拠したビルドツールが普及しはじめています。

```{note}
PEP518が提案されたときは、まだ標準のTOMLパーサーが存在しなかったはずです。
どうしてTOML形式を選んだのかは謎です。
Python3.11になってようやく`tomllib`（読み取り専用）が標準モジュールとして追加されました。
```

参考までに、このドキュメントの{file}`pyproject.toml`を表示しておきます。

```{literalinclude} ../../../pyproject.toml
---
language: toml
---
```

## プロジェクトしたい（`[project]`）

```toml
[project]
name = "プロジェクト名"
version = "M.m.p"
description = "説明"
readme = "README.md"
requires-python = "^3.11"
license = "MIT"
authors = [
    {name="名前", email="メールアドレス"},
    {name="名前", email="メールアドレス"},
]
maintainers = [
    {name="名前", email="メールアドレス"},
    {name="名前", email="メールアドレス"},
]
keywords = []
classifiers = []

[project.urls]
homepage = "URL"
repository = "URL"
document = "URL"

[project.scripts]
cli_name = "パッケージ名.モジュール名:関数名"
```

`[project]`にプロジェクト設定を記述します。
設定項目は[pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)を参照してください。
また、パッケージ管理ツールのドキュメントにある設定例も参照するとよいです。

`requires-python`でPython環境のバージョン要件を指定できます。
等号や不等号などを使って互換性のあるバージョンを指定できます。

| 記法 | 対象 |
|---|---|
| `>=3.11` | `3.11` 以上（Python4を含む） |
| `<=3.11` | `3.11` 以下 |
| `>=3.11,<3.12` | `3.11` 以上 `3.12`未満 |
| `==3.11` | `3.11` のみ |
| `==3.11.*` | `3.11` 系のみ |
| `~=3.11` | `3.11` 系のみ |
| `~=3.11.0` | `3.11.0` 系のみ |
| `!=3.11` | `3.11` を除く |

:::{note}

以前は`^3.12`のように`^`（キャレット）を使ってバージョン指定できましたが、
[PEP440](https://peps.python.org/pep-0440/)によりサポート外になりました。

:::

## ビルドシステムしたい（`[build-system]`）

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

`[build-system]`のセクションにビルドに使うツールを記述します。
上記サンプルは`poetry`の設定です。

```toml
[build-system]
requires = ["setuptools", "wheel"]
```

## 外部パッケージしたい（`[tool]`）

```toml
[tool.poetry]
package-mode = false

[tool.commitizen]
name = "cz_conventional_commits"
version = "M.m.p"
tag_format = "$version"
version_files = [
    "pyproject.toml:version",
    "docs/source/conf.py:version",
    "docs/source/conf.py:release",
]

[tool.ruff]
line-length = 88
select = ["E", "F", "I"]
ignore = ["E501"]

[tool.ruff.isort]
known-first-party = ["パッケージ名"]
combine-as-imports = true

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
skip-magic-trailing-comma = false
docstring-code-format = true

[tool.mypy]
strict = true
python_version = "3.11"

[tool.pytest.ini_options]
addopts = "-ra -q"
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["src"]
```

`[tool]`のセクションに、外部パッケージの設定を記述します。
設定項目は、それぞれのパッケージのドキュメントを参照してください。

:::{note}

パッケージによっては独自ファイル名を使っている場合があります。
また、まだ`pyproject.toml`に対応していないパッケージも多くあります。

:::

## リファレンス

- [pyproject.toml specification - Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PEP517 - A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP518 - Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/)
- [PEP621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)

`pyproject.toml`周りの仕様は
PEP518（2016年）のあとも段階的に拡張されており、
PEP517（2017年）でビルドシステムの独立化、
PEP621（2021年）でプロジェクトメタデータが標準化されました。

現在では、`poetry`や`hatch`などのビルドツールに依らず、
`pyproject.toml`だけでプロジェクト設定が完結できるようになっています。
