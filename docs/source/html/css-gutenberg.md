# Gutenbergしたい（`gutenberg-css`）

```html
<head>
    <!-- 本体（印刷時だけ適用） -->
    <link rel="stylesheet"
          href="https://unpkg.com/gutenberg-css@0.7" media="print">
    <!-- テーマ（任意） -->
    <link rel="stylesheet"
          href="https://unpkg.com/gutenberg-css@0.7/dist/themes/oldstyle.min.css" media="print">
</head>
```

Gutenbergは、ウェブページを紙に印刷するときの見た目を整えるCSSフレームワークです。

自分で`@media print`を書くほどではないけれど、印刷やPDF保存に最低限対応したい、というときに使います。
読み込むだけで、余白・文字サイズ・改ページなどが印刷向けに調整されます。

## 読み込みたい

```html
<link rel="stylesheet"
      href="https://unpkg.com/gutenberg-css@0.7" media="print">
```

`<link>`に`media="print"`を付けて読み込みます。

`media="print"`があると、このCSSは**画面表示には一切適用されず、印刷（と印刷プレビュー）のときだけ**効きます。
画面のデザインを壊さずに、印刷時の見た目だけを差し替えられます。

テーマ（`oldstyle`など）は追加の`<link>`で読み込みます。省略してもかまいません。

## リンク先URLを本文に出したい

```html
<p>詳しくは<a href="https://example.com/docs">ドキュメント</a>を参照。</p>
```

画面ではふつうのリンクですが、印刷すると次のように展開されます。

```text
詳しくはドキュメント (https://example.com/docs)を参照。
```

紙ではリンクをクリックできないため、Gutenbergが`href`の値を本文の後ろに書き足します。
自分で書くなら`a[href^="http"]::after { content: " (" attr(href) ")"; }`に相当します。

## 印刷したくない要素を隠したい（`.no-print`）

```html
<nav class="no-print">...</nav>
<aside class="no-print">...</aside>
<div class="share-buttons no-print">...</div>
```

`class="no-print"`を付けた要素は、印刷時だけ非表示になります。

紙に不要なものに付けておきます。

- グローバルナビゲーション、パンくず
- サイドバー、広告
- SNSシェアボタン、コメント欄
- 「ページの先頭へ戻る」などの操作ボタン

## リファレンス

- [Gutenberg 公式サイト](https://bafs.github.io/Gutenberg/)
- [BafS/Gutenberg - GitHub](https://github.com/BafS/Gutenberg)

:::{seealso}

- [](./css-media.md)
- [](./css-page.md)

:::
