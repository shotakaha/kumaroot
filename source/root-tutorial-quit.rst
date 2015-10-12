==================================================
ROOTの終了（ :command:`.q` ）
==================================================

.. code-block:: bash

    root [0] .q


ROOTセッション内で :kbd:`.q` を入力すると終了します。
自作のROOTマクロのエラーのなどで :kbd:`.q` で終了できないときは、 :kbd:`.qqq...` の様に :kbd:`q` をたくさんにします。

:file:`$TUTORIALS` で起動したROOTセッションを終了すると :numref:`fig-root-quit` のようになり、起動時と同じく、なにやらメッセージが表示されています。
これは同じディレクトリに :file:`rootlogoff.C` というファイルがあるためです。

.. _fig-root-quit:
.. figure:: ./root-tutorial/root-quit.png
   :align: center

   チュートリアルのあるディレクトリでCINTを終了したときの画面表示
