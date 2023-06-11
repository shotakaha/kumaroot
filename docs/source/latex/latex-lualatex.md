# LuaLaTeXしたい（``lualatex``）

```bash
$ lualatex ファイル名
$ latexmk -lualatex ファイル名
```

``LuaLaTeX``エンジンを使ってPDFを作成したい場合は、
``lualatex``コマンドもしくは``latexmk``コマンドに``-lualatex``オプションをつけて実行します。

## ドキュメントクラス

```latex
\documentclass{jlreq}
\documentclass{ltjsarticle}
```

``LuaLaTeX``を使う場合は、ドキュメントクラスに``jlreq``を使います。
昔からある``jsarticle``に相当するものを使いたい場合は``ltjsarticle``が使えます。

## latexmkrc

:::{literalinclude} ../_static/latex/templates/lualatex-jlreq/latexmkrc
---
language: text
---
:::

## main.tex

:::{literalinclude} ../_static/latex/templates/lualatex-jlreq/main.tex
---
language: tex
---
:::
