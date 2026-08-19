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
```

`[project]`テーブルに、プロジェクトのメタデータを書きます。
PEP 621で必須とされているのは`name`だけです。
`version`も必須ですが、`dynamic = ["version"]`と書けば、
ビルドツール側に動的に決定させることもできます（`commitizen`や`hatch version`などと組み合わせる場合に便利です）。
それ以外の`description`、`readme`、`authors`、`license`、`keywords`はすべて任意です。

## 依存パッケージ（`[project]`の`dependencies`）

```toml
[project]
dependencies = [
    "pydantic",
    "typer",
    "loguru",
]
```

プロジェクトの実行に必要な依存パッケージは、`[project]`テーブルの`dependencies`キーに書きます。
`[project.dependencies]`のような独立したテーブルではなく、`[project]`直下の配列である点に注意してください。
バージョンを指定したい場合は`"pydantic>=2.0"`のように、PEP 508形式の文字列で書きます。

## 依存パッケージ（オプション）（`[project.optional-dependencies]`）

```toml
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
```

インストール時に選択できる、追加の依存パッケージ群を定義します。
キーがextra名（`docs`、`dev`など）、値がその依存パッケージの配列です。
利用者は`pip install my-project[docs]`のように、extra名を指定してインストールできます。

`dev`のように開発専用のツールをここに置くこともできますが、
配布先（PyPIなど）にextraとして公開される点に注意してください。
CI/CD専用など、パッケージの利用者に見せる必要のない依存は、
`uv`や`poetry`が対応する`[dependency-groups]`（PEP 735）で管理する方が適切です。

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
