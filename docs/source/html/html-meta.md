# メタ情報したい（`meta`）

```html
<head>
    <meta charset="utf-8">
    <meta name="description" content="サイトの説明">
    <meta name="viewport" content="width=device-width">

    <!-- name属性は自由なキーを設定できる -->
    <meta name="キー" content="値">
</head>
```

メタ情報は`head`タグの中に記述します。
`meta`タグを使ってkey-valueペアで設定します。

`head`タグそのものや、`title`・`link`・`script`については [ヘッド情報したい（`head`）](html-head.md) を参照してください。

## 文字エンコーディングしたい（`charset`）

```html
<meta charset="utf-8">
```

`charset`キーで、文書の文字エンコーディングを設定できます。
HTML標準で使えるのは`utf-8`のみです。

この宣言は省略不可で、`head`の最初の方（`title`より前）に書いておく必要があります。

## サイト説明したい（`description`）

```html
<meta name="description" content="サイトの説明">
```

`description`キーで、ページの内容を要約する説明文を設定できます。
`content`に設定できる値は任意の文字列です。
省略すると、検索エンジンが本文から抜粋してスニペットを作ります。

検索結果のスニペットとして表示されることがあるため、ページごとに簡潔で具体的な説明を書いておくとよいです。

## クロール制御したい（`robots`）

```html
<meta name="robots" content="index,follow">
```

`robots`キーで、検索エンジンのクローラーへの指示を設定できます。
`content`に設定できる値は
`index`/`noindex`（インデックスするか）と
`follow`/`nofollow`（リンクを辿るか）の
組み合わせです。
デフォルトは`index,follow`です。

下書きページや検索結果に出したくないページには`noindex`を明示しておくとよいです。

## ビューポートしたい（`viewport`）

```html
<meta name="viewport" content="width=device-width">
```

`viewport`キーで、
[ビューポート](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta/name/viewport)
のサイズを設定できます。
`content`に設定できる値は
`width`（表示幅）や
`initial-scale`（初期表示倍率）などのカンマ区切りです。
省略するとブラウザ標準のレイアウト幅で表示されます。

画面の幅はデバイスによって異なるため、`width=device-width`を設定しておきましょう。
よく`initial-scale=1`を書いているサンプルがありますが、`initial-scale`のデフォルトは1倍なので省略してよいと思います。

## OGPしたい（`og:*`）

```html
<meta property="og:type" content="ページの種類（website / article）" />
<meta property="og:url" content="ページのパーマリンク（絶対URL）" />
<meta property="og:title" content="ページのタイトル" />
<meta property="og:description" content="ページのディスクリプション" />
<meta property="og:image" content="ページのサムネイル画像（絶対URL）" />
<meta property="og:site_name" content="サイト名" />
```

`og:*`キーで、OGP（The Open Graph Protocol）を設定できます。
ウェブサイトや記事がSNSなどでシェアされたときに利用されるメタデータです。
`og:type`（ページの種類）、`og:url`（絶対URL）、`og:title`（タイトル）、`og:description`（説明文）、`og:image`（サムネイル画像の絶対URL）、`og:site_name`（サイト名）などがあります。

昔は`<head prefix="og: http://ogp.me/ns#">`のように`prefix`属性が必要とされましたが、
いまの主要なSNSは`prefix`なしでも`og:*`を認識するので省略してかまいません。

適切に設定しておくと、シェアされたときにいい感じに表示されます。
OGPが適切に設定できたかどうかは
[OGP確認ツール](https://ogp.buta3.net/)
などの外部ツールで確認できます。

CMSではプラグインが用意されている場合もあり、自分で書く必要はないかもしれませんが、その構成要素は理解しておくとよいと思います。
また、上記のサンプルは必要最低限の要素を抜粋したものです。
[OGPの公式ページ](https://ogp.me/)を読むと、もっと広く表現できるようです。

## OGP画像したい（`og:image:*`）

```html
<meta property="og:image:url" content="og:imageと同じ">
<meta property="og:image:secure_url" content="HTTPSが要求されたときの画像URL">
<meta property="og:image:type" content="画像のMIMEタイプ">
<meta property="og:image:width" content="画像の幅（px）">
<meta property="og:image:height" content="画像の高さ（px）">
<meta property="og:image:alt" content="画像の代替テキスト">
```

`og:image:*`キーで、`og:image`に関する詳細情報を設定できます。
`og:image:url`（`og:image`と同じURL）、`og:image:secure_url`（HTTPS用URL）、`og:image:type`（MIMEタイプ）、`og:image:width`/`og:image:height`（画像サイズ、px）、`og:image:alt`（代替テキスト）があります。

いずれも省略可能なオプション項目です。

## X（Twitter）Cardしたい

```html
<meta name="twitter:card" content="カードの種類（summary / summary_large_image / app / player）" />
<meta name="twitter:site" content="@サイトのユーザー名" />
<meta name="twitter:creator" content="@ページ作成者のユーザー名" />
```

`twitter:*`キーで、X（旧Twitter）のCardを設定できます。
`twitter:card`（カードの種類）、`twitter:site`（サイトのユーザー名）、`twitter:creator`（ページ作成者のユーザー名）などがあります。

タイトル・説明・画像は`twitter:*`を書かなければ`og:*`の値が使われます。
そのため、OGPを設定していれば、追加で書くのは`twitter:card`くらいで足ります。

## リダイレクトしたい

```html
<meta http-equiv="refresh" content="秒数;url=リダイレクト先のURL">
```

`http-equiv="refresh"`キーで、ページのリダイレクトを設定できます。
`content`に設定できる値は「待機秒数」と「リダイレクト先URL」をセミコロンでつないだ文字列です。

:::{warning}

`meta`によるリダイレクトは、利用者の予告なくページが切り替わるためアクセシビリティ上の問題があります。
サーバー側で301／302リダイレクトを設定できる場合は、そちらを使うほうがよいです。

:::

:::{seealso}

- [](./html-head.md)
- [](./html-doctype.md)

:::

## リファレンス

- [meta](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta)
- [meta name="viewport"](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta/name/viewport)
- [Robots \<meta\> tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [OGPの公式ページ](https://ogp.me/)
- [OGP確認ツール](https://ogp.buta3.net/)
- [X Cards: Getting started](https://developer.x.com/en/docs/x-for-websites/cards/guides/getting-started)
