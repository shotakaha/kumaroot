==================================================
Emacs + Magit
==================================================

MagitはEmacsのGitインターフェースです。
とても便利なので、Emacs使い、かつ、Git使いの人はぜひ使いましょう。


Magitの起動（ ``M-x magit-status`` ）
--------------------------------------------------

Emacsの中で ``M-x magit-status`` と打ち込んで
Magit用バッファ（ ``magit-bufer`` ）を起動します（ :numref:`fig-magit-status` ）。

Magitはこのバッファを通じて操作をすることになるので、
キーバインド設定をしておきましょう。
マニュアルを読むと ``C-x g`` になってるのでそうしましょう。

.. _fig-magit-status:

.. figure:: ./emacs-magit/magit-status.png

   Magit用バッファ（ ``M-x magit-status`` ）


Magitのヘルプ
--------------------------------------------------

Magit-buffer で ``?`` を押すと使い方がポップアップします（ :numref:`fig-magit-dispatch-popup` ）。
``M-x magit-dispatch-popup`` でも同様です。
これもマニュアルに ``C-x M-g`` にセットするとよいと書いてあるので、そうしましょう。

困ったらこれで確認することができるので、
ある程度Gitの仕組みに関する基礎知識があれば、
コマンドを覚えていなくても使うことができます。
また、Magitを使っているうちにGitも使えるようになる。

.. _fig-magit-dispatch-popup:

.. figure:: ./emacs-magit/magit-dispatch-popup.png

   Magit用ヘルプ（ ``M-x magit-dispatch-popup`` ）


ステージ／アンステージ
--------------------------------------------------

``Untracked files`` の ``source/emacs-magit.rst`` に
カーソルを当て ``s`` を押してファイルをステージします（ :numref:`fig-magit-stage` ）。
ステージされたファイルは ``Staged changes`` に移動します。

ファイルを間違えてステージしてしまったなど
アンステージしたい場合は、そのファイルの先頭で ``u`` を押します。

.. _fig-magit-stage:

.. figure:: ./emacs-magit/magit-stage.png

   ファイルのステージ


コミット（ ``C-x g c c``）
--------------------------------------------------

``Staged changes`` にあるファイルはコミットすることができます。
``c`` を押すとコミット用バッファ（ ``magit-commit-popup`` ）がポップアップします（ :numref:`fig_magit-commit-popup` ）。
ポップアップ内にある ``Swithes`` 、 ``Options`` 、 ``Actions`` から操作を選択し、頭に付いている記号を入力します。
通常のコミットの場合は ``c`` を押します。

.. _fig-magit-commit-popup:

.. figure:: ./emacs-magit/magit-commit-popup.png

   コミット用バッファ


すると、画面が上下２分割されて ``magit-diff`` バッファ（画面上）と
``.git/COMMIT_EDITMSG`` （画面下）が表示されます（ :numref:`fig-magit-commit-edit` ）。
``magit-diff`` には変更した箇所が表示されているので、それを確認しながら、
``.git/COMMIT_EDITMSG`` にコミットメッセージを書きます。
コミットメッセージの編集が終わったら ``C-c C-c`` で保存します。
コミットをやめる場合は ``C-c C-k`` で破棄できます。

.. _fig-magit-commit-edit:

.. figure:: ./emacs-magit/magit-commit-edit.png

   コミットメッセージの編集


コミットが終わると ``Unpushed commits`` に
コミットメッセージが表示されます（ :numref:`fig-magit-commit-done` ）。

.. _fig-magit-commit-done:

.. figure:: ./emacs-magit/magit-commit-done.png

   magit-commit-done


コミットを取り消したい場合は ``C-x g U HEAD^`` とすればよいはずです（やったことない）。
もしくはシェルを起動して ``git reset HEAD^`` しましょう（やったことある）。


プッシュ（ ``C-x g P P`` ）
--------------------------------------------------

ある程度編集が進んだ場合や、１日の終わりには「プッシュ」を行い、
リモートへ変更を反映させましょう。

プッシュをするには ``magit-buffer`` で ``P`` を押して
``magit-push`` バッファを呼び出します（ :numref:`fig-magit-push` ）。
そこで ``P`` を押すとプッシュできます。

ただし、プッシュするブランチがローカルで作ったもので、
リモート先のブランチとの紐付けができていない場合、プッシュは失敗します。
そんな時は ``-u P`` （ ``--set-upstream`` ）すれば大丈夫です。


.. _fig-magit-push:

.. figure:: ./emacs-magit/magit-push.png


ちゃんとプッシュできているか確認したい場合は ``$`` を押します。
すると ``magit-process`` バッファが起動します（ :numref:`fig-magit-process` ）。
プロセスが成功していれば最後のコマンドの行頭のステータスが ``0``、
失敗していればエラーコードが赤色で表示されます。
プロセスの詳細は ``TAB`` もしくは ``C-i`` で展開することができます。

.. _fig-magit-process:

.. figure:: ./emacs-magit/magit-process.png

   Gitプロセスの表示


残りの操作
--------------------------------------------------

.. todo:: branch

.. todo:: log

.. todo:: fetch / pull

.. todo:: rebase / merge

.. todo:: show refs

.. todo:: stash

.. todo:: tag
