OrgのLaTeXエクスポート
----------------------

メインである「KumaROOT」のために、OrgのLaTeXエクスポートについて調べ
ていたら、いい感じの長さになってしまいました。

LaTeXエクスポートの手順
-----------------------

文章は、だいたい Org（のLaTeXエクスポート） + YaTeX
で書くことにしています。
具体的な手順は以下の通りです。YaTeXでのコンパイルにはpTeX（=ptex2pdf）を使っています

Orgファイルの編集
    emacs kumaroot.org
LaTeXエクスポート
    C-c C-e l l
LaTeXファイルのバッファを開く
    C-x b kumaroot.tex
YaTeXコマンドでコンパイル
    C-c C-t j
YaTeXコマンドでプレビュー
    C-c C-t p

LaTeXエクスポートの基本設定
---------------------------

過去に設定した内容を見直し＆テストしながら、基本的であろう項目を拾っ
てみました。

ox
    LaTeXエクスポートを担っているパッケージ [1]_
org
    No document
org
    No document
org
    LaTeXで使うクラスの設定。デフォルトは
    「article」。日本語を使う場合は「jsarticle」にする。ただし、後
    述する「org-latex-classes」に追加する必要がある。
org
    ファイルを開く外部プログラムを設定できる。何も設
    定しないとシステムデフォルトのプログラムを使うよ
    うになっている。ox-latexというより、orgの機能。
    PDFをPreview.appで開くように設定する（もしかして
    不要なのかな？）。デフォルトの設定を見ながら検討 する。

org
    LaTeXクラスのalist。Orgファイル中の
    「#+LATEX\ :sub:`CLASS`: [2]_」で指定
    できる。ない場合はデフォルト値が使われる。詳細は後述。
org
    OrgのLaTeXエクスポート（C-c C-e l p）で
    PDFを作るための設定。内部ではpdflatexが走ることになる。詳細は後述。
org
    LaTeXエクスポートした時に、ヘッダに挿
    入されるパッケージ群。org-latex-default-packages-alist の後に追
    記される。詳細は後述。

org-latex-classesの詳細
-----------------------

.. code:: commonlisp

    (class-name
      header-string
      (numberd-section . unnumberd-section)
      (...)

第１引数 : HEADER-STRING
~~~~~~~~~~~~~~~~~~~~~~~~

LaTeXファイルの挿入される文字列。documentclass や usepackage を書
くことができる。「org-latex-default-packages-alist」や
「org-latex-packages-alist」に入っているパッケージを呼び出すことができ
る。Orgファイル内の「#+LATEX\ :sub:`HEADER`:」、「#+LATEX:sub:`HEADEREXTRA`:」
キーワードの行で指定することもできる。

HEADER-STRINGの制御
^^^^^^^^^^^^^^^^^^^

-  「DEFAULT-PACKAGES」/「NO-DEFAULT-PACKAGES」（＝org-latex-default-packages-alist）
-  「PACKAGES」/「NO-PACKAGES」（＝org-latex-packages-alist）
-  「EXTRA」/「NO-EXTRA」

その他の関連する変数
^^^^^^^^^^^^^^^^^^^^

-  buffer-file-coding-system
-  org-latex-inputenc-alist
-  org-export-default-language

第２引数 : sectioning structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

説明するより、ソースを読んだ方が早いと思う。
以下にorg-latex-classesデフォルト値を掲載。

#+begin\ :sub:`src` emacs-lisp Original value was (("article" ;; <-- the
name of the class ;; HEADER-STRING : documentclass (+ default-packages)
"\\\\documentclass[11pt]{article}" ;; SECTIONING : matching for Org
headings and LaTeX sectioning ("\\\\section{%s}" . "\\\\section\*{%s}")
("\\\\subsection{%s}" . "\\\\subsection\*{%s}") ("\\\\subsubsection{%s}"
. "\\\\subsubsection\*{%s}") ("\\\\paragraph{%s}" .
"\\\\paragraph\*{%s}") ("\\\\subparagraph{%s}" .
"\\\\subparagraph\*{%s}"))

