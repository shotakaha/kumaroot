# プロジェクト管理したい（`pyproject.toml`）

```toml
[project]
name = "PyPIに公開するプロジェクト名"
version = "..."
description = "..."
readme = "README.md"
requires-python = ">=3.10"
authors = [
    {name = "qumasan", email = "..."}
]
license = { text = "MIT" }
keywords = ["...", "..."]
dependencies = [
    "pydantic",
    "typer",
    "loguru",
]

[project.optional-dependencies]
docs = [
    "mkdocs",
    "mkdocs-material",
    "mkdocstrings[python]",
]

dev = [
    "pytest",
    "pytest-cov",
    "ruff",
    "commitizen",
]

[project.scripts]
script_name = "..."

[project.urls]
Repository = "..."
Documentation = "..."
Issues = "..."

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
managed = true

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.commitizen]
name = "cz_conventional_commits"
tag_format = "$version"
version_scheme = "semver2"
version_provider = "uv"
update_changelog_on_bump = true
major_version_zero = true
version_files = [
    "..."
]
```

`pyproject.toml`は、Pythonプロジェクトの設定を一元管理するための標準ファイルです。
Python3.7以降からデファクトスタンダードになっており、ビルド・依存関係・パッケージ情報・ツール設定をまとめて書くことができます。

:::{note}

これまで、Pythonのプロジェクト設定は、
`setup.py`や`setup.cfg`、`requirements.txt`などに分散していました。

PEP518、PEP621、PEP517などにより標準化されました。

:::

## プロジェクト設定（`[project]`）

## 依存パッケージ（`[project.dependencies]`）

## 依存パッケージ（オプション）（`[project.optional-dependencies]`）

## ビルド環境（`[build-system]`）

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

`[build-system]`で、パッケージをビルドするためのツールを指定できます。

## パッケージ名とディレクトリ構造を変えたい

```toml
[project]
name = "osechi-kazunoko"

[tool.hatch.build.targets.wheel]
packages = ["src/kazunoko"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

`pyserial`パッケージを`import serial`でインポートできるように、
Pythonのパッケージ名とモジュール名は別々に設定できます。
しかし、いざ、自分で設定してみようとしたら、少し躓いたので紹介します。

`[build-system]`に`hatchling`を指定し、
`[tool.hatch.build.targets.wheel.packages]`を設定する必要がありました。
