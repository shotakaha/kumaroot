# パッケージ管理したい（`rye`）

```console
$ rye add パッケージ名
$ rye sync
$ rye fmt
$ rye lint
$ rye build
$ rye publish
```

## インストールしたい

```console
$ brew install rye
```

## 新規プロジェクトしたい（``rye init``）

```console
$ rye init  # デフォルトはカレントディレクトリ
$ rye init プロジェクト名
$ rye init --script
$ rye init --license ライセンス名
```

`rye init`コマンドでプロジェクトを初期化できます。
デフォルトはカレントディレクトリが対象です。

## パッケージを追加したい（``rye add``）

```console
$ rye add パッケージ名
$ rye add パッケージ名==バージョン
$ rye add パッケージ名 --features パッケージ名
$ rye add --git リポジトリ
$ rye add --url URL
```

`rye add`コマンドでプロジェクトにパッケージを追加できます。

### 開発環境を追加したい（``rye add --dev``）

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
