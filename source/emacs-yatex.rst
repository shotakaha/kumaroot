Emacs + YaTeXの使い方
=====================

YaTeX（野鳥）はEmacsでLaTeX文書を作成するための環境のこと。
少し前までは、 ``Mercurial`` を使ってインストールするしかなかったが、
いまは ``MELPA`` からインストールすることができる。

YaTeXのインストール
-------------------

MELPAを使ったインストール方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: emacs

    M-x package-install RET yatex RET

Mercurialを使ったインストール方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STEP1
    Mercurialのインストール

.. code:: bash

    $ sudo port install mercurial +bash_completion +zsh_completion

STEP2
    YaTeXのリポジトリをチェックアウト

.. code:: bash

    $ cd ~/.emacs.d/
    $ hg clone http://www.yatex.org/hgrepos/yatex yatex

STEP3
    YaTeXリポジトリの更新

.. code:: bash

    $ cd ~/.emacs.d/yatex
    $ hg pull -u

STEP4
    Makefileの編集

.. code:: bash

    $ cd ~/.emacs.d/yatex
    $ make
    Edit this makefile first.
    Type "make install" to install YaTeX.
    Type "make install-yahtml" to install yahtml.
    If you cling to elc files. type "make elc" before make install

    $ emacs makefile

    ## ---------- < editing makefile > ----------
    ...
    # Edit these variables to be suitable for your site
    #PREFIX  = /usr/local     ## comment out or modify
    PREFIX  = ${HOME}/.emacs.d  ## set your .emacs.d directory

    ...
    ## CarbonEmacs on Darwin (Sample)
    EMACS  = /Applications/Emacs.app/Contents/MacOS/Emacs   ## uncomment
    # PREFIX = /Applications/Emacs.app/Contents/Resources
    EMACSDIR = ${PREFIX}                                    ## uncomment

    LISPDIR = ${EMACSDIR}/site-lisp/yatex
    # LISPDIR   = ${EMACSDIR}/site-packages/lisp/yatex
    DOCDIR  = ${LISPDIR}/docs
    HELPDIR = ${EMACSDIR}/site-lisp
    INFODIR = ${PREFIX}/info
    ...
    ## ---------- < save changes > ----------

+------------+----------------------------------------------------+
| PREFIX     | ``/usr/local`` から ``${HOME}/.emacs.d`` に変更    |
+------------+----------------------------------------------------+
| EMACS      | ``/Applications/Emacs.app/Contents/MacOs/Emacs``   |
+------------+----------------------------------------------------+
| EMACSDIR   | ``${PREFIX}``                                      |
+------------+----------------------------------------------------+
| LISPDIR    | ``${EMACSDIR}/site-lisp/yatex``                    |
+------------+----------------------------------------------------+

STEP5
    YaTeXのインストール

.. code:: bash

    STEP5
    $ make install
    $ make install-info
    $ make install-yahtml

