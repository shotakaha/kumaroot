# パッケージ管理したい（``uv``）

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

## パッケージを追加したい（``uv add``）

```console
$ uv add パッケージ名
$ uv remove パッケージ名

$ uv add パッケージ名==バージョン
$ uv add パッケージ名 --extra パッケージ名
$ uv add --dev パッケージ名s
```

## パッケージをインストールしたい（``uv sync``）

```console
$ uv sync
$ uv sync --all-extras
```

## フォーマッターしたい

## リンターしたい

## パッケージをビルドしたい

## パッケージを公開したい