("report" "\\\\documentclass[11pt]{report}" ("\\\\part{%s}" .
"\\\\part\*{%s}") ("\\\\chapter{%s}" . "\\\\chapter\*{%s}")
("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
"\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
"\\\\subsubsection\*{%s}"))

("book" "\\\\documentclass[11pt]{book}" ("\\\\part{%s}" .
"\\\\part\*{%s}") ("\\\\chapter{%s}" . "\\\\chapter\*{%s}")
("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
"\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
"\\\\subsubsection\*{%s}")))

#+end\ :sub:`src`

jsarticleの場合
^^^^^^^^^^^^^^^

基本的には、「article」部分をコピペして、必要な部分を変更する。

#+begin\ :sub:`src` emacs-lisp ("jsarticle" ;; <-- set to "jsarticle"
(any name is OK) ;; HEADER-STRING : change documentclass to jsarticle ;;
: also set dvipdfmx driver "\\\\documentclass[12pt,
dvipdfmx]{jsarticle}" ;; SECTIONING : leave them as it is
("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
"\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
"\\\\subsubsection\*{%s}") ("\\\\paragraph{%s}" . "\\\\paragraph\*{%s}")
("\\\\subparagraph{%s}" . "\\\\subparagraph\*{%s}"))

#+end\ :sub:`src`

org-latex-pdf-processの詳細
---------------------------

#+begin\ :sub:`src` emacs-lisp Its value is ("pdflatex -interaction
nonstopmode -output-directory %o %f" "pdflatex -interaction nonstopmode
-output-directory %o %f" "pdflatex -interaction nonstopmode
-output-directory %o %f")

#+end\ :sub:`src`

Orgファイルから直接PDFを生成することもできる（C-c C-e l p ／ C-c C-e l
o）。これはそのための設定。デフォルトの設定だと、pdflatex を
使っている。３回も回しているとは知らなんだ。

リストになっているのは、途中でbibtexを入れたりできるように。Org自身
に適当なコンパイル方法を検知する仕組みが無いので、ユーザが好きにい
じれるようにしてるみたい。

日本語だとpdflatexがうまく動かないので、一度LaTeXファイルにエクスポー
トして、pTeXを使ってコンパイルしていたが、これをきちんと設定すれば、
楽になるのかも。

org-latex-packages-alistの詳細
------------------------------

#+begin\ :sub:`src` emacs-lisp A cell is of the format: ("options"
"package" SNIPPET-FLAG)

#+end\ :sub:`src`

第１引数
    パッケージのオプション
第２引数
    パッケージ名
第３引数
    よくわからん

パッケージの追加方法
~~~~~~~~~~~~~~~~~~~~

#+begin\ :sub:`src` emacs-lisp (add-to-list 'org-latex-packages-alist
'("" "atbegshi")) (add-to-list 'org-latex-packages-alist
"\\\\AtBeginShipoutFirst{\\\\special{pdf:tounicode EUC-UCS2}}")

