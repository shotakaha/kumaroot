# org-latex

``Org-mode`` で作成した文書を LaTeX 文書に変換する方法です。



## ワークフロー

1. Orgファイルの編集（``emacs kumaroot.org``）
1. LaTeXエクスポート（``C-c C-e l l``）
1. LaTeXファイルのバッファを開く（``C-x b kumaroot.tex``）
1. YaTeXコマンドでコンパイル（``C-c C-t j``）
1. YaTeXコマンドでプレビュー（``C-c C-t p``）


## 必要なパッケージ（``ox-latex``）

LaTeX文書へのエクスポートは``ox-latex.el``が担っています。
2014年に``org-latex``から``ox-latex``にパッケージ名が変更になりました。
``package.el``でインストールした場合は``autoload``されるはずなので、
``(require 'ox-latex)``はとくに要らないはずです。


## ドキュメントクラスの設定（``org-latex-default-class``）

LaTeXのエクスポートに使うドキュメントクラスを指定します。
デフォルトは``article``になっているので、日本語を使う場合は``jsarticle``にする必要があります。

ただし、まずは ``org-latex-classes`` （後述）に追加する必要がある。
Orgファイル中の ``#+LATEX_CLASS:`` （大文字／小文字の区別なし）で指定できる
（ない場合はデフォルト値が使われる）。

```lisp
Original value was
(("article"    ;; <-- the name of the class
    ;; HEADER-STRING : documentclass (+ default-packages)
    "\\documentclass[11pt]{article}"
    ;; SECTIONING : matching for Org headings and LaTeX sectioning
    ("\\section{%s}" . "\\section*{%s}")
    ("\\subsection{%s}" . "\\subsection*{%s}")
    ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
    ("\\paragraph{%s}" . "\\paragraph*{%s}")
    ("\\subparagraph{%s}" . "\\subparagraph*{%s}"))

("report"
    "\\documentclass[11pt]{report}"
    ("\\part{%s}" . "\\part*{%s}")
    ("\\chapter{%s}" . "\\chapter*{%s}")
    ("\\section{%s}" . "\\section*{%s}")
    ("\\subsection{%s}" . "\\subsection*{%s}")
    ("\\subsubsection{%s}" . "\\subsubsection*{%s}"))

("book"
    "\\documentclass[11pt]{book}"
    ("\\part{%s}" . "\\part*{%s}")
    ("\\chapter{%s}" . "\\chapter*{%s}")
    ("\\section{%s}" . "\\section*{%s}")
    ("\\subsection{%s}" . "\\subsection*{%s}")
    ("\\subsubsection{%s}" . "\\subsubsection*{%s}")))
```


# ドキュメントクラスの追加（``org-latex-classes``）

``alist`` になっているので``add-to-list``を使って自分で設定を追加できます。
``jsarticle``などの日本語ドキュメントクラスは各自で追加しておきましょう。

```lisp
(add-to-list 'org-latex-classes
            '("jsarticle"
                "\\documentclass[dvipdfmx,12pt]{jsarticle}"
                ("\\section{%s}" . "\\section*{%s}")
                ("\\subsection{%s}" . "\\subsection*{%s}")
                ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                ("\\paragraph{%s}" . "\\paragraph*{%s}")
                ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
            )
)
(add-to-list 'org-latex-classes
            '("jsreport"
                "\\documentclass[dvipdfmx,12pt,report]{jsbook}"
                ("\\chapter{%s}" . "\\chapter*{%s}")
                ("\\section{%s}" . "\\section*{%s}")
                ("\\subsection{%s}" . "\\subsection*{%s}")
                ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                ("\\paragraph{%s}" . "\\paragraph*{%s}")
            )
)
(add-to-list 'org-latex-classes
            '("jsbook"
                "\\documentclass[dvipdfmx,12pt]{jsbook}"
                ("\\part{%s}" . "\\part*{%s}")
                ("\\chapter{%s}" . "\\chapter*{%s}")
                ("\\section{%s}" . "\\section*{%s}")
                ("\\subsection{%s}" . "\\subsection*{%s}")
                ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
            )
)
(add-to-list 'org-latex-classes
            '("bxjsarticle"
                "\\documentclass[pdflatex,jadriver=standard,12pt]{bxjsarticle}"
                ("\\section{%s}" . "\\section*{%s}")
                ("\\subsection{%s}" . "\\subsection*{%s}")
                ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                ("\\paragraph{%s}" . "\\paragraph*{%s}")
                ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
            )
)
(add-to-list 'org-latex-classes
            '("beamer"
                "\\documentclass[dvipdfmx,12pt]{beamer}"
                ("\\section{%s}" . "\\section*{%s}")
                ("\\subsection{%s}" . "\\subsection*{%s}")
                ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                ("\\paragraph{%s}" . "\\paragraph*{%s}")
                ("\\subparagraph{%s}" . "\\subparagraph*{%s}")
            )
)
```


## パッケージの追加（``org-latex-packages-alist``）


LaTeXエクスポートした時に、ヘッダーに挿入されるパッケージ群です。
``org-latex-default-packages-alist`` の後に追記されます。

これも``alist``になっているので``add-to-list``を使って自分で設定を追加できます。
``hyperref``パッページを使ったときのしおりの文字化け対策として
``pxjahyper`` パッケージを追加したり、``hyperref``の設定（``hypersetup``）を追加するとよいです。

``add-to-list`` 第2引数にパッケージ名 or コマンド名を指定します。
``hypersetup`` などのコマンド名の先頭につけるバックスラッシュはエスケープが必要です。
第3引数を``t``にすることで、書いた順番でプリアンブルに出力されます。

使うパッケージは、すべてのファイルに共通なパッケージにします。
その際、すでに設定されている ``org-format-latex-header`` や
``org-latex-default-packages-alist`` のパッケージとコンフリクトしないように注意する必要があります。
``hyperref``パッケージはすでにインクルードされてるので ``hypersetup`` で設定を変更する必要があります。
また、Orgファイル内の``#+LATEX_HEADER:``でファイルに個別の設定ができます。

```lisp
;; usepackage型
(add-to-list 'org-latex-packages-alist '("オプション" "パッケージ名") t)

;; maketitle型
(add-to-list 'org-latex-packages-alist "\\コマンド名{オプション}" t)
```

## サンプルコード

```lisp
;; しおりの文字化け対策
(add-to-list 'org-latex-packages-alist '("" "pxjahyper") t)
;; (add-to-list 'org-latex-packages-alist '("" "atbegshi") t)
;; (add-to-list 'org-latex-packages-alist "\\AtBeginShipoutFirst{\\special{pdf:tounicode EUC-UCS2}}" t)

;; hyperrefの設定
(add-to-list 'org-latex-packages-alist "\\hypersetup{setpagesize=false}" t)
(add-to-list 'org-latex-packages-alist "\\hypersetup{colorlinks=true}" t)
(add-to-list 'org-latex-packages-alist "\\hypersetup{linkcolor=blue}" t)

;; その他のパッケージの追加
(add-to-list 'org-latex-packages-alist '("" "listings") t)
(add-to-list 'org-latex-packages-alist '("" "color") t)
(add-to-list 'org-latex-packages-alist '("" "fancyvrb") t)

;; 文字ハイライトに minted を使う（pdflatexじゃないと動かない）
;;(add-to-list 'org-latex-packages-alist '("" "minted"))
(setq org-latex-listings t)
```

## デフォルトで使われるパッケージ（ ``org-latex-default-packages-alist`` ）

デフォルトのパッケージは ``Org-mode`` を動かすために必要な最低限のパッケージなので基本的には変更しないほうがよいです。
ただし、あるパッケージを使いたいときに、ここにあるパッケージとコンフリクトするようなら修正が必要です。


### リストにあるパッケージ一覧

``inputenc``
: for basic font and character selection

``fixltx2e``
: Important patches of LaTeX itself

``graphicx``
: for including images
``longtable``
: For multipage tables

``float``
: for figure placement

``rotating``
: for sideways figures and tables

``ulem``
: for underline and strike-through

``amsmath``
: for subscript and superscript and math environments

``textcomp``
: for various symbols used for interpreting the entities in ``org-entities``.
    You can skip some of these packages if you don't use any of their symbols.

``hyperref``
: for cross-references


## デフォルト設定


``Emacs24.1`` で多少変更されたみたいです。

```lisp
Value:
(("AUTO" "inputenc" t)
("T1" "fontenc" t)
("" "fixltx2e" nil)
("" "graphicx" t)
("" "longtable" nil)
("" "float" nil)
("" "wrapfig" nil)
("" "rotating" nil)
("normalem" "ulem" t)
("" "amsmath" t)
("" "textcomp" t)
("" "marvosym" t)
("" "wasysym" t)
("" "amssymb" t)
("" "hyperref" nil)
"\\tolerance=1000")
```



## 上文字、下文字の自動変換をオフにする

```lisp
(setq org-use-sub-superscripts nil)
(setq org-export-with-sub-superscripts nil)
```

Orgファイル中の``^（ハット）``や``_（アンダースコア）``以降の英数字は自動的に上文字、下文字に変換されてしまいます。
便利なのかもしれませんが、意図しない箇所も変換されてしまうのはやっぱり不便なのでオフにします。
エクスポートするときも同じ理由でオフにしておきます。

上付き・下付きにしたい場合は、
``文字^{上付き}`` 、 ``文字_{下付き}`` のように ``中括弧 {}`` で囲みます。
Orgファイル中で ``C-c C-x \`` すればプレビューできます。

## hyperref の設定

```latex
\usepackage{hyperref}
\hypersetup{
    setpagesize=false,    %% <-- This line is very important
    pdfkeywords={},
    pdfsubject={},
    pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}
```

``hyperref`` パッケージと ``jsarticle`` は仲が良くないので、そのままコンパイルするとページの幅がおかしくなります。
``\hypersetup``で``setpagesize=false``を設定することで解決できます。

しかし、デフォルトの ``hyperref`` オプションは``ox-latex.el``にハードコーディングされていて追加／変更できないので
``org-latex-packages-alist``や``#+latex_headers:`` / ``#+latex_header_extra:``などを複数回使って、
1つずつ呼び出すことにします。

```latex
\\usepackage{hyperref}
\\hypersetup{pdfkeywords={},
            pdfsubject={},
            pdfcreator={Emacs 24.4.1 (Org mode8.2.10)}}
\\hypersetup{ setpagesize=false }
```

とりあえずテストしたい場合は、
編集しているOrgファイルの先頭に``#+latex_header:``もしくは``#+latex_header_extra:``を
使って定義するとよいです。

``latex_header``と``latex_header_extra`` の違いを調べるために、以下の順番で``hypersetup``を定義してみました。

```latex
#+latex_header: \hyperref{setpagesize=false}
#+latex_header_extra: \hyperref{colorlinks=true}
#+latex_header: \hyperref{linkcolor=blue}
```

これで``latex_header`` > ``latex_header_extra``の順に追加されることがわかりました。

```latex
\usepackage{hyperref}
\hypersetup{setpagesize=false}    %% latex_header:
\hypersetup{linkcolor=blue}       %% latex_header:
\hypersetup{colorlinks=true}      %% latex_header_extra:
\tolerance=1000
\author{Shota}
\date{\today}
\title{\LaTeX{} Export Test}
\hypersetup{pdfkeywords={},
           pdfsubject={},
           pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}
```

出力場所は、デフォルト出力の ``hypersetup`` の上になるが、コンパイルには影響しないのでこれで良しとします。

## その他

``org-export-latex-coding-system``
: No document

``org-export-latex-date-format``
: No document

``org-file-apps``
: ファイルを開く外部プログラムを設定できる。
  何も設定しないとシステムデフォルトのプログラムを使うようになっている。
  ``ox-latex`` というより、=org= の機能。 PDFを ``Preview.app``
  で開くように設定する（もしかして不要なのかな？）。
  デフォルトの設定を見ながら検討する。

``org-latex-pdf-process``
: OrgのLaTeXエクスポート（ ``C-c C-e l p`` ）でPDFを作るための設定。
  内部ではpdflatexが走ることになる。詳細は後述。

## org-latex-classesの詳細

第1引数
: LaTeXファイルの挿入される文字列。 ``documentclass`` や
  ``usepackage`` を書くことができる。
  ``org-latex-default-packages-alist`` や ``org-latex-packages-alist``
  に入っているパッケージを 呼び出すことができる。 Orgファイル内の
  ``#+LATEX_HEADER:`` 、 ``#+LATEX_HEADER_EXTRA:``
  キーワードの行で指定することもできる。

第2引数
: 説明するよりソースを読んだ方が早い。 以下に ``org-latex-classes``
  デフォルト値を掲載。

## HEADER-STRINGの制御

-  ``DEFAULT-PACKAGES`` / ``NO-DEFAULT-PACKAGES`` （＝
   ``org-latex-default-packages-alist`` ）
-  ``PACKAGES`` / ``NO-PACKAGES`` （＝ ``org-latex-packages-alist`` ）
-  ``EXTRA`` / ``NO-EXTRA``

## その他の関連する変数

-  ``buffer-file-coding-system``
-  ``org-latex-inputenc-alist``
-  ``org-export-default-language``

### org-latex-pdf-processの詳細

```lisp
Its value is
("pdflatex -interaction nonstopmode -output-directory %o %f"
 "pdflatex -interaction nonstopmode -output-directory %o %f"
 "pdflatex -interaction nonstopmode -output-directory %o %f")
```

Orgファイルから直接PDFを生成することもできる
（ ``C-c C-e l p`` / ``C-c C-e l o`` ）。
これはそのための設定。デフォルトの設定だと、pdflatex を使っている。
3回も回しているとは知らなんだ。

リストになっているのは、途中で ``bibtex`` を入れたりできるように。
Org自身に適当なコンパイル方法を検知する仕組みが無いので、
ユーザが好きにいじれるようにしてるみたい。

日本語だと ``pdflatex``
がうまく動かないので、一度LaTeXファイルにエクスポートして、
pTeXを使ってコンパイルしていたが、これをきちんと設定すれば、楽になるのかも。

### org-latex-packages-alistの詳細

```lisp
A cell is of the format: ("options" "package" SNIPPET-FLAG)
```

第1引数
: パッケージのオプション

第2引数
: パッケージ名

第3引数
: よくわからん

### org-format-latex-headerの詳細


あとでちゃんと読もうかな。

```{admonition} Documentation

The document header used for processing LaTeX fragments. It is
imperative that this header make sure that no page number appears on the
page. The package defined in the variables
\`org-latex-default-packages-alist' and \`org-latex-packages-alist' will
either replace the placeholder "[PACKAGES]" in this header, or they will
be appended.Documentation: The document header used for processing LaTeX
fragments. It is imperative that this header make sure that no page
number appears on the page. The package defined in the variables
\`org-latex-default-packages-alist' and \`org-latex-packages-alist' will
either replace the placeholder "[PACKAGES]" in this header, or they will
be appended.
```

### デフォルト値


```lisp
"\\\\documentclass{article}\\n
\\\\usepackage[usenames]{color}\\n [PACKAGES]\\n [DEFAULT-PACKAGES]\\n
\\\\pagestyle{empty} % do not remove\\n

% The settings below are copied from fullpage.sty\\n
\\\\setlength{\\\\textwidth}{\\\\paperwidth}\\n
\\\\addtolength{\\\\textwidth}{-3cm}\\n
\\\\setlength{\\\\oddsidemargin}{1.5cm}\\n
\\\\addtolength{\\\\oddsidemargin}{-2.54cm}\\n
\\\\setlength{\\\\evensidemargin}{\\\\oddsidemargin}\\n
\\\\setlength{\\\\textheight}{\\\\paperheight}\\n
\\\\addtolength{\\\\textheight}{-\\\\headheight}\\n
\\\\addtolength{\\\\textheight}{-\\\\headsep}\\n
\\\\addtolength{\\\\textheight}{-\\\\footskip}\\n
\\\\addtolength{\\\\textheight}{-3cm}\\n
\\\\setlength{\\\\topmargin}{1.5cm}\\n
\\\\addtolength{\\\\topmargin}{-2.54cm}"
```


### LaTeXエクスポートの再設定


基本設定の項目が分かったので、もう一度設定を見直してみます。

#### デフォルトの設定を確認する

org-latexの設定をすべてコメントアウトして、エクスポートしてみたときLaTeXファイルのヘッダーは
次のようになっていました。

```latex
\\documentclass[11pt]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{fixltx2e}
\\usepackage{graphicx}
\\usepackage{longtable}
\\usepackage{float}
\\usepackage{wrapfig}
\\usepackage{rotating}
\\usepackage[normalem]{ulem}
\\usepackage{amsmath}
\\usepackage{textcomp}
\\usepackage{marvosym}
\\usepackage{wasysym}
\\usepackage{amssymb}
\\usepackage{hyperref}
\\tolerance=1000
\\author{Shota}
\\date{\\today}
\\title{\\LaTeX{} Export Test}
\\hypersetup{pdfkeywords={},
            pdfsubject={},
            pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}

\\begin{document}

\\maketitle
\\tableofcontents
```

このままYaTeX環境でコンパイル（=``pTeX``）できますが、
たくさんの``dvipdfmx:warning:（error messages）`` という警告が表示されます。
LaTeXファイルを開き、ドキュメントクラスのオプションでドライバーに``dvipdfmx``を指定することで解決できます。

```latex
\\documentclass[11pt, dvipdfmx]{article}
```

直接出力（=``pdflatex``）も試してみましたが、
``org-latex-compile: PDF file ./testing.pdf wasn't produced: [package error]``
というログが**Messagesバッファ**に残っていてうまくいってないようです。


## org-latex-pdf-process を pTeXに変更する

```lisp
(use-package ox-latex
:config
    (setq org-latex-pdf-process
        ("ptex2pdf -l -ot -synctex=1 -file-line-error"
        "ptex2pdf -l -ot -synctex=1 -file-line-error"
        "ptex2pdf -l -ot -synctex=1 -file-line-error")
        )
```

``Warning: \`"ptex2pdf -l -ot -synctex=1 -file-line-error"' is a malformed function``
という警告が表示され、そもそもの設定がうまくできない。
``setq`` ではできないのか？後で調べる。



## ドキュメントクラスにjsarticleを追加する

```latex
\\documentclass[12pt, dvipdfmx]{jsarticle}
```

文字サイズは少し大きく（＝ ``12pt`` ）して、ドライバには ``dvipdfmx`` を指定する。
sectioning については、article のデフォルトを使う。

```lisp
(add-to-list 'org-latex-classes
            '("jsarticle"
            "\\\\documentclass[dvipdfmx,12pt]{jsarticle}"
                ("\\\\section{%s}" . "\\\\section\*{%s}")
                ("\\\\subsection{%s}" . "\\\\subsection\*{%s}")
                ("\\\\subsubsection{%s}" . "\\\\subsubsection\*{%s}")
                ("\\\\paragraph{%s}" . "\\\\paragraph\*{%s}")
                ("\\\\subparagraph{%s}" . "\\\\subparagraph\*{%s}") ))
