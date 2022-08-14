==================================================
はじめに
==================================================

こんにちは、くま です。

高エネルギー物理学の実験で必要だったROOTなどのソフトの使い方に関するメモを `ShotakahaDokuWiki <hepsrv_>`_ に書き貯めていたのですが、2014年に研究室を離れたためいつまでも古巣のスペースを間借りしているわけにはいかず、内容の引っ越しをちまちまと実行中です。

いまの職場のサーバではPHPなどが一切動かず、DokuWikiをそのまま引っ越しすることができなかったため、いろいろ検討した結果、Sphinxを使って文書を作成し、GitHubで管理・公開し、Read the Docs でHTMLを公開することにしました。
引っ越し版については、動作するサンプルコードも作成していこうと思っています。

.. toctree::
   :maxdepth: 1

   preface-kuma
   preface-sphinx
   disclaimer


.. _hepsrv: http://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php

.. todo::

   内容が古くなってきたので更新する

   #. 現在は ``MacPorts`` ではなく ``Homebrew`` （:command:`brew` コマンド）で管理している
   #. ``ROOT`` は最近使ってない（ ``ROOT6`` のことは分からないので、この部分は更新できない）
   #. ``Emacs`` から ``Visual Studio Code`` に乗り換えた
   #. ``Sphinx`` の使い方も見直したい（ ``Python2`` 系の記述は古いので、全部 ``Python3`` 系に読み替えてください）
   #. 日本語ドキュメントは ``LuaLaTeX`` への移行を検討中
