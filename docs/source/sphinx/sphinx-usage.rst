==================================================
Sphinxの使い方
==================================================

``Sphinx`` は ``reStructredText（reST）`` 形式で作成されたテキスト文書を、PDFやHTML、その他のフォーマットへと変換してくれる ``ドキュメンテーションビルダー`` というツールです。

この ``KumaROOT`` も ``Sphinx`` を使って生成しています。
プロジェクト自体は `GitHub <github_>`_ を使ってバージョン管理をして、
HTMLは `Read the Docs <rtd_>`_ で公開しています。
どんなものか気になる方は ``KumaROOT`` のGitHubリポジトリをクローンしてみるといいかもしれません。

元々、Pythonのドキュメント生成のために開発されたものなので、
プロジェクトのドキュメント作成にはもってこいです。
中身はPythonで書かれているので、へびつかいであれば、ある程度カスタマイズすることもできるはずです。

.. _github: https://github.com/shotakaha/kumaroot
.. _rtd: http://kumaroot.readthedocs.org/ja/latest/

.. toctree::
   :maxdepth: 1

   sphinx-install
   sphinx-quickstart
   sphinx-build
   sphinx-conf
   sphinx-myst
   sphinx-toctree
   sphinx-code-block
   sphinx-hyperlink
   sphinx-readthedocs
   sphinx-pandoc
