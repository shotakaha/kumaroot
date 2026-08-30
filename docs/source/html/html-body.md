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

## フォントしたい（`font-family`）

```css
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    line-height: 1.7;
    color: #333333;
}
```

`font-family`、`line-height`、`color`などの継承可能なプロパティは、`body`にまとめて指定しておくと便利です。

:::{note}

`rem`の基準になる`font-size`は、`body`ではなく`html`に指定します。

:::

:::{seealso}

- [](./html-html.md)
- [](./css-font.md)

:::

## 中央寄せしたい（`margin`）

```css
body {
    max-width: 720px;
    margin: 0 auto;
    padding: 0 1rem;
}
```

`margin: 0 auto`で、ページ両端の余白を自動設定して中央寄せにできます。
このとき、`width`（もしくは`max-width`）でページ幅（の上限）を設定します。

## 背景色したい（`background-color`）

```css
body {
    background-color: #ffffff;
}
```

`background-color`プロパティで、ページ全体の背景色を変更できます。

:::{note}

内容が短いページでは画面下部に地の色（`html`の背景色）が見えてしまいます。

:::

## リファレンス

- [body](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/body)
