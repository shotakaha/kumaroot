```{eval-rst}
.. index::
    pair: Sphinx; usage
```

# Sphinxの使い方

[Sphinx](https://www.sphinx-doc.org/ja/master/)は[reStructredText（reST）](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html) 形式で作成された文書を、PDFやHTML、その他のフォーマットへと変換してくれる**ドキュメンテーションビルダー**というツールです。
Pythonのドキュメント生成のために開発されたものなので、プロジェクトのドキュメント作成にはもってこいです。
また、中身もPythonで書かれているので、へびつかいであれば、ある程度カスタマイズすることもできるはずです。

この``KumaROOT``も``Sphinx``を使って生成しています。
プロジェクト自体は[GitHub](https://github.com/shotakaha/kumaroot/)を使ってバージョン管理をしてあり、ウェブ版は[Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開しています。
どういったものか気になる方はぜひ[KumaROOTのGitHubリポジトリ](https://github.com/shotakaha/kumaroot)をクローンしてみてください。

## はじめたい

ドキュメントのはじめかたや、拡張パッケージの設定方法などを整理しました。

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
sphinx-extensions-googleanalytics
sphinx-extensions-copybutton
sphinx-extensions-ablog
```

## マークアップしたい

ドキュメントをマークアップする方法を整理しました。
Sphinxの基本は[ディレクティブ（directive）](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html)と[ロール（role）](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/roles.html)です。

:::{hint}

**ディレクティブ**／**ロール**は、
HTMLだと**ブロック要素**／**インライン要素**、
LaTeXだと**環境**／**コマンド**、
に相当するイメージで、僕はドキュメントをマークアップしています。

:::

デフォルトの基本は``reST（reStructuredText）記法``なのですが、
このドキュメントでは[MyST記法](https://myst-parser.readthedocs.io/en/latest)を前提にコードのサンプルを例示します。

```{toctree}
---
maxdepth: 1
---
sphinx-syntax-toctree
sphinx-syntax-comment
sphinx-syntax-hyperlink
sphinx-syntax-code-block
sphinx-syntax-admonition
sphinx-syntax-image
sphinx-syntax-meta
sphinx-syntax-footnote
sphinx-syntax-include
sphinx-syntax-index
```

## HTMLしたい

```{toctree}
---
maxdepth: 1
---
sphinx-html-theme
sphinx-html-title
sphinx-html-logo
sphinx-html-htaccess
sphinx-html-sidebars
sphinx-html-css
```

% あとでsphinx-designのページを作る
% sphinx-html-sd

## LaTeX / PDFしたい

```{toctree}
---
maxdepth: 1
---
sphinx-latex-engine
sphinx-latex-docclass
sphinx-latex-documents
sphinx-latex-elements
sphinx-latex-logo
sphinx-latex-section
sphinx-latex-thesection
```

```{toctree}
---
maxdepth: 1
caption: 設定例
---
sphinx-latex-lualatex
sphinx-latex-uplatex
```

## ビルドしたい

ドキュメントをビルドする方法を整理しました。

```{toctree}
---
maxdepth: 1
---
sphinx-build
sphinx-build-html
sphinx-build-latexpdf
sphinx-build-linkcheck
sphinx-build-gettext
sphinx-autobuild
```

## デプロイしたい

```{toctree}
---
maxdepth: 1
---
sphinx-deploy-gitlab
sphinx-deploy-rtd
```
