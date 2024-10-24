# パーマリンクしたい（`[permalinks]` / `permalinks.toml`）

```toml
# config/_default/hugo.toml
[permalinks]
directory_name = "パーマリンクのフォーマット"
```

`[permalinks]`セクション、もしくは`config/_default/permalinks.toml`で、ビルドした記事やページのパーマリンク（URLパターン）を設定できます。
デフォルト（＝設定なし）はファイル名をベースとしたURLです。

## ファイル名をベースにしたい

```toml
[permalinks]
post = "/blog/:filename"
# ==> /blog/記事1/

post = "/:section/:filename"
# ==> /post/記事1/
```

ファイル名やパス、ページのタイトルを使ってパーマリンクを定義できます。

ページ（`page` kind）用のパーマリンク設定に適しています。

- `:section`: セクション名
- `:sections`: 階層をもったセクション名。スライス可能
- `:title`: ページタイトル。front matterで設定
- `:slug`: スラグ。front matterで設定
- `:filename`: 拡張子を除外したファイル名
- `:slugorfilename`: `slug` もしくは `filename`

## 公開日をベースにしたい

```toml
[permalinks]
post = "/:section/:year/:month/:day"
# ==> /post/2023/10/23/

post = "/:section/:year/:yearday"
# ==> /post/2023/123
```

日付トークンを使って、公開日を挿入できます。
記事（`post` kind）用のパーマリンク設定に適しています。

- `:year`: 年（4桁）
- `:month`: 月（01 - 12）
- `:monthname` : 月名
- `:day`: 日（01 - 31）
- `:weekday`: 曜日（0 - 6）
- `:weekdayname`: 曜日名
- `:yearday`: 日数（001 - 365）

個人的に`:year/:yearday`を使うのが好きです。

## セクションしたい

```toml
[permalinks]
[permalinks.page]
posts = "/articles/:year/:yearday"
tutorials = "/training/:slug"
# posts/記事/index.md ==> /articles/年/日数/index.html
# tutorials/記事/index.md ==> /training/スラグ/index.html

[permalinks.section]
posts = "/articles/"
tutorials = "/training/"
# posts/index.md ==> /articles/index.html
# tutorials/index.md ==> /training/index.html
```

セクションごとにパーマリンクを設定できます。

## タクソノミーしたい

```toml
[permalinks]
[permalinks.term]
tags = "/:slug/"
# ==> /タグ名/
```

`/tags/タグ名/`を`/タグ名/`に変更できます。

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

## パーマリンク設計を考える

パーマリンク設定は、HugoだけでなくどのCMSでも構築時に検討が必要な項目です。
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
