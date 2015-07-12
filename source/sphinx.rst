Sphinxの使い方
==============

このドキュメントを生成している ``Sphinx`` の使い方についてのメモです。

ワークフロー
------------

#. Orgモードで文章を作成（ただし ``QuickLook`` できるように ``.txt形式`` で保存）
#. ``pandoc`` を使って ``reST形式`` に変換
#. ``Sphinx`` を使って HTML と PDFに変換



pandocコマンドの使い方
----------------------

OrgのreSTエクスポート（ ``ox-rst`` ）が、うまくいかないので ``pandoc`` を使って変換している。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc -f org -t rst source/FILENAME.txt -o source/FILENAME.rst

おためしワンライナー。これをMakefileに書いておけばいいのかもしれない。

.. code-block:: bash

    $ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done



PDF変換
-------

PDFの変換には、pdflatex／dvipdfmxを使う。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf



HTML変換
--------

.. code-block:: bash

    $ cd $KUMAROOT
    $ make html
    $ open build/html/index.html



conf.pyの設定
-------------

HTMLやPDF変換に必要な設定をしておく。



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

上の ``latex_elements``
の中で複数のパッケージを書くと見た目がカッコ悪いので、 以下のように
``latex_elements['preamble']`` に直接追加することにした。

.. code-block:: python

    latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
    latex_elements['preamble'] += '\\usepackage{graphics}\n'



LaTeXのドキュメントクラスの設定（ ``latex_docclass`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``latex_documents`` はデフォルトのままにしておき、 ``latex_docclass``
を変更する。

.. code-block:: python

    latex_docclass = {'manual' : 'jsbook'}



LaTeXの表紙の設定（ ``latex_logo`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

表紙に挿入する絵の設定。 必要ないなら ``None``
（デフォルト値）にしておけばよい。

.. code-block:: python

    # The name of an image file (relative to this directory)
    # to place at the top of the title page.
    latex_logo = './images/toumin_kuma.png'



HTMLテーマの設定
~~~~~~~~~~~~~~~~

まず、 ``pip`` を使って ``sphinx_bootstrap_theme`` をインストールする。
登録されているパッケージ名は ``sphinx-bootstrap-theme``
（ハイフンでつないである）という、
ちょっとしたトラップがある（そのうち直るのかな？）

インストール時にエラーが出たので、エラーメッセージに従って、 ``sudo -H``
を使って実行した。

.. code-block:: python

    $ sudo -H pip install sphinx-bootstrap-theme

`Installation <https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#installation>`__
の通りに、 ``html_theme`` 、 ``html_theme_path`` を設定する。

.. code-block:: python

    import sphinx_bootstrap_theme
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

``html_theme_options`` は `Theme
options <https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#theme-options>`__
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
