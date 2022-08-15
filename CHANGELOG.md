## v1.1.0 (2022-08-15)

### Fix

- **emacs/emacs-yatex.md**: 修正した
- **emacs/emacs-install.md**: 修正した
- **emacs/emacs-usage.md**: 修正した 	modified:   docs/source/emacs/emacs-usage.md
- **emacs/emacs-org-latex.md**: 追加した
- **command/command-texdoc.md**: 修正した
- **python/python-icecream.md**: 修正した
- **latex/latex-jlreq.md**: 整理した
- **latex/latex-document.md**: 整理した
- **latex/latex-maketitle.md**: 修正した
- **sphinx/sphinx-latex.md**: 整理した
- **conf.py**: LaTeX設定:Polyglossiaパッケージを無効にした

### Feat

- **emacs/emacs-magit.md**: 大きく整理した
- **command/command-tlmgr.md**: 追加した
- **python/python-icecream.md**: 追加した
- **python/python-requests.md**: 追加した
- **python/python-random.md**: 追加した
- **latex/latex-jsclasses.md**: 追加した
- **latex/latex-usepackage.md**: 追加した
- **latex/latex-documentclass.md**: 追加した
- **geant4/geant4-usage.md**: 追加した
- **sphinx/sphinx-latex-section.md**: 追加した
- **sphinx/sphinx-latex-preamble.md**: 追加した
- **sphinx/sphinx-latex-engine.md**: 追加した
- **sphinx/sphinx-latex-elements.md**: 追加した
- **sphinx/sphinx-latex-docclass.md**: 追加した

## v1.0.0 (2022-08-15)

### Feat

- **index.md**: コンテンツの順番を変更した
- **disclaimer.md**: 免責事項を追加した
- **conf.py**: LuaLaTeXとjlreqに設定した
- **command/command-ssh-keygen.md**: ssh-keygenを追加した
- **command/command-tldr.md**: tldrを追加した
- **command/command-uname.md**: unameを追加した
- **python/python-poetry.md**: poetryを追加した

### Fix

- **latex/latex-usage.md**: リファレンスを整理した
- **pandas/pandas-usage.md**: リファレンスを整理した
- **python/python-usage.md**: リファレンスを整理した
- **root/root-usage.md**: リファレンスを整理した
- **sphinx/sphinx-usage.md**: リファレンスを整理した

## v0.6.0 (2022-08-14)

### Feat

- **command/command-bash.md**: bashを追加した
- **command/command-rsync.md**: rsyncを追加した
- **command/command-sed.md**: sedを追加した
- **command/command-xargs.md**: xargsを追加した
- **git/git-semver.md**: semverを追加した
- **latex/latex-plautopatch.md**: plautopachを追加した
- **latex/latex-ref.md**: LaTeXで相互参照を追加した
- **root/root-tlegend.md**: TLegend編を追加した
- **root/root-tgraph.md**: TGraph編を追加した
- **root/root-tfile.md**: TFile編を追加した
- **docs/deploy.sh**: デプロイ用のスクリプトを作成した

### Fix

- **command/command-find.md**: findを修正した
- **emacs/emacs-vim.md**: 内容が古めだったので削除した
- **emacs/emacs-keyboard.md**: Emacsのキーボード設定を修正した
- **git/git-config.md**: git configを修正した
- **git/git-semver.md**: semverを修正した
- **latex/latex-lualatex.md**: ltjsarticleを追加した
- **root/root-install.md**: ROOTのインストール方法を整理した
- **root/root-global.md**: gROOT設定を修正した
- **root/root-usage.md**: 修正した
- **root/root-tstring.md**: TString編を修正した
- **sphinx/sphinx-myst-syntax.md**: MyST記法を修正した
- **sphinx/sphinx-html**: sphinx-htmlを整理している
- **sphinx-latex-lualatex.md**: sphinx-latexを整理している
- **sphinx/sphinx-latex.md**: SphinxのLaTeX設定を整理している
- **toctree**: toctree周りのwarningを修正した

### Refactor

- **root/**: .mdに変換した
- **emacs/**: .mdに変換した
- **sphinx/**: .mdに変換した
- **emacs/fig/**: Emacs関係の図の置き場を変更した
- **README.md**: renamed README.rst -> README.md

## v0.5.0 (2022-08-12)

### Fix

- **conf.py**: myst_parserを使えるようにした
- **index.rst**: 目次を修正した
- **altair/altair-usage**: Altairを整理した
- **git/git-usage**: Gitを整理した
- **latex/latex-usage**: LaTeXを整理した
- **latex/latex-install**: オンラインツールを紹介した
- **latex/latex-document**: LaTeX文書の基本構造を整理した
- **pandas/pandas-usage**: Pandasを整理した
- **python/python-usage**: Pythonを整理した
- **sphinx/sphinx-usage**: Sphinxを整理した
- **sphinx/sphinx-pandoc**: pandocの使い方を整理した
- **sphinx/sphinx-latex**: PDF文書を作成する方法を整理した
- **sphinx/sphinx-html**: HTML文書を作成する方法を整理した
- **sphinx/sphinx-myst**: MySTを追加した
- **sphinx/sphinx-readthedocs**: RTDの設定ファイルを追加した

### Feat

- **python/python-plotly**: plotlyを新規作成した
- **python/python-altair**: altairを新規作成した
- **python/python-pandas.md**: pandasを新規作成した
- **python/python-loguru.md**: loguruを新規作成した
- **python/python-pathlib**: pathlibを新規作成した
- **latex/latex-maketitle**: maketitleを新規作成した
- **pandas/pandas-usage**: Pandasを新規作成した
- **command/command-grep**: grepを新規作成した
- **command/command-texdoc**: texdocを新規作成した
- **command/command-usage**: コマンドの使い方を新規作成した
- **vscode/vscode-usage**: VS Codeの使い方を新規作成した
- **latex/latex-lualatex**: LuaLaTeXの使い方を追加した
- **latex/latex-latexmk**: latexmkの使い方を追加した

## v0.4.0 (2022-08-07)

### Fix

- **conf.py**
  - Markdown拡張（myst_parser）を追加した

### Feat

- **altair**
  - Altairの章を追加した
- **python**
  - Pythonの章を追加した

### Refactor

- **root**
  - ROOT関係のファイルを root 以下に移動した
- **latex**
  - LaTeX関係のファイルを latex 以下に移動した
- **emacs**
  - Emacs関係のファイルを emacs 以下に移動した
- **sphinx**
  - Sphinx関係のファイルを sphinx 以下に移動した

## v0.3.1 (2021-01-18)


### Fix

- **preface**
  - TODOを追加した
- **latex**
  - ドキュメントの基本を修正した
  - LuaLaTeXコマンドの説明を追加した
  - 目次にハイパーリンクをつけるパッケージの説明を追加した
- **sphinx**
  -  Sphinx環境の構築方法を更新した
- **conf.py**
  - LaTeX設定を整理した
  - HTML設定を整理した
  - i18n設定を整理した
  - Epub設定を整理した
  - Texinfo設定を削除した

## v0.3 (2016-01-23)

## v0.2 (2015-12-03)

## v0.1 (2015-10-13)
