# パッケージ管理したい（`uv`）

```console
// 新規プロジェクト作成
$ uv init my-project
$ cd my-project

// 依存関係の管理
$ uv add requests
$ uv add --dev pytest
$ uv add --group docs zensical
$ uv remove requests

// 依存関係のインストール
$ uv sync

// パッケージの実行とテスト
$ uv run main_script.py
$ uv run pytest

// パッケージ公開
$ uv build
$ uv publish
```

`uv`はRustで書かれた超高速なPythonパッケージ＆プロジェクト管理ツールです。
`uv`を使って、依存関係の管理、仮想環境の作成、スクリプトの実行、パッケージのビルドと公開など、Pythonプロジェクトのあらゆる側面を効率的に管理できます。

:::{hint}

`uv`には
プロジェクト管理ツールとしての側面と、
pip alternativeとしてパッケージ管理ツール（`uv pip`）としての側面があります。

どちらの文脈で使われているかを把握すると、　使い方がより理解しやすくなると思います。

:::

## インストールしたい（`uv`）

```console
// Homebrewでインストール
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

// 仮想環境を作成
$ uv venv
Using CPython 3.12.7
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

// 仮想環境を有効化
$ source .venv/bin/activate       // for bash/zsh
$ source .venv/bin/activate.fish  // for fish
$ .venv\Scripts\activate          // for PowerShell
(.venv) $

// 仮想環境を無効化
(.venv) $ deactivate
```

`uv venv`コマンドで仮想環境を作成できます。
仮想環境にある`activate`スクリプトを実行して、仮想環境を有効化します。

```console
// 任意のパスに仮想環境を作成
$ uv venv /tmp/test-uv/
$ source /tmp/test-uv/bin/activate
```

仮想環境を作成するパスを変更できます。
デフォルトで`.venv`です。

```console
// 特定のPythonバージョンを指定
$ uv venv --python 3.11        // バージョンを指定
$ uv venv --python python3.12  // 実行コマンドを指定
```

`--python`オプションで、仮想環境に使用するPythonを指定できます。
指定したPythonがシステムにインストールされていない場合は、`uv`が自動的にダウンロードしてインストールします。

:::{note}

Pythonの仮想環境については、
標準ライブラリの[venv](./python-venv.md)や、
その上位互換的な`virtualenv`などがあります。
また、Pythonのバージョン管理ツールである`pyenv`も、仮想環境の管理に利用できます。
`uv venv`コマンドはこれらのツールの機能を統合して提供しています。

:::

## パッケージを追加したい（`uv pip install`）

```console
// 仮想環境を作成
$ uv venv

// パッケージを追加
$ uv pip install pandas

// パッケージを削除
$ uv pip uninstall pandas
```

`uv pip install`コマンドで仮想環境にパッケージを追加できます。

```console
// 仮想環境が存在しない場合はエラー
$ uv pip install pandas
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment
```

仮想環境が存在しない場合はエラーになります。
エラーメッセージにしたがって仮想環境を作成すればOKです。

:::{note}

Pythonのパッケージ管理については、
標準ライブラリの[pip](./python-pip.md)があります。
`uv pip`コマンドは、`pip`コマンドを高速化した実装です。
`pip`との互換性が保たれているため、簡単に乗り換えることができます。

:::

## 新規プロジェクトしたい（`uv init`）

```console
// 作業用ディレクトリに移動
$ uv init --lib --package /tmp/test-uv
Initialized project `test-uv` at `/tmp/test-uv`
```

`uv init`コマンドでプロジェクトを初期化できます。

```console
$ ls -1a /tmp/test-uv
.git/
.gitignore
.python-version
README.md
main.py
pyproject.toml
src/
```

指定したパスに`pyproject.toml`ファイルや`src/`ディレクトリ、
`.python-version`ファイルなどが自動生成されます。
また、Gitリポジトリとして設定されます。

```console
$ uv init --bare /tmp/test-uv-bare    // 最小構成のプロジェクトを作成
$ uv init --app /tmp/test-uv-app      // CLI中心のプロジェクトを作成
$ uv init --lib /tmp/test-uv-lib      // ライブラリ中心のプロジェクトを作成
```

作成するプロジェクトの形態に合わせて`--lib`、`--app`、`--bare`オプションから選択します。
PyPIでパッケージとして公開する予定であれば`--package`オプションを追加します。
利用形態を迷っている場合は、とりあえず`--lib --package`オプションで作成しておくのが無難です。

```console
$ uv init /tmp/test-uv
error: Project is already initialized in `/tmp/test-uv` (`pyproject.toml` file exists)
```

すでにプロジェクトが存在する場合はエラーになります。
プロジェクトをリセットしたい場合は、`pyproject.toml`ファイルを削除してから
再度`uv init`を実行してください。

