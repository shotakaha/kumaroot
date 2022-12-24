# ハイパーリンクしたい（``hyperref``）

```latex
\usepackage{hyperref}
\usepackage{pxjahyper}  % (u)pLaTeXの場合、これも追加推奨
```

文書にハイパーリンクを作成するためのパッケージです。
パッケージを読み込む順番は一番最後にしたほうがよいようです。

日本語のドキュメントクラスで``hyperref``を使った場合、文章がページからはみ出したり、目次のしおりが文字化けしたりするため、``pxjahyper``パッケージも一緒に読み込んでおくとよいです。

## オプションを設定したい

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

1. パッケージオプションを使う方法
1. ``\hypersetup``コマンドを使う方法
1. ``hyperref.cfg``を使う方法

僕は、設定が読みやすいのと、ソース管理していると変更が分かりやすいので``\hypersetup``コマンドを使う方法を好んで使っています。

## リンクに色をつけたい

```latex
\hypersetup{colorlinks=true}   % リンクの文字に色を追加する
\hypersetup{allcolors=blue}    % すべてのリンクの色を設定する
% \hypersetup{linkcolor=red}     % 内部リンクの色設定
% \hypersetup{citecolor=green}   % 参照文献のリンクの色設定
% \hypersetup{filecolor=cyan}    % 参照文献のリンクの色設定
% \hypersetup{urlcolor=magenta}  % URLのリンクの色設定
\hypersetup{hidelinks=false}   % リンクに色をつけない
```

デフォルトだとリンクは枠（``pdfborder``）で囲まれて表示されます。
リンクの対象ごとに文字色を設定できますが、``allcolors``を使って一括設定するのが楽ちんです。

## PDFのしおりを作成したい

```latex
\hypersetup{bookmarks=true}  % デフォルト
\hypersetup{bookmarksnumbered=true}    %  しおりのタイトルに章番号を表示する
```

PDFのしおり（ブックマーク）は自動で生成されるようになっています。
長い文書の場合は、章番号も表示するとよいです。

## しおりの文字化け対策

```latex
\usepackage{pxjahyper}
\pxjahypersetup{キー=値, ...}
```

(u)pLaTeXで``hyperref``を使うとPDFのしおりが文字化けします。
その場合には``pxjahyper``パッケージを読み込んで対応します。

## ページサイズ対策

```latex
\hypersetup{setpagesize=false}
```

## PDFのメタ情報を設定したい

```latex
\hypersetup{pdftitle=PDFのタイトル}
\hypersetup{pdfauthor=PDFの著者}
\hypersetup{pdfsubject=PDFのサブジェクト}
% \hypersetup{pdfcreator=LaTeX with hyperref}
\hypersetup{pdfkeywords="キーワード1,キーワード2,..."}
\hypersetup{pdfduplex="Simplex|DuplexFlipShortEdge|DuplexFlipLongEdge"}  % 両面印刷の設定
```

PDFのメタ情報を設定できます。
``Preview.app``の場合、``[Tools] → [Show inspector]``（{kbd}`⌘ + i`）で確認できます。
ひとの目に入る情報ではないので設定しなくても構いません。
設定する文字列は``"..."``で囲む必要はありません。

## リファレンス

- {command}`texdoc hyperref`
- {command}`texdoc pxjahyper`
