# LuaLaTeXしたい（``lualatex``）

```bash
$ lualatex ファイル名
$ latexmk -lualatex ファイル名
```

``LuaLaTeX``エンジンを使ってPDFを作成したい場合は、
``lualatex``コマンドもしくは``latexmk``コマンドに``-lualatex``オプションをつけて実行します。

## .latexmkrc

```unixconfig
$pdf_mode = 4;
```

`$pdf_mode = 4`でLuaLaTeXを指定できます。

## ドキュメントクラス

```latex
\documentclass{jlreq}
```

和文の場合 `jlreq`を使えばOKです。

```latex
\documentclass{ltjsarticle}
```

昔からある`jsarticle`に相当するものを使いたい場合は`ltjsarticle`があります。

```latex
\documentclass{article}
\usepackage{luatexja}
```

欧文のテンプレートの中で、日本語を使いたい場合は、`luatexja`パッケージを読み込みます。

:::{note}

国際会議によっては、プロシーディングスなどのテンプレートが用意されていますが、
その多くは欧文しか想定されていません。
そのような場合に、下書きを日本語で作成したい場合に有効です。

:::

## main.tex

:::{literalinclude} ../_static/latex/templates/lualatex-jlreq/main.tex
---
language: tex
---
:::
