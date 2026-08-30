# ルート要素したい（`html`）

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>ページタイトル | サイト名</title>
    </head>
    <body>
        ...
    </body>
</html>
```

`html`タグは、HTML文書のいちばん外側を囲むタグです。
文書全体で1つだけあり、他のすべてのタグはこの中に入るので「ルート要素」と呼ばれます。

直下に置けるのは`head`タグと`body`タグの2つだけです。
`head`にはページの情報（タイトル、文字コード、読み込むCSSなど）、`body`には表示される内容を書きます。

## 言語を指定したい（`lang`）

```html
<html lang="ja">
```

`html`タグには`lang`属性でページの言語を指定します。
日本語なら`ja`、英語なら`en`です。

`lang`を指定すると、スクリーンリーダーが正しい発音で読み上げ、
ブラウザが翻訳機能や辞書機能を適切に動かせます。
検索エンジンも言語の判定に使うので、必ず付けておきます。

## remの基準にしたい（`font-size`）

```css
html {
    font-size: 16px;
}

h1 {
    font-size: 2rem;   /* 16px の 2倍 = 32px */
}
```

CSSの`rem`という単位は、`html`タグの`font-size`を基準にした倍率です。

`html`の`font-size`を1か所変えるだけで、`rem`で指定したすべての文字が一括で拡大・縮小されます。
ページ全体の文字サイズをまとめて管理したいときに使います。

`body`ではなく`html`が基準になる点に注意します。

## 背景色を指定したい

```css
html {
    background-color: #f4f4f4;
}
```

`html`に背景色を指定すると、`body`の外側まで含めた画面全体がその色になります。

`body`だけに背景色を指定すると、内容が少ないページでは下のほうに`html`の地の色（通常は白）が見えてしまうことがあります。
画面全体を1色で塗りたいときは`html`に指定します。

## リファレンス

- [html](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/html)
- [lang 属性](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Global_attributes/lang)
