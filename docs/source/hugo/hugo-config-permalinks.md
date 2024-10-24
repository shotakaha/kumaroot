# パーマリンクしたい（`[permalinks]`）

```toml
[permalinks]
# セクション名 = "パーマリンクのフォーマット"
post = "/:section/:filename"          # ==> /{ja, en}/post/記事1/
post = "/:section/:year/:month/:day"  # ==> /{ja, en}/post/2023/10/23/
post = "/blog/:year/:month/:day"      # ==> /{ja, en}/blog/2023/123
```

`[permalinks]`セクションで、ビルドした記事やページのURLパターンを設定できます。
デフォルト（＝設定なし）はファイル名をベースとしたURLです。
パーマリンクはサイト全体で統一したほうがよいため、全体設定（`config/_default/hugo.toml`）に記述します。

## 多言語したい

パーマリンクは多言語サイトでも同じように設定できます。
実際に次のようなコンテンツ構造のサイトで動作確認しました。

```console
content/
|-- _index.ja.md    --> public/ja/index.html
|-- _index.en.md    --> public/en/index.html
|-- about.ja.md     --> public/ja/about/index.html
|-- about.en.md     --> public/en/about/index.html
|-- post/
    |-- _index.ja.md   --> public/ja/blog/index.html
    |-- _index.en.md   --> public/en/blog/index.html
    |-- 記事1.ja.md     --> public/ja/blog/年/月/日/index.html
    |-- 記事1.en.md     --> public/en/blog/年/月/日/index.html
```

## セクション名を変更したい

```toml
[permalinks]
[permalinks.page]
post = "/articles/:year/:yearday"

[permalinks.section]
post = "/articles/"
```

``post``セクションのパーマリンクを``/articles/``に変更しています。
ディレクトリ名を変更しなくても、ビルド先のディレクトリ名を変更できます。

## タクソノミー名を省略したい

```toml

[permalinks]
  [permalinks.term]
    tags = "/:slug/"
```

``/tags/タグ名`` → ``/タグ名``のようにタクソノミー名を省略してURLを構築できます。

## パーマリンク設計を考える

パーマリンク設定はHugoだけでなく、どのCMSでも構築時に検討が必要な項目です。
固定ページはファイル名をベースとしたパターンで問題ありませんが、
記事ページはファイル名やタイトル名に依存しないパターンが好ましいです。

また、記事ページは作成頻度が高く、また内容が更新される可能性があります。
そのため、記事タイトルに依存するようなパターンや、
URLが重複してりまうようなパターンは好ましくありません。

僕の中では、WordPressのようなデータベースを利用したCMSであれば、
記事ごと一意なページIDが割り振られるので、それを利用するのがパターンがベストだと思います。

Hugoの場合、ページIDは自動で割り振られないので、運用でカバーするしかありません。
同じ日にいくつも記事を作成しないのであれば、公開日ベースのパターンにするのがよいと思います。

## リファレンス

- [permalinks](https://gohugo.io/content-management/urls/#permalinks)
