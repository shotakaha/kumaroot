# ドキュメントクラスしたい（`\documentclass`）

```latex
\documentclass[オプション]{クラス名}
```

**ドキュメントクラス** は文書全体の構成やスタイルを決めるテンプレート的なものです。
LaTeXの文書作成は、まず、このドキュメントクラス選びからはじまります。
目的や使用する言語に応じて、適切なクラスを選択してください。
また、学会や雑誌によっては専用のクラスを用意している場合もあります。

## 欧文クラスしたい

```latex
% classes
\documentclass[オプション]{article}
\documentclass[オプション]{report}
\documentclass[オプション]{book}
```

欧文の場合は、標準クラス（`article`、`report`、`book`）でOKです。
日報のような短い文書の場合は`article`、
修士論文や博士論文などのように、ある程度の構成がある文書は`report`、
それらを製本したい場合は`book`が適しています。

```{toctree}
latex-classes
```

## 和文クラスしたい

和文の場合は、歴史的な経緯からいくつかの選択肢があります。
ただし、新しく書きはじめる場合は`jlreq`クラスを利用すればOKです。

```latex
% jlreq
\documentclass{jlreq}
```

LuaTeX-jaコミュニティが開発している和文用のドキュメントクラスです。
W3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」の実装を試しているクラスファイルで
`LuaLaTeX`と`(u)pLaTeX`のどちらにも対応しています。

美文書LaTeXも第9版からこのクラスに移行したそうなので、
これからの日本語標準クラスになると思います。
これから新しく文書を作成する場合は、迷わずこちらを使うとよいと思います。

```{toctree}
latex-jlreq
latex-documentclass-paper
latex-documentclass-fontsize
latex-documentclass-twocolumn
latex-documentclass-landscape
latex-documentclass-hanging
latex-documentclass-tate
```

```latex
% ltjsclasses
\documentclass[オプション]{ltjsarticle}
\documentclass[オプション]{ltjsreport}
\documentclass[オプション]{ltjsbook}
```

こちらもLuaTeX-jaコミュニティが開発している和文用のドキュメントクラスです。
後述する`jsclasses`クラスに慣れている場合は、このクラスが使いやすいと思います。
ただし、過去のファイルを書き換えることはオススメしません。

```latex
% jsclasses
\documentclass[uplatex, dvipdfmx]{jsarticle}
\documentclass[uplatex, dvipdfmx]{jsreport}
\documentclass[uplatex, dvipdfmx]{jsbook}
```

三重大の奥村さんが作成し、現在は日本語TeX開発コミュニティで管理されているドキュメントクラスです。
(u)pLaTeXを利用するときにお世話になることが多いと思います。
僕も修論を作成したときは、このクラスを利用しました。

また、ウェブ検索した結果に多数ヒットするので、知っておくとよい情報です。
オプションにエンジン（`uplatex`）とドライバー（`dvipdfmx`）は必須です。
また、他に追加したほうがよいパッケージもいくつかあります。


:::{note}

``(u)pLaTeX + jsclasses系``のサンプルも、わかる範囲で載せておきます。

:::

```{toctree}
---
maxdepth: 1
---
latex-jsclasses
```
