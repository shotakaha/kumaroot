==================================================
初期設定
==================================================


ユーザ名やメールアドレス、使用するエディタなどを設定することができます。

.. code:: bash

   $ git config --global user.name "Shota Takahashi"
   $ git config --global user.email "shotakaha@gmail.com"
   $ git config --global core.editor emacslient

``--global`` オプションをつけた場合は :file:`$HOME/.gitconfig` に書き込まれます。
このファイルに直接書き込んでもOKです。


エイリアスの設定
==================================================

各種コマンドのエイリアス（＝ショートカットキー）を設定できます。
この場合、たくさん設定することになるので、 :command:`git config` を使うより、
:file:`$HOME/.gitconfig` に直接書き込んだ方が楽ちんです。

僕は以下のエイリアスを設定しています。
上の４つはよくある設定で、 ``hist`` 以下の部分はどこかのサイトからのコピペです。
後述する ``Magit`` （EmacsのGitクライアント）を使い始めてから、コマンド操作することは減りました。

.. code:: bash

   [alias]
      co = checkout
      ci = commit
      st = status
      br = branch
      hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
      type = cat-file -t
      dump = cat-file -p
      lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
      lga = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative --all
