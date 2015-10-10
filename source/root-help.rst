==================================================
EmacsでROOTを編集したい
==================================================

あまり知られていないのかもしれませんが、EmacsでROOTマクロのコーディングを補助するパッケージ :file:`root-help.el` が一緒にインストールされています。

とりあえず :command:`locate` コマンドでどこにあるか調べておきましょう。
  ちなみに、僕の場合（＝MacPortsの場合）、以下にありました。


  .. code-block:: bash

     $ locate root-help.el    # check path
     ## ROOT5 => /opt/local/libexec/root5/share/emacs/site-lisp/root-help.el
     ## ROOT6 => /opt/local/libexec/root6/share/emacs/site-lisp/root-help.el

.. note::

   これの使い方に関しては、あとできちんと調べて書くことにします。
