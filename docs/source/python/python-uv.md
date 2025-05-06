# パッケージ管理したい（``uv``）

```console
$ uv init プロジェクト名 --app --package --vcs git
$ uv python pin バージョン
$ uv add パッケージ名
$ uv add --dev パッケージ名
$ uv update
$ uv sync

// 開発と検証
$ uv run コマンド
$ uv pip compile
$ uv pip check

// パッケージ公開
$ uv build
$ uv publish

// 補助コマンド
$ uv tool install パッケージ名
$ uv tool uninstall パッケージ名
$ uv tool list

// pip互換モード
$ uv pip install パッケージ名
$ uv pip uninstall パッケージ名
$ uv pip freeze
```

`uv`はPython環境の管理とパッケージ管理を一元管理できるツールです。
`.python-version`でPython環境を管理し、
`pyproject.toml`と`uv.lock`のファイルを使って依存関係を管理できます。

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
CI/CDで使う場合は`pipx install uv`がよいと思います。

:::

## 新規プロジェクトしたい（`uv init`）

```console
$ uv init --version
uv-init 0.6.13 (Homebrew 2025-04-07)

// デフォルト（--app --no-package）
$ uv init PROJECT_NAME

// ライブラリ作成（--lib --package）
$ uv init PROJECT_NAME --lib

// CLI&パッケージ（--app --package）
$ uv init PROJECT_NAME --app --package

// ドキュメントのみ
$ uv init --bare --no-package PROJECT_DOCS
```

`init`コマンドでプロジェクトを初期化できます。
同名のプロジェクトがすでに存在する場合は、エラーになります
プロジェクト名を省略した場合は、カレントディレクトリが初期化されます。

目的にあったディレクトリ構造を自動で構成できるオプションも用意されています。
デフォルトは`--app --no-package`に相当し、ローカルで利用するCLIの仕様になっています。

| PyPI | ライブラリ（`--lib`） | アプリ（`--app`） |
|---|---|---|
| 公開したい（`--package`） | `--lib` | `--app --package` |
| 公開しない（`--no-package`） | `--lib --no-package` | `--app` |

:::{caution}

`--app` / `--lib` / `--script`オプションは同時に使えないようになっています。

:::

```console
// プロジェクト名を指定して初期化する
$ uv init PROJECT_NAME
Initialized project `PROJECT_NAME` at `./PROJECT_NAME`

// 初期化後のディレクトリ構造
$ tree PROJECT_NAME
PROJECT_NAME
├── README.md
├── hello.py
└── pyproject.toml

// 既存のプロジェクトがあるとエラーになる
$ uv init PROJECT_NAME
error: Project is already initialized in `./PROJECT_NAME`
```

## パッケージを追加したい（``uv add`` / `uv remove`）

```console
$ uv add パッケージ名
$ uv remove パッケージ名

$ uv add パッケージ名==バージョン
$ uv add パッケージ名 --extra パッケージ名
$ uv add --dev パッケージ名s
```

`add`コマンドで`pyproject.toml`に依存パッケージを追加できます。
`remove`コマンドで削除できます。

## パッケージをインストールしたい（`uv sync` / `uv lock`）

```console
$ uv lock

$ uv sync
$ uv sync --all-extras
```

`lock`コマンドでロックファイル（`uv.lock`）を更新できます。

`sync`コマンドでロックファイルを元に、プロジェクトに必要なパッケージを追加／更新できます。
`--all-extras`オプションで、依存パッケージのオプションも追加できます。

## パッケージを実行したい（`uv run`）

```console
$ uv run コマンド名

// ユニットテストを実行
$ uv run pytest

// フォーマッターを実行
$ uv run ruff format

// 自作ツールを実行
$ uv run 自作ツール名 [オプション]
```

`uv run`で仮想環境に追加したパッケージを実行できます。
また`pyproject.toml`の`[project.scripts]`で設定した自作ツールも実行できます。
自作パッケージの開発時にもっとも多く使うコマンドです。

## パッケージを公開したい（`uv build` / `uv publish`）

```console
$ uv build

$ uv publish
$ uv publish -r testpypi
```

`build`コマンドでパッケージを作成できます。
`/dist/`の中に`sdist`形式と`wheel`形式のパッケージが生成されます。

`publish`コマンドでPyPIにパッケージを公開できます。
`-r testpypi`でTestPyPIにテスト公開できます。
作成したパッケージをはじめて公開する場合は、TestPyPIにアップできるか試してみるとよいです。

:::{caution}

