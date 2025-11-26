# パッケージ管理したい（`hatch`）

```console
// プロジェクト初期化
$ hatch new プロジェクト名

// 環境管理
$ hatch shell
$ hatch env show
$ hatch env remove 環境名

// パッケージ実行と開発
$ hatch run コマンド
$ hatch run pytest

// テスト実行
$ hatch test

// パッケージ公開
$ hatch build
$ hatch publish
```

`hatch`はPythonプロジェクトの開発から公開まで、統合的に管理できるツールです。
`pyproject.toml`で依存関係を管理し、
複数のPythonバージョン環境を自動で構築・テストできます。

:::{note}

`hatch`はパッケージ開発に特化しており、テストやビルド、公開までのワークフローが統合されています。

:::

## インストールしたい（`hatch`）

```console
$ brew install hatch

$ which -a hatch
/opt/homebrew/bin/hatch

$ hatch --version
hatch, version 1.13.0
```

`hatch`はHomebrewでインストールできます。
`pipx`を使ったインストール方法もあります。

:::{note}

`pip`や`pipx`でもインストールできます。
推奨されるインストール方法は`pipx install hatch`です。

:::

## 仮想環境したい（`hatch env`）

```console
$ cd PROJECT_NAME
$ hatch shell
Creating environment: default
Python 3.12.7

(default) $
```

`hatch shell`コマンドで仮想環境を作成・アクティブ化できます。
デフォルトで`default`という名前の環境が作成されます。
環境はプロジェクトディレクトリの`.venv`（または他の場所）に保存されます。

:::{note}

`hatch env create`で環境を明示的に作成することもできますが、
通常は`hatch shell`や`hatch run`で自動的に作成されます。

:::

## 依存関係を管理したい（`pyproject.toml`）

hatchでは`pyproject.toml`を直接編集して依存関係を管理します。
`hatch`にはコマンドで依存関係を追加・削除する機能がありません。

```toml
# プロジェクトの依存関係
[project]
dependencies = [
  "requests>=2.28.0",
  "click>=8.0.0",
]

# 開発用の依存関係
[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "pytest-cov>=4.0",
]

# テスト環境の依存関係
[tool.hatch.envs.test]
dependencies = [
  "pytest>=8.0",
  "pytest-cov>=4.0",
]
```

`pyproject.toml`を編集した後、以下のコマンドで環境を更新できます：

```console
$ hatch env create
Creating environment: default

$ hatch run pytest
Running tests in default environment...
```

`hatch`は自動的に依存関係を解決してインストールします。

:::{note}

`pyproject.toml`を編集したら、`hatch shell`や`hatch run`で環境を再作成すると自動的に依存関係が更新されます。

:::

## 新規プロジェクトしたい（`hatch new`）

```console
$ hatch --version
hatch, version 1.13.0

$ hatch new PROJECT_NAME
Created project `PROJECT_NAME` at `/path/to/PROJECT_NAME`
```

`hatch new`コマンドでプロジェクトを初期化できます。
同名のプロジェクトがすでに存在する場合は、エラーになります。

hatchで作成されるプロジェクト構造は、Pythonパッケージ開発に最適化されています：

```console
$ tree PROJECT_NAME
PROJECT_NAME
├── README.md
├── LICENSE.txt
├── pyproject.toml
├── src/
│   └── project_name/
│       ├── __about__.py
│       └── __init__.py
└── tests/
    ├── __init__.py
    └── test_example.py
```

`src/`レイアウトを使用することで、パッケージの依存関係の問題を回避できます。
`__about__.py`にバージョン情報が集約されており、バージョン管理が簡単です。

:::{note}

`hatch new`は対話形式で詳細情報を入力することもできます。
`hatch new -i`で対話モードを起動できます。

:::

## パッケージを実行したい（`hatch run`）

```console
$ hatch run コマンド名

// ユニットテストを実行
$ hatch run pytest

// フォーマッターを実行
$ hatch run ruff format

// 自作スクリプトを実行
$ hatch run python src/my_script.py [オプション]
```

`hatch run`で仮想環境内のパッケージを実行できます。
また`pyproject.toml`の`[project.scripts]`で設定したスクリプトエントリーポイントも実行できます。

`pyproject.toml`に環境別のスクリプトを定義することもできます：

