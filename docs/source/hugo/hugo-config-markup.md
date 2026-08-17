# マークアップ設定したい（`[markup]` / `markup.toml`）

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

## シンタックスハイライトしたい

```toml
[markup]
[markup.highlight]
codeFences = true
guessSyntax = false
lineNos = true
lineNoStart = 1
noClasses = false
style = "solarized-dark"
tabWidth = 4
```

[シンタックス・ハイライト](https://gohugo.io/getting-started/configuration-markup/#highlight)を``markup.highlight``セクションで設定できます。

``codeFences``でコードブロック（\`\`\`）のハイライトを有効化し、``style``でカラーテーマ（[Chromaのスタイル一覧](https://gohugo.io/quick-reference/syntax-highlighting-styles/)）を指定します。
``lineNos``を有効にすると行番号が表示され、``lineNoStart``で開始番号を変更できます。

``guessSyntax = false``にしておくと、言語指定がないコードブロックは言語推測をせず、プレーンテキストとして表示します。

## 拡張記法を有効にしたい

```toml
[markup]
[markup.goldmark]
[markup.goldmark.extensions]
strikethrough = true
[markup.goldmark.extensions.extras]
[markup.goldmark.extensions.extras.subscript]
enable = true
[markup.goldmark.extensions.extras.superscript]
enable = true
[markup.goldmark.extensions.typographer]
disable = false
[markup.goldmark.extensions.passthrough]
enable = true
```

goldmarkは[GFM（GitHub Flavored Markdown）](https://github.github.com/gfm/)をベースに、いくつかの拡張記法を``markup.goldmark.extensions``でオン・オフできます。

- ``strikethrough``: ``~~取り消し線~~``（デフォルト有効）
- ``extras.subscript`` / ``extras.superscript``: ``H~2~O``、``x^2^``（デフォルトは``subscript``のみ有効）
- ``typographer``: 引用符やダッシュを自動できれいな記号に変換（デフォルト有効）
- ``passthrough``: LaTeX数式など、Markdownとして解釈させたくない記法をそのまま通す（デフォルト無効）

:::{attention}
``subscript``と``strikethrough``はどちらも``~``を使うため、
``extras.subscript.enable = true``にする場合は``strikethrough = false``にしないと記法が衝突します。
:::

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

## リファレンス

- [Configure Markup](https://gohugo.io/getting-started/configuration-markup/)
