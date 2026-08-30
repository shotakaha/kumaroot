# レスポンシブしたい

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
</head>
```

```css
/* スマホ向けを全体に適用（モバイルファースト） */
img {
    max-width: 100%;
    height: auto;
}

/* 画面が広いときだけ上書きする */
@media (min-width: 768px) {
    .container {
        max-width: 720px;
        margin: 0 auto;
    }
}
```

さまざまな画面サイズの端末で、1つのHTMLとCSSを使ってレイアウトを自動調整するデザイン手法を「[レスポンシブ・ウェブ・デザイン](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_media_queries/Using_media_queries)」と呼びます。

やることは大きく3つです。

1. `viewport`の`meta`タグを入れる
2. 画像や要素の幅を固定値にせず、画面に対する割合で指定する
3. メディアクエリ（`@media`）で、画面幅に応じてスタイルを切り替える

メディアクエリの詳しい書き方は [メディアクエリしたい（`@media`）](css-media.md) を参照してください。
このページでは、レスポンシブ特有の話をまとめます。

## ビューポートを設定したい（`viewport`）

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

スマホのブラウザは、デフォルトでは「幅980pxの画面」としてページを描画し、それを縮小表示します。
このままだとPC向けレイアウトがそのまま縮んで表示され、文字が小さくなってしまいます。

`viewport`の`meta`タグを入れると、この挙動を止められます。

- `width=device-width` … ページの幅を端末の画面幅に合わせる
- `initial-scale=1` … 初期表示の拡大率を等倍にする

メディアクエリを使うなら、このタグは必須です。
入れ忘れると`@media (max-width: ...)`が意図通りに効きません。

## 幅を固定値で指定しない（流動レイアウト）

```css
/* 悪い例：画面が狭いと横スクロールが出る */
.card {
    width: 600px;
}

/* 良い例：親要素の幅に追従する */
.card {
    max-width: 600px;
    width: 100%;
}
```

`width: 600px`のように固定すると、画面幅がそれより狭い端末で横スクロールが発生します。
`max-width`で上限だけ決めて、`width: 100%`で親要素に追従させると、狭い画面でも収まります。

幅の単位は`px`より`%`や`rem`、`fr`（グリッド）などの相対値を使うと、画面サイズに合わせて伸縮します。

## 画像を画面からはみ出させない

```css
img,
video {
    max-width: 100%;
    height: auto;
}
```

画像は元のサイズで表示されるため、画面より大きい画像は横にはみ出します。
`max-width: 100%`で親要素の幅を超えないようにし、`height: auto`で縦横比を保ちます。

`reset.css`やベーススタイルにこの1行を入れておくと、個別に指定しなくてもすべての画像が収まります。

## 画面サイズごとに別の画像を出したい（`srcset`）

```html
<img
    src="photo-800.jpg"
    srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
    sizes="(max-width: 600px) 100vw, 800px"
    alt="サンプル写真">
```

`srcset`に「画像ファイルとその実寸幅（`400w`）」を複数並べておくと、
ブラウザが画面サイズや解像度に合わせて最適な1枚を選んで読み込みます。

スマホに巨大な画像を送りつけずに済むので、表示速度と通信量に効きます。
`sizes`は「その画像が実際に表示される幅」をブラウザに伝えるためのヒントです。

## ブレークポイントの目安

```css
@media (min-width: 768px)  { /* タブレット以上 */ }
@media (min-width: 1024px) { /* デスクトップ以上 */ }
```

スタイルを切り替える幅の区切りを「ブレークポイント」と呼びます。
`768px`（タブレット）と`1024px`（デスクトップ）あたりが目安ですが、
端末の普及状況で変わるので、コンテンツが崩れる幅で区切るのが基本です。

:::{note}

Bootstrap5は`576px` / `768px` / `992px` / `1200px` / `1400px`を採用しています。
`max-width`側を`767.98px`のように端数にしているのは、`min-width: 768px`と1px未満で重ならないようにするためです。

:::

## リファレンス

- [メディアクエリーの使用](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_media_queries/Using_media_queries)
- [ビューポートのメタタグ](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta/name/viewport)
- [レスポンシブ画像](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Responsive_images)
- [img 要素](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/img)
- [Bootstrap5 Breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/)
