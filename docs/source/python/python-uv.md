# パッケージ管理したい（``uv``）

```console
$ uv init プロジェクト名
$ uv python pin バージョン
$ uv sync
$ uv add パッケージ名
$ uv add --dev パッケージ名
```

`uv`はPython環境の管理とパッケージ管理を一元管理できるツールです。
`.python-version`でPython環境を管理し、
`pyproject.toml`と`uv.lock`のファイルを使って依存関係を管理できます。

## インストールしたい

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

## 新規プロジェクトしたい（``uv init``）

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

``init``コマンドでプロジェクトを初期化できます。
同名のプロジェクトがすでに存在する場合は、エラーになります
プロジェクト名を省略した場合は、カレントディレクトリが初期化されます。

```console
$ uv init --package PROJECT_NAME
PROJECT_NAME
├── README.md
├── pyproject.toml
└── src
    └── project_name
        └── __init__.py

$ uv init --app PROJECT_NAME
PROJECT_NAME
├── README.md
├── hello.py
└── pyproject.toml

$ uv init --lib PROJECT_NAME
PROJECT_NAME
├── README.md
├── pyproject.toml
└── src
    └── project_name
        └── __init__.py
```

また、``--package``、``--app``、``--lib``オプションで
作成したいパッケージの目的に適したディレクトリ／ファイル構造を作成できます。

## 仮想環境したい（`uv venv`）

```console
$ cd PROJECT_NAME
$ uv venv
Using CPython 3.12.6 interpreter at: /opt/homebrew/opt/python@3.12/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate.fish

$ source .venv/bin/activate.fish
```

`venv`コマンドで仮想環境を`.venv/`ディレクトリに作成できます。
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
