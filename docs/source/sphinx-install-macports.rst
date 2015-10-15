==================================================
MacPortsを使う方法
==================================================

``sphinx-bootstrap-theme`` 以外は ``MacPorts`` でインストールします。
``variants`` は特にありません。

.. code-block:: bash

   $ sudo port install python27     ## or python34
   $ sudo port install py27-sphinx  ## or py34-sphinx
   $ sudo port install py27-pip     ## or py34-pip
   $ sudo port install pandoc

MacPortsを使ったバージョンの切り替え
--------------------------------------------------

それぞれのパッケージのバージョン切り替えは ``port select`` を使って行います。
切り替えることができるパッケージ名、バージョンは ``port select --summary`` で確認できます。
``python`` に関しては ``python2`` と ``python3`` もあるので、
とりあえず設定しておきます。

.. code-block:: bash

   $ port select --summary
   $ sudo port select python python27  ## or python34
   $ sudo port select python2 python27
   $ sudo port select python3 python34

   $ sudo port select sphinx py27-sphinx  ## or py34-sphinx

   $ sudo port select pip pip27  ## or pip34
