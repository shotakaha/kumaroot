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

## フォントサイズしたい（`font-size`）

```css
html {
    font-size: 16px;
}

h1 {
    font-size: 2rem;   /* 16px の 2倍 = 32px */
}
```

`font-size`プロパティで、HTML全体の文字の大きさを変更できます。
ここで設定した値は、`rem`という単位の基準になります。
デフォルトは`16px`です。

## 背景色したい（`background-color`）

```css
html {
    background-color: #f4f4f4;
}
```

`background-color`プロパティで、HTML全体の背景色を変更できます。
このとき`body`の外側まで含めた画面全体がその色になります。
デフォルトは白です。

:::{note}

`body`だけに背景色を指定すると、内容が少ないページでは下のほうに`html`の地の色（通常は白）が見えてしまうことがあります。

:::

## リファレンス

- [html](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/html)
- [lang 属性](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Global_attributes/lang)
