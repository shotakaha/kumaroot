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
$ uv init    # デフォルトはカレントディレクトリ
$ uv init プロジェクト名
$ uv init --package プロジェクト名
$ uv init --app プロジェクト名
$ uv init --lib プロジェクト名
```

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
