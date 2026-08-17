# ビルド設定したい（`development` / `production`）

```toml
# config/_default/hugo.toml
buildDrafts = true
buildFuture = true
```

```toml
# config/[環境名]/hugo.toml
buildDrafts = false
buildFuture = true
```

```toml
# config/production/hugo.toml
buildDrafts = false
buildFuture = true
```

```console
$ hugo server --openBrowser    # 開発環境（`_default`）で起動
$ hugo server -e 環境名   # 指定した環境（`[環境名]`）で起動
$ hugo server -e production   # 本番環境（`production`）で起動
```

`--environment`で、Hugoのビルド環境を変更できます。
デフォルトは開発環境（`development`）で、`config/_default/`の設定が読み込まれます。
`--environment`で指定した環境（`[環境名]`）の設定は、`_default`の設定を上書きします。

## 開発環境したい（`_default` / `development`）

```toml
# config/_default/hugo.toml
buildDrafts = true
buildFuture = true
```

```console
$ hugo server --openBrowser
```

`config/_default/`は、デフォルトの設定を配置するディレクトリです。
いわゆる「開発環境」の設定で、`hugo server`を実行すると、この設定が読み込まれます。

## 本番環境したい（`production`）

```toml
# config/production/hugo.toml
buildDrafts = false
buildFuture = true
```

```console
$ hugo build
```

`config/production/`は、本番環境の設定を配置するディレクトリです。
`hugo build`を実行すると、デフォルトの設定に加えて、この設定が読み込まれます。

```console
$ hugo server --environment production --openBrowser
```

ローカルで本番環境の設定を確認したい場合は、`--environment`オプションで環境名を指定して実行します。

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
