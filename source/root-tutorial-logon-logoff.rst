==================================================
:file:`rootlogon.C` と :file:`rootlogoff.C`
==================================================

さて ``tutorials`` をコピーしたディレクトリ（ ``$TUTORIALS`` ）で
ROOTを起動／終了すると、以下の様なメッセージが表示されるはずです。

.. code-block:: bash

   $ cd $TUTORIAL
   $ root    ## 起動

   Welcome to the ROOT tutorials

   Type ".x demos.C" to get a toolbar from which to execute the demos

   Type ".x demoshelp.C" to see the help window

   ==> Many tutorials use the file hsimple.root produced by hsimple.C
   ==> It is recommended to execute hsimple.C before any other script

   root [0] .q    ## 終了

   Taking a break from ROOT? Hope to see you back!


これは、同じディレクトリに :file:`rooglogon.C` と :file:`rootlogoff.C` があるからです。
この２つのファイルを用意しておくことで、ROOT起動時および終了時の動作を設定することができます。
気になる人は覗いてみましょう（ ``printf`` してるだけですが）。

僕の場合、数ヶ月ぶりに触るプログラムなんてほとんど忘れてしまっています。
なので :file:`rootlogon.C` に手順を書いて残したりしています。


ROOT起動時に読み込まれるファイルの順番
==================================================

ROOT起動時には以下の順番で設定ファイルが読み込まれます。

#. ``system.rootrc``
#. ``~/.rootrc``
#. ``./rootlogon.C``

``system.rootrc`` の場所は ``locate`` して確認してください。
これを ``~/.rootrc`` にコピーして編集すれば自分用の全体設定の完了です。
プロジェクト毎の設定は ``./rootlogon.C`` に書いておけばよいです。
