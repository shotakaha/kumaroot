==================================================
インストール
==================================================

Sphinxには以下のプログラムが必要です。

#. ``python`` （MacPorts）
#. ``Sphinx`` （MacPorts）
#. ``pip`` （MacPorts)
#. ``sphinx_rtd_theme`` （MacPorts）
#. ``pandoc`` （MacPorts、オプショナル）


``sphinx`` 本体をはじめ、いくつかのパッケージは MacPorts と pip の両方にあります。
しかし両方インストールしようとすると、どっちかでエラーがでます。
なので、基本的に ``MacPorts`` からインストールし、
そこにない場合は ``pip`` を使うことにします。


また ``Sphinx`` と ``pip`` のバージョンは ``python`` のバージョンに合わせます。
ここでは ``python34`` と ``python27`` の両方をインストールし、
``port select`` を使って ``python34`` にしています。



Python
==================================================

.. code-block:: bash

   $ sudo port install python27
   $ sudo port install python34
   $ sudo port select python python34




Sphinx
==================================================

.. code-block:: bash

   $ sudo port install py27-sphinx
   $ sudo port install py34-sphinx
   $ sudo port select sphinx py34-sphinx

pip
==================================================

.. code-block:: bash

   $ sudo port install py27-pip
   $ sudo port install py34-pip
   $ sudo port select pip py34-pip


sphinx_rtd_theme
==================================================

.. code-block:: bash

   $ sudo port install py27-sphinx_rtd_theme
   $ sudo port install py34-sphinx_rtd_theme



pandoc
==================================================

``pandoc`` は文書フォーマット変換コマンドです。
Sphinxとは直接関係がありませんが、既存の文書（HTMLだったり、Orgだったり）を
reSTに変換したいときにあると便利です。


.. code-block:: bash

   $ sudo port install pandoc
