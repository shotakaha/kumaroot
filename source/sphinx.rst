.. toctree::

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


KumaROOTの生成（ビルド）
==================================================

.. code-block:: bash

   git clone https://github.com/shotakaha/kumaroot.git
   cd kumaroot
   make html        ## HTMLの生成
   make latexpdfja  ## PDFの生成

たぶんこのままじゃビルドできないので、必要なものを追加でインストールします。


必要なものとインストール方法
--------------------------------------------------

Sphinxを使うために以下のものが必要です。
ここでのインストールには ``MacPorts`` を使用します。
MacPortsにポートがない場合は ``pip`` を使います。

#. ``python`` （MacPorts）
#. ``Sphinx`` （MacPorts）
#. ``pip`` （MacPorts)
#. ``sphinx-bootstrap-theme`` （pip）
#. ``pandoc`` （MacPorts、オプショナル）

``python`` のバージョンに合わせて ``Sphinx`` と ``pip`` のバージョンを決めます。
``port select`` で簡単に切り替えることができるので、両方インストールしても大丈夫です。

``pandoc`` は文書フォーマット変換コマンドです。
Sphinxとは直接関係がありませんが、
既存の文書（HTMLだったり、Orgだったり）を
reSTに変換したいときにあると便利です。


MacPortsを使ったインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx-bootstrap-theme`` 以外は ``MacPorts`` でインストールします。
``variants`` は特にありません。

.. code-block:: bash

   $ sudo port install python27     ## or python34
   $ sudo port install py27-sphinx  ## or py34-sphinx
   $ sudo port install py27-pip     ## or py34-pip
   $ sudo port install pandoc

MacPortsを使ったバージョンの切り替え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上記のように使用する ``pip`` をセットしてから ``pip install`` します。
``/opt/local/Library/Frameworks/Python.framework/Versions/バージョン/lib/pythonバージョン/site-packages/``
以下にインストールされるため ``sudo`` が必要になるはずです。
それでもエラーが出る場合は、エラーメッセージに従うか、ググってください [1]_ 。

.. code-block:: bash

   $ sudo pip install sphinx-bootstrap-theme
   ## sudo -H pip install sphinx-bootstrap-theme


HTML文書のビルド
--------------------------------------------------

HTML変換には ``make html`` を実行します。
変換ファイルは ``build/html/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make html
    $ open build/html/index.html



PDF文書のビルド
--------------------------------------------------

日本語を含む文書のPDF変換には ``make latexpdfja`` を実行します。
これは裏で ``platex`` / ``dvipdfmx`` を実行しているため、
日本語もきちんと処理できます [3]_ 。
変換ファイルは ``build/latex/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf


conf.pyの設定
==================================================

ドキュメントの全体設定は ``conf.py`` で行います。
ここでは、HTML文書とPDF文書に必要な設定をしておきます。

PDF文書の設定
--------------------------------------------------

PDF文書の生成にはLaTeXを使います。
そのため、使いたいLaTeXパッケージなどの設定が主になります。

LaTeXのドキュメントクラスの設定（ ``latex_docclass`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``latex_documents`` はデフォルトのままにしておき、
``latex_docclass`` を変更します。

.. code-block:: python

    latex_docclass = {'manual' : 'jsbook'}



ドキュメントクラスオプションの設定（ ``latex_elements`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ドキュメントクラス（ ``\documentclass`` ）のオプションを設定する部分です。
プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけして、中身はあとで書くことにします。


.. code-block:: python

    latex_elements = {
        'papersize' = 'a4paper',
        'pointsize' = '12pt',
        'preamble': '',    # あとで追加するので定義だけしておく
        'figure_align': 'htbp',
    #   'fontpkg': '\\usepackage{times}',
    }


``LaTeX`` 文書の出力は以下のようになります。

.. code-block:: latex

   \documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}



プリアンブルの追加（ ``latex_elements['preamble']`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上の ``latex_elements`` の中で複数のパッケージを書くと見た目がカッコ悪いので、
以下のように ``latex_elements['preamble']`` に直接追加することにしました。

.. code-block:: python

    latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
    latex_elements['preamble'] += '\\usepackage{graphics}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
    latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
    latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'

``LaTeX`` 文書の出力は以下のようになります。

.. code-block:: latex

   \usepackage{pxjahyper}
   \usepackage{graphics}
   \hypersetup{bookmarksopen=true}
   \hypersetup{bookmarksopenlevel=2}
   \hypersetup{colorlinks=true}
   \hypersetup{pdfpagemode=UseOutlines}


表紙の設定（ ``latex_logo`` ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

表紙が寂しい場合、ロゴを挿入することもできます。
必要ないなら ``None`` （デフォルト値）にしておけばよいです。

.. code-block:: python

    # The name of an image file (relative to this directory)
    # to place at the top of the title page.
    latex_logo = './images/toumin_kuma.png'



HTML文書の設定
--------------------------------------------------

テーマの設定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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





pandocコマンドの使い方
==================================================

``Org`` や ``Markdown`` をすでに使っている場合、
新しく ``reST`` の書式を覚えるのは少しめんどくさいです。
そのような場合、``pandoc`` コマンドがあれば、以下のようなワークフローを考えることができます。

#. Orgモードで文章を作成（ただし ``QuickLook`` できるように ``.txt形式`` で保存）
#. ``pandoc`` を使って ``reST形式`` に変換
#. ``Sphinx`` を使って HTML と PDFに変換

以下では ``Org`` と ``HTML`` から ``reST`` に変換する例を挙げておきます。
残念ながらWordファイル（ ``doc`` or ``docx`` ）を ``reST`` に直接変換することはできませんが [2]_ 、
Word から HTML に書き出せば ``reST`` に変換することができます。


Org から reST への変換
--------------------------------------------------

``Org`` には ``reST`` エクスポート（ ``ox-rst`` ）があるのですが、
なぜかうまく働かないので ``pandoc`` を使って変換します。
今回の場合、Org文書の拡張子が ``.txt`` なので
``-f org`` を使って ``pandoc`` に入力フォーマットを教えています。
出力ファイルは拡張子で reST形式（ ``-o FILENAME.rst`` ）と分かるので、
出力フォーマットを指定する必要はありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc -f org source/FILENAME.txt -o source/FILENAME.rst

毎回、手動で変換するのが面倒くさいのでワンライナーを書いてみました。
これを ``Makefile`` に書いておけばいいのかもしれないです。

.. code-block:: bash

    $ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done


HTML から reST への変換
--------------------------------------------------

Org から reST形式への変換ができれば簡単にできます。
この場合は、入力フォーマットも出力フォーマットも、ファイル形式を見れば分かるので、
オプションは必要ありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc source/FILENAME.html -o source/FILENAME.rst


.. [1]
   僕の場合は ``sudo -H`` する必要がありました

.. [2]
   逆はできるみたいです

.. [3]
   ビルドする環境でLaTeXがきちんと使える必要があります
