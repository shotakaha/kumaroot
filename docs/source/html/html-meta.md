# メタ情報したい（``meta``）

```html
<head>
    <meta name="キー" content="値">
</head>
```

``meta``タグや``head``タグの中に配置します。
基本的にkey-valueペアで設定します。

## 文字エンコーディングしたい（``charset``）

```html
<meta charset="utf-8">
```

文書の文字エンコーディングを宣言します。
といっても、``utf-8``以外の値は指定できません。
また、この宣言は文書の最初の方に書いておく必要があります。

## ビューポートしたい（``viewport``）

```html
<meta name="viewport" content="width=device-width">
```

[ビューポート](https://developer.mozilla.org/ja/docs/Web/HTML/Viewport_meta_tag)のサイズを設定できます。
画面の幅はデバイスによって異なるため、``width=device-width``を設定しておきましょう。
また、``initial-scale``で読み込んだときの表示倍率を設定できます。
よく``initial-scale=1``を書いているサンプルがありますが、デフォルトで1倍なので省略してよいと思います。

## サイトを説明したい（``description``）

```html
<meta name="description" content="サイトの説明">
```

## OGPしたい

```html
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# article: http://ogp.me/ns/article#">
<title>ページのタイトル</title>
<meta property="og:title" content="ページのタイトル" />
<meta property="og:type" content="ページの種類（website / article）" />
<meta property="og:url" content="ページのパーマリンク（絶対URL）" />
<meta property="og:image" content="ページのサムネイル画像（絶対URL）" />
<meta property="og:site_name" content="サイト名" />
<meta property="og:description" content="ページのディスクリプション" />
```

OGP（The Open Graph Protocol）を適切に設定しておくと、SNSなどでページをシェアしたときに、いい感じに表示できます。
上記のサンプルは必要最低限の要素を抜粋してみましたが、[OGPの公式ページ](https://ogp.me/)を読むと、もっと広く表現できるようです。

CMSなどを使う場合、自分で書く必要はほとんどなく、まず使い勝手のよさそうなプラグインを探してみるとよいです。

### Twitter Cardしたい

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
