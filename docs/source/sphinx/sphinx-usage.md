# Sphinxの使い方

Sphinxは``reStructredText（reST）`` 形式で作成されたテキスト文書を、PDFやHTML、その他のフォーマットへと変換してくれる**ドキュメンテーションビルダー**というツールです。

この``KumaROOT``も``Sphinx``を使って生成しています。
プロジェクト自体は[GitHub](https://github.com/shotakaha/kumaroot/)を使ってバージョン管理をしてあり、ウェブ版は[Read the Docs](http://kumaroot.readthedocs.org/ja/latest/)で公開しています。
どういったものか気になる方はぜひ[KumaROOTのGitHubリポジトリ](https://github.com/shotakaha/kumaroot)をクローンしてみてください。

元々、Pythonのドキュメント生成のために開発されたものなので、
プロジェクトのドキュメント作成にはもってこいです。
中身はPythonで書かれているので、へびつかいであれば、ある程度カスタマイズすることもできるはずです。

```{toctree}
---
maxdepth: 1
---
sphinx-install
sphinx-quickstart
sphinx-build
sphinx-conf
sphinx-theme
sphinx-myst
sphinx-toctree
sphinx-code-block
sphinx-hyperlink
sphinx-readthedocs
sphinx-pandoc
```
