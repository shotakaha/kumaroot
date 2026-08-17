# ビルド環境別に設定したい（オススメ）

```txt
config
├── _default
│   ├── hugo.toml
│   ├── languages.en.toml
│   ├── languages.ja.toml
│   ├── menus.en.toml
│   ├── menus.ja.toml
│   └── params.toml
└── production
    └── hugo.toml
```

[前ページの設定ファイルの分割機能](./hugo-config-sections.md)を使って、
環境ごとにディレクトリを分けることができます。
すべての環境に共通する設定は`config/_default/`に作成し、
環境ごとに異なる差分だけを`config/環境名/`に作成します。

## デフォルトとproductionを分けたい

```toml
# config/_default/hugo.toml
buildDrafts = true
buildFuture = true
```

```toml
# config/production/hugo.toml
buildDrafts = false
buildFuture = true
```

もっとも単純な例として、下書き記事の扱いを環境ごとに変える設定です。
`config/_default/hugo.toml`では`buildDrafts = true`にして、
`hugo server`でのローカル開発中は下書きも確認できるようにします。

`config/production/hugo.toml`では`buildDrafts`だけを`false`に上書きします。
書き直す必要があるのはこの1行だけで、他の設定は`_default`のものがそのまま引き継がれます。

`production`環境は`hugo build`（`hugo`のみの実行を含む）のデフォルトです。
一方`hugo server`のデフォルトは`development`環境なので、
明示的に指定しない限りは`config/_default/`の設定のまま動きます。

```console
$ hugo server
# ==> development環境（_defaultのみ適用、buildDrafts = true）

$ hugo
$ hugo build
# ==> production環境（_default + productionが適用、buildDrafts = false）
```

## カスタム環境を追加したい（`baseURL`の切り替え）

```toml
# config/gitlab/hugo.toml
baseURL = "https://ユーザー名.gitlab.io/リポジトリ名/"
```

`_default`と`production`以外にも、好きな名前で環境を追加できます。
GitLab Pagesにデプロイする場合など、本番用とは異なる`baseURL`を使いたいときに便利です。

```console
$ hugo -e gitlab
# ==> _default + gitlabが適用される
```

`-e`（`--environment`）オプションで環境名を指定して実行します。
`config/gitlab/`ディレクトリに置いたファイルが`config/_default/`の設定に上書きされます。

## リファレンス

- [Configuration directory](https://gohugo.io/getting-started/configuration/#configuration-directory)
- [Configure Build](https://gohugo.io/getting-started/configuration/#configure-build)
