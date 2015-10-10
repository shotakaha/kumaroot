==================================================
Preludeの使い方
==================================================

Emacsを便利に使うためには設定をきちんとしないといけません。
それを一から設定するのも面白いのですが、なかなかめんどくさいです。
そんなめんどくさがり屋さんのために（？）、
GitHubで公開されているEmacs初期設定集があります。
（ありがたや、ありがたや）

`Prelude <https://github.com/bbatsov/prelude>`__ はそのひとつです。
他にも、
`oh-my-emacs <https://github.com/xiaohanyu/oh-my-emacs>`__ や
`emacs24-starter-kit <https://github.com/eschulte/emacs24-starter-kit>`__
など探せばいろいろありますが、
名前がオシャレだなと思ったので、Preludeに決めました。


Preludeのインストール
==================================================

PreludeはGitHubから取ってくることができます。
しかし、本家リポジトリを直接cloneしてしまうと、
自分の変更をpushしたときに大変なことになるので、
自分のGitHubにforkしたリポジトリをcloneすることにします。

ただし、本家の更新も取り込みたいので、
いつでも参照できるように専用のブランチを作ります。
（あとで追記する）

.. code:: bash

    $ cd ~/repos/github/
    $ git clone https://github.com/shotakaha/prelude
    $ export PRELUDE_URL="https://github.com/yourname/prelude.git" && curl -L https://github.com/bbatsov/prelude/raw/master/utils/installer.sh | sh


Preludeの更新・管理
==================================================
