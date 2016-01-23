==================================================
Git Flow の使い方
==================================================

``git flow`` は
`Vincent Driessenのブランチモデル <http://nvie.com/posts/a-successful-git-branching-model/>`__
に基づいたGit拡張です。

要するに、**ブランチの用途（開発なのか、リリースなのか、ホットフィックスなのか）** に焦点をあて、
それに合ったブランチ切り替えが簡単にできるように何種類かのGitコマンドをまとめたものです。
実際 ``git-flow`` コマンドの中身はシェルスクリプトです。

下の図は ``git-flow`` を整理するために自分で作ってみた図です。
上のリンク先にある図と内容は同じだけど、ちょっと見た目をシンプルにしてみました。


例えば ``git flow start MyFeature`` の場合、

#. develop ブランチをチェックアウトする（ ``$ git checkout develop``）
#. develop ブランチから feature ブランチを作成する（ ``$ git branch feature/MyFeature``）
#. その feature ブランチをチェックアウトする（ ``$ git checkout feature/MyFeature``）

といったように、３手間かかるのが１手間で済みます。

``git flow release finish MyRelease`` の場合の部分を眺めてみると分かるかもですが、
ブランチ管理がとても楽になるので、おすすめです。


.. figure:: ./git/fig/git-flow.png
