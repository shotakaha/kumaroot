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
    "rich",
    "loguru",
]

[project.optional-dependencies]
docs = [
    "zensical",
]

dev = [
    "pytest",
    "pytest-cov",
    "ruff",
    "commitizen",
    "pre-commit",
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
    "rich",
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
    "zensical",
]

dev = [
    "pytest",
    "pytest-cov",
    "ruff",
    "commitizen",
    "pre-commit",
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

`[build-system]`で、パッケージをビルドするためのツール（ビルドバックエンド）を指定できます。
`requires`に必要なパッケージ、`build-backend`にビルド処理を担うモジュールを書きます（PEP 517、PEP 518）。
使っているプロジェクト管理ツールに合わせて選びます。

### hatchしたい（`hatchling`）

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

[hatch](./python-hatch.md)のビルドバックエンドです。
`hatch new`で作成したプロジェクトでは、デフォルトでこの設定になります。

### poetryしたい（`poetry-core`）

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

[poetry](./python-poetry.md)のビルドバックエンドです。
`poetry new`や`poetry init`で作成したプロジェクトでは、デフォルトでこの設定になります。

### uvしたい（`uv_build`）

```toml
[build-system]
requires = ["uv_build>=0.12.5,<0.13.0"]
build-backend = "uv_build"
```

[uv](./python-uv.md)のビルドバックエンドです。
`uv init`で作成したプロジェクトでは、デフォルトでこの設定になります。
`requires`のバージョン範囲は、インストールされている`uv`のバージョンに合わせて自動で設定されます。

:::{note}

`uv`はプロジェクト管理ツールであり、ビルドバックエンドとは独立した仕組みです。
`[build-system]`を`hatchling`など他のバックエンドに書き換えても、
`uv build`や`uv sync`は問題なく動作します。

:::

### flitしたい（`flit_core`）

```toml
[build-system]
requires = ["flit_core>=3.11,<5"]
build-backend = "flit_core.buildapi"
```

シンプルな単一パッケージの配布に特化した[flit](https://flit.pypa.io/)のビルドバックエンドです。
複雑な設定を必要としない、小規模なプロジェクトに向いています。

### setuptoolsしたい（`setuptools`）

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

古くから使われている[setuptools](https://setuptools.pypa.io/)のビルドバックエンドです。
`[build-system]`テーブル自体を省略した場合も、フォールバックとしてsetuptoolsが使われます。

### それぞれの特徴

| バックエンド | 特徴 | C拡張 |
| --- | --- | --- |
| `hatchling` | プラグインが豊富で設定の柔軟性が高い | プラグイン経由 |
| `poetry-core` | `poetry`と一体で、依存関係管理に強い | 未対応 |
| `uv_build` | 最速・ゼロコンフィグ志向 | 非対応 |
| `flit_core` | 最小限・軽量、設定項目が少ない | 非対応 |
| `setuptools` | もっとも枯れていて実績が豊富 | 標準対応 |

生成される`wheel`・`sdist`はどのバックエンドでも標準形式（PEP 517・PEP 427）なので、
`pip install`する利用者側は違いを意識する必要はありません。
一方、`[tool.poetry.*]`や`[tool.hatch.*]`のようなツール固有の設定は共通化されていないため、
バックエンドを乗り換える際は書き直しが必要になることがあります。

C拡張やCythonなど、コンパイルが必要なパッケージを作る場合は`setuptools`を選ぶのが無難です。
それ以外の純粋なPythonパッケージであれば、使っているプロジェクト管理ツール純正のバックエンドを選ぶと摩擦が少ないです。

## ツールの設定したい（`tool.ツール名`）

```toml
[tool.uv]
managed = true
```

`[tool.ツール名]`テーブルに、各ツール独自の設定を書きます。
`[project]`や`[build-system]`と違って標準化されておらず、書式や項目はツールごとに異なります。
`[tool.uv]`は[uv](./python-uv.md)の設定です。
`managed = true`（デフォルト）で、このプロジェクトを`uv`が管理していることを明示します。

```toml
[tool.ruff]
line-length = 100
target-version = "py312"
```

`[tool.ruff]`は[Ruff](https://docs.astral.sh/ruff/)の設定です。
`line-length`で1行の最大文字数、`target-version`で対象のPythonバージョンを指定できます。

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version_provider = "pep621"
tag_format = "v$version"
```

`[tool.commitizen]`は[commitizen](https://commitizen-tools.github.io/commitizen/)の設定です。
`version_provider`で、バージョン番号をどこから読み書きするか指定します。
`"pep621"`を指定すると、`[project]`の`version`キーと連動します。

:::{note}

`[tool.hatch.build.targets.wheel]`のように、ツール名の下にさらに階層を作ることもできます。
どんなキーが使えるかは、それぞれのツールの公式ドキュメントを参照してください。

:::

## パッケージ名とディレクトリ構造を変えたい

```toml
[project]
name = "osechi-kazunoko"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/kazunoko"]
```

`pyserial`パッケージを`import serial`でインポートできるように、
Pythonのパッケージ名とモジュール名は別々に設定できます。
しかし、いざ、自分で設定してみようとしたら、少し躓いたので紹介します。

`[build-system]`に`hatchling`を指定し、
`[tool.hatch.build.targets.wheel.packages]`を設定する必要がありました。
`src/<パッケージ名>`のディレクトリ名（この例では`kazunoko`）が、
そのまま`import`するモジュール名になります。

### CLIコマンド名を変えたい（`[project.scripts]`）

```toml
[project]
name = "osechi-kazunoko"

[project.scripts]
kazunoko = "kazunoko.cli:app"
```

`[project.scripts]`で、インストール後に使えるコマンド名を設定できます。
左辺（`kazunoko`）がコマンド名、右辺（`kazunoko.cli:app`）が実行するモジュールと変数（または関数）です。
パッケージ名は`osechi-kazunoko`のままでも、
`uvx osechi-kazunoko`ではなく`uvx --from osechi-kazunoko kazunoko`のように、
コマンド名だけを短く保てます。

PyPIでの配布名（`osechi-kazunoko`）と、
importするモジュール名・コマンド名（`kazunoko`）を分けたい場合に使います。
名前空間の衝突を避けつつ、利用者には短いコマンド名を提供できます。
