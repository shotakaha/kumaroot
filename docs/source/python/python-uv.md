# パッケージ管理したい（`uv`）

```console
// 新規プロジェクト作成
$ uv init my-project
$ cd my-project

// 依存関係の管理
$ uv add requests
$ uv add --dev pytest
$ uv remove requests

// パッケージの実行とテスト
$ uv run python main.py
$ uv run pytest

// 環境管理
$ uv sync
$ uv python pin 3.12

// パッケージ公開
$ uv build
$ uv publish

// 外部ツールを一時実行
$ uvx ruff check .
```

`uv`はRustで書かれた超高速なPythonパッケージ＆プロジェクトマネージャーです。
pip、pip-tools、pipx、poetry、pyenvなど、複数のツールを1つに統合し、
10～100倍の速度でパッケージを管理できます。

:::{note}

`uv`はPEPに準拠した標準的なツールで、`pip`の完全な代替を目指しています。

:::

## インストールしたい（`uv`）

```console
$ brew install uv

$ which -a uv
/opt/homebrew/bin/uv

$ uv --version
uv 0.6.13 (Homebrew 2025-04-07)

$ which -a uvx
/opt/homebrew/bin/uvx

$ uvx --version
uv-tool-uvx 0.6.13 (Homebrew 2025-04-07)
```

`uv`はHomebrewでインストールできます。
`pipx`と同じような思想の`uvx`コマンドも使えるようになります。

:::{note}

`pip`や`pipx`、`poetry`でもインストールできます。
CI/CDでPythonノベースイメージを使う場合は`pipx install uv`するのがよいと思います。

:::

## 仮想環境したい（`uv venv`）

```console
$ cd my-project

$ uv venv
Using CPython 3.12.7
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

$ source .venv/bin/activate
(.venv) $
```

`uv venv`コマンドで仮想環境を作成できます。
デフォルトで`.venv/`ディレクトリに作成されます。

:::{note}

実は、`uv init`でプロジェクトを作成すると、`uv sync`や`uv run`を実行する際に
自動的に仮想環境が作成されるため、手動で`uv venv`を実行する必要はありません。

:::

```console
// カスタムディレクトリに作成
$ uv venv myenv
$ source myenv/bin/activate

// 特定のPythonバージョンを指定
$ uv venv --python 3.11
$ uv venv --python python3.12
```

## パッケージを追加・削除したい（`uv add` / `uv remove`）

```console
$ uv add requests
Resolved 1 package in 0.12s
Created environment
Installed 1 package in 0.09s
 + requests==2.31.0

$ uv add --dev pytest
Resolved 1 package in 0.08s
Installed 1 package in 0.07s
 + pytest==7.4.3

$ uv remove requests
Removed 1 package in 0.05s
```

`uv add`コマンドで`pyproject.toml`にパッケージを追加し、自動的にインストールします。
パッケージ情報は`pyproject.toml`と`uv.lock`に記録されます。

`uv add --dev`で開発用の依存関係（テストツールなど）を追加できます。

:::{note}

`uv add`を使うと`pyproject.toml`と`uv.lock`の両方が自動更新されます。
推移的な依存関係も自動的に削除されるため、pipより安全です。

:::

## パッケージを一時的にインストールしたい（`uv pip install`）

```console
$ uv pip install pandas
Resolved 1 package in 0.08s
Installed 1 package in 0.06s
 + pandas==2.1.1

$ uv pip list
Name            Version
-----------     -------
pandas          2.1.1
...

$ uv pip uninstall pandas
Removed 1 package in 0.02s
```

`uv pip`は[pipコマンド](./python-pip.md)の互換モードで、より高速に動作します。
`pyproject.toml`に記録されない一時的なインストールに適しています。

:::{caution}

`uv pip install`した場合、`pyproject.toml`には追加されません。
プロジェクトの依存関係として記録したい場合は`uv add`を使用してください。

:::

## 新規プロジェクトしたい（`uv init`）

```console
$ uv init my-app
Created project `my-app` at `/path/to/my-app`

$ cd my-app
$ tree .
.
├── README.md
├── .python-version
├── pyproject.toml
├── src/
│   └── my_app/
│       └── __init__.py
└── hello.py
```

`uv init`コマンドで新しいPythonプロジェクトを初期化できます。
デフォルトでアプリケーションプロジェクトが作成されます。

### プロジェクトタイプの選択

```console
// アプリケーションプロジェクト（デフォルト）
$ uv init my-app

// PyPIに公開するパッケージプロジェクト
$ uv init --package my-library

// 最小限のセットアップ（pyproject.tomlのみ）
$ uv init --bare
```

