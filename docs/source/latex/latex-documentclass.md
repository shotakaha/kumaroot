# ドキュメントクラスしたい（``\documentclass``）

```latex
% LuaLaTeX + jlreq
\documentclass{jlreq}
```

```{toctree}
latex-jlreq
latex-documentclass-paper
latex-documentclass-fontsize
latex-documentclass-twocolumn
latex-documentclass-landscape
latex-documentclass-hanging
latex-documentclass-tate
latex-jsclasses
```


```latex
% LuaLaTeX + ltjsarticle
\documentclass{ltjsarticle}

% upLaTeX + jsarticle
\documentclass[uplatex, dvipdfmx]{jsarticle}
```

日本語でLaTeXする場合、ドキュメントクラスに``jlreq``もしくは``jsclasses``系を使います。

``jlreq``は、W3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」の実装を試みたクラスファイルです。
``LuaLaTeX``と``(u)pLaTeX``のどちらにも対応しています。
これから新しく文書を作成する場合は、迷わずこちらを使うとよいと思います。

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
また、ウェブ検索した結果に多数ヒットするので、知っておくとよい情報です。
オプションにエンジン（``uplatex``）とドライバー（``dvipdfmx``）は必須です。
日本語の設定に[fontenc](./latex-fontenc.md)や[otf](./latex-otf.md)など追加必須のパッケージではオリジナルのドキュメントクラスが用意されていることもあります。
