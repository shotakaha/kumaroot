==================================================
ヘルプの使い方
==================================================

Gitのコマンドはいろいろあるので、いちいち覚えてられないし、覚える必要もない。
ヘルプを表示すれば一覧できる

.. code-block:: bash

   $ git help
   $ git --help


コマンド毎のヘルプ（ :command:`-h` ）もある。

.. code-block:: bash

   $ git init -h
   $ git status -h
   $ git branch -h
   $ git remote -h


ロングヘルプ（ :command:`--help` ）は :command:`man` コマンドになる。

.. code-block:: bash

   $ git init --help    ## = $ man git-init
   $ git status --help  ## = $ man git-status
   $ git branch --help  ## = $ man git-branch
   $ git remote --help  ## = $ man git-remote
