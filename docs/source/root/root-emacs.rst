==================================================
ROOT + Emacs
==================================================

あまり知られていないのかもしれませんが、EmacsでROOTマクロのコーディングを補助する :file:`root-help.el` というパッケージがあります。
ROOTと一緒にインストールされるので、とりあえず :command:`locate` コマンドでどこにあるか調べておきましょう。
ちなみに、僕の場合（＝MacPortsの場合）、以下にありました。

.. code-block:: bash

   $ locate root-help.el    # check path
   ## ROOT5 => /opt/local/libexec/root5/share/emacs/site-lisp/root-help.el
   ## ROOT6 => /opt/local/libexec/root6/share/emacs/site-lisp/root-help.el

.. note::

   これの使い方に関しては、あとできちんと調べて書くことにします。
