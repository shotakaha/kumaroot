==================================================
日本語とLaTeX
==================================================

日本語はマルチバイトコードであるため、LaTeXでコンパイルするのが難しかったみたいです。
それに対処する歴史的な紆余曲折から日本語版LaTeXにはさまざまな派生品が存在します。
この歴史の詳細に関しては、三重大学の奥村さんのウェブサイトをはじめ、ググってみるとよいでしょう。


2020年ころの話
==================================================

日本語のLaTeX文書の作成には ``(u)pLaTeX + dvipdfmx`` もしくは ``LuaLaTeX`` を使うのがよいです。
特に ``LuaLaTeX`` はDVIファイルを作成せずに、PDFファイルを作ってくれます。おすすめです。

.. code-block:: bash

   $ lualatex hoge.tex


2015年ころの話
==================================================

.. deprecated:: 2021-01-18

   pLaTeXを使うのは少し昔の話。2020年からはLuaLaTeXを使うのがおすすめです。


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
