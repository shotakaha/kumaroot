# パッケージ管理したい（``uv``）

```console
$ uv init プロジェクト名 --app --package --vcs git
$ uv python pin バージョン
$ uv sync
$ uv add パッケージ名
$ uv add --dev パッケージ名
```

`uv`はPython環境の管理とパッケージ管理を一元管理できるツールです。
`.python-version`でPython環境を管理し、
`pyproject.toml`と`uv.lock`のファイルを使って依存関係を管理できます。

## インストールしたい（`uv`）

```console
$ brew install uv

$ uv --version
uv 0.4.1 (Homebrew 2024-08-30)
$ uvx --version
uv-tool-uvx 0.4.1 (Homebrew 2024-08-30)

$ which -a uv
/opt/homebrew/bin/uv
$ which -a uvx
/opt/homebrew/bin/uvx
```

Pythonの実行環境を操作できるコマンドなので、
Homebrewを使ってシステム全体にインストールしました。
`pipx`や`poetry`でもインストールできます。

## 新規プロジェクトしたい（``uv init``）

```console
$ uv --version
uv 0.4.20 (Homebrew 2024-10-08)

// デフォルト（--app --no-package）
$ uv init PROJECT_NAME

// ライブラリ作成（--lib --package）
$ uv init PROJECT_NAME --lib

// CLI&パッケージ（--app --package）
$ uv init PROJECT_NAME --app --package
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

## Python管理したい（`uv python`）

```console
$ uv python pin 3.12
$ uv run python --version
```

`uv python`コマンドでPythonの実行環境を設定できます。
`pin`コマンドでPythonのバージョンをピン留めできます。
ピン留めしたバージョン情報は`.python-version`に保存されます。

また、それぞれのサブコマンドの`--python`オプションで、実行環境を変更できます。

```console
// インストール先のパスを確認
$ uv python dir
~/.local/share/uv/python

// インストール
$ uv python install 3.12

// アンインストール
$ uv python uninstall 3.12
```

`install`コマンドでPython実行環境をインストールできます。
ピン留めしたいバージョンがインストールしてない場合、

```console
$ uv python list
$ uv python list --only-installed
cpython-3.13.0-macos-aarch64-none     /opt/homebrew/opt/python@3.13/bin/python3.13 -> ../Frameworks/Python.framework/Versions/3.13/bin/python3.13
cpython-3.12.7-macos-aarch64-none     /opt/homebrew/opt/python@3.12/bin/python3.12 -> ../Frameworks/Python.framework/Versions/3.12/bin/python3.12
cpython-3.11.10-macos-aarch64-none    /opt/homebrew/opt/python@3.11/bin/python3.11 -> ../Frameworks/Python.framework/Versions/3.11/bin/python3.11
cpython-3.11.10-macos-aarch64-none    ~/.local/share/uv/python/cpython-3.11.10-macos-aarch64-none/bin/python3.11
cpython-3.9.6-macos-aarch64-none      /Library/Developer/CommandLineTools/usr/bin/python3 -> ../../Library/Frameworks/Python3.framework/Versions/3.9/bin/python3
```

`list`コマンドで、インストールできるバージョンを確認できます。
`--only-installed`オプションで、現在の環境にインストールされているPython実行環境を確認できます。
システムのデフォルトとHomebrewでインストールしたパスも表示されます。

## 仮想環境したい（`uv venv`）

```console
$ cd PROJECT_NAME
$ uv venv
Using CPython 3.12.6 interpreter at: /opt/homebrew/opt/python@3.12/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate.fish

$ source .venv/bin/activate.fish
```

`venv`コマンドで仮想環境を作成できます。
仮想環境はデフォルトで`.venv/`ディレクトリに作成されます。
`source .venv/bin/activate.fish`で仮想環境をアクティベートできます。

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

## フォーマッターしたい

```console
$ uvx ruff format
```

`uvx`コマンドは、`pipx run`のようなことができます。
`uv tool run`のエイリアスになっています。

## リンターしたい

```console
$ uvx ruff check
```

## パッケージをビルドしたい（`uv build`）

## パッケージを公開したい（`uv publish`）

## 外部パッケージしたい（``uv tool``）

```console
$ uv tool dir
~/.local/share/uv/tools

$ uv tool update-shell
Executable directory ~/.local/bin is already in PATH

$ uv tool list
$ uv tool run コマンド [オプション]
$ uv tool install コマンド
$ uv tool upgrade コマンド
$ uv tool uninstall コマンド
```

`uv tool`コマンドで`pipx`のようなことができます。
インストールされたパッケージは``uv tool dir``ディレクトリに保存され、
コマンドは``~/.local/bin``に配置されます。

:::{caution}

`~/.local/bin`は`pipx`でインストールされるコマンドと同じパスです。
同名のコマンドがある場合はインストールに**失敗**します。

:::

:::{note}

`uv tool`でインストールしたコマンドを、
一括でアップグレードする方法はありません。
現在、[uvのGitHub issue](https://github.com/astral-sh/uv/issues/1419)で議論されているようです。

:::
