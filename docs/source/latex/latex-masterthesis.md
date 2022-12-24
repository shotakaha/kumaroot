# 修論を書きたい

自分の書いた修士論文を振り返りながら、どういうLaTeX文書にしたらいいかを考えてみます。
これから修論を書く準備をする際の参考になればよいなと思っています。

```latex
\documentclass[report, paper=a4paper, fontsize=11pt, jafontsize=11pt, line_length=40zw, ]{jlreq}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{wrapfig}
\usepackage{subfigure}
\usepackage{wallpaper}
\usepackage{ulem}
\usepackage{float}
\usepackage{lineno}
\usepackage{physics}
\usepackage{hyperref}

\begin{document}

\maketitle

\begin{abstract}
\end{abstract}

\tableofcontents
\listoffigures
\listoftables



\end{document}
```

## コンパイルの設定

LuaLaTeXを使ってコンパイルします。
[latexmkrc](./latex-latexmk.md)を設定することで、目次や参照の失敗など、コンパイル時のミスを防ぐことができます。
また、長いコマンドを覚える必要がないため、執筆に集中できます。

## ドキュメントクラスの設定

ドキュメントクラスは[jlreq](./latex-jlreq.md)を使います。
修論は比較的長め（100ページくらい？）文書になるので、``report``スタイルがよいと思います。製本する場合は``book``スタイルのほうがいいかもしれません。
フォントサイズ（``fontsize`` / ``jafontsize``）や行あたりの文字数（``line_length``）はお好みで設定してください。

## パッケージの読み込み

読み込んでおくとよさそうなパッケージは別途整理します。
