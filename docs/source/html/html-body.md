# 本文したい（`body`）

```html
<!DOCTYPE html>
<html lang="ja">
    <head>...</head>
    <body>
        <header>...</header>
        <main>...</main>
        <footer>...</footer>
    </body>
</html>
```

`body`タグは、ブラウザの画面に表示される内容をすべて囲むタグです。
`html`タグの直下に1つだけ置き、`head`タグの後に書きます。

見出し、段落、画像、ナビゲーションなど、利用者が見るものはすべて`body`の中に入ります。
`body`の外（`head`の中）に書いた内容は画面に表示されません。

## ページ全体のフォントを指定したい

```css
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    line-height: 1.7;
    color: #333333;
}
```

`font-family`、`line-height`、`color`などは継承されるプロパティなので、
`body`にまとめて指定しておくと、中のすべての要素にその設定が伝わります。

ページの基本スタイルを1か所で決める場所として使います。
一部だけ変えたい要素には、そこにプロパティを指定し直します。

:::{note}

`rem`の基準になる`font-size`は、`body`ではなく`html`に指定します。
詳しくは [ルート要素したい（`html`）](html-html.md) を参照してください。

:::

## 中央寄せのレイアウトにしたい

```css
body {
    max-width: 720px;
    margin: 0 auto;
    padding: 0 1rem;
}
```

`body`自体にも幅や余白を指定できます。

`max-width`で本文の広がりすぎを防ぎ、`margin: 0 auto`で画面中央に寄せると、
シンプルなページなら`body`だけで読みやすいレイアウトになります。

## 背景色を指定したい

```css
body {
    background-color: #ffffff;
}
```

`body`に背景色を指定すると、内容のある範囲がその色になります。

内容が短いページで画面下部に地の色が見えるのを避けたい場合は、
`body`ではなく`html`に背景色を指定します。

## リファレンス

- [body](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/body)
