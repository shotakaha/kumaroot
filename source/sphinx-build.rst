==================================================
ドキュメントの生成（ビルド）
==================================================

この文書（ ``KumaROOT`` ）をGitHubからクローンして、ビルドする方法です。

.. code-block:: bash

   $ git clone https://github.com/shotakaha/kumaroot.git
   $ cd kumaroot
   $ make html        ## HTMLの生成
   $ make latexpdfja  ## PDFの生成

ただし、このままじゃビルドできないので、必要なものを追加でインストールします。


必要なものとインストール方法
==================================================

Sphinxを使うために以下のものが必要です。
基本的に ``MacPorts`` を使ってインストールします。
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


インストール（MacPorts）
==================================================

``sphinx-bootstrap-theme`` 以外は ``MacPorts`` でインストールします。
``variants`` は特にありません。

.. code-block:: bash

   $ sudo port install python27     ## or python34
   $ sudo port install py27-sphinx  ## or py34-sphinx
   $ sudo port install py27-pip     ## or py34-pip
   $ sudo port install pandoc

MacPortsを使ったバージョンの切り替え
--------------------------------------------------

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



インストール（pip）
==================================================

上記のように使用する ``pip`` をセットしてから ``pip install`` します。
``/opt/local/Library/Frameworks/Python.framework/Versions/バージョン/lib/pythonバージョン/site-packages/``
以下にインストールされるため ``sudo`` が必要になるはずです。
それでもエラーが出る場合は、エラーメッセージに従うか、ググってください [1]_ 。

.. code-block:: bash

   $ sudo pip install sphinx-bootstrap-theme
   ## sudo -H pip install sphinx-bootstrap-theme


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

日本語を含む文書のPDF変換には ``make latexpdfja`` を実行します。
これは裏で ``platex`` / ``dvipdfmx`` を実行しているため、
日本語もきちんと処理できます [3]_ 。
変換ファイルは ``build/latex/`` 以下に作成されます。

.. code-block:: bash

    $ cd $KUMAROOT
    $ make latexpdfja
    $ open build/latex/KumaROOT.pdf
