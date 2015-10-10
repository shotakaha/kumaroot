============================================================
初期設定したい（ :file:`rootrc` , :file:`rootlogon.C` ）
============================================================


:file:`rootrc`
==================================================

bashの設定を :file:`~/.bashrc` に書くように、ROOTの設定は :file:`~/.rootrc` に書きます。
デフォルト値は :file:`{ROOTをインストールしたパス}/etc/system.rootrc` に書かれているので、とりあえずこれをホームディレクトリにコピーして編集したらOKです。

.. code:: bash

    $ locate system.root
    ## =>  $ROOTSYS/etc/system.rootrc
    $ cp $ROOTSYS/etc/system.rootrc ~/.rootrc


:file:`rootlogon.C`
==================================================
