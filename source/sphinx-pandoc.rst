==================================================
pandocコマンドの使い方
==================================================

``Org`` や ``Markdown`` をすでに使っている場合、 ``reST形式`` の書式を新しく覚えるのは、やはりめんどうです。
そのような場合 :command:`pandoc` コマンドがあれば、以下のようなワークフローを考えることができます。

#. Orgモードで文章を作成（ただし ``QuickLook`` できるように ``.txt形式`` で保存）
#. ``pandoc`` を使って ``reST形式`` に変換
#. ``Sphinx`` を使って HTML と PDFに変換

.. caution::

   複数のマシンを使う場合、環境の構築に手間がかかったりするので ``reST形式`` を覚える方が近道だったりします。


以下では ``Org`` と ``HTML`` から ``reST`` に変換する例を挙げておきます。
残念ながらWordファイル（ ``doc`` or ``docx`` ）を ``reST`` に直接変換することはできませんが [#]_ 、
Word から HTML に書き出せば ``reST`` に変換することができます。

.. [#]
   逆（rest -> Word）はできるみたいです




Org から reST への変換
==================================================

``Org`` には ``reST`` エクスポート（ ``ox-rst`` ）があるのですが、なぜかうまく働かないので :command:`pandoc` を使って変換します。
今回の場合、Org文書の拡張子が ``.txt`` なので ``-f org`` を使って :command:`pandoc` に入力フォーマットを教えています。
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
==================================================

Org から reST形式への変換ができれば簡単にできます。
この場合は、入力フォーマットも出力フォーマットも、ファイル形式を見れば分かるので、
オプションは必要ありません。

.. code-block:: bash

    $ cd $KUMAROOT
    $ pandoc source/FILENAME.html -o source/FILENAME.rst
