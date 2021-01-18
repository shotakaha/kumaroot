==================================================
ドキュメントの生成（ビルド）
==================================================

例として、この文書（ ``KumaROOT`` ）をGitHubからクローンして、ビルドする方法です。
開発環境のセットアップに ``poetry`` を使っているので、予めインストールしておきます。

.. code-block:: bash

   $ pip3 install poetry


.. code-block:: bash

   $ git clone https://github.com/shotakaha/kumaroot.git
   $ cd kumaroot
   $ poetry install  ## 開発環境のセットアップ
   $ poetry shell    ## 開発環境の立ち上げ
   $ cd docs/
   $ make html        ## HTMLの生成
   $ make latexpdfja  ## PDFの生成


HTML文書のビルド
==================================================

HTML変換には ``make html`` を実行します。
変換ファイルは ``build/html/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make html
    $ open build/html/index.html



PDF文書のビルド
==================================================

.. note::

   ビルドする環境でLaTeXがきちんと使える必要があります

日本語を含む文書のPDF変換には ``make latexpdfja`` を実行します。
これは裏で ``platex`` / ``dvipdfmx`` を実行しているため、日本語もきちんと処理できます。
変換ファイルは ``build/latex/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf
