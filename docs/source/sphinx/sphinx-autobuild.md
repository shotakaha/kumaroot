```{eval-rst}
.. index::
    pair: プレビューしたい; Sphinx
```

# 自動ビルドしたい（`sphinx-autobuild`）

```console
$ pip3 install sphinx-autobuild
```

```console
$ cd プロジェクト名/docs
$ sphinx-autobuild source/ build/html/
```

[sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild)を使うと、ライブリロードしながら編集できます。

## ブラウザを開きたい（`--open-browser`）

```console
$ sphinx-autobuild --open-browser source/ build/html/
```

`--open-browser`オプションをつけておくと、
コマンド実行と一緒に、該当するURLをブラウザで開くことができます。

## ファイルを除外したい（`--ignore`）

```console
$ sphinx-autobuild source/ build/html/ --ignore "除外パターン"
```

`--ignore`オプションで、自動ビルドに含めたくないファイルを設定できます。
プラグインによっては、ビルド環境に中間ファイルを作成する場合があります。
このようなファイルが存在すると、自動ビルドが（無限）ループに入る可能性があるため、除外する必要があります。

## さらに自動化したい

```make
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# ------------------------------
# ここから下を追記する
# ------------------------------

livehtml:
	sphinx-autobuild --open-browser "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O) --ignore "**/_tags/*"
```

自動ビルド用のコマンドを`Makefile`に追記しておくと便利です。
ターミナル上で`make livehtml`を実行すると、ブラウザで``http://127.0.0.1:8000``が開くようになります。
`docs`以下のファイルを編集して保存するたびにSphinxが実行され、ブラウザ表示も更新されます。

ページがうまく更新できない場合は、ビルド時にエラーが発生している可能性があります。
まずターミナル上の表示を確認してください。

```console
$ cd docs
$ make livehtml
...（省略）...
[I 230520 23:34:44 server:335] Serving on http://127.0.0.1:8000
[I 230520 23:34:44 handlers:62] Start watching changes
[I 230520 23:34:44 handlers:64] Start detecting changes
```
