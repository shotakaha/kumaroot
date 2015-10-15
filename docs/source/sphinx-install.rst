==================================================
インストール
==================================================

Sphinxを使うために以下のものが必要です。
基本的に ``MacPorts`` を使ってインストールします。
MacPortsにポートがない場合は ``pip`` を使います。


必要なプログラム
==================================================

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


.. toctree::
   :maxdepth: 1

   sphinx-install-macports
   sphinx-install-pip
