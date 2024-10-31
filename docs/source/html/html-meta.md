# メタ情報したい（``meta``）

```html
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="サイトの説明">

    <meta name="キー" content="値">

    <title>サイト名</title>
</head>
```

メタ情報は`head`タグの中に記述します。
`meta`タグを使ってkey-valueペアで設定します。

## 文字エンコーディングしたい（``charset``）

```html
<meta charset="utf-8">
```

`charset`キーで文書の文字エンコーディングを設定します。
といっても、``utf-8``以外の値は指定できません。
この宣言は文書の最初の方に書いておく必要があります。

## ビューポートしたい（``viewport``）

```html
<meta name="viewport" content="width=device-width">
```

[ビューポート](https://developer.mozilla.org/ja/docs/Web/HTML/Viewport_meta_tag)のサイズを設定できます。
画面の幅はデバイスによって異なるため、``width=device-width``を設定しておきましょう。
また、``initial-scale``で読み込んだときの表示倍率を設定できます。
よく``initial-scale=1``を書いているサンプルがありますが、デフォルトで1倍なので省略してよいと思います。

## サイト名したい（`title`）

```html
<!--トップページ-->
<title>サイト名</title>

<!--記事／ページ-->
<title>記事のタイトル | サイト名</title>
<title>ページのタイトル | サイト名</title>
```

`title`タグでそのページのタイトルを設定できます。
このタイトルはブックマークに保存するときや、
ウェブ検索の結果の見出しとしても利用されます。
トップページは`サイト名`、記事／ページの場合は「`タイトル | サイト名`」のようにするとよいです。

## サイト説明したい（``description``）

```html
<meta name="description" content="サイトの説明">
```

## OGPしたい

```html
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# article: http://ogp.me/ns/article#">
<title>ページのタイトル</title>
<meta property="og:type" content="ページの種類（website / article）" />
<meta property="og:url" content="ページのパーマリンク（絶対URL）" />
<meta property="og:title" content="ページのタイトル" />
<meta property="og:description" content="ページのディスクリプション" />
<meta property="og:image" content="ページのサムネイル画像（絶対URL）" />
<meta property="og:site_name" content="サイト名" />
```

OGP（The Open Graph Protocol）はウェブサイトや記事が、SNSなどシェアされたときに利用されるメタデータです。
適切に設定しておくと、シェアされたときにいい感じに表示されます。
OGPが適切に設定できたかどうかは[OGP確認ツール](https://ogp.buta3.net/)などの外部ツールで確認できます。

CMSではプラグインが用意されている場合もあり、自分で書く必要はないかもしれませんが、その構成要素は理解しておくとよいと思います。
また、上記のサンプルは必要最低限の要素を抜粋したものです。
[OGPの公式ページ](https://ogp.me/)を読むと、もっと広く表現できるようです。

## OGP画像したい

```html
<meta propery="og:image:url" content="og:imageと同じ">
<meta propery="og:image:secure_url" content="HTTPSが要求されたときの画像URL">
<meta propery="og:image:type" content="画像のMIMEタイプ">
<meta propery="og:image:width" content="画像の幅（px）">
<meta propery="og:image:height" content="画像の高さ（px）">
<meta propery="og:image:alt" content="画像の代替テキスト">
```

画像の設定項目はオプションがあります。

## Twitter Cardしたい

```html
<meta name="twitter:card" content="カードの種類（summary / summary_large_image / app / player）" />
<meta name="twitter:site" content="@サイトのユーザー名" />
<meta name="twitter:creator" content="@ページ作成者のユーザー名" />
```

Twitterには[Card](https://developer.twitter.com/ja/docs/tweets/optimize-with-cards/guides/getting-started)という専用のOGPがあります。
これも追加で設定しておくとよいでしょう。

## リダイレクトしたい

```html
<meta http-equiv="refresh" content="秒数;url=リダイレクト先のURL">
```

リダイレクトの設定も``meta``タグに書きます。
リダイレクトするのに、そのページを読み込むのはもったいないので、この設定もはじめのほうに書いておくとよいです。