```

## ドキュメントクラスにjsbookを追加する

```latex
\\documentclass[12pt, dvipdfmx]{jsbook}
```

文字サイズは少し大きく（＝12pt）して、ドライバには dvipdfmx を指定する。
sectioning については、book のデフォルトを使う。

```lisp
(add-to-list 'org-latex-classes
            '("jsbook"
                "\\\\documentclass[dvipdfmx,12pt]{jsbook}"
                ("\\\\part{%s}" . "\\\\part\*{%s}")
                ("\\\\chapter{%s}" . "\\\\chapter\*{%s}")
                ("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
                "\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
                "\\\\subsubsection\*{%s}") ) )
```


## ドキュメントクラスにjsreportを追加する

```
\\documentclass[12pt, dvipdfmx, report]{jsbook}
```

文字サイズは少し大きく（＝12pt）して、ドライバには dvipdfmx を指定する。
「jsreport」というクラスファイルはないが、jsbook に report
オプションをつければいいらしい。 sectioning については、article
のデフォルトを部分に chapter を付け加えた。

```lisp
(add-to-list 'org-latex-classes
            '("jsreport"
                "\\\\documentclass[dvipdfmx,12pt,report]{jsbook}"
                ("\\\\chapter{%s}" . "\\\\chapter\*{%s}")
                ("\\\\section{%s}" . "\\\\section\*{%s}")
                ("\\\\subsection{%s}" . "\\\\subsection\*{%s}")
                ("\\\\subsubsection{%s}" . "\\\\subsubsection\*{%s}")
                ("\\\\paragraph{%s}" . "\\\\paragraph\*{%s}") ) )
