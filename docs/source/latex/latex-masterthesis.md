# 修論を書きたい

自分の修士論文を振り返りながら、いまならどういう風にLaTeXを使うとよいか考えてみます。
これから修論を書く準備をする学生の参考になればよいなと思っています。

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

## LaTeX環境の準備

ローカルに環境を構築するならば、HomebrewでMacTeXをインストールすればよいでしょう。
また、オンラインのLaTeXサービスを使うのもありかもしれません。

## LaTeXエンジンの選択

修論は日本語で書く学生がほとんどだと思います。
その場合、LuaLaTeXを選択すればよいでしょう。
ローカル環境であれば[latexmkrc](./latex-latexmk.md)を作成し、目次や参照の生成失敗など、コンパイル時のミスを防ぐようにします。
また、長いコマンドを覚える必要がないため、執筆に集中できます。

## ドキュメントクラスの選択

LuaLaTeXを選択した場合、ドキュメントクラスは[jlreq](./latex-jlreq.md)を使えばよいと思います。
修論は比較的に長め（100ページくらい？）の文書なので
`report`スタイルがよいと思います。
製本する場合は`book`スタイルでもいいかもしれません。

## ページの設定

用紙サイズはA4（297mm x 210mm）に設定し、
フォントサイズ（`fontsize` / `jafontsize`）や
行あたりの文字数（`line_length`）はお好みで設定してください。

もし、大学や研究室で形式が決まっているならば
[geometry](./latex-usepackage-geometry.md)パッケージで
ページ設定するとよいかもしれません。

ヘッダーやフッターを表示したい場合は[fancyhdr](./latex-usepackage-fancyhdr.md)パッケージ、
表紙をカスタマイズしたい場合は[titlepage](./latex-titlepage.md)環境を使うとよいと思います。

## フォントの選択

TeX Liveの和文フォントは、源ノフォント（源ノ明朝、源ノ角ゴシック）をベースにした**原ノ味フォント**（原ノ味明朝、原ノ味角ゴシック）がデフォルトになっています。とくに変更する必要はないです。

フォントを変更したい場合は[luatexja-fontspec](./latex-luatexja-fontspec.md)パッケージを使います。

## 参考文献の管理

参考文献の管理は文献管理ソフトやオンラインのサービスを利用するとよいとです。
これは、日頃から使い慣れておく必要があります。

修論の文献リストを出力する場合は[biblatex](./latex-biblatex.md)パッケージを使います。
文献ファイルはBibTeX形式で保存します。

## パッケージの選択

```latex
\documentclass[report]{jlreq}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{enuitem}
\usepackage{physics}
\usepackage{siunitx}
\usepackage{hyperref}

\begin{document}


\end{document}
```

## ディレクトリ構造

```console
masterthesis
  |-- README.md
  |-- LICENSE.md
  |-- Makefile
  |-- .gitignore
  |-- src/
  |    |-- latexmkrc
  |    |-- main.tex
  |    |-- ch1/
  |    |    |-- ch1.tex
  |    |    |-- fig1.pdf
  |    |    |-- fig2.pdf
  |    |-- ch2/
  |    |    |-- ch2.tex
  |    |    |-- fig3.pdf
  |    |    |-- fig4.pdf
  |    |-- bib/
  |    |    |-- references.bib
  |-- build/
  |    |-- main.pdf
  |    |-- main.aux
  |    |-- main.log
  |-- shared/
  |    |-- 20241227_main.pdf
  |    |-- 20250106_main.pdf
```

チャプターごとにディレクトリを分割し、
それぞれにソースと画像をまとめておくとよいと思います。
また、出力ファイルはソースとは別のディレクトリに生成するとよいです。

指導教官（や共同研究者）に添削／校正をお願いしたファイルは、
別のディレクトリに、共有した日付ごとに保存しておくとよいです。

## バージョン管理

ソースはGitでバージョン管理します。
また、GitHubもしくはGitLabにリポジトリを作成し、ソース一式を保存しておきます。

GitHubもGitLabも無料プランでプライベートリポジトリを作成できます。
