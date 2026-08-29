# メディアクエリしたい（`@media`）

```css
@media (max-width: 600px) {
  body {
    background-color: lightblue;
  }
}
```

`@media`は、表示している環境の条件に合わせてCSSを切り替えるためのルールです。
画面の幅、縦向きか横向きか、ダークモードかどうか、印刷中かどうか、といった条件を指定できます。
上記の例では、画面の幅が600ピクセル以下のときだけ`body`要素の背景色をライトブルーに変更しています。

条件に合わないときは中のCSSはまるごと無視されるので、
「特定の状況のときだけ上書きしたいスタイル」を`@media`の中に書いていくのが基本の使い方です。

## メディア種別したい（`screen` / `print` / `all`）

```css
@media screen {
  /* 画面表示のとき */
}

@media print {
  /* 印刷のとき */
}

@media all {
  /* すべて（省略時と同じ） */
}
```

`@media メディア種別`で、メディア種別ごとにCSSを切り替えられます。

`screen`は通常の画面表示、
`print`は印刷やPDF保存のとき、
`all`はすべての環境で適用されます。
省略すると`all`として扱われます。

```html
<link rel="stylesheet" href="print.css" media="print">
```

メディア種別は、HTMLの`<link>`タグでも指定できます。
`media=print`で印刷用CSSをファイルごと分けられます。

```css
@import url("print.css") print;
```

`@import`で、外部CSSファイルを読み込むときも、メディア種別を指定できます。

## 画面幅で切り替えたい

```css
/* まずはスマホ向けのスタイルを普通に書く */
.container {
  width: 100%;
  padding: 16px;
}

/* 幅768px以上のときだけ上書きする */
@media (min-width: 768px) {
  .container {
    width: 720px;
    margin: 0 auto;
  }
}
```

もっともよく使う用途です。
`min-width`は「その幅以上のとき」、`max-width`は「その幅以下のとき」に適用されます。

スマホ向けのスタイルを先に書いておき、画面が広いときだけ`@media (min-width: ...)`で上書きする書き方を「モバイルファースト」と呼びます。
分岐が読みやすくなるので、迷ったらこの順番で書きます。

幅の区切り（ブレークポイント）は端末の普及状況で変わりますが、`768px`（タブレット）と`1024px`（PC）あたりを目安にすることが多いです。

## 範囲を指定して切り替えたい

```css
@media (min-width: 768px) and (max-width: 1023px) {
  .container {
    width: 720px;
  }
}
```

`and`でつなぐと「すべての条件を満たすとき」になります。
上の例は「幅768px以上、かつ1023px以下」、つまりタブレットくらいのサイズのときだけ適用されます。

```css
@media (width >= 768px) and (width <= 1023px) {
  .container {
    width: 720px;
  }
}
```

新しいブラウザでは、上のように`>=`や`<=`の比較記号でも書けます（範囲構文）。
`min-width` / `max-width`より直感的ですが、古い環境も対象にする場合は従来の書き方が無難です。

## 縦向き・横向きで切り替えたい

```css
@media (orientation: portrait) {
  /* 縦向き（縦長）のとき */
}

@media (orientation: landscape) {
  /* 横向き（横長）のとき */
}
```

`orientation`で端末の向きを判定できます。
スマホを横にしたときだけレイアウトを変えたい、といった場合に使います。

## ダークモードに対応したい

```css
/* 通常（ライト）のスタイル */
body {
  background: #ffffff;
  color: #1a1a1a;
}

/* OS・ブラウザがダークモードのとき */
@media (prefers-color-scheme: dark) {
  body {
    background: #1a1a1a;
    color: #eeeeee;
  }
}
```

`prefers-color-scheme`は、利用者がOSやブラウザで設定している外観（ライト／ダーク）に反応します。
`dark`のときだけ色を差し替えれば、ダークモード対応になります。

CSS変数（カスタムプロパティ）と組み合わせると、色の定義を1か所にまとめられて管理しやすくなります。

## 印刷用のスタイルにしたい

```css
@media print {
  nav,
  footer,
  .no-print {
    display: none;
  }

  body {
    font-size: 11pt;
    color: #000;
  }
}
```

`@media print`の中身は、印刷やPDF保存のときだけ適用されます。
ナビゲーションやボタンなど紙に不要な部分を隠したり、文字サイズを`pt`（ポイント）で指定し直したりします。

## アニメーションを控えめにしたい

```css
.panel {
  transition: transform 0.3s ease;
}

/* 「動きを減らす」設定をしている人向け */
@media (prefers-reduced-motion: reduce) {
  .panel {
    transition: none;
  }
}
```

`prefers-reduced-motion`は、OSで「視差効果を減らす」「アニメーションを減らす」を設定している人に反応します。
動きで気分が悪くなる人への配慮として、アニメーションやスクロール演出を弱める・止めるために使います。

## 条件を否定・複数指定したい

```css
/* ダークモード「以外」のとき */
@media not (prefers-color-scheme: dark) {
  ...
}

/* 幅600px以下 または 印刷のとき（カンマは「または」） */
@media (max-width: 600px), print {
  ...
}
```

- `not`: 条件を否定する
- `,`（カンマ）: どれか1つでも当てはまれば適用（「または」）
- `and`: すべて当てはまれば適用（「かつ」）

## その他に指定できる条件

| 条件 | 内容 |
| --- | --- |
| `hover` | マウスなどでホバーできる環境か（`hover: hover` / `hover: none`） |
| `pointer` | ポインターの精度（`fine`はマウス、`coarse`は指） |
| `aspect-ratio` | 表示領域の縦横比 |
| `resolution` | 画面の解像度（高解像度ディスプレイの判定など） |
| `prefers-contrast` | コントラストを強めたい設定か |

## 親要素の幅で切り替えたい（`@container`）

```css
/* 監視対象のコンテナーを宣言する */
.card-list {
  container-type: inline-size;
}

/* .card-list の幅が400px以上のとき、中の .card を横並びにする */
@container (min-width: 400px) {
  .card {
    display: flex;
    gap: 16px;
  }
}
```

`@media`が「画面（ビューポート）の幅」を見るのに対し、
`@container`は「親コンテナーの幅」を見てスタイルを切り替えます。

同じ部品をサイドバーとメインの両方に置くような場合、
画面幅ではなく置かれた場所の幅で見た目を変えられるので、部品を使い回しやすくなります。
細かい部品はコンテナクエリ、ページ全体のレイアウトはメディアクエリ、と使い分けます。
