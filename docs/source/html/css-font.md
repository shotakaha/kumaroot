# フォントしたい（`font-family`）

```css
html {
    font-size: 16px;
}

body {
    font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    line-height: 1.7;
}
```

文字の見た目は、書体・大きさ・太さ・行間などのプロパティで決まります。
`body`にまとめて指定しておくと、ページ全体の文字にその設定が継承されます。

一部だけ変えたいときは、その要素にプロパティを指定し直します。

## フォント書体したい（`font-family`）

```css
body {
    font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
}
```

`font-family`プロパティで、文字の書体を変更できます。
スペースを含む書体名は`"Hiragino Kaku Gothic ProN"`のように引用符で囲みます。

書体はカンマで区切って複数指定できます。
ただし、利用者の環境にない書体はスキップされます。

:::{note}

`sans-serif`（ゴシック体）や`serif`（明朝体）は総称ファミリーです。
どの環境でも必ず何かの書体に割り当てられるため、最後に指定しておくと安全です。

:::

## フォントサイズしたい（`font-size`）

```css
html {
    font-size: 16px;
}

h1 {
    font-size: 2rem;   /* 16px の 2倍 = 32px */
}
```

`font-size`プロパティで、文字の大きさを変更できます。
単位は`px`や`rem`などで指定します。
`px`は絶対単位で、`rem`はルート要素（`html`）の`font-size`を基準にした相対単位です。

:::{note}

`em`という相対単位もあります。
これは親要素の`font-size`を基準にした倍率で指定します。

:::

## フォントウェイトしたい（`font-weight`）

```css
strong {
    font-weight: bold;
}

.thin-heading {
    font-weight: 300;
}
```

`font-weight`プロパティで、文字の太さを変更できます。

`normal`（標準）と`bold`（太字）のキーワードのほか、
`100`から`900`までの数値でも指定できます。`normal`が`400`、`bold`が`700`に相当します。

## 行間を広げたい（`line-height`）

```css
body {
    line-height: 1.7;
}
```

`line-height`プロパティで、行と行の間隔を変更できます。

単位なしの数値を指定すると、その要素の`font-size`に対する倍率になります。
`1.7`なら文字の高さの1.7倍が1行の高さです。

本文は`1.5`〜`1.8`くらいにすると読みやすくなります。
見出しは行が詰まっていてよいので、`1.2`前後にすることが多いです。

## リファレンス

- [font-family](https://developer.mozilla.org/ja/docs/Web/CSS/font-family)
- [font-size](https://developer.mozilla.org/ja/docs/Web/CSS/font-size)
- [font-weight](https://developer.mozilla.org/ja/docs/Web/CSS/font-weight)
- [line-height](https://developer.mozilla.org/ja/docs/Web/CSS/line-height)
