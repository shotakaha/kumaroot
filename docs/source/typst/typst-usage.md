```{eval-rst}
.. index::
    pair: Typst; usage
```

# Typstの使い方

[Typst](https://typst.app/)は[2023年3月にベータ版が公開](https://typst.app/blog/2023/beta-oss-launch)されたばかりの新しい組版システムです。

科学分野の組版システムといえばLaTeXが定番ですが、使いこなすのはなかなか大変です。
Typstは、LaTeXのような科学技術文書作成を念頭に、より使いやすいシステムを目指したものです。

文章のマークアップには完全独自の言語体系が使われています。
LaTeXよりMarkdownに近い記法になっているのですが、
Markdownより構造化した文章が書けるようになっています。
また、[pandoc](../command/command-pandoc.md)で変換できるので、既存の文書も比較的簡単に転用できそうです。

:::{note}

まだまだパブリックベータ版なので、いろいろと仕様が変わる可能性はあります。
このページも常に最新状況を追っているものとは限らないので、公式ドキュメントも覗いてみてください。

:::

```{toctree}
---
maxdepth: 1
---
typst-install
typst-build
typst-import
```

## 全体設定したい

```{toctree}
---
maxdepth: 1
---
typst-page
typst-par
typst-text
typst-document
```

## テキストしたい

```{toctree}
---
maxdepth: 1
---
typst-outline
typst-heading
typst-raw
typst-list
typst-strong
typst-lorem
typst-link
typst-math
```

## カスタマイズしたい

```{toctree}
---
maxdepth: 1
---
typst-styling
typst-set
typst-show
typst-let
typst-title
typst-logo
typst-state
typst-block
typst-box
```

## パッケージしたい

[Typst Universe](https://typst.app/universe)をさまよって、便利そうなパッケージだなと思ったものをリストしています。

```{toctree}
---
maxdepth: 1
---
typst-gentle-clues
```

## 物理したい

パッケージの中で、物理学のレポートで使うと便利そうなものをリストしています。

```{toctree}
---
maxdepth: 1
---
typst-physica
typst-metro
typst-unify
```

## TypstとLaTeXのちがい

Typstの**一番の長所**だと感じたのは、LaTeXのプリアンブルような設定が不要でタイプセットできる点です。
ドキュメントクラスやエンジン、ドライバー、入力ファイルのエンコーディング、フォントマップの設定をしなくても、
和文ドキュメントからPDFが生成できます。

タイプセットそのものも爆速です。
差分コンパイルに対応しているため、ライブプレビューしながらの編集作業がとてもとても快適です。

また、ページ設定や図・数式の挿入、ハイパーリンクの書式なども標準装備となっていて、外部パッケージを必要としません。
公式ドキュメントには[LaTeX経験者向けのユーザーガイド](https://typst.app/docs/guides/guide-for-latex-users/)が
用意されており、LaTeXパッケージとTypstコマンドの対応が書かれています。
ここを参照すれば、やりたいことはすぐに表現できると思います。

**短所**は、まだ、日本語の情報が少なく、うまくいかないときに難儀するかもしれない点です。
修論の執筆に使うにはちょっと勇気が必要ですが、長めのレポート作成に使ってみるのはアリだと思います。
