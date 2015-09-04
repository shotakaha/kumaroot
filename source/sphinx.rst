==================================================
Sphinxの使い方
==================================================

``Sphinx`` とは、
テキスト文書をreST形式で作成しておけば、
良きように噛み砕いてくれ、PDFやHTMLやその他のフォーマットへと出力してくれるツールです。

元々、Pythonのドキュメント生成のために開発されたので、中身はPythonで書かれています。
そのため、Pythonを知っていればある程度カスタマイズすることができます。

実はこのドキュメントも ``Sphinx`` を使って生成しています。
どんなものか、気軽に試したい方は、このリポジトリをクローンするとよいでしょう。


KumaROOTを生成してみる
==================================================

.. code-block:: bash

   git clone https://github.com/shotakaha/kumaroot.git
   cd kumaroot
   make html        ## HTMLの生成
   make latexpdfja  ## PDFの生成

たぶんこのままじゃ動かないので Sphinx など必要なものを追加でインストールします。


Sphinxのインストール
--------------------------------------------------


ワークフロー
------------

#. Orgモードで文章を作成（ただし ``QuickLook`` できるように ``.txt形式`` で保存）
#. ``pandoc`` を使って ``reST形式`` に変換
#. ``Sphinx`` を使って HTML と PDFに変換


使うための準備
--------------------

Sphinxを使うために以下のものをインストールします。
インストールには ``MacPorts`` を使用しました。
MacPortsにポートがない場合は ``pip`` を使います。

#. ``python`` （MacPorts）
#. ``Sphinx`` （MacPorts）
#. ``pip`` （MacPorts)
#. ``sphinx-bootstrap-theme`` （pip）
#. ``pandoc`` （MacPorts、オプショナル）

``python`` のバージョンに合わせて
``Sphinx`` と ``pip`` のバージョンを決めます。
``port select`` で簡単に切り替えることができるので、
両方インストールしても大丈夫です。

``pandoc`` は文書フォーマット変換コマンドです。
Sphinxとは直接関係がありませんが、
既存の文書（HTMLだったり、Orgだったり）を
reSTに変換したいときにあると便利です。


MacPortsを使ったインストールとバージョンの切り替え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx-bootstrap-theme`` 以外は ``MacPorts`` でインストールします。
``variants`` は特にありません。

.. code-block:: bash

   $ sudo port install python27     ## or python34
   $ sudo port install py27-sphinx  ## or py34-sphinx
   $ sudo port install py27-pip     ## or py34-pip
   $ sudo port install pandoc


それぞれのパッケージのバージョン切り替えは ``port select`` を使って行います。
切り替えることができるパッケージ名、バージョンは ``port select --summary`` で確認できます。
``python`` に関しては ``python2`` と ``python3`` もあるので、
とりあえず設定しておきます。

.. code-block:: bash

   $ port select --summary
   $ sudo port select python python27  ## or python34
   $ sudo port select python2 python27
   $ sudo port select python3 python34

   $ sudo port select sphinx py27-sphinx  ## or py34-sphinx

   $ sudo port select pip pip27  ## or pip34



pipを使ったインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上記のように使用する ``pip`` をセットしてから ``pip install`` します。
``/opt/local/Library/Frameworks/Python.framework/Versions/バージョン/lib/pythonバージョン/site-packages/``
以下にインストールされるため ``sudo`` が必要になるはずです。
それでもエラーが出る場合は、エラーメッセージに従うか、ググってください [1]_ 。

.. code-block:: bash

   $ sudo pip install sphinx-bootstrap-theme
   ## sudo -H pip install sphinx-bootstrap-theme


pandocコマンドの使い方
----------------------

``Org`` と ``HTML`` からから ``reST`` に変換する例を挙げておきます。
残念ながらWordファイル（ ``doc`` or ``docx`` ）を ``reST`` に直接変換することはできません [2]_ 。
しかし、Word から HTML に書き出せば ``reST`` に変換することができます。


Org から reST への変換
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OrgのreSTエクスポート（ ``ox-rst`` ）がうまく動かないので ``pandoc`` を使って変換します。
今回の場合、Org文書の拡張子が ``.txt`` なので
``-f org`` を使って ``pandoc`` に入力フォーマットを教えています。
出力ファイルが reST形式（ ``-o FILENAME.rst`` ）なので、
出力フォーマットを指定する必要はありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc -f org source/FILENAME.txt -o source/FILENAME.rst

毎回、手動で変換するのが面倒くさいのでワンライナーを書いてみました。
これを ``Makefile`` に書いておけばいいのかもしれない。

.. code-block:: bash

    $ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done


HTML から reST への変換
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Org から reST形式への変換ができれば簡単にできます。
この場合は、入力フォーマットも出力フォーマットも、ファイル形式を見れば分かるので、
オプションは必要ありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc source/FILENAME.html -o source/FILENAME.rst


