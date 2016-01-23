==================================================
日本語とLaTeX
==================================================

日本語はマルチバイトコードであるため、LaTeXでコンパイルするのが難しかったみたいです。
それに対処する歴史的な紆余曲折から日本語版LaTeXにはさまざまな派生品が存在します。
この歴史の詳細に関しては、三重大学の奥村さんのウェブサイトをはじめ、ググってみるとよいでしょう。

日本語のLaTeX文書の作成には ``pLaTeX`` と ``dvipdfmx`` を使えばよいです。
:command:`platex` コマンドでLaTeX文書をコンパイルしDVIファイルを作成、
:command:`dvipdfmx` コマンドでDVIファイルをPDFファイルに変換します。

.. code-block:: bash

   $ platex hoge.tex
   $ dvipdfmx hoge.dvi

これをまとめてやってくれるのが :command:`ptex2pdf` コマンドで、
（おそらく）MacTeXをインストールすると勝手についてきます。
ただのシェルスクリプト（Luaで書かれてるみたい）なので、
気になる人は中を見てみるとよいでしょう。

.. code-block:: bash

   $ where ptex2pdf
   /Library/TeX/texbin/ptex2pdf

   $ less /Library/TeX/texbin/ptex2pdf
