==================================================
インストール
==================================================

Sphinxには以下のプログラムが必要です。

#. ``python`` （Homebrew）
#. ``pip`` （pythonについてくる)
#. ``sphinx`` （pip）
#. ``sphinx_rtd_theme`` （pip）
#. ``pandoc`` （Homebrew、オプショナル）


``sphinx`` 本体をはじめ、いくつかのパッケージは Homebrew と pip の両方にあります。
しかし両方インストールしようとすると、どっちかでエラーがでます。
基本的に :command:`pip` コマンドでインストールすることにします。


Python
==================================================

.. code-block:: bash

   $ brew install python@3.9

pip
==================================================

.. code-block:: bash

   $ pip3 install -U pip


Sphinx
==================================================

.. code-block:: bash

   $ pip3 install sphinx


sphinx_rtd_theme
==================================================

.. code-block:: bash

   $ pip3 install sphinx_rtd_theme


pandoc
==================================================

``pandoc`` は文書フォーマット変換コマンドです。
Sphinxとは直接関係がありませんが、既存の文書（HTMLだったり、Orgだったり）を
reSTに変換したいときにあると便利です。


.. code-block:: bash

   $ brew install pandoc