| 目的 | コマンド | 用途 |
|---|---|---|
| 個人用スクリプト | `uv init` | ローカルで実行するツール |
| PyPIで公開 | `uv init --package` | 他のプロジェクトで使用される |
| 既存プロジェクトに追加 | `uv init --bare` | pyproject.tomlのみ追加 |

:::{note}

`uv init`でプロジェクトを作成すると、`.python-version`ファイルが自動で作成されます。
これにより、プロジェクトで使用するPythonバージョンが固定されます。

:::

## 環境を同期したい（`uv sync` / `uv lock`）

```console
$ uv sync
Resolved 5 packages in 0.09s
Created environment
Installed 5 packages in 0.14s

$ uv lock --upgrade
Updated 3 packages

$ uv sync --upgrade
Updated 3 packages in 0.18s
```

`uv sync`コマンドで`pyproject.toml`と`uv.lock`をプロジェクト環境に同期します。
不足しているパッケージをインストールし、不要なパッケージを削除します。

`uv lock`コマンドで`uv.lock`ファイル（ロックファイル）を更新します。

### 依存関係を更新したい場合

```console
// ロックファイルのみを更新（環境は同期しない）
$ uv lock --upgrade

// ロックファイルと環境の両方を更新
$ uv sync --upgrade

// 特定のパッケージのみ更新
$ uv sync --upgrade-package requests
```

:::{note}

`uv lock --upgrade`と`uv sync --upgrade`の違い：

- `uv lock --upgrade`：`uv.lock`ファイルのみ更新
- `uv sync --upgrade`：`uv.lock`と環境の両方を更新

:::

## パッケージを実行したい（`uv run`）

```console
$ uv run python main.py
Hello, World!

$ uv run pytest
===== test session starts =====
tests/test_main.py .                                       [100%]
1 passed

$ uv run ruff check .
All checks passed!

$ uv run ruff format .
1 file reformatted
```

`uv run`コマンドで、プロジェクトの仮想環境内でコマンドやスクリプトを実行します。
`pyproject.toml`に記録された依存関係が自動的に利用可能になります。

### スクリプトの実行

```console
// Pythonスクリプト
$ uv run python script.py

// スクリプトに引数を渡す
$ uv run python script.py --arg value

// プロジェクト内のスクリプト
$ uv run hello.py
```

:::{note}

`uv run`を使うことで、仮想環境の手動アクティベーション（`source .venv/bin/activate`）が不要になります。

:::

## パッケージを公開したい（`uv build` / `uv publish`）

```console
$ uv build
Building wheel for my-package
Successfully built dist/my_package-0.1.0-py3-none-any.whl
Building sdist for my-package
Successfully built dist/my_package-0.1.0.tar.gz

$ uv publish
Uploading my_package-0.1.0-py3-none-any.whl to PyPI...
Uploading my_package-0.1.0.tar.gz to PyPI...
```

`uv build`コマンドでパッケージをビルドします。
`dist/`ディレクトリに以下のファイルが生成されます：

- `wheel`形式（`.whl`）：バイナリパッケージ
- `sdist`形式（`.tar.gz`）：ソースパッケージ

### 公開手順

```console
// 1. パッケージをビルド
$ uv build

// 2. TestPyPIで動作確認（初回時推奨）
$ uv publish --publish-url https://test.pypi.org/legacy/

// 3. PyPIに公開
$ uv publish
```

`uv publish`コマンドでPyPIにパッケージを公開します。

:::{caution}

- 同じパッケージ名はPyPIに登録できません。公開前に名前の重複を確認してください
- 同じバージョンの再アップロード（上書き）はできません。変更内容に応じてバージョンを更新してください
- PyPIアカウントとAPIトークンが必要です

:::

## Pythonバージョンを管理したい（`uv python`）

```console
$ uv python pin 3.12
Pinned `.python-version` to `3.12`

$ cat .python-version
3.12

$ uv run python --version
Python 3.12.7
```

`uv python pin`コマンドで、プロジェクトで使用するPythonバージョンを指定します。
設定は`.python-version`ファイルに保存され、`uv`や`pyenv`などのツールで共通に使用されます。

### Pythonバージョンのインストール

```console
// インストール可能なバージョンを確認
$ uv python list
cpython-3.13.0
cpython-3.12.7
cpython-3.11.10
...

// 特定のバージョンをインストール
$ uv python install 3.12
Installed Python 3.12.7 in 5.67s

// 複数バージョンをインストール
$ uv python install 3.11 3.12

// インストール済みバージョンを確認
$ uv python list --only-installed
cpython-3.13.0-macos-aarch64-none     /opt/homebrew/opt/python@3.13/bin/python3.13
cpython-3.12.7-macos-aarch64-none     ~/.local/share/uv/python/cpython-3.12.7-macos-aarch64-none/bin/python3.12
```

