# OGPしたい（`og:*`）

```html
<head>
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://example.com/" />
    <meta property="og:title" content="ページのタイトル" />
    <meta property="og:description" content="ページの説明" />
    <meta property="og:image" content="https://example.com/ogp.png" />
    <meta property="og:site_name" content="サイト名" />
</head>
```

OGP（The Open Graph Protocol）は、ページがSNSでシェアされたときの見た目を指定するためのメタデータです。
`meta`タグの`property`属性に`og:*`のキーを、`content`属性に値を書きます。

`name`ではなく`property`を使う点が、他の`meta`タグと違います。

## 基本の6項目したい

```html
<meta property="og:type" content="website" />
<meta property="og:url" content="https://example.com/blog/1" />
<meta property="og:title" content="記事のタイトル" />
<meta property="og:description" content="記事の要約" />
<meta property="og:image" content="https://example.com/blog/1/ogp.png" />
<meta property="og:site_name" content="サイト名" />
```

まず設定するのはこの6つです。

- `og:type` … ページの種類。トップページは`website`、記事は`article`
- `og:url` … ページのURL。相対パスではなく`https://`から始まる絶対URLにします
- `og:title` … シェア時に表示されるタイトル
- `og:description` … シェア時に表示される説明文
- `og:image` … サムネイル画像のURL。これも絶対URLにします
- `og:site_name` … サイト全体の名前

:::{note}

昔は`<head prefix="og: http://ogp.me/ns#">`のように`prefix`属性が必要とされましたが、
いまの主要なSNSは`prefix`なしでも`og:*`を認識するので省略してかまいません。

:::

## OGP画像を細かく指定したい（`og:image:*`）

```html
<meta property="og:image" content="https://example.com/ogp.png" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="画像の内容の説明" />
```

`og:image`に続けて`og:image:*`を書くと、画像の詳細を補足できます。

- `og:image:type` … 画像のMIMEタイプ（`image/png`など）
- `og:image:width` / `og:image:height` … 画像のピクセルサイズ
- `og:image:alt` … 画像の代替テキスト

いずれも省略できます。
サイズを伝えておくと、SNS側が画像を読み込む前にレイアウトを確保できます。
OGP画像は`1200 x 630`ピクセルがよく使われます。

## X（旧Twitter）のCardしたい（`twitter:*`）

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@サイトのアカウント" />
```

X（旧Twitter）は独自の`twitter:*`メタデータを持ちますが、
`twitter:*`がない項目は`og:*`の値にフォールバックします。

そのため、OGPを設定していれば、追加で書くのは次のくらいで足ります。

- `twitter:card` … カードの形式。大きい画像なら`summary_large_image`、小さいサムネイルなら`summary`
- `twitter:site` … サイトのXアカウント（`@`から始まる）

`twitter:*`は`property`ではなく`name`属性を使います。

## 確認したい

書いたOGPが意図どおりに表示されるかは、外部のプレビューツールで確認できます。

- [OGP確認ツール](https://ogp.buta3.net/)
- 各SNSの公式デバッガー（Facebook Sharing Debuggerなど）

SNSはOGPの情報をキャッシュするので、修正がすぐ反映されないことがあります。
デバッガーからキャッシュの再取得を指示できます。

## リファレンス

- [OGP 公式ページ](https://ogp.me/)
- [OGP確認ツール](https://ogp.buta3.net/)
- [X Cards: Getting started](https://developer.x.com/en/docs/x-for-websites/cards/guides/getting-started)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