```

## デフォルトのドキュメントクラスを jsarticle に変更する

すべてのOrgファイルに
``#+latex_class: jsarticle`` を付けるのはめんどくさいので デフォルトに設定する。

```lisp
(setq org-latex-default-class "jsarticle")
```

## listingsを使ってコードブロックの装飾する

```lisp
(setq org-latex-listings t)
(add-to-list 'org-latex-packages-alist '("" "listings"))
(add-to-list 'org-latex-packages-alist '("" "color"))
(add-to-list 'org-latex-packages-alist '("" "fancyvrb"))
```

listlingsパッケージの初期設定はlstsetを使う。hypersetupのときと同じ
ように、Orgファイルの先頭に書いておく。

```lisp
#+latex_header: \lstset{language=[LaTeX]TeX}
#+latex_header: \lstset{basicstyle=\small}
#+latex_header: \lstset{stringstyle=\ttfamily}
#+latex_header: \lstset{commentstyle=\ttfamily}
#+latex_header: \lstset{showstringspaces=false}
#+latex_header: \lstset{frame=shadowbox}
#+latex_header: \lstset{rulesepcolor=\color{black}}
#+latex_header: \lstset{fancyvrb=true}
```

## 簡単なテスト方法

LaTeXエクスポートの設定のテスト [1]_のために、必要なemacs設定ファイルを編集してー、ロー
ドしてー、確認してー、とやっていると結構疲れます。

Org文書中に記述できるソースコードのブロックは、なんと内容を実行する
機能がついています。なので、テストの際はそれを使うと格段に捗ります。あるので、それを使うと

```lisp
#+begin\ :sub:`src` emacs-lisp /#+BEGIN:sub:`SRC` emacs-lisp :exports
results :results silent (setq org-latex-listings t) (add-to-list
'org-latex-packages-alist '("" "listings")) (add-to-list
'org-latex-packages-alist '("" "color")) /#+END:sub:`SRC`

