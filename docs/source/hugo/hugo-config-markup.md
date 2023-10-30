# マークアップしたい

```toml
[markup]
  defaultMarkdownHandler = "goldmark"
  [markup.goldmark]
  [markup.goldmark.extensions.cjk]
    eastAsianLineBreaks = true
    enable = true
    escapedSpace = true
```

HugoのコンテンツはMarkdown記法で作成できます。
Markdownのパーサーには[goldmark](https://github.com/yuin/goldmark/)が使われています
（v0.60以前は[blackfriday](https://github.com/russross/blackfriday)が使われていました）。

パーサーは他にも``asciidocext``、``org``、``pandoc``、``rst``を使うことができ、
[全体のマークアップ設定](https://gohugo.io/getting-started/configuration-markup/)で変更できます。

基本的には[goldmarkのデフォルト設定](https://gohugo.io/getting-started/configuration-markup/#goldmark)のままで十分ですが、日本語記事を扱うので、CJK設定を有効にしてみました。

## raw HTMLしたい

```toml
[markup]
[markup.goldmark.renderer]
  unsafe = true
```

デフォルトでraw HTMLや危なそうなリンクはレンダリングしません。
インラインのHTMLやJavaScriptをたくさん含むサイトを構築するなど、
必要な場合は、``markup.goldmark.renderer.unsafe = true``で有効にできます。

## シンタックスしたい

[シンタックス・ハイライト](https://gohugo.io/getting-started/configuration-markup/#highlight)を設定できます。

## 目次したい

```toml
[markup]
  [markup.tableOfContents]
    startLevel = 2
    endLevel = 3
    ordered = false
```

Goldmarkを使っている場合、[目次の設定](https://gohugo.io/getting-started/configuration-markup/#table-of-contents)ができます。
デフォルトでは``h2``見出しから``h3``見出しを``ul``でマークアップします。
