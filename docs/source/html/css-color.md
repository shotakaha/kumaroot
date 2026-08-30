# 色したい（`color`）

```css
p {
    color: #333333;
}
```

`color`プロパティで文字色を変更できます。
色の指定には、16進数、`rgb()`、`hsl()`、色名などいくつかの書き方があります。

`background-color`で背景色、
`border-color`で枠線の色をを変更できます。

## 文字色したい（`color`）

```css
body {
    color: #333333;
}

a {
    color: #0066cc;
}
```

`color`プロパティで文字色を変更できます。

`color`は継承されるプロパティなので、`body`に指定しておけば、中の見出しや段落にも同じ色が適用されます。
一部だけ色を変えたいときに、その要素に`color`を指定し直します。

## 背景色したい（`background-color`）

```css
.note {
    background-color: #f4f4f4;
    color: #333333;
}
```

`background-color`プロパティで背景色を変更できます。

背景色を指定するときは、文字色もセットで指定します。
背景だけ濃くすると、文字が読めなくなることがあるためです。

## 16進数表記したい（`#rrggbb`）

```css
.box {
    color: #ff6600;
    background-color: #fff;
}
```

色は16進数表記で指定できます。
`#`のあとに赤・緑・青の明るさを2桁ずつ並べて指定します。

`#ff6600`なら、赤が`ff`、緑が`66`、青が`00`です。
各桁は`00`から`ff`までで、数字が大きいほどその色が明るくなります。

同じ数字が2つずつ並ぶときは、`#ffffff`を`#fff`のように3桁に省略できます。

## 半透明にしたい（`rgb()`）

```css
.overlay {
    background-color: rgb(0 0 0 / 50%);
}
```

`rgb()`で赤・緑・青を10進数の数値で指定できます。
値は`0`から`255`までです。

`/`のあとに不透明度を書くと、半透明の色になります。
`50%`ならちょうど半分の透明度で、下にある要素が透けて見えます。

## 色をなじませて調整したい（`hsl()`）

```css
:root {
    --accent: hsl(210 100% 50%);
    --accent-dark: hsl(210 100% 35%);
}
```

`hsl()`で、色相・彩度・明度の3つで色を指定できます。

- 1つ目は色相で、`0`から`360`の角度です。`0`が赤、`120`が緑、`240`が青です
- 2つ目は彩度で、`0%`が灰色、`100%`が鮮やかな色です
- 3つ目は明度で、`0%`が黒、`100%`が白です

色相と彩度をそろえて明度だけ変えると、同じ系統の濃い色・淡い色を作れます。
テーマ色のバリエーションを用意するときに便利です。

## 色名で指定したい

```css
.demo {
    color: red;
    background-color: white;
    border: 1px solid black;
}
```

`red`や`white`のような色名でも色を指定できます。

色名は`red`、`blue`、`green`、`white`、`black`など約150種類が使えます。
すぐ書けるので試作や学習には便利ですが、微妙な色の調整ができないため、本番では16進数や`hsl()`を使うことが多いです。

`transparent`は完全な透明を表す特別なキーワードです。

## リファレンス

- [color](https://developer.mozilla.org/ja/docs/Web/CSS/color)
- [background-color](https://developer.mozilla.org/ja/docs/Web/CSS/background-color)
- [color の値](https://developer.mozilla.org/ja/docs/Web/CSS/color_value)
- [色名の一覧](https://developer.mozilla.org/ja/docs/Web/CSS/named-color)
