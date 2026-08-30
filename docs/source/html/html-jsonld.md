# 構造化データしたい（`JSON-LD`）

```html
<head>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "url": "https://example.com/",
        "name": "サイト名"
    }
    </script>
</head>
```

構造化データは、ページの内容を検索エンジンが理解できる形で書き添えるしくみです。
うまく認識されると、検索結果にパンくずや記事の日付、レビューの星などが表示されることがあります（リッチリザルト）。

語彙（どんな種類・項目があるか）は[Schema.org](https://schema.org/)で定義されています。
書き方には`Microdata`、`RDFa`、`JSON-LD`の3つがあります。
このうち`JSON-LD`は、HTML本体と分けて`script`タグにまとめて書けるため、CMSやテンプレートと相性がよく、いまの主流です。

`script`タグは`head`内に置くのが一般的ですが、`body`内でもかまいません。

## JSON-LDの書き方

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "記事のタイトル"
}
</script>
```

`<script type="application/ld+json">`の中に、JSON形式でデータを書きます。

- `@context` … 常に`"https://schema.org"`。語彙の定義元を指します
- `@type` … データの種類（`WebSite`、`Article`、`BreadcrumbList`など）
- それ以降 … その種類ごとに決まった項目

:::{warning}

中身はJSONなので、最後の項目の後ろにカンマを付けると構文エラーになります。
（JavaScriptのオブジェクトと違い、末尾カンマは許されません）

書いたあとは[リッチリザルトテスト](https://search.google.com/test/rich-results)や
[スキーマ マークアップ検証ツール](https://validator.schema.org/)で確認します。

:::

## サイト情報を伝えたい（`WebSite`）

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "url": "https://example.com/",
    "name": "サイト名",
    "description": "サイトの説明"
}
</script>
```

`WebSite`は、サイト全体を表す種類です。
トップページに1つ置きます。

`url`と`name`が基本の項目です。

## 記事情報を伝えたい（`Article`）

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "記事のタイトル",
    "description": "記事の概要",
    "image": "https://example.com/blog/1/ogp.png",
    "datePublished": "2026-08-30T09:00:00+09:00",
    "dateModified": "2026-08-31T12:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "組織名"
    }
}
</script>
```

`Article`は、ブログ記事やニュース記事を表す種類です。
各記事ページに置きます。

項目には決まった型があります。

- `headline` … 記事のタイトル（文字列）
- `image` … 画像のURL（文字列）。絶対URLにします
- `datePublished` / `dateModified` … 日時。`2026-08-30`または`2026-08-30T09:00:00+09:00`の形式（ISO 8601）
- `author` … `Person`または`Organization`のオブジェクト。名前だけの文字列にはしません

## パンくずを伝えたい（`BreadcrumbList`）

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "ホーム",
            "item": "https://example.com/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "ブログ",
            "item": "https://example.com/blog/"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "この記事のタイトル"
        }
    ]
}
</script>
```

`BreadcrumbList`は、いまページが階層のどこにいるかを表します。
うまく認識されると、検索結果のURL部分がパンくず表示になります。

- `itemListElement` … `ListItem`の配列
- `position` … 1から始まる順番（数値）
- `item` … そのページのURL。最後の項目（現在ページ）では省略します

`BreadcrumbList`は、画面に表示するパンくず（`nav`タグ）を、検索エンジン向けに書き添えるものです。

:::{seealso}

- [](./html-nav.md)

:::

## リファレンス

- [Schema.org](https://schema.org/)
- [構造化データの仕組みについて - Google 検索セントラル](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [リッチリザルトテスト](https://search.google.com/test/rich-results)
- [スキーマ マークアップ検証ツール](https://validator.schema.org/)
- [マイクロデータ - MDN](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Microdata)
