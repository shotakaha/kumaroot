==================================================
起動時に読み込まれるファイル
==================================================

ROOT起動時には以下の順番で設定ファイルが読み込まれます。

#. :file:`system.rootrc`
#. :file:`~/.rootrc`
#. :file:`./rootlogon.C`

:file:`system.rootrc` の場所は :command:`locate` コマンドで確認できます（ :numref:`fig-rootrc` ）。
:file:`/opt/local/...` にあるのは ``MacPorts`` で、 :file:`/private/etc/...` にあるのはGitを使ってインストールしたときに生成されたファイルです。


.. _fig-rootrc:
.. figure:: ./root-tutorial/root-rootrc.png
   :align: center

   :file:`system.rootrc` を :command:`locate` した結果


この :file:`system.rootrc` のどれか一つを :file:`~/.rootrc` にコピーして編集すれば自分用の全体設定の完了です。
変数の説明はファイルの中にきちんと書かれているので、それを参照してください。

プロジェクト毎の設定は :file:`./rootlogon.C` に書いておけばよいです。
設定内容はこの :file:`~/.rootrc` から抜き出すか、後述する全体設定のためのグローバル変数を使います。
