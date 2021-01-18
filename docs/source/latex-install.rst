==================================================
インストール
==================================================


つい最近までは「Mac LaTeX インストール」などでググると、なんだかまとまりのない情報で溢れていました。
しかし、現在はそれらを取りまとめようということで開発が進んでいるようで、これからはTeXLive一択で良いみたいです。
TeXLiveは年１回更新されます。


MacTeX
==================================================

MacOSXでLaTeXを使う場合は、これで決まりです。
`MacTeX <https://tug.org/mactex/>`__ からダウンロードできます。

TeX環境の本体であるTeXLiveと一緒に、TeX編集の統合環境であるTeXShopやTeXworks、
TeX関連のパッケージ管理ツールであるTeX Live Utilityがついてきます。
他にも、文献管理のBibDesk、スペルチェックのExcalibur、そして、
Keynoteに数式を貼り付けるのに必要なLaTeXiTがついてきます。

MacTeX (Homebrew)
==================================================

TeXLiveはHomebrewを使ってインストールできます。

.. code-block:: bash

   $ brew install --cask mactex



TeXLive (MacPorts)
==================================================

.. deprecated:: 2021-01-18
   だいぶ前にHomebrewを使う方法に変更しました

TeXLiveはMacPortsからインストールすることもできます。
特に理由がなければ ``texlive +full`` をインストールすればいいと思います。

.. code-block:: bash

   $ sudo port install texlive +full
