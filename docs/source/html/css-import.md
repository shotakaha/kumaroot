# インポートしたい（`@import`）

```css
/* style.css の先頭 */
@import url("reset.css");
@import url("base.css");
@import url("components.css");
```

`@import`ルールで、CSSファイルの中から別のCSSファイルを読み込めます。

1つのCSSを機能ごとに分割して管理したいときに使います。
`@import`はCSSファイルの**いちばん先頭**（`@charset`の直後）に書く必要があり、
途中や末尾に書くと無視されます。

## 条件をつけて読み込みたい

```css
@import url("print.css") print;
@import url("wide.css") (min-width: 1024px);
```

`@import`のあとにメディアクエリを書くと、その条件のときだけファイルを読み込みます。

- `print` … 印刷時だけ
- `(min-width: 1024px)` … 画面幅が1024px以上のときだけ

## レイヤーに入れて読み込みたい（`layer`）

```css
@import url("reset.css") layer(reset);
@import url("theme.css") layer(theme);
```

`layer()`を付けると、読み込んだCSSをカスケードレイヤー（`@layer`）に入れられます。

フレームワークのCSSを低い優先度のレイヤーに入れておけば、
自分のCSSで詳細度を気にせず上書きできます。

:::{seealso}

- [](./css-layer.md)

:::

## `<link>` との違い

```html
<!-- HTML で読み込む -->
<link rel="stylesheet" href="style.css">
```

外部CSSの読み込みは、HTMLの`<link>`タグでもできます。

`@import`はCSSを1つずつ順番に読み込むため、ファイル数が多いと表示が遅くなりがちです。
本番のサイトでは`<link>`で読み込むか、ビルドツールで1ファイルにまとめることが多く、
`@import`は開発中の分割管理に向いています。

## リファレンス

- [@import](https://developer.mozilla.org/ja/docs/Web/CSS/@import)
- [@layer](https://developer.mozilla.org/ja/docs/Web/CSS/@layer)
- [link](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/link)
