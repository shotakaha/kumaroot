# 設定ファイル（``hugo.toml``）

サイトの設定は``hugo.toml``に記述します。
設定の形式は``TOML`` / ``YAML`` / ``JSON``が利用できます。
僕は``TOML``を好んで使っています。

:::{attention}
v0.110からデフォルトの設定ファイル名が``hugo.toml``に変更されました。
しばらくは``config.toml``も使えるようですが、``hugo.toml``に変更することが推奨されています。
詳しくは[hugo.toml vs config.toml - Hugoドキュメント](https://gohugo.io/getting-started/configuration/#hugotoml-vs-configtoml)を参照してください。
:::

## 設定ファイルしたい（``--config``）

```console
$ hugo --config 設定ファイル
$ hugo --config 設定ファイル1,設定ファイル2,設定ファイル3
```

``--config``オプションで設定ファイルを指定できます。
設定ファイルは複数指定できる。

## 設定ファイルを分割したい（``/config/``）

``/config/環境名/``以下に設定ファイルを分割して配置できます。
デフォルトの設定は``/config/_default/``に配置します。

設定項目は[Configuration directory](https://gohugo.io/getting-started/configuration/#configuration-directory)にあるとおりです。

以下に書き出してみましたが、Hugoのデフォルト（＝ビルトイン）の設定でよい場合は、
ファイルを作成する必要はありません。

```console
/config/_default/
hugo.toml
build.toml
cache.toml
cascade.toml
deployment.toml
frontmatter.toml
imaging.toml
languages.toml
markup.toml
mediatypes.toml
menus.toml
minify.toml
module.toml
outputformats.toml
outputs.toml
params.toml
permalinks.toml
privacy.toml
related.toml
security.toml
server.toml
services.toml
sitemap.toml
taxonomies.toml
```

### Blowfishの場合

[Blowfishテーマの設定ファイル](https://blowfish.page/docs/configuration/)のセクションでは、次のように設定ファイルを分割しています。

```console
/config/_default/config.toml
/config/_default/languages.ja.toml # 言語関係の設定
/config/_default/menus.ja.toml     # ナビゲーションの設定
/config/_default/params.toml       # テーマ独自の設定
```

多言語サイトにする場合、設定ファイル名も言語ごとに作成できます。

## 用途別に設定したい（``--environment``）

```bash
$ hugo -e 環境名
$ hugo -e gitlab  # デフォルト + GitLab Pagesの設定
$ hugo -e production   # デフォルト + 公開設定
```

``--environment``オプションで、用途別に設定を切り替えることができます。
設定ファイルは``/config/環境名/``ディレクトリの以下に配置します。
デフォルトは``/config/_default/``ディレクトリです。

上記のサンプルでは、次のような設定ファイルの配置を仮定しています。

```console
/config/_default/hugo.toml    # デフォルト設定（ステージング用）
/config/gitlab/hugo.toml      # GitLab Pagesに公開する設定
/config/production/hugo.toml  # 本番環境に公開する設定
```

ローカルでの開発（やステージング環境）では``/config/_default/``、
GitLab Pagesでの構築時は``/config/gitlab/``、
本番環境に公開する場合は``/config/production/``の設定ファイルに切り替えて適用されるようにしています。

### テーマごとに設定したい

この機能を使うと、テーマごとの設定を共存させることができます。
Hugoのテーマ作成はとても自由度が高く、テーマ間の互換性はほぼありません。

お気に入りのテーマを探す過程で、設定ファイルを毎回書き換えるのは面倒です。
次のように、テーマごとに設定ファイル環境を作成すると、その手間がぐっと抑えられます。

```console
/config/_default/hugo.toml    # 実行: hugo server
/config/blowfish/[...].toml   # 実行: hugo -e blowfish server; Blowfishテーマ
/config/ananke/[...].toml     # 実行: hugo -e ananke server; Anankeテーマ
```

## リファレンス

- [Configure Hugo](https://gohugo.io/getting-started/configuration/)
