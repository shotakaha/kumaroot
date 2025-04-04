# 設定ファイル（``hugo.toml``）

```toml
# /hugo.toml もしくは
# /config/_default/hugo.toml

baseURL = "https://example.com/sub/"
title = "サイト全体のタイトル"
theme = ["テーマ名"]

# サイト言語の設定
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = false
hasCJKLanguage = true

# サイトのオプション
enableEmoji = true
enableGitInfo = false
enableMissingTranslationPlaceholder = true
enableRobotsTXT = true

# ビルド時のオプション設定
buildDrafts = true
buildFuture = true
timeout = "30s"

# パーマリンク設定
[permalinks]
pages = "/:section/:filename"
posts = "/:section/:year/:yearday"

# タクソノミーの設定
[taxonomies]
tag = "tags"
category = "categories"
author = "authors"

# ページ割の設定
[pagination]
pageSize = 20

# ビルドするファイルの設定
[outputs]
home = ["HTML", "RSS", "JSON"]

# GAの設定
[services]
[services.googleAnalytics]
ID = "G-測定タグID"

# プライバシー設定
[privacy]
[privacy.googleAnalytics]
disable = true
respectDoNotTrack = true
```

サイトの設定は``hugo.toml``に記述します。
設定の形式は``TOML`` / ``YAML`` / ``JSON``が利用できます。
僕は``TOML``形式を使っています。

:::{attention}
v0.110からデフォルトの設定ファイル名が``hugo.toml``に変更されました。
しばらくは``config.toml``も使えるようですが、``hugo.toml``に変更することが推奨されています。
詳しくは[hugo.toml vs config.toml - Hugoドキュメント](https://gohugo.io/getting-started/configuration/#hugotoml-vs-configtoml)を参照してください。
:::

## 設定セクション名

設定できるセクション（root configuration keys）は

1. `build`
2. `caches`
3. `cascade`
4. `deployment`
5. `frontmatter`
6. `imaging`
7. `languages`
8. `markup`
9. `mediatypes`
10. `menus`
11. `minify`
12. `module`
13. `outputformats`
14. `outputs`
15. `params`
16. `permalinks`
17. `privacy`
18. `related`
19. `security`
20. `segments`
21. `server`
22. `services`
23. `sitemap`
24. `taxonomies`

です。

たくさんのセクションがありますが、
すべてにHugoのデフォルト設定が用意されています。
カスタムしたいセクションのみ設定ファイルに追加すればOKです。
