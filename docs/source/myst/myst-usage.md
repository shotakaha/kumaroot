# MySTの使い方

``MyST（Markedly Structured Text）``（ミスト）はMarkdownの拡張のひとつで、科学技術文書の執筆にフォーカスしたものです。
Markdown記法は文書作成を簡単にしてくれますが、仕様のシンプルさゆえに手が届かないケースがあります。
MySTは、そんなMarkdownにreSTの``directive``（ディレクティブ）と``role``（ロール）といった構造化を追加することで、
画像や数式などの書式設定にも対応できるようになっています。

[MyST Tools](https://myst-tools.org/)はSphinxにインスパイアされて開発されているMySTのエコシステムです。
``.md``形式や``.ipynb``形式のファイルから、ウェブサイトと文書（LaTeXやPDF、Word形式）を生成できます。
ウェブサイトは``React``がベースとなっています。
PDF（やLaTeX）のテンプレートはさまざまなジャーナルに対応していて、デフォルトで400種類以上用意されています。
もちろん自作することもできます。
これらのことは[公式ドキュメント](https://myst-tools.org/docs/mystjs/background)に詳しく書かれています。

```{toctree}
---
maxdepth: 1
---
myst-install
myst-quickstart
myst-templates
```

## リファレンス

- [MyST Tools](https://myst-tools.org/)
