# 構造化データしたい（``JSON+LD``）

```html
<script type="application/ld+json">
    {
        構造化データ
    }
</script>
```

ウェブサイトのHTMLに[構造化データ](https://developer.mozilla.org/ja/docs/Web/HTML/Microdata)を追加して、検索エンジンに情報を渡すことができます。
主要な検索エンジンは[Schema.org](https://schema.org/)で定義されているアイテムに対応しています。
[Schema Validator](https://validator.schema.org/)で設定をチェックできます。

構造化データを記述する方法は``Microdata``、``RDFa``、``JSON-LD``があります。
MicrodataとRDFaはHTMLタグに直接記述する形式で、
``JSON+LD``は``script``タグを使って``head``内に記述する形式です。
CMSのテンプレート機能と組み合わせる場合は、``JSON+LD``形式が有用だと思います。

## 固定ページ（``WebSite``）

```html
<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "url": "ウェブサイトのURL",
        "name": "ウェブサイト名",
        "description": "ウェブサイトの説明",
        "image": "OGP画像",
        "author": "機関名",
    }
</script>
```

固定ページは[WebSite](https://schema.org/WebSite)を使います。

## 記事ページ

```html
<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Article",
        "url": "記事のURL",
        "name": "記事のタイトル | ウェブサイト名",
        "description": "記事の概要",
        "image": "OGP画像",
        "author": "機関名",
        "wordCount": "記事の文字数",
        "datePublished": "記事の公開日",
        "dateModified": "記事の最終更新日",
    }
</script>
```

記事ページは[Article](https://schema.org/Article)を使います。

## 記事リスト（``ItemList``）

```html
<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "url": "記事リストのURL",
        "name": "記事リストのタイトル | ウェブサイト名",
        "description": "記事リストの内容",
        "image": "OGP画像",
        "itemListElement": [
            {
                "@type": "Article",
                "url": "記事のURL",
                "name": "記事のタイトル",
                "description": "記事の概要",
                "image": "OGP画像",
                "author": "機関名",
                "wordCount": "記事の文字数",
                "datePublished": "記事の公開日",
                "dateModified": "記事の最終更新日",
            },
            {
                ...
            },
        ]
        "itemListOrder": "https://schema.org/ItemListOrderAscending"
        "numberOfItems": "記事数"
    }
</script>
```

記事リストは[ItemList](https://schema.org/ItemList)を使います。
また、[itemListElement](https://schema.org/itemListElement)の中に、記事（``Article``オブジェクト）を並べます。
リストの順序は[itemListOrder](https://schema.org/itemListOrder)で指定します。
テンプレート言語を使ってすでにソート済みの場合は、``Unorderd``がよいかもしれません。
