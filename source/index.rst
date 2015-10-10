.. KumaROOT documentation master file, created by
   sphinx-quickstart on Sat Jul 11 17:44:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to KumaROOT's documentation!

KumaROOT
==================================================

はじめに
==================================================

古巣の研究室に設置した `ShotakahaDokuWiki <http://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php>`__ にROOTなど研究に関する情報を書き貯めていましたのですが、いつまでも場所を借りているわけにはいかないので、そのうち消されてしまうかもしれません。

せっかくなのでどこかに残しておきたいのですが、いまの職場のサーバではPHPなどが一切動かず、DokuWikiをそのまま引っ越しすることができません。

いろいろ探した結果、Sphinxを使って文書を作成し、GitHubで管理・公開し、Read the Docs でHTMLを公開することにしました
ドキュメントに最新版については、動作するサンプルコードも作成していこうと思っています。

.. toctree::
   :maxdepth: 1

   preface-kuma
   preface-root
   preface-sphinx
   useful-links


ROOTの使い方
==================================================

.. toctree::
   :maxdepth: 1

   root-install
   root5-root6
   root-pyroot
   root-help
   root-tutorial
   root-global
   root-hist
   root-tree
   root-chain
   root-file
   root-string
   root-canvas


Emacsの使い方
==================================================

エディタはプログラミングを楽にするための道具です。
自分に合ったものを選ぶのが一番です。
その参考になるように、Emacsの簡単な使い方と、
便利なパッケージなどを紹介しておこうと思います。

.. toctree::
   :maxdepth: 1

   emacs-editor
   emacs-install
   emacs-prelude
   emacs-package
   emacs-org
   emacs-yatex
   emacs-magit
   emacs-twitter
   emacs-vim

Sphinxの使い方
==================================================

.. toctree::
   :maxdepth: 1

   sphinx


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
