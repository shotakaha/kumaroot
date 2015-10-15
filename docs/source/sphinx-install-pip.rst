==================================================
pipを使う方法
==================================================

上記のように使用する ``pip`` をセットしてから ``pip install`` します。
``/opt/local/Library/Frameworks/Python.framework/Versions/バージョン/lib/pythonバージョン/site-packages/``
以下にインストールされるため ``sudo`` が必要になるはずです。

.. code-block:: bash

   $ sudo pip install sphinx-bootstrap-theme
   ## sudo -H pip install sphinx-bootstrap-theme

エラーが出る場合は、エラーメッセージに従うか、ググってください [#]_ 。

.. [#]
   僕の場合は :command:`sudo -H` が必要でした
