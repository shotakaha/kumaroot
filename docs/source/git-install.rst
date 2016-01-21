==================================================
インストール
==================================================

デフォルトで ``git`` は入っていますが、
MacPortsを使って最新版をインストールしておきます。
よく分からないけれど ``Perl5`` の ``variants`` は一番新しいのにしておきます。

.. code:: bash

   $ sudo port install git +bash_completion +perl5_22


``git flow`` もMacPortsからインストールできます。

.. code:: bash

   $ sudo port install git-flow

``git flow`` は
`Vincent Driessenのブランチモデル <http://nvie.com/posts/a-successful-git-branching-model/>`__
のような目的を持ったブランチを用意し、そのブランチ間の切り替えを容易にしてくれる
Git拡張（＝Gitコマンドを何種類かまとめたスクリプト）。

プロジェクトのブランチ管理がとても楽になるので、おすすめです。
