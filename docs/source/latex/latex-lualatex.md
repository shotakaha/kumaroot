# LuaLaTeXしたい（`lualatex`）

```console
$ lualatex --version
This is LuaHBTeX, Version 1.18.0 (TeX Live 2024)
Development id: 7611

$ lualatex ファイル名.tex
```

`lualatex`コマンドで、`LuaTeX`エンジン（現在は、その後継の`LuaHBTeX`）を
使ってPDFファイルを生成できます。

```console
$ latexmk -lualatex ファイル名.tex
```

`latexmk`コマンドの場合は、`-lualatex`オプションをつけて実行します。

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
