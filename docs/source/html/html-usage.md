# HTML / CSSの使い方

ウェブサイト作成の基本はHTMLとCSS（とJavaScript）です。
[HTML（Hyper Text Markup Language）](https://developer.mozilla.org/ja/docs/Web/HTML)はサイトの骨組み、[CSS（Cascading Style Sheets）](https://developer.mozilla.org/ja/docs/Web/CSS)はサイトに服を着せる言語です。

ウェブ技術に関することなので、ウェブ検索するとさまざまな情報がヒットします。
中にはすでに古い情報もあります。
最新の機能や仕様に関することは[MDN](https://developer.mozilla.org/ja/docs/Web)のドキュメントを調べるとよいです。

また、現在のウェブ標準は[WHATWG](https://developer.mozilla.org/ja/docs/Glossary/WHATWG)が決めた[HTML Living Standard](https://html.spec.whatwg.org/multipage/)です。
[Can I Use](https://caniuse.com/)でブラウザごとの対応状況を調べることができます。

## HTMLしたい

```{toctree}
---
maxdepth: 1
---
html-doctype
html-semantic
html-meta
html-p
html-img
html-figure
html-a
html-jsonld
html-htaccess
```

## CSSしたい

```{toctree}
css-selectors
css-variables
css-nest
css-font
css-display
css-margin
css-padding
css-responsive
```

## ウェブフォントしたい

- [FontAwesome](https://fontawesome.com/search?o=r&m=free)

## フレームワークしたい

CSSフレームワークを使うと、比較的簡単にウェブをデザイン／レイアウトできます。
そこそこの見た目をさくっと作りたい場合に便利です。
たいていの場合、CDNを経由して読み込ませるのでよいと思います。

以下は、僕がこれまで使ったことがある順番に並べてみました。

- [Materialize](https://materializecss.com/)
- [Bootstrap](https://getbootstrap.jp/)
- [MDB - Material Design for Bootstrap v5 & v4](https://mdbootstrap.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [Tailwind Components](https://tailwindcomponents.com/)
- [PicoCSS](https://picocss.com/)
- [Sakura](https://oxal.org/projects/sakura/)
- [MVP.CSS](https://andybrewer.github.io/mvp/)

## SSGしたい

- [](../sphinx/sphinx-usage.md)
- [](../hugo/hugo-usage.md)
- [](../myst/myst-usage.md)

## サーバーしたい

```{toctree}
---
maxdepth: 1
---
webdev-httpd
webdev-nginx
```

## 未分類

```{toctree}
---
maxdepth: 1
---
webdev-rss
webdev-browser
webdev-css-gutenberg
```