(add-to-list 'org-latex-packages-alist
"\\\\hypersetup{setpagesize=false}") (add-to-list
'org-latex-packages-alist "\\\\hypersetup{colorlinks=true}")
(add-to-list 'org-latex-packages-alist "\\\\hypersetup{linkcolor=blue}")

(add-to-list 'org-latex-packages-alist '("" "listings")) (add-to-list
'org-latex-packages-alist '("" "color")) (add-to-list
'org-latex-packages-alist '("" "fancyvrb"))

#+end\ :sub:`src`

このように「add-to-list」を使って、追加する。
「hypersetup」などの先頭につけるバックスラッシュはエスケープする。
すると以下のようにLaTeXファイルのヘッダに追加される。

#+begin\ :sub:`src` latex \\hypersetup{linkcolor=blue}
\\hypersetup{colorlinks=true} \\hypersetup{setpagesize=false}
\\usepackage{fancyvrb} \\usepackage{color} \\usepackage{listings}
\\AtBeginShipoutFirst{\\special{pdf:tounicode EUC-UCS2}}
\\usepackage{atbegshi}

#+end\ :sub:`src`

・・・なんと、よくわからない順番にソートされる。

これは、add-to-list の第３引数を t にすることで解決できた。 t
にしておくとalist の最後に足されるため。

これで思い通りの順番に並べることができる。また、
「add-to-list」の他に、「add-to-order-list」というのがあるみたいな
のでそちらも調べてみる。

設定するときの注意点
~~~~~~~~~~~~~~~~~~~~

-  すべてのファイルに使いたいパッケージであること
-  「org-format-latex-header」の設定とコンフリクトしないこと
-  「org-latex-default-packages-alist」のパッケージとコンフリクトしないこと

\`

org-latex-default-packages-alistの詳細
--------------------------------------

このリストにあるパッケージはOrg-modeを動かすために必要な最低限のパッ
ケージなので、基本的には変更しないこと。ただし、あるパッケージを使
いたいときに、ここにあるパッケージとコンフリクトするようなら修正す
るようにする。

リストにあるパッケージ一覧
~~~~~~~~~~~~~~~~~~~~~~~~~~

inputenc,
    for basic font and character selection
fixltx2e
    Important patches of LaTeX itself
graphicx
    for including images
longtable
    For multipage tables
float,
    for figure placement
rotating
    for sideways figures and tables
ulem
    for underline and strike-through
amsmath
    for subscript and superscript and math environments
textcomp,
    for various symbols used for interpreting the entities in
    \`org-entities'. You can skip some of these packages if you don't
    use any of their symbols.
hyperref
    for cross references

デフォルト設定
~~~~~~~~~~~~~~

Emacs24.1 で多少変更されたらしい。

#+begin\ :sub:`src` emacs-lisp Value: (("AUTO" "inputenc" t) ("T1"
"fontenc" t) ("" "fixltx2e" nil) ("" "graphicx" t) ("" "longtable" nil)
("" "float" nil) ("" "wrapfig" nil) ("" "rotating" nil) ("normalem"
"ulem" t) ("" "amsmath" t) ("" "textcomp" t) ("" "marvosym" t) (""
"wasysym" t) ("" "amssymb" t) ("" "hyperref" nil) "\\\\tolerance=1000")

#+end\ :sub:`src`

org-format-latex-headerの詳細
-----------------------------

あとでちゃんと読もうかな。

Documentation:
~~~~~~~~~~~~~~

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

デフォルト値
~~~~~~~~~~~~

#+begin\ :sub:`src` emacs-lisp "\\\\documentclass{article}\\n
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

#+end\ :sub:`src`

LaTeXエクスポートの再設定
-------------------------

基本設定の項目が分かったので、もう一度設定を見直してみます。

デフォルトの設定を確認する
--------------------------

org-latexの設定をすべてコメントアウトして、エクスポートしてみたとき
LaTeXファイルのヘッダは以下のようになっている。

#+begin\ :sub:`src` latex \\documentclass[11pt]{article}
\\usepackage[utf8]{inputenc} \\usepackage[T1]{fontenc}
\\usepackage{fixltx2e} \\usepackage{graphicx} \\usepackage{longtable}
\\usepackage{float} \\usepackage{wrapfig} \\usepackage{rotating}
\\usepackage[normalem]{ulem} \\usepackage{amsmath}
\\usepackage{textcomp} \\usepackage{marvosym} \\usepackage{wasysym}
\\usepackage{amssymb} \\usepackage{hyperref} \\tolerance=1000
\\author{Shota} \\date{\\today} \\title{\\LaTeX{} Export Test}
\\hypersetup{ pdfkeywords={}, pdfsubject={}, pdfcreator={Emacs 24.4.1
(Org mode 8.2.10)}}

\\begin{document}

\\maketitle \\tableofcontents

#+end\ :sub:`src`

このまま、YaTeX環境でのコンパイル（＝pTeX）は可能だが、
「dvipdfmx:warning:（error messages）」という警告がたくさんでる。
LaTeXファイルを開き、ドキュメントクラスのオプションでドライバを
dvipdfmxに指定するとこのエラーはでなくなる。

#+begin\ :sub:`src` latex \\documentclass[11pt, dvipdfmx]{article}

#+end\ :sub:`src`

直接出力（＝pdflatex）も試してみたが、「org-latex-compile: PDF file
./testing.pdf wasn't produced: [package error]」というログが
Messagesバッファに残り、うまくいってない。

org-latex-pdf-process を pTeXに変更する
---------------------------------------

#+begin\ :sub:`src` emacs-lisp (use-package ox-latex :config (setq
org-latex-pdf-process ("ptex2pdf -l -ot -synctex=1 -file-line-error"
"ptex2pdf -l -ot -synctex=1 -file-line-error" "ptex2pdf -l -ot
-synctex=1 -file-line-error" ) )

#+end\ :sub:`src`

「Warning: \`"ptex2pdf -l -ot -synctex=1 -file-line-error"' is a
malformed function」とう警告が表示され、そもそもの設定がうまくでき
ない。setq ではできんのか？後で調べる。

ドキュメントクラスにjsarticleを追加する
---------------------------------------

#+begin\ :sub:`src` latex \\documentclass[12pt, dvipdfmx]{jsarticle}

#+end\ :sub:`src`

文字サイズは少し大きく（＝12pt）して、ドライバには dvipdfmx を指定する。
sectioning については、article のデフォルトを使う。

#+begin\ :sub:`src` emacs-lisp (add-to-list 'org-latex-classes
'("jsarticle" "\\\\documentclass[dvipdfmx,12pt]{jsarticle}"
("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
"\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
"\\\\subsubsection\*{%s}") ("\\\\paragraph{%s}" . "\\\\paragraph\*{%s}")
("\\\\subparagraph{%s}" . "\\\\subparagraph\*{%s}") ))

#+end\ :sub:`src`

ドキュメントクラスにjsbookを追加する
------------------------------------

#+begin\ :sub:`src` latex \\documentclass[12pt, dvipdfmx]{jsbook}

#+end\ :sub:`src`

文字サイズは少し大きく（＝12pt）して、ドライバには dvipdfmx を指定する。
sectioning については、book のデフォルトを使う。

#+begin\ :sub:`src` emacs-lisp (add-to-list 'org-latex-classes
'("jsbook" "\\\\documentclass[dvipdfmx,12pt]{jsbook}" ("\\\\part{%s}" .
"\\\\part\*{%s}") ("\\\\chapter{%s}" . "\\\\chapter\*{%s}")
("\\\\section{%s}" . "\\\\section\*{%s}") ("\\\\subsection{%s}" .
"\\\\subsection\*{%s}") ("\\\\subsubsection{%s}" .
"\\\\subsubsection\*{%s}") ) )

#+end\ :sub:`src`

ドキュメントクラスにjsreportを追加する
--------------------------------------

#+begin\ :sub:`src` latex \\documentclass[12pt, dvipdfmx,
report]{jsbook}

#+end\ :sub:`src`

文字サイズは少し大きく（＝12pt）して、ドライバには dvipdfmx を指定する。
「jsreport」というクラスファイルはないが、jsbook に report
オプションをつければいいらしい。 sectioning については、article
のデフォルトを部分に chapter を付け加えた。

#+begin\ :sub:`src` latex (add-to-list 'org-latex-classes '("jsreport"
"\\\\documentclass[dvipdfmx,12pt,report]{jsbook}" ("\\\\chapter{%s}" .
"\\\\chapter\*{%s}") ("\\\\section{%s}" . "\\\\section\*{%s}")
("\\\\subsection{%s}" . "\\\\subsection\*{%s}") ("\\\\subsubsection{%s}"
. "\\\\subsubsection\*{%s}") ("\\\\paragraph{%s}" .
"\\\\paragraph\*{%s}") ) )

#+end\ :sub:`src`

デフォルトのドキュメントクラスを jsarticle に変更する
-----------------------------------------------------

すべてのOrgファイルに「#+latex\ :sub:`class`:
jsarticle」を付けるのはめんどくさいので、 デフォルトに設定する。

#+begin\ :sub:`src` emacs-lisp (setq org-latex-default-class
"jsarticle")

#+end\ :sub:`src`

hyperref の設定
---------------

#+begin\ :sub:`src` latex \\usepackage{hyperref} \\hypersetup{
setpagesize=false, %% <-- This line is very important pdfkeywords={},
pdfsubject={}, pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}

#+end\ :sub:`src`

hyperref パッケージと jsarticle は仲が良くなくて、そのままコンパイ
ルするとページの幅がおかしくなってしまう。これは setpagesize=false
とすることで解決する。hyperrefパッケージの設定は、hypersetupの中で
行うことができる。

しかし、デフォルトのhyperrefの中身は、ox-latex.elにハードコーディ
ングされていて追加／変更できないので、以下のように、hypersetupを２
回呼び出すことにする。

#+begin\ :sub:`src` latex \\usepackage{hyperref} \\hypersetup{
pdfkeywords={}, pdfsubject={}, pdfcreator={Emacs 24.4.1 (Org mode
8.2.10)}} \\hypersetup{ setpagesize=false }

#+end\ :sub:`src`

とりあえずテストしたい場合は、編集しているOrgファイルの先頭に
「#+latex\ :sub:`header`:」もしくは「#+latex:sub:`headerextra`:」を使って定義す
るとよい。

latex\ :sub:`header` と latex\ :sub:`headerextra`
の違いを調べるために、以下の順 番でhypersetupを定義してみた。

#+begin\ :sub:`src` latex

#+end\ :sub:`src`

すると、latex\ :sub:`header` > latex\ :sub:`headerextra`
の順に書かれることが分かっ
た。いまいちどういう時に順番を考えたらいいのか思いつかないけれど。

#+begin\ :sub:`src` latex \\usepackage{hyperref}
\\hypersetup{setpagesize=false} %% latex\ :sub:`header`:
\\hypersetup{linkcolor=blue} %% latex\ :sub:`header`:
\\hypersetup{colorlinks=true} %% latex\ :sub:`headerextra`:
\\tolerance=1000 \\author{Shota} \\date{\\today} \\title{\\LaTeX{}
Export Test} \\hypersetup{ pdfkeywords={}, pdfsubject={},
pdfcreator={Emacs 24.4.1 (Org mode 8.2.10)}}

#+end\ :sub:`src`

出力場所は、デフォルト出力のhypersetupの上になるが、コンパイルには
影響しないのでこれで良しとする。

上文字、下文字の自動変換をオフにする
------------------------------------

#+begin\ :sub:`src` emacs-lisp (setq org-use-sub-superscripts nil) (setq
org-export-with-sub-superscripts nil)

#+end\ :sub:`src`

Orgファイル中の「^（ハット）」「\_（アンダースコア）」以降の数文字は、
自動的に上文字、下文字に変換されてしまいます。便利なのかもしれませ
んが、意図しない箇所も変換されてしまうのはやっぱり不便なのでオフに
します。エクスポートするときも同じ理由でオフにしておきます。

上付き・下付きにしたい場合は、文字\ :sup:`上付き`\ 、文字\ :sub:`下付き`\ 、のよう
に中括弧（{}）で囲みます。Orgファイル中で「C-c C-x \\」すればプレビュー
できます。

listingsを使ってコードブロックの装飾する
----------------------------------------

#+begin\ :sub:`src` emacs-lisp (setq org-latex-listings t) (add-to-list
'org-latex-packages-alist '("" "listings")) (add-to-list
'org-latex-packages-alist '("" "color")) (add-to-list
'org-latex-packages-alist '("" "fancyvrb"))

#+end\ :sub:`src`

listlingsパッケージの初期設定はlstsetを使う。hypersetupのときと同じ
ように、Orgファイルの先頭に書いておく。

.. code:: commonlisp

    #+latex_header: \lstset{language=[LaTeX]TeX}
    #+latex_header: \lstset{basicstyle=\small}
    #+latex_header: \lstset{stringstyle=\ttfamily}
    #+latex_header: \lstset{commentstyle=\ttfamily}
    #+latex_header: \lstset{showstringspaces=false}
    #+latex_header: \lstset{frame=shadowbox}
    #+latex_header: \lstset{rulesepcolor=\color{black}}
    #+latex_header: \lstset{fancyvrb=true}

簡単なテスト方法
----------------

LaTeXエクスポートの設定のテスト [3]_のために、必要なemacs設定ファイルを編集してー、ロー
ドしてー、確認してー、とやっていると結構疲れます。

Org文書中に記述できるソースコードのブロックは、なんと内容を実行する
機能がついています。なので、テストの際はそれを使うと格段に捗ります。あるので、それを使うと

#+begin\ :sub:`src` emacs-lisp /#+BEGIN:sub:`SRC` emacs-lisp :exports
results :results silent (setq org-latex-listings t) (add-to-list
'org-latex-packages-alist '("" "listings")) (add-to-list
'org-latex-packages-alist '("" "color")) /#+END:sub:`SRC`

#+end\ :sub:`src`

上のコードをOrg文書の最初の方に書いておきます。エクスポートしたLaTeX
文書のヘッダには、「listings」「color」パッケージが追加されています。

#+begin\ :sub:`src` latex \\usepackage{hyperref} \\tolerance=1000
\\usepackage{color} %% <-- Added here \\usepackage{listings} %% <--
Added here \\hypersetup{setpagesize=false} \\hypersetup{linkcolor=blue}
\\hypersetup{colorlinks=true} \\author{Shota}

#+end\ :sub:`src`

思った通りの動きが確認できたのち、emacs設定ファイルに移動させればOKです。

PDFLaTeXの設定
--------------

ソースコードのハイライトに minted.sty を使うためにはpdflatexを使わな
ければいけません。そのための設定をここにメモします。

日本語 + PDFLaTeX
-----------------

BXjsclsというクラスファイルを使います。これまで何回やっても失敗して
たのは、TeXLive2014について来たバージョン（v0.3）が古かったためで
した。GitHubから最新版（v0.9）を取ってきたら解決しました。

.. code:: bash

    $ cd ~/repos/github/
    $ git clone git clone https://github.com/zr-tex8r/BXjscls.git
    $ cd BXjscls
    $ sudo mkdir /usr/local/texlive/texmf-local/tex/latex/bxjscls
    $ sudo cp *.cls *.def /usr/local/texlive/texmf-local/tex/latex/bxjscls/
    $ sudo mktexlsr

最後にmktexlsrすることで、 「
/usr/local/texlive/2014/texmf-dist/tex/latex/bxjscls/bxjsarticle.cls
」から
「/usr/local/texlive/texmf-local/tex/latex/bxjscls/bxjsarticle.cls」
へと参照先が代わります。

これで奥村さんのページのサンプルがコンパイルできるようになりました。

PDFLaTeX + minted.sty
---------------------

minted.sty は外部プログラムのPygmentsを呼ぶため、コンパイル時
に-shell-escape オプションを付ける必要があります。

#+begin\ :sub:`src` sh $ pdflatex -shell-escape sample.tex

#+end\ :sub:`src`

Org-LaTeXエクスポート + minted.sty
----------------------------------

さて、ようやく本来の目的にたどり着きました。少し使ってみたところ、
minted環境の中では日本語が使えないみたいなので、それを修正してから
いろいろ試した方が良さそうです。

.. [1]
   最近 org-latex \\rightarrow ox-latex に変更されたみたい。 (require
   'org-latex) しているサイトは内容が古いので、
   更新日を確認してみましょう。そしてより新しい情報を探し ましょう

.. [2]
   大文字・小文字の区別はない。以下のサンプル
   コードでも適当に使ってるだけなので気にしないでください

.. [3]
   Orgの機能なのでLaTeXエクスポート 以外でも使えます