PDF変換
-------

日本語を含む文書のPDF変換には ``make latexpdfja`` を実行します。
これは裏で ``platex`` / ``dvipdfmx`` を実行しているため、
日本語もきちんと処理できます [3]_ 。
変換ファイルは ``build/latex/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf


HTML変換
--------

HTML変換には ``make html`` を実行します。
変換ファイルは ``build/html/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make html
    $ open build/html/index.html



conf.pyの設定
-------------

HTMLやPDF変換に必要な設定をしておきます。


LaTeXドキュメントの設定（ ``latex_elements`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    latex_elements = {
        'papersize' = 'a4paper',
        'pointsize' = '12pt',
        'preamble': '',    # あとで追加するので定義だけしておく
        'figure_align': 'htbp',
    #   'fontpkg': '\\usepackage{times}',
    }



プリアンブルの追加（ ``latex_elements['preamble']`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上の ``latex_elements`` の中で複数のパッケージを書くと見た目がカッコ悪いので、
以下のように ``latex_elements['preamble']`` に直接追加することにしました。

.. code-block:: python

    latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
    latex_elements['preamble'] += '\\usepackage{graphics}\n'



LaTeXのドキュメントクラスの設定（ ``latex_docclass`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``latex_documents`` はデフォルトのままにしておき、
``latex_docclass`` を変更する。

.. code-block:: python

    latex_docclass = {'manual' : 'jsbook'}



LaTeXの表紙の設定（ ``latex_logo`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

表紙に挿入する絵の設定。
必要ないなら ``None`` （デフォルト値）にしておけばよい。

.. code-block:: python

    # The name of an image file (relative to this directory)
    # to place at the top of the title page.
    latex_logo = './images/toumin_kuma.png'



HTMLテーマの設定
~~~~~~~~~~~~~~~~

まず、 ``pip`` を使って ``sphinx_bootstrap_theme`` をインストールする。
登録されているパッケージ名は
``sphinx-bootstrap-theme`` （ハイフンでつないである）という、
ちょっとしたトラップがある。

インストール時にエラーが出たので、
エラーメッセージに従って、 ``sudo -H`` を使って実行した。

.. code-block:: python

    $ sudo -H pip install sphinx-bootstrap-theme

`Installation <https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#installation>`__
の通りに ``html_theme`` と ``html_theme_path`` を設定する。

.. code-block:: python

    import sphinx_bootstrap_theme
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

``html_theme_options`` は
`Theme options <https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#theme-options>`__
をとりあえずコピペして、 いろいろテストしてみる。

.. code-block:: python

    html_theme_options = {
        # Navigation bar title. (Default: ``project`` value)
        # 'navbar_title': "Demo",

        # Tab name for entire site. (Default: "Site")
        # 'navbar_site_name': "Site",

        # A list of tuples containing pages or urls to link to.
        # Valid tuples should be in the following forms:
        #    (name, page)                 # a link to a page
        #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
        #    (name, "http://example.com", True) # arbitrary absolute url
        # Note the "1" or "True" value above as the third argument to indicate
        # an arbitrary url.
        # 'navbar_links': [
        #     ("Examples", "examples"),
        #     ("Link", "http://example.com", True),
        # ],

        # Render the next and previous page links in navbar. (Default: true)
        'navbar_sidebarrel': True,

        # Render the current pages TOC in the navbar. (Default: true)
        'navbar_pagenav': True,

        # Tab name for the current pages TOC. (Default: "Page")
        'navbar_pagenav_name': "Page",

        # Global TOC depth for "site" navbar tab. (Default: 1)
        # Switching to -1 shows all levels.
        'globaltoc_depth': 2,

        # Include hidden TOCs in Site navbar?
        #
        # Note: If this is "false", you cannot have mixed ``:hidden:`` and
        # non-hidden ``toctree`` directives in the same page, or else the build
        # will break.
        #
        # Values: "true" (default) or "false"
        'globaltoc_includehidden': "true",

        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        'navbar_class': "navbar navbar-inverse",

        # Fix navigation bar to top of page?
        # Values: "true" (default) or "false"
        'navbar_fixed_top': "true",

        # Location of link to source.
        # Options are "nav" (default), "footer" or anything else to exclude.
        'source_link_position': "nav",

        # Bootswatch (http://bootswatch.com/) theme.
        #
        # Options are nothing (default) or the name of a valid theme
        # such as "amelia" or "cosmo".
        # 'bootswatch_theme': "united",
        # 'bootswatch_theme': "cosmo",

        # Choose Bootstrap version.
        # Values: "3" (default) or "2" (in quotes)
        'bootstrap_version': "3",
    }


.. [1]
   僕の場合は ``sudo -H`` する必要がありました

.. [2]
   逆はできるみたいです

.. [3]
   ビルドする環境でLaTeXがきちんと使える必要があります
