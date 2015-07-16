==================================================
Emacs + Magit
==================================================

MagitはEmacsのGitインターフェースです。
とても便利なので、Emacs使い、かつ、Git使いの人はぜひ使いましょう。


Magitの起動（ ``M-x magit-status`` ）
--------------------------------------------------

Emacsの中で ``M-x magit-status`` と打ち込んで
``magit-bufer`` を起動します（ `図 #fig-emacs-magit-001` ）

Magitはこのバッファを通じて操作をすることになるので、
キーバインド設定をしておきましょう。
マニュアルを読むと ``C-x g`` になってるのでそうしましょう。

.. _fig-emacs-magit-001:

.. figure:: ./emacs-magit/emacs-magit-001.png

   Magit-buffer


Magitのヘルプ
--------------------------------------------------

Magit-buffer で ``?`` を押すと使い方がポップアップします（ :num:`図 #fig-emacs-magit-002` ）。
``M-x magit-dispatch-popup`` でも同様です。
これもマニュアルに ``C-x M-g`` にセットするとよいと書いてあるので、そうしましょう。

困ったらこれで確認することができるので、
ある程度Gitの仕組みに関する基礎知識があれば、
コマンドを覚えていなくても使うことができます。
また、Magitを使っているうちにGitも使えるようになる。

.. _fig-emacs-magit-002:

.. figure:: ./emacs-magit/emacs-magit-002.png