同じパッケージ名はPyPIに登録できません。
パッケージを公開する前に名前の重複がないか確認が必要です。

また、自分のパッケージでも同じバージョンを追加（＝上書き）することはできません。
軽微な修正であっても、別のバージョンにして公開する必要があります。

:::

## pip互換したい（`uv pip`）

```console
$ uv pip install パッケージ
```

`uv pip`で[pipコマンド](./python-pip.md)の互換モードを利用できます。
ロックファイルや仮想環境を作成せずにパッケージをインストールできます。
一時的なインストールに利用できます。

## 仮想環境したい（`uv venv`）

```console
$ cd PROJECT_NAME
$ uv venv
Using CPython 3.12.7
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate.fish

$ source .venv/bin/activate.fish
```

`venv`コマンドで仮想環境を作成できます。
仮想環境はデフォルトで`.venv/`ディレクトリに作成されます。
`source .venv/bin/activate.fish`で仮想環境をアクティベートできます。

:::{note}

`uv init`や`uv add`、`uv sync`を実行するときに`.venv`は自動で作成されます。
なので、`uv venv`は省略して構いません。

CI/CD環境で`uv pip install`を使う場合は、`uv venv`を事前に書いておくとよさそうです。

:::

## Pythonを管理したい（`uv python`）

```console
$ uv python pin 3.12
Pinned `.python-version` to `3.12`

$ uv run python --version
Python 3.12.7

// HomebrewのPythonは3.13.0
$ python3 --version
Python 3.13.0
```

`uv`の大きな特徴のひとつはPythonのバージョンも管理できることです。
`uv python pin`コマンドで、プロジェクトが利用するPythonのバージョンを固定できます。
ピン留めしたバージョン情報は`.python-version`に保存されます。

:::{note}

`.python-version`は`uv`や`pyenv`などで共通に使われる
Pythonのバージョンを指定するためのファイルです。

:::

```console
// Pythonの実行環境をインストール
$ uv python install 3.12
Installed Python 3.12.7 in 5.67s
 + cpython-3.12.7-macos-aarch64-none

// 実行環境をアンインストール
$ uv python uninstall 3.12

// 実行環境がインストールされるパスを確認
$ uv python dir
~/.local/share/uv/python
```

`uv python install`で指定したPython実行環境をインストールできます。
Pythonは`uv python dir`で表示されるパスにインストールされます。

```console
$ uv python list
```

インストール可能なPythonの実行環境は
`uv python list`で確認できます。

```console
$ uv python list --only-installed
cpython-3.13.0-macos-aarch64-none     /opt/homebrew/opt/python@3.13/bin/python3.13 -> ../Frameworks/Python.framework/Versions/3.13/bin/python3.13
cpython-3.12.7-macos-aarch64-none     /opt/homebrew/opt/python@3.12/bin/python3.12 -> ../Frameworks/Python.framework/Versions/3.12/bin/python3.12
cpython-3.11.10-macos-aarch64-none    /opt/homebrew/opt/python@3.11/bin/python3.11 -> ../Frameworks/Python.framework/Versions/3.11/bin/python3.11
cpython-3.11.10-macos-aarch64-none    ~/.local/share/uv/python/cpython-3.11.10-macos-aarch64-none/bin/python3.11
cpython-3.9.6-macos-aarch64-none      /Library/Developer/CommandLineTools/usr/bin/python3 -> ../../Library/Frameworks/Python3.framework/Versions/3.9/bin/python3
```

`--only-installed`オプションで、現在インストール済みのPython実行環境を確認できます。
システムのデフォルトとHomebrewでインストールしたパスも表示されます。

## 外部ツールしたい（`uv tool` / `uvx`）

```console
// CLIパッケージをインストール
$ uv tool install パッケージ名

// CLIパッケージをアンインストール
$ uv tool uninstall パッケージ名

// CLIパッケージを実行
$ uv tool run コマンド名 [オプション]
$ uvx コマンド名 [オプション]
```

`uv tool`でCLI形式で公開されているパッケージを、ユーザーごとの仮想環境で管理できます。
`uv tool run`もしくは`uvx`で実行できます。

:::{note}

`uv tool run`と`uvx`は同じことができますが、内部処理が異なります。
`uvx`は簡単に入力できるので普段使いに適していますが、
スクリプトから呼び出すときは`uv tool run`を使うほうがよいそうです。

:::

```console
// パッケージを確認する
$ uv tool list

$ uv tool dir
~/.local/share/uv/tools

$ uv tool update-shell
Executable directory ~/.local/bin is already in PATH
```

