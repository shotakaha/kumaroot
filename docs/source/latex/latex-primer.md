# A first set of LaTeX packages

[ZRさんのツイート](https://twitter.com/zr_tex8r/status/1557559175453872128)が流れてきたので、そこにリンクされていた[A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)を斜め読みしてみました。

## Abstract

- 初心者がやりたいと考えていることのほとんどをカバーするパッケージの厳選リスト
- それぞれの領域において有能で信頼できるパッケージの名前を挙げようとしています

## Overview

- TUG2019で報告した内容
- SNSを使って初心者が必要としているパッケージを調査
- 初心者が欲しいのは網羅的なリストではないと考え、2ページに収まるようにまとめた
- 標準的なディストリビューションに入っているパッケージから選択している

## Every document

1. **geometry** : ページのサイズや余白、向きなどの設定
1. **amsmath** / **amssymb** / **amsthm** / **mathtools** : 数式を多用する場合に必要
1. **microtype** : 組版を微修正して見た目が（見分けがつかないレベル）よくなる

## Inside a document

1. **enumitem** : リストをカスタマイズ
2. **caption** : キャプションをカスタマイズ
3. **float** : float環境をカスタマイズ
4. **hyperref** : 参照をハイパーリンクにする
5. **cleveref** : 相互参照をスマートにする（hyperrefの後に読み込む）
6. **listings** / **minted** : コードブロックをきれいに表示
7. **pythontex** / **sagetex** : スクリプトの実行結果を表示
8. **array** : テーブルをカスタマイズ
9. **siunitx** : 単位
10. **mdframed** : 色付き／枠付きのボックス
11. **lipsum** : サンプル文で埋めたいとき

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
