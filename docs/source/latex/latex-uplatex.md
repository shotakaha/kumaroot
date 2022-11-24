# (u)pLaTeXを使いたい

``(u)pLaTeX``を使う場合は、ドキュメントクラスに``jlreq``を使います。
昔からある``jsarticle``系や``ltjsarticle``系も使えます。

```latex
\documentclass{jlreq}
\documentclass[dvipdfmx]{jsarticle}    % pLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}     % upLaTeX
```

## PDFを作成したい

```bash
$ ptex2pdf -l main.tex    % pLaTeX
$ ptex2pdf -u -l main.tex    % upLaTeX
```

upLaTeXを使う場合は``-u -l``オプションを使います。

## ヘルプを確認したい

```bash
$ ptex2pdf -h
```

## バージョンを確認したい

```bash
ptex2pdf -v
This is ptex2pdf[.lua] version 20200520.0.
```
