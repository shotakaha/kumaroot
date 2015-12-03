==================================================
Sphinxの使い方
==================================================

``Sphinx`` は、reST形式で作成されたテキスト文書を、PDFやHTML、その他のフォーマットへと変換してくれる ``ドキュメンテーションビルダー`` というツールです。

元々、Pythonのドキュメント生成のために開発されたそうで、中身はPythonで書かれています。
そのため、Pythonを知っていればある程度カスタマイズすることができます。

``KumaROOT`` も ``Sphinx`` を使って生成していて、 リポジトリを `GitHub <github_>`_ で管理、 HTMLを `Read the Docs <rtd_>`_ で公開しています。
どんなものか気になる方は、``KumaROOT`` のGitHubリポジトリをクローンしてみるといいかもしれません。

.. _github: https://github.com/shotakaha/kumaroot
.. _rtd: http://kumaroot.readthedocs.org/ja/latest/

.. toctree::
   :maxdepth: 1

   sphinx-install
   sphinx-build
   sphinx-conf
   sphinx-readthedocs
   sphinx-pandoc
