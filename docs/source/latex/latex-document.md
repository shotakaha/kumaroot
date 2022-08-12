==================================================
ドキュメントのキホン（``upLaTeX``）
==================================================


LaTeX文書の詳細な作成方法に関してはググッた方がよいでしょう。
基本的な形は以下の通りです。

.. code-block:: latex

   %% ドキュメントクラスの指定
   \documentclass[uplatex, dvipdfmx,12pt]{jsarticle}

   %% プリアンブル
   \usepackage[utf8]{inputenc}
   \usepackage[T1]{fontenc}
   \usepackage{fixltx2e}
   \usepackage{graphicx}
   ...

   %% ハイパーリンクのカスタマイズ
   \usepackage{hyperref}
   \usepackage{pxjahyper}
   \hypersetup{setpagesize=false}
   \hypersetup{colorlinks=true}
   \hypersetup{linkcolor=blue}

   %% 書籍情報の設定
   \author{Shota TAKAHASHI}
   \date{2016-01-14 Monday}
   \title{第一回打ち合わせ}

   %% 本文
   \begin{document}

   \maketitle
   \tableofcontents

   \section{登山計画}

       \subsection{頂上：アインシュタイン方程式を理解する}

       \begin{itemize}
           \item デ 15. アインシュタインの重力の法則
           \item デ 24. 物質の存在によるアインシュタイン方程式の変更
           \item デ 25. 物質のエネルギー・運動量テンソル
           \item 杉 10. アインシュタイン方程式
       \end{itemize}

       \subsection{頂上からの眺め：アインシュタイン方程式で分かる物理}

       \begin{itemize}
           \item デ 33. 重力波
           \item デ 19. ブラック・ホール
           \item デ 18. シュヴァルツシルトの解
           \item 杉 11. 球対称時空
           \item 杉 12. 一般相対性理論の検証
       \end{itemize}

   \end{document}

構成要素
==================================================

:ドキュメントクラス: 文書のスタイルを指定します。日本語の場合 ``jsarticle`` 系 を使っておけばよいです。``upLaTeX`` を使う場合は ``[uplatex]`` オプションが必要です。
:プリアンブル: パッケージの追加や設定を行う部分です。自前マクロもここに書きます。要するに **本文以外** の部分。
:本文: 文章を書く部分です。セクションや図といった文書構造をLaTeX語（ **環境** というのかな）でマークアップします。


ドキュメントクラスの指定
==================================================

.. code-block:: latex

   \documentclass[dvipdfmx,12pt]{jsarticle}

* 日本語には ``jsarticle`` クラスを指定。他には ``jsreport`` 、``jsbook`` がある
* ドライバは ``dvipdfmx`` にする
* フォントサイズはお好みに指定

プリアンブルの設定
==================================================

* ``\documentclass`` から ``\begin{document}`` までのエリアを ``プリアンブル`` と呼ぶ
* パッケージ追加などのドキュメントの設定はここに追記する



パッケージの追加
==================================================

.. code-block:: latex

   \usepackage[utf8]{inputenc}    %% inputencパッケージ
   \usepackage[T1]{fontenc}       %% fontenc パッケージ

* パッケージ毎にさまざまなオプションがある
* オプションの詳細は各パッケージを調べる

.. code-block:: bash

   $ texdoc hyperref


目次の設定
==================================================

* ビルドされたPDFの目次にハイパーリンクを設定できる
* 目次が文字化けしないように ``hyperref`` と ``pxjahyper`` の2つのパッケージを読み込む必要がある


.. code-block:: latex

   \usepackage{hyperref}
   \usepackage{pxjahyper}


タイトル、著者などの設定
==================================================

.. code-block:: latex

   \author{Shota TAKAHASHI}
   \date{2016-01-14 Monday}
   \title{第一回打ち合わせ}

   \begin{document}

   \maketitle

   \end{document}


* プリアンブルの中に記述したあと、本文内で ``\maketitle`` する
* ``\date{\today}`` とすれば、コンパイルした日付になる。
