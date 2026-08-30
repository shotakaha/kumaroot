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

## 書体を指定したい（`font-family`）

```css
body {
    font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
}
```

`font-family`プロパティで、文字の書体を指定します。

カンマで区切って複数の書体を並べると、左から順に「使えるものがあるか」を試します。
利用者の環境にない書体は飛ばされるので、よく使われる書体から書き、最後は総称ファミリーで締めます。

- 名前にスペースが含まれる書体は`"Hiragino Kaku Gothic ProN"`のように引用符で囲みます
- 最後の`sans-serif`（ゴシック体）や`serif`（明朝体）は総称ファミリーで、どの環境でも必ず何かの書体に割り当てられます

## 大きさを指定したい（`font-size`）

```css
html {
    font-size: 16px;
}

h1 {
    font-size: 2rem;   /* 16px の 2倍 = 32px */
}
```

`font-size`プロパティで、文字の大きさを指定します。

単位は`px`と`rem`をよく使います。

- `px` … 常に固定の大きさ
- `rem` … ルート要素（`html`）の`font-size`を基準にした倍率

`rem`を使うと、`html`の`font-size`を変えるだけでページ全体の文字が一括で拡大・縮小できるので、統一感を保ちやすくなります。

## 太さを変えたい（`font-weight`）

```css
strong {
    font-weight: bold;
}

.thin-heading {
    font-weight: 300;
}
```

`font-weight`プロパティで、文字の太さを指定します。

`normal`（標準）と`bold`（太字）のキーワードのほか、
`100`から`900`までの数値でも指定できます。`normal`が`400`、`bold`が`700`に相当します。

## 行間を広げたい（`line-height`）

```css
body {
    line-height: 1.7;
}
```

`line-height`プロパティで、行と行の間隔を指定します。

単位なしの数値を指定すると、その要素の`font-size`に対する倍率になります。
`1.7`なら文字の高さの1.7倍が1行の高さです。

本文は`1.5`〜`1.8`くらいにすると読みやすくなります。
見出しは行が詰まっていてよいので、`1.2`前後にすることが多いです。

## リファレンス

- [font-family](https://developer.mozilla.org/ja/docs/Web/CSS/font-family)
- [font-size](https://developer.mozilla.org/ja/docs/Web/CSS/font-size)
- [font-weight](https://developer.mozilla.org/ja/docs/Web/CSS/font-weight)
- [line-height](https://developer.mozilla.org/ja/docs/Web/CSS/line-height)
