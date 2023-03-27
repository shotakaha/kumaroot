# Sphinxの使い方

Sphinxは``reStructredText（reST）`` 形式で作成されたテキスト文書を、PDFやHTML、その他のフォーマットへと変換してくれる**ドキュメンテーションビルダー**というツールです。
Pythonのドキュメント生成のために開発されたものなので、プロジェクトのドキュメント作成にはもってこいです。
また、中身もPythonで書かれているので、へびつかいであれば、ある程度カスタマイズすることもできるはずです。

この``KumaROOT``も``Sphinx``を使って生成しています。
プロジェクト自体は[GitHub](https://github.com/shotakaha/kumaroot/)を使ってバージョン管理をしてあり、ウェブ版は[Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開しています。
どういったものか気になる方はぜひ[KumaROOTのGitHubリポジトリ](https://github.com/shotakaha/kumaroot)をクローンしてみてください。

```{toctree}
---
maxdepth: 1
---
sphinx-install
sphinx-quickstart
sphinx-conf
sphinx-extensions
sphinx-extensions-myst
sphinx-extensions-opengraph
sphinx-builder
sphinx-builder-html
sphinx-builder-latexpdf
sphinx-builder-linkcheck
sphinx-syntax-toctree
sphinx-syntax-hyperlink
sphinx-syntax-code-block
sphinx-syntax-admonition
sphinx-syntax-image
sphinx-syntax-meta
sphinx-syntax-footnote
sphinx-readthedocs
```

## リファレンス

- [Sphinx 日本語ドキュメント](https://www.sphinx-doc.org/ja/master/index.html)
- [Sphinx-Users.jp - 逆引き辞典](https://sphinx-users.jp/reverse-dict/index.html)
- [reStructuredText入門](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html)
- [CommonMark](https://commonmark.org/)
- [MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest)
- [Sphinx Design](https://sphinx-design.readthedocs.io/en/latest/)
- [Sphinx Extensions](https://sphinx-extensions.readthedocs.io/en/latest/)
- [Read the Docs](https://readthedocs.org/)
