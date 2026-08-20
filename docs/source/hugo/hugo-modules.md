# モジュールしたい（`go.mod`）

```console
$ hugo mod init モジュール名
$ hugo mod get テーマのモジュールパス
$ hugo mod tidy
```

Hugoは内部でGo言語のパッケージ管理の仕組み（`go.mod`/`go.sum`）を使って、
テーマや依存関係を管理できます。
これを「Hugoモジュール」と呼びます。

[テーマしたい](./hugo-themes.md)で紹介した`git submodule`によるテーマ追加とは別の方法で、
`pyproject.toml`のように依存関係をファイルで宣言的に管理できるのが特徴です。

## モジュールを初期化したい（`hugo mod init`)

```console
$ hugo mod init github.com/ユーザー名/リポジトリ名
```

```toml
# go.mod
module github.com/ユーザー名/リポジトリ名

go 1.26.7
```

`hugo mod init`でサイトのルートに`go.mod`が生成され、サイト自体がひとつのモジュールになります。
モジュール名にはGitHubなどのリポジトリパスを使うのが一般的です。

## テーマを追加したい（`hugo mod get`）

```console
$ hugo mod get github.com/nunocoracao/blowfish/v2
```

```toml
# hugo.toml
[module]
  [[module.imports]]
    path = "github.com/nunocoracao/blowfish/v2"
```

`hugo.toml`の`[module.imports]`にテーマのモジュールパスを指定してから`hugo mod get`を実行すると、
テーマをダウンロードして`go.mod`・`go.sum`に依存関係が追記されます。
`themes/`ディレクトリにサブモジュールを追加する必要がなく、リポジトリがすっきりします。

## 依存関係を整理したい（`hugo mod tidy`）

```console
$ hugo mod tidy
```

`go.mod`・`go.sum`から使われていない依存関係を削除し、必要な依存関係を補います。
`pyproject.toml`に対する`uv lock`のような役割です。

## 依存関係を確認したい（`hugo mod graph`）

```console
$ hugo mod graph
```

```console
github.com/ユーザー名/リポジトリ名 github.com/nunocoracao/blowfish/v2@v2.106.0
```

サイトが依存しているモジュールの一覧を、依存関係のグラフ形式で表示します。

:::{note}

`go.sum`にはモジュールのハッシュ値が記録されるため、`git`に含めてバージョン管理しておくとよいです。
チーム開発や別環境でのビルド時に、同じバージョンの依存関係を再現できます。

:::

## リファレンス

- [Hugo Modules](https://gohugo.io/hugo-modules/)
