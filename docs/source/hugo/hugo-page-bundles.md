# コンテンツ構造とメディア管理

Hugo 0.32から[Page Bundles機能](https://gohugo.io/content-management/page-bundles/)が追加され、``Leaf Bundle``と``Branch Bundle``を使ってコンテンツ構造とメディア管理を設計できるようになりました。

ロゴ画像など、サイト全体に共通するファイルは``/static/``に配置すればよいですが、
ブログ記事のカバー画像は、その記事の周辺に配置したほうが管理の観点から便利です。
そんな運用を可能にしてくれる機能です。

## Leaf Bundle

```console
/content/
 |--- about/
 |     |--- index.md
 |     |--- cover.jpg
 |     |--- heading1.md
 |     |--- heading2.md
 |     |--- heading3.md
 |
 |--- section1/
       |--- subsection1/
       |     |--- index.md
       |     |--- cover.jpg
       |     |--- heading1.md
       |
       |--- subsection2/
             |--- index.md
             |--- cover.jpg
             |--- heading1.md
             |--- heading2.md
```

メインのファイルは``index.md``で、単体テンプレート（``single.html``）が適用されます。

## Branch Bundle

```console
/content/
 |--- about/
       |--- _index.md
       |--- cover.jpg
```

メインのファイルは``_index.md``で、リストテンプレート（``list.html``）が適用されます。
