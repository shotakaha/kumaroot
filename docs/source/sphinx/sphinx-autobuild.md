# 自動ビルドしたい（``sphinx-autobuild``）

```console
$ pip3 install sphinx-autobuild
```

```console
$ cd プロジェクト名/docs
$ sphinx-autobuild source/ build/html/
```

[sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild)を使うと、ライブリロードしながら編集できます。
``Makefile``の末尾に次のように追記します。

```make
# ...（省略）...
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

ターミナル上で``make livehtml``を走らせた状態で、ブラウザで``http://127.0.0.1:8000``を開くと準備完了です。
``docs``以下のファイルを編集して保存するたびにSphinxが実行され、ブラウザが更新されます。
うまく更新できない場合は、まずターミナル上の表示を確認してください。エラーの素が見つかるかもしれません。

```console
$ cd docs
$ make livehtml
...（省略）...
[I 230520 23:34:44 server:335] Serving on http://127.0.0.1:8000
[I 230520 23:34:44 handlers:62] Start watching changes
[I 230520 23:34:44 handlers:64] Start detecting changes
```