`uv tool`でインストールしたパッケージの一覧を確認できます。
`uv tool`でインストールしたパッケージ本体は`uv tool dir`ディレクトリに保存されます。
コマンドは`~/.local/bin`に（エイリアスが）配置されます。
`uv tool update-shell`を実行してパスを通すことができます。

:::{caution}

`~/.local/bin`は`pipx`でインストールされるコマンドと同じパスです。
同名のコマンドがある場合はインストールに**失敗**します。

`uv`経由のコマンドに置き換える場合は、まず
`pipx uninstall`してから
`uv tool install`してください。

:::

```console
// パッケージを更新する
$ uv tool upgrade パッケージ名
$ uv tool upgrade --all
```

`uv tool upgrade`でパッケージを更新できます。
`--all`オプションで一括更新できます。

:::{note}

~~`uv tool`でインストールしたコマンドを、
一括でアップグレードする方法はありません。~~
現在、[uvのGitHub issue](https://github.com/astral-sh/uv/issues/1419)で議論されているようです。
→ issueはopenになっていますが、`upgrade --all`オプションが追加されていました（2024/11/29）

:::

## ユニットテストしたい（`uvx pytest`）

```console
$ uv tool install pytest

$ uvx pytest
```

## フォーマッター＆リンターしたい（`uvx ruff`）

```console
$ uv tool install ruff

$ uvx ruff format
$ uvx ruff check
```

## 他ツールと比較したい

以下の`uv`のコマンドが、他のパッケージ管理ツール（`poetry`、`pip`、`pipx`）の
どのコマンドに対応しているかを整理しました。

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
|---|---|---|---|---|
| プロジェクト初期化 | `uv init` | `poetry init` | × | × |
| 仮想環境作成 | `uv venv`（自動でもOK） | 内部で自動 | `python -m venv` | 内部で自動 |
| Pythonバージョン固定 | `uv python pin 3.12` | .python-version に依存（pyenv） | × | × |
| Pythonバージョン取得 | `uv python list` | × | × | × |
| パッケージ追加 | `uv add パッケージ` | `poetry add` | `pip install` | `pipx install` |
| 開発用依存追加 | `uv add --dev` | `poetry add --dev` | `pip install` + 手動管理 | × |
| パッケージ削除 | `uv remove` | `poetry remove` | `pip uninstall` | `pipx uninstall` |
| 依存ロック生成 | `uv lock / uv pip compile` | `poetry lock` | `pip freeze`（用途が異なる） | × |
| 依存インストール | `uv sync` | `poetry install` | `pip install -r` | × |
| パッケージ更新 | `uv update` | `poetry update` | `pip install -U` | `pipx upgrade` |
| パッケージ実行 | `uv run` | `poetry run` | `python -m`や手動 | `pipx run` |
| ビルド | `uv build` | `poetry build` | `python -m build` | × |
| パッケージ公開 | `uv publish` | `poetry publish` | × (`twine upload`) | × |
| CLIツールのインストール | `uv tool install` | × | × | `pipx install` |
| CLIツールの実行 | `uv tool run / uvx` | × | × | `pipx run` |
| CLIツールの一覧確認 | `uv tool list` | × | × | `pipx list` |
| 一時的なインストール | `uv pip install` | × | `pip install` | `pipx install` |

Pythonには標準の`pip`のほかにさまざまなパッケージマネージャーが存在します。
力不足な`pip`の機能の補うためにさまざまなツールが登場し、
まるで戦国時代のような混乱がずっと続いていました。

しかし、2024年ころに、それらの役割をひとつに統合し、高速で一貫性のある操作を提供する
パッケージマネージャーとして`uv`が注目されはじめました。

`uv`はPEPに準拠しており、今後のデファクトスタンダードになっていく可能性が高いため、
新規プロジェクトは`uv`で作りはじめるのがよいと思います。

:::{note}

とても人気の高いプログラミング言語であるPythonですが、
長い間パッケージの依存性を管理する方法が標準化されていませんでした。

2018年のPIP518で導入された`pyproject.toml`は、
それまでの`setup.py`や`requirements.tx`に代わるモダンなパッケージ記述方式です。

パッケージングに関する詳細を確認したい場合は、
PEP518（ビルドツールの標準化）、
PEP517（ビルド手順の標準化）、
PEP621（メタデータの標準化）、
PEP508（依存関係の記法）
の公式ドキュメントを参照してください。

:::