#+end\ :sub:`src`
```

上のコードをOrg文書の最初の方に書いておきます。エクスポートしたLaTeX
文書のヘッダには、「listings」「color」パッケージが追加されています。

```
#+begin\ :sub:`src` latex \\usepackage{hyperref} \\tolerance=1000
\\usepackage{color} %% <-- Added here \\usepackage{listings} %% <--
Added here \\hypersetup{setpagesize=false} \\hypersetup{linkcolor=blue}
\\hypersetup{colorlinks=true} \\author{Shota}

#+end\ :sub:`src`
```

思った通りの動きが確認できたのち、emacs設定ファイルに移動させればOKです。

## PDFLaTeXの設定

ソースコードのハイライトに minted.sty を使うためにはpdflatexを使わな
ければいけません。そのための設定をここにメモします。

## 日本語 + PDFLaTeX

BXjsclsというクラスファイルを使います。

### PDFLaTeX + minted.sty

minted.sty は外部プログラムのPygmentsを呼ぶため、コンパイル時
に-shell-escape オプションを付ける必要があります。

```
#+begin\ :sub:`src` sh $ pdflatex -shell-escape sample.tex

#+end\ :sub:`src`
```

### Org-LaTeXエクスポート + minted.sty

さて、ようやく本来の目的にたどり着きました。少し使ってみたところ、
minted環境の中では日本語が使えないみたいなので、それを修正してから
いろいろ試した方が良さそうです。
