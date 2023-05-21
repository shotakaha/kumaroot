# Gutenberg

```html
<link rel="stylesheet" href="https://unpkg.com/gutenberg-css@0.7" media="print">
<link rel="stylesheet" href="https://unpkg.com/gutenberg-css@0.7/dist/themes/oldstyle.min.css" media="print">
```

ウェブサイトを印刷する場合（＝印刷プレビュー含む）の表示内容を切り替えるためのCSSフレームワークです。

たとえば、ウェブページのハイパーリンクはとても便利ですが、
紙に印刷した場合はリンク先のURLに飛ぶことができず不便です。
このCSSフレームワークを読み込めば、文中のハイパーリンク（``href``）に対して、
ウェブページでは通常のハイパーリンク表示、
紙に印刷するときはリンク先URLを本文中に展開してくれます。

また、印刷したくない箇所は``class="no-print"``を追記するだけで非表示にできます。

## ナビゲーションを表示しない

```html
<nav class="no-print">...</nav>
```

ウェブサイトにグローバルナビゲーションは必須ですが、印刷物には不要です。

## リファレンス

- [BafS/Gutenberg - GitHub](https://github.com/BafS/Gutenberg)
