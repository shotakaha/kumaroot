# (u)pLaTeXしたい（``ptex2pdf``）

```console
$ ptex2pdf -v
This is ptex2pdf[.lua] version 20200520.0.

$ ptex2pdf -l ファイル名     # pLaTeX
$ ptex2pdf -l -u ファイル名  # upLaTeX
```

`ptex2pdf`で、`(u)pLateX`を使ってPDFを出力できます。
`upLaTeX`エンジンの場合は、`-l -u`オプション、
`pLaTeX`エンジンの場合は、`-l`オプションをつけて実行します。

## .latexmkrc

```unixconfig
# platex
$latex = "ptex2pdf -l %O"

# uplatex
$latex = "ptex2pdf -l -u %O"
```

## ドキュメントクラス

```latex
% pLaTeX
\documentclass[dvipdfmx]{jsarticle}
```

`pLateX`の場合、ドキュメントクラスは`jsarticle`を使います。
ドライバーは`dvipdfmx`を指定します。

```latex
% upLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}     % upLaTeX
```

`upLaTeX`を使う場合、ドキュメントクラスのオプションに`uplatex`が必要です。

```latex
% (u)pLaTeX
\documentclass{jlreq}
```

`jlreq`クラスは、`(u)pLaTeX`にも対応しています。

## 併用パッケージ

`(u)pLaTeX`はいわゆる「レガシーLaTeX」です。
フォント周りの設定や、パッケージ互換性の自動検出など、一緒に利用することが推奨されているパッケージが多々あります。

```{toctree}
---
maxdepth: 1
---
latex-plautopatch
latex-inputenc
latex-fontenc
```
