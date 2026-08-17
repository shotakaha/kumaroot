# ビルド設定したい（`development` / `production`）

```toml
# config/_default/hugo.toml
buildDrafts = true
buildFuture = true
```

```toml
# config/production/hugo.toml
buildDrafts = false

[services]
[services.googleAnalytics]
ID = "G-測定ID"
```

```console
$ hugo server --openBrowser    # 開発環境（`_default`）で起動
$ hugo server -e production    # 本番環境（`_default` + `production`）で起動
$ hugo build                   # 本番環境（`_default` + `production`）でビルド
```

`--environment`（`-e`）で、Hugoのビルド環境を変更できます。
デフォルトは開発環境（`development`）で、`config/_default/`の設定だけが読み込まれます。
本番環境（`production`）を指定すると、`config/production/`の設定が`_default`の設定に上書きされます。

上記サンプルでは2つのことをしています。
1つは下書き記事の扱いで、開発中は`buildDrafts = true`にして下書きもその場で確認できるようにし、
本番ビルドでは`config/production/hugo.toml`の`buildDrafts = false`だけを上書きして、下書きを公開しないようにしています。

もう1つは[Google Analytics](./hugo-config-googleAnalytics.md)の計測タグです。
`_default`には設定せず、`production`にだけ`[services.googleAnalytics]`を追加しています。
こうすることで、ローカル開発中のアクセスが計測データに混ざるのを防げます。

## 開発環境したい（`_default` / `development`）

`config/_default/`は、デフォルトの設定を配置するディレクトリです。
いわゆる「開発環境」の設定で、`hugo server`を実行すると、この設定が読み込まれます。

## 本番環境したい（`production`）

`config/production/`は、本番環境の設定を配置するディレクトリです。
`hugo build`を実行すると、デフォルトの設定に加えて、この設定が読み込まれます。

```console
$ hugo server --environment production --openBrowser
```

ローカルで本番環境の設定を確認したい場合は、`--environment`オプションで環境名を指定して`hugo server`を実行します。

## GitLab Pagesにデプロイしたい

```toml
# config/_default/hugo.toml
baseURL = "https://www.example.com/custom/"
```

```toml
# config/gitlab/hugo.toml
baseURL = "https://qumasan.gitlab.io/custom/"
```

```console
$ hugo build  # URL = https://www.example.com/custom/
$ hugo -e gitlab  # URL = https://qumasan.gitlab.io/custom/
```

GitLab Pagesは、リポジトリ名によってURLが自動で割り当てられます。
`config/gitlab/`に置いた設定は、`config/_default/`の設定を上書きします。

## リファレンス

- [Configuration directory](https://gohugo.io/getting-started/configuration/#configuration-directory)
- [Configure Build](https://gohugo.io/getting-started/configuration/#configure-build)
