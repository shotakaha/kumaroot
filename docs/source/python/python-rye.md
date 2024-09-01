# パッケージ管理したい（`rye`）

```console
$ rye init プロジェクト名
$ rye pin バージョン
$ rye sync
$ rye add パッケージ名
$ rye add --dev パッケージ名
$ rye sync
$ rye fmt
$ rye lint
$ rye build
$ rye publish
```

`rye`はPython環境の管理とパッケージ管理を一元管理できるツールです。
`.python-version`でPython環境を管理し、
`pyproject.toml`と`requirements.loc`（と`requirements-dev.lock`）のファイルを使って、依存関係を管理できます。

## インストールしたい

```console
$ brew install rye

$ rye --version
rye 0.39.0
commit: 0.39.0 (2024-08-21)
platform: macos (aarch64)
self-python: cpython@3.12.2
symlink support: true
uv enabled: true

$ which -a rye
/opt/homebrew/bin/rye
~/.local/share/mise/installs/rye/latest/bin/rye
~/.rye/shims/rye
```

## 新規プロジェクトしたい（``rye init``）

```console
$ rye init PROJECT_NAME
success: Initialized project in ./PROJECT_NAME
  Run `rye sync` to get started

$ tree PROJECT_NAME
PROJECT_NAME
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── project_name
        └── __init__.py

$ rye init PROJECT_NAME
error: pyproject.toml already exists
```

``init``コマンドでプロジェクトを初期化できます。
Git関係のファイルも自動で生成されます。
同名のプロジェクトがすでに存在する場合は、エラーになります
プロジェクト名を省略した場合は、カレントディレクトリが初期化されます。

```console
$ rye init --script PROJECT_NAME
PROJECT_NAME
├── README.md
├── pyproject.toml
└── src
    └── project_name
        ├── __init__.py
        └── __main__.py
```

``--script``オプションでスクリプト／CLIの作成に適したディレクトリ／ファイル構造を作成できます。

```console
$ rye init --license ライセンス名
PROJECT_NAME
├── LICENSE.txt
├── README.md
├── pyproject.toml
└── src
    └── project_name
        └── __init__.py
```

``--license``オプションで、指定したライセンスの``LICENSE.txt``を自動で生成できます。
ライセンス名が正しくない場合、初期化に失敗します。

## パッケージを追加したい（``rye add``）

```console
$ rye add パッケージ名
$ rye remove パッケージ名

$ rye add パッケージ名==バージョン
$ rye add パッケージ名 --features パッケージ名
$ rye add --dev パッケージ名
$ rye add --git リポジトリ
$ rye add --url URL
```

`rye add`コマンドでプロジェクトにパッケージを追加できます。

## パッケージをインストールしたい（``rye sync``）

```console
$ rye sync
$ rye sync --update パッケージ名
$ rye sync --update-all
```

`rye sync`コマンドで、`pyproject.toml`にしたがってパッケージをインストールします。
`--update`オプションで特定のパッケージを更新できます。

## フォーマッターしたい（``rye fmt``）

```console
$ rye fmt          # ファイル修正
$ rye fmt --check  # チェックのみ
```

`fmt`（もしくは`format`）コマンドで、コードをフォーマット（＝整形）できます。
フォーマッターは[ruff](./python-ruff.md)を利用します。
フォーマット時のオプションは`pyproject.toml`の`[tool.ruff.format]`セクション、もしくは``ruff.toml``、``.ruff.toml``で設定できます。

``--check``オプションは、フォーマットが必要かどうかのチェックのみで、ファイルは書き換えられません。
CIなどのチェックにいれる場合に有用です。

## リンターしたい（``rye lint``）

```console
$ rye lint        # チェックのみ
$ rye lint --fix  # ファイル修正
```

`lint`コマンドで、コーディングスタイルを確認できます。
リンターは[ruff](./python-ruff.md)を利用します。
リンター時のオプションは`pyproject.toml`の`[tool.ruff.lint]`セクション、もしくは``ruff.toml``、``.ruff.toml``で設定できます。

``--fix``オプションは、修正が必要な場合にファイルを書き換えます。

## パッケージをビルドしたい（``rye build``）

```console
$ rye build
```

`build`コマンドでパッケージをビルドできます。

## パッケージを公開したい（``rye publish``）

```console
$ rye publish
```

``publish``コマンドでビルドしたパッケージを公開できます。

## 設定したい（``rye config``）

```console
$ rye config --show-path
~/.rye/config.toml

$ rye config --get behavior.use-uv
$ rye config --get behavior.global-python
```

``config``コマンドで設定オプションを確認、変更できます。
デフォルトは``~/.rye/config.toml``が対象です。

## Python環境したい（``rye pin`` / ``rye toolchain``）

```console
$ rye pin 3.12.5
pinned 3.12.5 in ./.python-version

$ rye sync
Downloading cpython@3.12.5
Checking checksum
Unpacking
Downloaded cpython@3.12.5
...
```

`pin`コマンドでPython環境を指定できます。
その設定は`.python-version`に保存されます。
`pin`した時点では環境は変わらず、`sync`することで切り替えることができます。
指定したバージョンがない場合は、自動ダウンロードがはじまります。

```console
// バージョンを指定してダウンロード
$ rye toolchain fetch 3.12.4
Downloading cpython@3.12.4
Checking checksum
Unpacking
Downloaded cpython@3.12.4

// 利用できるバージョンを確認
$ rye toolchain list
cpython@3.12.5 (~/.rye/py/cpython@3.12.5/bin/python3)
cpython@3.12.4 (~/.rye/py/cpython@3.12.4/bin/python3)
cpython@3.12.2 (~/.rye/py/cpython@3.12.2/bin/python3)
cpython@3.11.8 (~/.rye/py/cpython@3.11.8/bin/python3)

// 不要なバージョンを削除
$ rye toolchain remove 3.12.4
Removed installed toolchain cpython@3.12.4

// パスを指定してローカル環境を使用
$ rye toolchain register パス
```

また、``toolchain``コマンドで、Python環境を操作できます。

```console
$ rye toolchain remove 3.12.5
error: toolchain cpython@3.12.5 is still in use by tool sphinx
$ rye tools uninstall sphinx
Uninstalled sphinx
$ rye tools remove 3.12.5
error: unrecognized subcommand
```

削除指定したバージョンがどこかで使われている場合は、エラーになります。
その環境を利用しているパッケージ名が表示されるので、まずアンインストールして対応します。

## 外部パッケージしたい（``rye tools``）

```console
$ rye tools list
$ rye tools install パッケージ名
$ rye tools uninstall パッケージ名
```

`tools`コマンドで`pipx`のようなことができます。
コマンドは``~/.local/bin``に配置されます。

:::{caution}

`~/.local/bin`は`pipx`でインストールされるコマンドと同じパスです。
同名のコマンドがある場合は**上書き**されます。

:::
