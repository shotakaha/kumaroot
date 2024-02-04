```{eval-rst}
.. index::
    pair: た|使い方; Typst
```

# Typstの使い方

[Typst](https://typst.app/)は[2023年3月にベータ版が公開](https://typst.app/blog/2023/beta-oss-launch)されたばかりの新しい組版システムです。

科学分野の組版システムといえばLaTeXですが、使いこなすのはなかなか大変です。
Typstは、LaTeXのような科学技術文書作成を念頭に、より使いやすいシステムを目指しています。

:::{note}

まだまだパブリックベータ版なので、いろいろと仕様が変わる可能性はあります。
このページも常に最新状況を追っているものとは限らないので、公式ドキュメントも覗いてみてください。

:::

文章のマークアップは完全独自の言語体系が使われています。
LaTeXよりMarkdownに近い記法になっているのですが、
Markdownより構造化した文章が書けるようになっています。
また、[pandoc](../command/command-pandoc.md)で変換できるので、既存の文書も比較的簡単に転用できます。

LaTeXと比べて**一番の長所**だと感じたのは、プリアンブルの設定不要でタイプセットできる点です。
ドキュメントクラスやエンジン、ドライバー、入力ファイルのエンコーディング、フォントマップの設定をしなくても、
内容が書かれたテキストファイルさえあれば、和文PDFが生成できます。

また、ページ設定や図・数式の挿入、ハイパーリンクの書式などが標準装備となっていて、外部パッケージを使う必要がありません。
公式リファレンスには[LaTeX経験者向けのユーザーガイド](https://typst.app/docs/guides/guide-for-latex-users/)があり、
ここにLaTeXパッケージとの対応が書かれています。
これをきちんと読めば、やりたいことはすぐに表現できると思います。

また、タイプセットそのものが爆速なのですが、差分コンパイルに対応しているため、ライブプレビューも快適です。
まだ、日本語の情報が少なく、うまくいかないときに難儀するかもしれません。
修論の執筆に使うにはちょっと勇気が必要ですが、長めのレポート作成に使ってみるのはアリだと思います。

```{toctree}
---
maxdepth: 1
---
typst-install
typst-build
typst-import
typst-text
typst-page
typst-par
typst-heading
typst-outline
typst-list
typst-strong
typst-link
typst-document
typst-lorem
typst-styling
```

## 物理したい

```{toctree}
---
maxdepth: 1
---
typst-physica
typst-metro
```

