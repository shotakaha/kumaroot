# ハイパーリンクしたい（``hyperref``）

```latex
\usepackage{hyperref}
\usepackage{pxjahyper}  % (u)pLaTeXの場合、これも追加推奨
```

文書にハイパーリンクを作成するためのパッケージです。
ドキュメントを読むと、パッケージを読み込む順番は一番最後にしたほうがよいようです。

``hyperref``パッケージは、日本語のドキュメントクラスを使った場合に、文章がページからはみ出したり、目次のしおりが文字化けしたりするので、``PXjahyper``パッケージも一緒に読み込んでおきます。

## hyperrefを設定したい

```latex
% パッケージオプション
\usepackage[オプション]{hyperref}
```

```latex
% hypersetupで追加
\usepackage{hyperref}
\hypersetup{オプション}
```

``hyperref``を設定する方法は3種類あります。
（1）パッケージオプションに書く方法、
（2）``\hypersetup``コマンドを使う方法、そして
（3）``hyperref.cfg``に書く方法です。

僕は、設定が読みやすいのと、ソース管理していると変更が分かりやすいので（2）の方法を好んで使っています。

## リンクに色をつけたい

```latex
\hypersetup{colorlinks=true}
\hypersetup{allcolors=blue}    % Set all color options
\hypersetup{hidelinks=false}   % Hide links (removing color and border)
```

デフォルトだとリンクは枠（``pdfborder``）で囲まれています。
リンクの種類によって色も異なっています。
``allcolors``を使ってすべて青色にしています。

## PDFのしおり（ブックマーク）を作成したい

```latex
\hypersetup{bookmarks=true}  % デフォルト
\hypersetup{bookmarksnumbered=true}    %  しおりのタイトルに章番号を表示する
```

PDFのしおり（ブックマーク）は自動で生成されるようになっています。
長い文書の場合は、章番号も表示するとよいです。

## ページサイズ対策

```latex
\hypersetup{setpagesize=false}
```

## しおりの文字化け対策

```latex
\usepackage{atbegshi}
\AtBeginShipoutFirst{\special{pdf:tounicode EUC-UCS2}}
\AtBeginShipoutFirst{\special{pdf:tounicode 90ms-RKSJ-UCS2}}
```

何をしているのかまったく理解していないが、とりあえず両方書いておけばよいです。
それでうまくいかない場合は片方する試してみてください。
