==================================================
リポジトリの作成
==================================================

.. code-block:: bash

   $ cd MyPROJECT
   $ git init


リポジトリを作成するときに一度だけ使うコマンドです。
Git管理をしたいプロジェクトのディレクトリに移動してから :command:`git init` を実行します。
ディレクトリ内に、すでにファイルが存在していても大丈夫です。

実行すると :file:`MyProject/.git/` ディレクトリが作成され、
その中のファイルにリポジトリの情報が保存されます。
通常、それらのファイルを直接編集することはないですが、
ただのテキストファイルなので、困ったときに調べることができます。

また、Git管理をやめる場合は :file:`.git/` ディレクトリを削除すればOKです。
中のファイルのパーミッションによっては、削除確認のメッセージが表示されるので、
:command:`-f` オプションを付けてあります。

.. code-block:: bash

   $ cd MyPROJECT
   $ rm -rf .git
