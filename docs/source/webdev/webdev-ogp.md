# OGPの作り方

OGPはウェブサイトや記事が、SNSなどシェアされたときに利用されるメタデータです。
CMSではプラグインが用意されている場合もありますが、
公式ドキュメントを参考に自作できます。

## 基本のOGPタグ

```html
<meta property="og:title" content="記事のタイトル">
<meta property="og:description" content="記事の概要">
<meta property="og:type" content="article">
<meta property="og:image" content="画像のURL（絶対URL）">
<meta property="og:url" content="記事のURL（絶対URL）">
```

## 画像の追加OGPタグ

```html
<meta propery="og:image:url" content="og:imageと同じ">
<meta propery="og:image:secure_url" content="HTTPSが要求されたときの画像URL">
<meta propery="og:image:type" content="画像のMIMEタイプ">
<meta propery="og:image:width" content="画像の幅（px）">
<meta propery="og:image:height" content="画像の高さ（px）">
<meta propery="og:image:alt" content="画像の代替テキスト">
```

## リファレンス

- [Open Graph Protocol](https://ogp.me/)
