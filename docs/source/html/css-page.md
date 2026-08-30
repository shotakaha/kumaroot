# ページ設定したい（`@page`）

```css
@page {
    size: A4 portrait;
    margin: 20mm;
}
```

`@page`ルールで、印刷やPDF保存のときの「用紙のサイズ」と「余白」を指定できます。

`@page`が効くのは印刷時だけなので、画面表示には影響しません。
`@media print`の中にも外にも書けます。

:::{note}

印刷用CSSは、そもそも印刷されることが少ないため、あまり普及していません。
利用者はブラウザの見た目どおりに印刷されることを想定しているかもしれないので、導入するかは検討してください。

:::

## 用紙サイズを指定したい（`size`）

```css
@page {
    size: A4 portrait;
}
```

`size`ディスクリプタで、用紙のサイズと向きを指定します。

- `A4`、`A5`、`Letter`などの用紙名
- `portrait`（縦）、`landscape`（横）の向き
- `210mm 297mm`のように「幅 高さ」を直接指定することもできます

用紙名と向きは`size: A4 landscape`のように並べて書けます。
省略すると、ブラウザの印刷設定で選ばれた用紙が使われます。

## 余白を指定したい（`margin`）

```css
@page {
    margin: 20mm;
}
```

`margin`ディスクリプタで、用紙の端からの余白を指定します。

通常のCSSの`margin`と同じく、値の数で指定範囲が変わります。

```css
@page {
    margin: 20mm 15mm;        /* 上下 左右 */
    margin: 25mm 15mm 20mm;   /* 上 左右 下 */
}
```

単位は`mm`や`cm`がよく使われます。
プリンタには印刷できない外周部分があるため、`0`にしても端まで印刷されるとは限りません。

## 最初のページだけ変えたい（`:first`）

```css
@page {
    margin: 20mm;
}

@page :first {
    margin-top: 60mm;   /* 表紙のように上を大きくあける */
}
```

`@page :first`で、1ページ目だけに別の設定を当てられます。

表紙のタイトルを中央寄りに見せたいときなどに使います。

## 左右のページで変えたい（`:left` / `:right`）

```css
@page :left {
    margin-left: 25mm;
    margin-right: 15mm;
}

@page :right {
    margin-left: 15mm;
    margin-right: 25mm;
}
```

`@page :left` / `@page :right`で、綴じる側の余白を広くとった、冊子向けの設定ができます。

`:left`は偶数ページ、`:right`は奇数ページに対応します。

## 名前付きページを使い分けたい

```css
@page landscape-page {
    size: A4 landscape;
}

.wide-table {
    page: landscape-page;
    break-before: page;
}
```

`@page 名前 { ... }`で名前付きのページ設定を作り、
要素側の`page`プロパティでその名前を指定すると、その要素のあるページだけ設定を切り替えられます。

横長の表やグラフだけ横向きで印刷したい、といったときに使います。

## ブラウザ対応の注意

`@page`の`size`と`margin`、`:first` / `:left` / `:right`は主要ブラウザで使えます。

一方、`@page`の中でヘッダーやフッターを組む`@top-center`などのマージンボックスは、
ほとんどのブラウザが未対応です。
ページ番号や柱を入れたい場合は、印刷用のCSS組版ツール（Paged.jsなど）を使います。

## リファレンス

- [@page](https://developer.mozilla.org/ja/docs/Web/CSS/@page)
- [size](https://developer.mozilla.org/ja/docs/Web/CSS/@page/size)
- [印刷用ウェブサイトの作成](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_media_queries/Printing)
