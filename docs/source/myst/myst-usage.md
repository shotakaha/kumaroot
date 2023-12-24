```{eval-rst}
.. index::
    pair: MyST; usage
```

# MySTの使い方

``MyST（Markedly Structured Text）``（ミスト）はMarkdownの拡張のひとつで、科学技術文書の作成の効率化を目的にしています。
調べてみると、よさそうな感じだったので、ここにまとめていこうと思います。
Markdown記法は技術文書のデファクトです（と思っています）。
シンプルな仕様のため、READMEを書いたり、簡単な会議メモを作ったりするのにとても適しています。
しかし、シンプルがゆえに図表や数式の書式設定など、融通が効かない場面もあります。

MySTは、そんなMarkdownにreSTの表現力（＝``directive``と``role``を使った構造化）を追加し、図表や数式などの書式設定にも対応できるようになっています。

[MyST Tools](https://mystmd.org/)はSphinxにインスパイアされて開発されていたMySTのエコシステムです。
``.md``形式や``.ipynb``形式のファイルから、ウェブサイトと文書（LaTeXやPDF、Word形式）を生成できます。
ウェブサイトは``React``がベースとなっています。
PDF（やLaTeX）のテンプレートはさまざまなジャーナルに対応していて、デフォルトで400種類以上用意されています。
もちろん自作することもできます。
これらのことは[公式ドキュメント](https://mystmd.org/guide/background)に詳しく書かれています。

```{toctree}
---
maxdepth: 1
---
myst-install
myst-quickstart
myst-init
myst-toc
myst-templates
```

% myst-config
% myst-theme
% myst-css

## ビルドしたい（``myst build``）

```console
$ myst build --help
```

``--help``オプションでビルド形式を確認できます。
PDF（``--pdf``）やTeX（``--tex``）、Typst（``--typst``）、Word（``--word, --docx``）、HTML（``--html``）など、多くの形式に対応しています。

ビルドされたファイルは``_build``以下に作成されます。
``_build``は``.gitignore``に追記しておくとよいです。

```{toctree}
---
maxdepth: 1
---
myst-build-html
myst-build-pdf
myst-build-docx
myst-build-typst
```