```console
$ cat /tmp/test-uv/pyproject.toml
[project]
name = "test-uv"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

プロジェクトのメタデータは`pyproject.toml`の`[project]`セクションに保存されます。
このファイルはユーザーが直接編集することを想定しています。
`uv init`コマンドで初期化した後は、必要に応じて直接編集してください。

## パッケージを追加・削除したい（`uv add` / `uv remove`）

```console
// dependenciesに追加
$ uv add requests
Resolved 1 package in 0.12s
Created environment
Installed 1 package in 0.09s
 + requests==2.31.0

// パッケージを削除
$ uv remove requests
Removed 1 package in 0.05s

// パッケージをインストール
$ uv sync
```

`uv add`でパッケージを追加できます。
`pyproject.toml`の`[dependencies]`セクションにパッケージ情報が追加され、
`uv.lock`ファイルも自動で更新されます。
`uv remove`でパッケージを削除できます。

```console
// dependency-groups.devに追加
$ uv add --dev pytest
$ uv add --group dev pre-commit
$ uv add --group dev commitizen
$ uv add --group dev ruff
// dependency-groups.docsに追加
$ uv add --group docs sphinx
```

`--group`オプションで、パッケージの用途に合わせてグループ化できます。
`pyproject.toml`の`[dependency-groups]`セクションにグループ情報が追加されます。
`--dev`オプションは`--group dev`と同じです。

```console
$ uv add pandas
error: No `pyproject.toml` found in current directory or any parent directory
```

`pyproject.toml`がない場合はエラーになります。
`uv init`コマンドでプロジェクトを初期化してから、`uv add`を実行してください。

## パッケージを同期したい（`uv sync`）

```console
$ uv sync
Resolved 5 packages in 0.09s
Created environment
Installed 5 packages in 0.14s
```

`uv sync`は、仮想環境を`uv.lock`の内容に一致させるコマンドです。
ロックファイルにあるパッケージはインストールされ、
ロックファイルにないパッケージはアンインストールされます。

:::{note}

`uv add`（や`uv remove`）コマンドでは`pyproject.toml`と`uv.lock`が更新されます。
`uv sync`コマンドは、それらのファイルを更新せず、`uv.lock`の内容が仮想環境に再現されます。

:::

## パッケージを更新したい（`uv lock`）

```console
// 更新できるパッケージを確認
$ uv lock --upgrade --dry-run

// パッケージを更新
$ uv lock --upgrade
$ uv sync
```

`uv lock`は、`pyproject.toml`の内容をもとに、`uv.lock`ファイルを更新するコマンドです。
`--upgrade`オプションで、パッケージを最新バージョンに更新できます。
`--dry-run`オプションで、更新されるパッケージを確認できます。

```console
// パッケージを更新してから同期
$ uv sync --upgrade
```

`uv sync --upgrade`コマンドは、
`uv lock --upgrade`と`uv sync`を組み合わせたコマンドです。

## パッケージを実行したい（`uv run`）

```console
$ uv run path/to/script.py
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

`uv run`コマンドで、プロジェクトの仮想環境を使って外部コマンドやスクリプトを実行できます。
仮想環境の手動アクティベーションは不要です。

```console
$ .venv/bin/activate
(.venv) $ python path/to/script.py
```

`uv run`を使わない場合は、仮想環境を手動でアクティベートしてからコマンドを実行してください。

## パッケージをビルドしたい（`uv build`）

```console
$ uv build
Building wheel for my-package
Successfully built dist/my_package-0.1.0-py3-none-any.whl
Building sdist for my-package
Successfully built dist/my_package-0.1.0.tar.gz

$ uv build --format wheel
$ uv build --format sdist
```

`uv build`コマンドでパッケージをビルドできます。
ビルドすると、`dist/`ディレクトリの中に、
`wheel`形式（`.whl`）と`sdist`形式（`.tar.gz`）のファイルが生成されます。
`--format`オプションで、ビルドするパッケージの形式を指定できます。

:::{note}

`wheel`形式はバイナリパッケージで、インストールが高速です。
`sdist`形式はソースパッケージで、古くからある配布形式です。
ビルドに時間がかかりますが、幅広い環境でインストールできます。
通常は両方の形式でビルドしておけばOKです。

:::

## パッケージを公開したい（`uv publish`）

```console
// TestPyPIに公開
$ uv publish --publish-url https://test.pypi.org/legacy/

// PyPIに公開
$ uv publish
Uploading my_package-0.1.0-py3-none-any.whl to PyPI...
Uploading my_package-0.1.0.tar.gz to PyPI...
```

`uv publish`コマンドでPyPIにパッケージを公開します。
`--publish-url`オプションで公開先を変更できます。
はじめて公開する場合は、TestPyPIでテスト公開してからPyPIに本番公開することをオススメします。

:::{note}

PyPIとTestPyPIは、サービスとしては別物です。
それぞれのサービスでアカウントを作成してください。
また、プロジェクトごとにAPIトークンを発行してください。

:::

:::{caution}

PyPIとTestPyPIには、同じ名前のパッケージは登録できません。
プロジェクトを作成する段階で、パッケージ名の重複がないか確認してください。
また、同じバージョンの再アップロード（上書き）もできません。
変更内容に応じてバージョンを更新してください。

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