```toml
[tool.hatch.envs.default.scripts]
format = "ruff format ."
lint = "ruff check ."
test = "pytest"
```

定義したスクリプトは以下のように実行できます：

```console
$ hatch run format
$ hatch run lint
$ hatch run test
```

:::{note}

`hatch run`は指定した環境内でコマンドを実行します。
環境を指定しない場合はデフォルト環境で実行されます。

:::

## パッケージを公開したい（`hatch build` / `hatch publish`）

```console
$ hatch build
Building `wheel` wheel (src/project_name)
Successfully built dist/project_name-0.0.1-py3-none-any.whl
Building `sdist` sdist (src/project_name)
Successfully built dist/project_name-0.0.1.tar.gz

$ hatch publish
Publishing to PyPI with token
```

`hatch build`コマンドでパッケージを作成できます。
`dist/`ディレクトリ内に`sdist`形式（`.tar.gz`）と`wheel`形式（`.whl`）のパッケージが生成されます。

`hatch publish`コマンドでPyPIにパッケージを公開できます。
初回公開時はTestPyPIにテスト公開することをオススメします：

```console
$ hatch publish -r testpypi
Publishing to https://test.pypi.org/legacy/
```

PyPIへのアップロード前に、PyPIアカウントとAPIトークンを用意する必要があります。

:::{caution}

同じパッケージ名はPyPIに登録できません。
パッケージを公開する前に名前の重複がないか確認が必要です。

また、同じバージョンの再アップロード（上書き）はできません。
変更内容に応じてバージョンを更新する必要があります。

:::

## 複数のPythonバージョンでテストしたい（`hatch test`）

```console
$ hatch test
Running tests for multiple Python versions...
3.10: PASSED
3.11: PASSED
3.12: PASSED
```

`hatch test`コマンドで複数のPythonバージョンを使用してテストを実行できます。
hatchは必要なPythonディストリビューションを自動的にダウンロードするため、事前インストールが不要です。

テスト対象のPythonバージョンは`pyproject.toml`で指定します：

```toml
[tool.hatch.envs.test]
python = ["3.10", "3.11", "3.12"]
```

テスト実行時のオプション：

```console
$ hatch test --parallel
$ hatch test --cover
$ hatch test 3.12
```

`--parallel`オプションで複数バージョンのテストを並列実行できます。
`--cover`オプションでコードカバレッジを測定できます。

:::{note}

hatchは複数のPythonバージョン環境を自動的に管理し、
各バージョンで同じテストスイートを実行します。

:::

## バージョンを管理したい（`hatch version`）

```console
$ hatch version
0.0.1

$ hatch version patch
Bumped version from 0.0.1 to 0.0.2

$ hatch version minor
Bumped version from 0.0.2 to 0.1.0

$ hatch version major
Bumped version from 0.1.0 to 1.0.0
```

`hatch version`でプロジェクトのバージョンを管理できます。
バージョン情報は`src/project_name/__about__.py`に保存されます。

バージョンバンプコマンド：

- `hatch version patch`：パッチバージョンをアップ（バグ修正）
- `hatch version minor`：マイナーバージョンをアップ（新機能）
- `hatch version major`：メジャーバージョンをアップ（大きな変更）

:::{note}

`hatch`は`src/`レイアウトを採用しており、
バージョン情報は`__about__.py`で一元管理されます。

:::

## hatchとpytestの統合

hatchで作成したプロジェクトには、デフォルトで`pytest`がテスト環境に含まれています。
以下のコマンドでテストを実行できます：

```console
$ hatch run test
Running tests...
tests/test_example.py .                                    [100%]
1 passed

$ hatch run pytest tests/
Running tests...
tests/test_example.py .                                    [100%]
1 passed

$ hatch run pytest tests/ -v
Running tests...
tests/test_example.py::test_example PASSED              [100%]
1 passed
```

hatchは複数のPythonバージョンでテストを実行する機能が統合されているため、
CI/CDパイプラインの設定も簡単です。

## hatchとpyprojectの関係

hatchはPEP 517/518に完全準拠しており、`pyproject.toml`は標準的なPythonパッケージング仕様にしたがっています。
これにより、他のツール（`pip`、`build`など）との互換性が保証されています。

:::{note}

`pyproject.toml`はPythonパッケージの標準メタデータ形式です。
hatchはこの仕様に準拠した最新のパッケージマネージャーです。

:::
