# (u)pLaTeXしたい

```bash
$ ptex2pdf -l -u ファイル名  # upLaTeX
$ ptex2pdf -l ファイル名     # pLaTeX
```

``(u)pLaTeX``を使ってPDFを作成する場合は``ptex2pdf``コマンドを使います。
``upLaTeX``のタイプセットは``-l -u``オプション、
``pLaTeX``のタイプセットは``-l``オプションをつけて実行します。


## ドキュメントクラス

```latex
\documentclass{jlreq}
\documentclass[dvipdfmx]{jsarticle}    % pLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}     % upLaTeX
```

``(u)pLaTeX``を使う場合も、ドキュメントクラスに``jlreq``が使えます。
昔からある``jsarticle``系も使えます。
