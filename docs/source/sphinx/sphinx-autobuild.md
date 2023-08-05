```{eval-rst}
.. index::
    pair: プレビューしたい; Sphinx
```

# 自動ビルドしたい（``sphinx-autobuild``）

```console
$ pip3 install sphinx-autobuild
```

```console
$ cd プロジェクト名/docs
$ sphinx-autobuild source/ build/html/
```

[sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild)を使うと、ライブリロードしながら編集できます。

## さらに自動化したい

```make
# ...（省略）...
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild --open-browser "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

``Makefile``の末尾に上記のコマンドを追記しておくと便利です。
ターミナル上で``make livehtml``を実行すると、ブラウザで``http://127.0.0.1:8000``が開くようになります。
``docs``以下のファイルを編集して保存するたびにSphinxが実行され、ブラウザ表示も更新されます。

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
