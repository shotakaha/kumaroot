==================================================
PyROOTを使いたい
==================================================

``PyROOT`` というモジュールを使えば、Python上でROOTが使えます。
その場合は、MacPortsでインストールする際に ``variants`` で ``+pythonXX`` を指定すればよいです。

.. code-block:: bash

    $ sudo port install root5 +python27   ## when ROOT5, you need to specify +pythonXX variants
    $ sudo port install root6             ## when ROOT6, no need to specify variants


ただし、この ``variants`` は自分の使っているPythonのバージョンに合わせる必要があります。
ミスマッチな場合は、動作せず、クラッシュします。

``ROOT6`` の場合は ``python27`` がデフォルトでONになっています。

他にも `rootpy <http://www.rootpy.org>`__ というのもあります。
こっちのほうがPython nativeな感じです。
前に試そうとしてたのですがインストールでコケてしまいました。
動かせたら項目を作るかも。
