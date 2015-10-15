==================================================
LaTeXの使い方
==================================================


ほとんどの人は修論の時にLaTeXをがしがし使うことになると思います。
その時に「インストールできないー」などと焦っていては時既に時間切れ
[fn::ピンと来ない人は「ブロント語」でググってください]なので、簡単
にまとめておきます。

.. toctree::

   latex-install
   latex-japanese
   latex-yatex
   latex-packages




**** 日本語とLaTeX



     つい最近までは「Mac LaTeX インストール」などでググると、なんだか
     まとまりのない情報で溢れていました。しかし、現在はそれらを取りま
     とめようということで開発が進んでいるようで、これからはTeXLive一択
     で良いみたいです。

*** pdfLaTeX

*** jsarticleドキュメントクラス

     #+begin_src latex
\documentclass[dvipdfmx,12pt]{jsarticle}
     #+end_src

    日本語のLaTeX文書にはjsarticleドキュメントクラスを使います。
    ドライバはdvipdfmxを使います。

*** graphicxパッケージ

     #+begin_src latex
\usepackage[hiresbb]{graphicx}
     #+end_src

    画像を扱う場合はgraphicxパッケージを使います。
    ドライバはdvipdfmxを使います。ドキュメントクラス指定時に宣言していてれば、ここで指定する必要はありません。
    画像のバウンディングボックスに「HiResBoundingBox」を使う場合は、hiresbbオプションを付けておきます。

*** hyperrefパッケージ

    LaTeX文書内にハイパーリンクを置く場合には、hyperrefパッケージを使うとよい。
    しかし、日本語のドキュメントクラスを使うとページから文章がはみ出たり、目次のしおりが文字化けしたりするので、以下のように対処する必要がある。

**** PXjahyperパッケージも読み込む

     #+begin_src latex
\usepackage{pxjahyper}
     #+end_src

     PXjahyperパッケージを読み込んでおけば、万事解決するみたい。
     それでも解決しない場合は、以下のように個別に対処する。

**** ページサイズ対策

     #+begin_src latex
\hypersetup{setpagesize=false}
     #+end_src

**** しおりの文字化け対策

     #+begin_src latex
\usepackage{atbegshi}
\AtBeginShipoutFirst{\special{pdf:tounicode EUC-UCS2}}
\AtBeginShipoutFirst{\special{pdf:tounicode 90ms-RKSJ-UCS2}}
     #+end_src

     何をしてくのか全く分かっていないけれど、両方書いておけばいい。
     それでだめな場合は片方にする。
