# ページ設定したい（``frontmatter``）

```toml
title = "タイトル"
date = "日付"
images = ["画像パス", "画像パス"]
tags = ["hugo", "frontmatter"]
draft = true
```

ファイルの先頭に記述する[フロントマター](https://gohugo.io/content-management/front-matter/)で
ページごとの設定を記述できます。
フロントマターで設定した変数は、テンプレートで使うことができます。
また、ユーザー定義の変数も設定できます。

HugoではTOML、YAML、JSON、ORGの4つの形式でフロントマターを記述できます。
このドキュメントのサンプルはTOML形式で記述しています。

## タイトルしたい

```toml
title = "正式なタイトル"
linktitle = "リンク用のタイトル"
```

```html
<ul>
    {{ range .Pages.ByLinkTitle }}
    <li>{{ .LinkTitle }}</li>
    {{ end }}
</ul>
```

``.LinkTitle``を使ってリンク用の短いタイトルを設定できます。
関連コンテンツやサイドバーなどにリンク一覧を生成する場合に使ったりします。
``.LinkTitle``が設定されていない場合は``.Title``が表示されます。

## 日付したい

```toml
date = "2023-10-26T15:20:00+09:00"
publishdate = "2023-10-26T15:20:00+09:00"
lastmod = "2023-10-26T15:40:00+09:00"
expirydate = "2024-10-26T15:40:00+09:00"
```

さまざまな日付を設定できます。
日付フォーマットはISO8601形式を採用し、タイムゾーン情報もつけるとよいでしょう。

## 下書きしたい

```toml
draft = true
```

ページの状態を「下書き」に設定できます。
下書き状態のページはレンダリングされません。

確認用に表示したい場合は、``hugo --buildDraft``オプションを使います。

## 日本語したい

```toml
isCJKLanguage = true
```

日本語などを使う場合は設定しましょう。
マルチバイト文字に対して、``.WordCount`` や``.Count``が正確になるらしいです。

## 関連画像したい

```toml
images = [
    "画像のパス",
    "画像のパス",
    "画像のパス",
    ]
```

ページに関連する画像がある場合は、``images``で画像パスをリスト型で設定できます。
この変数は、[OGP用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/opengraph.html)や[Twitter Cards用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/twitter_cards.html)、[Schema用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/schema.html)の内部テンプレートでも使われています。

:::{note}

これらの内部テンプレートの中では、``images``が明示的に設定されていない場合には、リソース（=``$.Resources``）にある**feature**や**cover**、**thumbnail**がファイル名に含まれる画像ファイルを探すようになっています。

:::
