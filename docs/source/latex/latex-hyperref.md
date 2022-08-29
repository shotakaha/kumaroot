# hyperref

```latex
\usepackage{hyperref}
\usepackage{pxjahyper}
```

文書にハイパーリンクを作成するためのパッケージです。
ドキュメントを読むと、パッケージを読み込む順番は一番最後にしたほうがよいようです。

``hyperref``パッケージは、日本語のドキュメントクラスを使った場合に、
文章がページからはみ出したり、目次のしおりが文字化けしたりするので、
``PXjahyper``パッケージも一緒に読み込んでおきます。

## hyperrefを設定したい

```latex
\usepackage[オプション]{hyperref}
```

```latex
\usepackage{hyperref}
\hypersetup{オプション}
```

``hyperref``を設定する方法は3種類あります。
1つ目は通常のパッケージのようにパッケージオプションに書く方法、
2つ目は``\hypersetup``コマンドを使う方法、そして
3つ目は``hyperref.cfg``に書く方法です。

## リンクに色をつけたい

```latex
\hypersetup{colorlinks=true}
\hypersetup{linkcolor=red}      % 内部リンクの色
\hypersetup{citecolor=green}    % Color for bibliographical citations
\hypersetup{filecolor=cyan}     % Color for URLs which open local files
\hypersetup{menucolor=red}      % Color for Acrobat menu items
\hypersetup{urlcolor=magenta}   % Color for linked URLs
\hypersetup{allcolors=magenta}  % Set all color options
\hypersetup{hidelinks=false}    % Hide links (removing color and border)
```

デフォルトだとリンクは枠（``pdfborder``）で囲まれています。

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
