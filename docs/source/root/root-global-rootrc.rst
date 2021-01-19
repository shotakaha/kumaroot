==================================================
個人設定したい（ :file:`.rootrc` ）
==================================================

bashの個人設定を :file:`~/.bashrc` に書くように、ROOTの個人設定は :file:`~/.rootrc` に書きます。
デフォルト値は :file:`{ROOTをインストールしたパス}/etc/system.rootrc` に書かれているので、これをホームディレクトリにコピーして編集すればOKです。

.. code:: bash

    $ locate system.root
    ## =>  $ROOTSYS/etc/system.rootrc
    $ cp $ROOTSYS/etc/system.rootrc ~/.rootrc


ディレクトリ毎の設定（ :file:`rootlogon.C` ）
==================================================

ディレクトリ（やプロジェクト）毎の設定はROOTマクロを起動するディレクトリ直下の :file:`rootlogon.C` に書きます。