### Pythonバージョンの削除

```console
$ uv python uninstall 3.12
Uninstalled Python 3.12.7
```

:::{note}

`uv init`でプロジェクトを作成すると、`.python-version`が自動で作成されます。
システムにインストールされていないバージョンが指定されている場合、
`uv`は自動的にそのバージョンをダウンロードしてインストールします。

:::

## 外部ツールを使いたい（`uvx` / `uv tool install`）

### 一時的に実行したい場合（`uvx`）

```console
$ uvx ruff check .
All checks passed!

$ uvx black --version
black, 23.12.1

$ uvx --with pandas --with matplotlib jupyter notebook
[notebook starts...]
```

`uvx`コマンドで、ツールをインストールせずに実行できます。
初回実行時にダウンロードされ、以後キャッシュされるため高速です。

### グローバルにインストールしたい場合（`uv tool install`）

```console
$ uv tool install ruff
Installed `ruff` with executable `ruff`

$ uv tool install black mypy
Installed `black` and `mypy` with executables `black` and `mypy`

// インストール済みツールを確認
$ uv tool list
Tool                Version     Python
----                -------     ------
black               23.12.1     3.12.7
mypy                1.7.0       3.12.7
ruff                0.1.8       3.12.7

// ツールをアップグレード
$ uv tool upgrade ruff
Upgraded `ruff` from 0.1.8 to 0.1.9

// すべてのツールをアップグレード
$ uv tool upgrade --all
Upgraded 3 tools
```

頻繁に使用するツール（`ruff`、`black`、`mypy`など）をグローバルにインストールします。

### uvxとuv tool installの使い分け

| 用途 | コマンド | 例 |
|---|---|---|
| 一時的に使用 | `uvx` | `uvx pytest script.py` |
| 最新版を試したい | `uvx` | `uvx ruff@0.2.0 check .` |
| 頻繁に使用 | `uv tool install` | `uv tool install ruff` |
| CI/CD環境 | `uv tool install` | Dockerイメージに含める |

:::{note}

`uv tool run`と`uvx`は同等のコマンドです。
`uvx`はより簡潔なため、通常は`uvx`を使用してください。

:::

:::{caution}

`~/.local/bin`は他のツール（`pipx`など）と共有されます。
同名のコマンドがある場合はインストールに失敗します。
置き換える場合は、まず古いツールをアンインストールしてください。

:::

## 他のツールと比較したい

`uv`は複数のツールの役割を統合しています。以下は機能比較表です：

### プロジェクト管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| プロジェクト初期化 | `uv init` | `poetry init` | × | × |
| 仮想環境作成 | 自動 | 自動 | `python -m venv` | 自動 |

### 依存関係管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| パッケージ追加 | `uv add` | `poetry add` | `pip install` | × |
| パッケージ削除 | `uv remove` | `poetry remove` | `pip uninstall` | × |
| 開発用依存 | `uv add --dev` | `poetry add --dev` | 手動管理 | × |
| ロックファイル | `uv lock` | `poetry lock` | `pip freeze` | × |
| 環境同期 | `uv sync` | `poetry install` | `pip install -r` | × |

### 実行と開発

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| スクリプト実行 | `uv run` | `poetry run` | 手動 | × |

### Python管理とツール管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| バージョン固定 | `uv python pin` | 外部ツール依存 | × | × |
| バージョンリスト | `uv python list` | × | × | × |
| 一時実行 | `uvx` | × | × | × |
| グローバルインストール | `uv tool install` | × | × | グローバル |

### ビルドと公開

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| ビルド | `uv build` | `poetry build` | `python -m build` | × |
| 公開 | `uv publish` | `poetry publish` | twine | × |

### uvの優位性

1. **速度**：Rustで実装され、他のツールより10～100倍高速
2. **統合性**：pip、poetry、pyenvなど複数ツールの機能を1つに統合
3. **使いやすさ**：直感的なコマンド体系と安定した動作
4. **再現性**：ロックファイルによる確実な依存関係管理

:::{note}

Pythonには歴史的にさまざまなパッケージマネージャー（pip、poetry、pipx、pyenv）が存在し、
それぞれ異なる目的で使用されていました。

2024年に登場した`uv`は、これらの機能を統一し、
PEP準拠で今後のデファクトスタンダードになる可能性が高いツールです。

新規プロジェクトは`uv`で始めることをオススメします。

:::
