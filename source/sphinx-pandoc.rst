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
