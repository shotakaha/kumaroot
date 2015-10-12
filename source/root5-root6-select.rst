==================================================
バージョンの切り替え
==================================================


現在使っているROOTバージョンの確認
==================================================

.. code-block:: bash

   $ port select --list root
   Available versions for root:
	none
	root5
	root6 (active)


ROOT6への切り替え
==================================================

.. code-block:: bash

    $ sudo port select root root6   ## use ROOT6

ROOT5への切り替え
==================================================

.. code-block:: bash

    $ sudo port select root root5   ## use ROOT5


:command:`port select` コマンド
==================================================

実はこの :command:`port select` はROOTだけでなく、Pythonのバージョン切り替えなどもできます。
どのパッケージが使えるかは以下のコマンドで確認できます

.. code-block:: bash

    $ port select --summary
