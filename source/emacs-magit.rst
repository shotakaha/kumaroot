==================================================
Emacs + Magit
==================================================

MagitはEmacsのGitインターフェースです。
とても便利なので、Emacs使い、かつ、Git使いの人はぜひ使いましょう。


Magitの起動（ ``M-x magit-status`` ）
--------------------------------------------------

Emacsの中で ``M-x magit-status`` と打ち込んで
``magit-bufer`` を起動します（ `図 #fig-magit-status` ）

Magitはこのバッファを通じて操作をすることになるので、
キーバインド設定をしておきましょう。
マニュアルを読むと ``C-x g`` になってるのでそうしましょう。

.. _fig-magit-status:

.. figure:: ./emacs-magit/magit-status.png

   Magit-buffer


Magitのヘルプ
--------------------------------------------------

Magit-buffer で ``?`` を押すと使い方がポップアップします（ :num:`図 #magit-popup` ）。
``M-x magit-dispatch-popup`` でも同様です。
これもマニュアルに ``C-x M-g`` にセットするとよいと書いてあるので、そうしましょう。

困ったらこれで確認することができるので、
ある程度Gitの仕組みに関する基礎知識があれば、
コマンドを覚えていなくても使うことができます。
また、Magitを使っているうちにGitも使えるようになる。

.. _fig-magit-popup:

.. figure:: ./emacs-magit/magit-popup.png


ステージ
--------------------------------------------------

``Untracked files`` の ``source/emacs-magit.rst`` に
カーソルを当て ``s`` を押してファイルをステージします（ :num:`図 #fig-magit-stage` ）

.. _fig-magit-stage

.. figure:: ./emacs-magit/magit-commit-001.png

ステージされたファイルは ``Staged changes`` に移動します。



コミット
--------------------------------------------------
