# 修論したい

自分の修士論文を執筆した経験を思い出しながら、
いまならどういう風に準備するかまとめてみます。
これから修論を書く準備をする学生の参考になればよいなと思っています。

## 日々準備する

当たり前ですが、修士論文は一朝一夕で完成するものではありません。
日々の研究活動やグループの定例ミーティングでの報告などの積み重ねが大切です。
ミーティングではスライド形式で報告することが多いかもしれませんが、
定期的に文章化しておくとよいと思います。

この段階では、LaTeXを触る必要はなく、WordやGoogleドキュメントなど、
日頃から使い慣れているツールを使うとよいと思います。

:::{note}

週に1回の定例ミーティングで作ったスライドのおかげで、
修論に使う図やグラフの準備には（あまり）困りませんでした。
ただし、議論した経緯を忘れているところもあり、
文章化するのが大変なところもありました。
いま思い返すと、学会発表のあとなどに、文章に整理するよい機会だったのではと思います。

:::

## LaTeX環境を準備する

macOSやLinuxを使っているならば、HomebrewでMacTeXをインストールして、ローカル環境を構築できます。
最近では、OverleafやCloudLaTeXのようなオンラインサービスを使うのもありかもしれません。

ただし、無料プランだと容量の制限や、コンパイル時間の制限などがあります。
また、サービスがメンテに入ったり、ダウンすると使えなくなります。
個人的にはローカルに環境を構築することをオススメします。

:::{seealso}

- [](./latex-install.md)
- [](./latex-online.md)

:::

## ディレクトリを準備する

```console
masterthesis
  |-- README.md
  |-- LICENSE.md
  |-- Makefile
  |-- .gitignore
  |
  |-- latexmkrc (or .latexmkrc)
  |-- main.tex
  |
  |-- preamble/
  |    |-- pages.tex
  |    |-- figure.tex
  |    |-- math.tex
  |    |-- physics.tex
  |    |-- hyperref.tex
  |
  |-- src/
  |    |-- main.tex
  |    |-- ch1/
  |    |    |-- ch1.tex
  |    |    |-- fig1.pdf
  |    |    |-- fig2.pdf
  |    |-- ch2/
  |    |    |-- ch2.tex
  |    |    |-- fig3.pdf
  |    |    |-- fig4.pdf
  |
  |-- references/
  |    |-- biblatex_format.bib
  |
  |-- _aux/
  |    |-- main.aux
  |    |-- main.log
  |
  |-- _build/
  |    |-- main.pdf
  |
  |-- _shared/
  |    |-- 20241227_v01_main.pdf
  |    |-- 20250106_v02_main.pdf
```

ページ数が多くなるため、章ごとにディレクトリ／ファイルを分割して管理するとよいと思います。
ここでは章ごとにディレクトリを分割し、
それぞれにソースと画像をまとめてるようにしています。
また、出力ファイルはソースとは別のディレクトリに生成するとよいです。

それぞれのファイルの役割や以下の通りです。

| パス | 内容 | Git管理 |
|---|---|---|
| `latexmkrc` | ビルドの設定 | True |
| `Makefile` | タイプセットの手順書 | True |
| `main.tex` | ビルド対象のファイル | True |
| `preamble` | プリアンブル設定の保存先 | True |
| `src` | 本文ファイルの保存先 | True |
| `references` | 文献ファイルの保存先 | True |
| `_aux` | `aux`ファイルの出力先 | `.gitignore`に追加 |
| `_build` | ビルドしたPDFの出力先 | `.gitignore`に追加 |
| `_shared` | 関係者に回覧した原稿データ | `.gitignore`に追加 |

関係者（指導教員や共同研究者）に添削／校正をお願いしたファイルは、
あとで確認できるように、別のディレクトリにコピーを保存しておくとよいです。
ファイル名は共有した日付（とバージョン）を含めるとよいです。

:::{tip}

日付は西暦を含めた`yyyymmdd`形式が認識しやすいです。
バージョン番号は、日ごとではなく、全体の通し番号にしておくと、
最新版がわかりやすくなります。

「最新版（latest）」や「最終版（final）」などは、
切羽詰まったときほど混乱の元になるので、
絶対に使わないようにしましょう。

:::

## Gitで管理する

修論の執筆者は原則ひとりですが、ソースはGitでバージョン管理するとよいです。
また、GitHubもGitLabも、無料プランでプライベートリポジトリを作成できるため、
修論用のリポジトリを作成しておくとよいです。
CI/CD機能を活用すれば、最新版のビルドを自動化することもできます。

これらのリポジトリは、修論データのバックアップ先にもなります。
〆切間際にパソコンの調子が悪くなったという話は（なぜか）よく聞きます。
バックアップ先を分散させることで、万が一の場合のリスクを減らすことができます。

## エンジンを選択する

