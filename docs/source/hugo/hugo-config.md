# 設定ファイルしたい（`/config/`）

```{toctree}
---
maxdepth: 1
---
hugo-config-hugo
hugo-config-permalinks
hugo-config-copyright
hugo-config-format
hugo-config-paginate
hugo-config-markup
hugo-config-services
hugo-config-menu
hugo-config-taxonomies
hugo-config-languages
```

## 分割したい（オススメ）

```txt
config
├── _default
│   ├── hugo.toml
│   ├── languages.en.toml
│   ├── languages.ja.toml
│   ├── menus.en.toml
│   ├── menus.ja.toml
│   └── params.toml
└── production
    └── hugo.toml
```

設定ファイルは、セクションごとにファイルを分割できます。
準備する手間はかかりますが`/hugo.toml`にまとめるより、分割することをオススメします。
増築する可能性が少しでもあるならば強くオススメします。

また、ステージング用やプロダクション用など
環境ごとにディレクトリを分けることができます。
すべての環境に共通する設定はデフォルト設定（`config/_default/`）に作成します。
環境ごとに異なる差分を`config/環境名/`に作成します。

多言語サイトにしたい場合も、そのセクションの言語別ファイルを作成するだけで簡単に対応できます。

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

## 設定ファイルしたい（`hugo --config`）

```console
$ hugo --config 設定ファイル
$ hugo --config 設定ファイル1,設定ファイル2,設定ファイル3
```

`--config`オプションで設定ファイルのパスを変更できます。
複数の設定ファイルを指定したり、
ディレクトリを指定したりできます。

## リファレンス

- [Configuration](https://gohugo.io/getting-started/configuration/)
