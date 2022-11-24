# ドキュメントクラスを設定したい（``\documentclass``）

```latex
% LuaLaTeX + jlreq
\documentclass{jlreq}

% LuaLaTeX + ltjsarticle
\documentclass{ltjsarticle}

% upLaTeX + jsarticle
\documentclass[uplatex, dvipdfmx]{jsarticle}
```

日本語のドキュメントクラスには、``jlreq``と``jsclasses``系があります。

``jlreq``は、W3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」の実装を試みたクラスファイルです。
LuaLaTeX、(u)pLaTeXに対応していて、これから新しく文書を作成する場合は、迷わず使うとよいと思います。

``jsclasses``系は、おなじみのクラスファイルです。
(u)pLaTeX用に``jsarticle``クラスがあり、
LuaTeX用には``jsarticle``クラスと互換性の高い``ltjsarticle``クラスがあります。

## 基本的な組み合わせ

日本語でLaTeXする場合のエンジンとドキュメントクラスの組み合わせは、冒頭の3通りから選ぶとよいと思います。
参考までに、それぞれの使い分け方について僕の感想を下記に添えてみました。
用途にあった組み合わせを選んでください。

### LuaLaTeX + jlreq

```latex
\documentclass{jlreq}
```

新しくLaTeXに入門する場合は、この組み合わせから始めるとよいと思います。
また、これから新規に作成する文書もこれ一択でいいと思います。

### LuaLaTeX + ltjsarticle

```latex
\documentclass{ltjsarticle}
```

LaTeX経験者で、これまでの知識を活かしながらLuaLaTeXを使い方は、この組み合わせがよいと思います。
過去のファイルを書き換えることはオススメしません。

### upLaTeX + jsarticle

```latex
\documentclass[uplatex, dvipdfmx]{jsarticle}
```

これまでに作成したLaTeX文書を再コンパイルする際に必要な組み合わせです。
また、ウェブの情報を読むときに知っておくとよい情報です。
オプションにエンジン（``uplatex``）とドライバー（``dvipdfmx``）は必須です。
日本語の設定に[fontenc](./latex-fontenc.md)や[otf](./latex-otf.md)なeど追加必須のパッケーではオリジナルのドキュメントクラスが用意されていることもあります。

## 文書スタイルを設定したい

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
```

ドキュメントクラスには``article``や``report``などのような文書スタイルを指定するオプションがあります。
 デフォルトは``article``になっています。

### article

トップレベルが節（``\section``）の文書ができます。
**片面印刷を想定**して、左右ページのデザインは同じです。
学生実験のレポートなど短めの文章作成に向いています。

### report

トップレベルが章（``\chapter``）の文書ができます。
**片面印刷を想定**して、左右ページのデザインは同じです。
修士論文など長めの文章作成に向いています。

### book

 トップレベルが章（``\chapter``）の文書ができます。
**両面印刷を想定**して、左右ページのデザインが異なっています。
僕は使ったことがありませんが、書籍の作成に向いているようです。

## その他の設定

ドキュメントクラスのオプションで設定できることを整理しておきます。

```{toctree}
---
maxdepth: 1
---
latex-documentclass-paper
latex-documentclass-fontsize
latex-documentclass-twocolumn
latex-documentclass-landscape
latex-jsclasses
latex-jlreq
```
