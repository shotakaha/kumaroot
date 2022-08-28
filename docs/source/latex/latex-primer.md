# 初心者にオススメのパッケージ？

この前、[ZRさんのツイート](https://twitter.com/zr_tex8r/status/1557559175453872128)が流れてきたので、
そこにリンクされていた
[A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)を斜め読みしてみました。

## Overview

- SNSを使って初心者が必要としているパッケージを調査した
- TUG2019で報告した

## Every document

- ページのサイズや余白、向きなどの設定は[geometry](https://ctan.org/pkg/geometry)
- 数式をたくさん使う場合は**amsmath**と**amssymb**。定理環境を使う場合は**amsthm**も追加する。**amssymb**は**amsfonts**を読みこでくれる。**amsmath**のあとに**amsthm**を読み込む必要がある。**mathtools**を読み込んでもよい。
- **microtype**パッケージで、見た目がちょっとよくなる。ほとんど見分けがつかないらしい。

## Inside a document

- リストをいじるために**enumitem**
- キャプションには**caption**
- ハイパーリンクには**hyperref**。相互参照をスマートにするには**cleveref**を追加する。
- コードブロックには**listings** もしくは **minted**
- スクリプトの実行結果を表示したい場合は、**pythontex**（Python）や**sagetex**（Sage）がある。他にもR、Haskell、Schemeに同様のパッケージがある。
- テーブルレイアウトは**array**
- 単位は**siunitx**
- 色付きのボックス**mdframed**
- テキストの自動生成は**lipsum**

## Graphics and color


- **graphicx**
- PDF文書の一部を挿入するのは**pdfpages**
- 動画は**media9**
- 色を増やすには**xcolor**
- プロットを描く**Asymptote** or **TikZ**

## Front and back matter, headers, footers

- 章タイトル、節タイトルをスタイル **titlesec**
- ヘッダーとフッター **fancyhdr**
- 目次、図目次、表目次を調整 **tocloft**
- **answers**
- **footmisc**
- 索引 **makeindex**

## Special documents

- テストの作成 **exam**
- [履歴書](https://ctan.org/topic/cv)
- スライド作成 **beamer**

## Fonts and engines

- デフォルトは Computer Modern fonts
- LaTeX Font Catalogue
- **fontspec**



.. toctree::
   :maxdepth: 1

   latex-packages-graphic
   latex-packages-hyperlink
