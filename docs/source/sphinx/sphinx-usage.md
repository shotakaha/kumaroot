# Sphinxの使い方

Sphinxは``reStructredText（reST）`` 形式で作成されたテキスト文書を、PDFやHTML、その他のフォーマットへと変換してくれる**ドキュメンテーションビルダー**というツールです。

この``KumaROOT``も``Sphinx``を使って生成しています。
プロジェクト自体は[GitHub](https://github.com/shotakaha/kumaroot/)を使ってバージョン管理をしてあり、ウェブ版は[Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開しています。
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
sphinx-conf
sphinx-extensions
sphinx-make
sphinx-make-html
sphinx-make-latexpdf
sphinx-make-linkcheck
sphinx-hyperlink
sphinx-toctree
sphinx-code-block
sphinx-meta
sphinx-footnote
sphinx-readthedocs
sphinx-html-ogp
```

## リファレンス

- [Sphinx 日本語ドキュメント](https://www.sphinx-doc.org/ja/master/index.html)
- [reStructuredText入門](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html)
- [CommonMark](https://commonmark.org/)
- [MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest)
- [Read the Docs](https://readthedocs.org/)