`LuaLaTeX`を選択しておけば間違いないです。
エンジンに合わせて`latexmk`を設定します。

目次や参照の生成失敗など、コンパイル時のミスを防ぐことができます。
また、長いコマンドを覚える必要がないため、執筆に集中できます。

```unixconfig
@default_file = ("main.tex");
$pdf_mode = 4;
$out_dir = "_build";
$aux_dir = "_aux";
```

:::{seealso}

- [](./latex-latexmk.md)
- [](./latex-latexmkrc.md)

:::

## ドキュメントクラスを選択する

`LuaLaTeX`の場合、`ltjsclasses`と`jlreq`の選択肢があります。
とくにこだわりがなければ`jlreq`で問題ありません。
比較的に長め（100ページくらい？）の文書になるので、
スタイルは`report`形式がよいと思います。

:::{seealso}

- [](./latex-jlreq.md)
- [](./latex-jsclasses.md)

:::

## メインファイルを作成する

```latex
\documentclass[report]{jlreq}

% 和文の設定
\usepackage{luatexja}
\usepackage{luatexja-fontspec}

% 表紙の情報を入力
\title{修士論文}
\author{僕}

\begin{document}

% 表紙を出力
\maketitle

% 目次を出力
\tableofcontents

% アウトラインに沿って章タイトルを入力
\chapter{章のタイトル}
\chapter{章のタイトル}
\chapter{章のタイトル}

\end{document}
```

エンジンとドキュメントクラスに合わせて、メインファイルを作成します。
`LuaLaTeX`と`jlreq`の場合、まずこの内容で`main.tex`を作成します。

```console
$ latexmk main.tex
```

そして、タイプセットできるか確認します。

## メインファイルを増築する

タイプセットできることが確認できたら、
ディレクトリ構造にしたがって、メインファイルを増築します。

```latex
\documentclass[report]{jlreq}

% 和文の設定
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{luatexja-ruby}

% 参考文献の設定
\usepackage{biblatex}
\addbibresources{references/biblatex_format.bib}

% パッケージ設定
\input{preamble/pages.tex}
\input{preamble/figure.tex}
\input{preamble/math.tex}
\input{preamble/physics.tex}
\input{preamble/hyperref.tex}

% 自作マクロの設定
\input{preamble/macros.tex}

% ビルドするページの設定
\includeonly{
    src/title/title,
    %src/abstract/abstract,
    src/ch1/ch1,
    % ...
    %src/chN/chN,
    %src/thanks/thanks,
    %src/refs/refs,
}

\begin{document}

% 表紙
% titlepage環境で表紙を作成する
\include{src/title/title}

% 概要
% abstract環境で概要を作成する
\include{src/abstract/abstract}

% 目次を出力
\tableofcontents
\listoffigures
\listoftables

% 本文
\include{src/ch1/ch1}
\include{src/ch2/ch2}
% ...
\include{src/chN/chN}

% 謝辞
\include{src/thanks/thanks}

% 参考文献
\printbibliograpy[title={参考文献}]

\end{document}
```

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

## 表紙（`src/title/title.tex`）

```latex
\begin{titlepage}

\begingroup
修士論文
\endgroup

\begingroup
\Large
論文のタイトル\\
長い場合は改行して整える
\endgroup

\begingroup
\includegraphics[0.3\textwidth]{ロゴ.pdf}
\endgroup

\begingroup
著者名
\endgroup

\begingroup
所属
\endgroup

\begingroup
提出日
\endgroup

\end{titlepage}
```

修士論文の表紙は、記載する内容も多く`\maketitle`では力不足です。
`titlepage`環境を使って、イチから並べるのがよいと思います。
タイトルを見栄えのよいサイズに変更したり、
大学のロゴを挿入したり、自由にカスタマイズできます。

## 参考文献の管理

参考文献の管理は文献管理ソフトやオンラインのサービスを利用するとよいとです。
これは、日頃から使い慣れておく必要があります。

修論の文献リストを出力する場合は[biblatex](./latex-biblatex.md)パッケージを使います。
文献ファイルはBibTeX形式で保存します。

## パッケージの選択

```latex
\documentclass[report]{jlreq}

\usepackage{geometry}  % ページ設定
\usepackage{fancyhdr}  % ヘッダー／フッターの装飾
\usepackage{graphicx}  % 画像
\usepackage{xcolor}  % 色
\usepackage{enuitem}  % 箇条書き
\usepackage{biblatex}  % 参考文献
\usepackage{physics}  % 物理記号
\usepackage{siunitx}  % 物理量・単位
\usepackage{tikz-feynman}  % ファインマン図
\usepackage{hyperref}  % ハイパーリンク

\begin{document}

% 表紙の作成

% 概要

% 本文

\include{ch1/ch1.tex}
\include{ch2/ch2.tex}
\include{ch2/ch2.tex}

% 補遺

% 参考文献

\end{document}
```
