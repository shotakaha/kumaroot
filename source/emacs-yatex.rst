==================================================
YaTeXの使い方
==================================================

YaTeX（野鳥）はEmacsでLaTeX文書を作成するためのパッケージです。
ちょっと前までは ``Mercurial`` を使って手動でインストールするしかなかったのですが、最近は ``MELPA`` からインストールすることができます。

インストール（MELPA）
==================================================

.. code:: emacs

    M-x package-install RET yatex RET

インストール（Mercurial）
==================================================

:STEP1: Mercurialのインストール

.. code:: bash

    $ sudo port install mercurial +bash_completion +zsh_completion

:STEP2: YaTeXのリポジトリをチェックアウト

.. code:: bash

    $ cd ~/.emacs.d/
    $ hg clone http://www.yatex.org/hgrepos/yatex yatex

:STEP3: YaTeXリポジトリの更新

.. code:: bash

    $ cd ~/.emacs.d/yatex
    $ hg pull -u

:STEP4: Makefileの編集

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

.. list-table::
   :header-rows: 1

   * - 変数
     - 変更点
   * - PREFIX
     - :file:`/usr/local` から :file:`${HOME}/.emacs.d` に変更
   * - EMACS
     - :file:`/Applications/Emacs.app/Contents/MacOs/Emacs`
   * - EMACSDIR
     - :file:`${PREFIX}`
   * - LISPDIR
     - :file:`${EMACSDIR}/site-lisp/yatex`


:STEP5: YaTeXのインストール

.. code:: bash

    $ make install
    $ make install-info
    $ make install-yahtml



設定
==================================================


.. code-block:: elisp

   (use-package yatex
       :ensure t
       :mode (("\\.tex$" . yatex-mode))
       :bind (("C-c C-t" . YaTeX-typeset-menu))
       :config
       ;; automatically selected according to current language
       ;; (setq YaTeX-japan t)

       ;; change default kanji-code from 2:JIS to 4:UTF-8
       ;; (setq latex-message-kanji-code 4)
       ;; (setq YaTeX-kanji-code 4)
       ;; (setq YaTeX-coding-system 4)

       ;; declared in yatexlib.el
       (setq YaTeX-inhibit-prefix-letter t)
       ;; local dictionary is NOT needed
       (setq YaTeX-nervous nil)

       ;; declared in yatex.el
       (setq tex-command "ptex2pdf -l -ot -synctex=1 -file-line-error")
       (setq bibtex-command "pbibtex")
       (setq dvi2-command "open -a Preview")    ;; use Preview.app
       (setq tex-pdfview-command "open -a Preview")
       (setq dviprint-command-format "dvipdfmx %s")
       (setq YaTeX-skip-default-reader t)
       (setq YaTeX-simple-messages t)
       ;; (setq YaTeX-template-file "...")
       )
