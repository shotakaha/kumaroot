# hyperref

```latex
\usepackage{hyperref}
\usepackage{pxjahyper}
```

文書内にハイパーリンクを作成するためのパッケージです。

``hyperref``パッケージは、日本語のドキュメントクラスを使った場合に、
文章がページからはみ出したり、目次のしおりが文字化けしたりするので、
``PXjahyper``パッケージも一緒に読み込んでおきます。

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
