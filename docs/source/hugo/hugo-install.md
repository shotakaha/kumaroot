```{eval-rst}
.. index::
    pair: Hugo; install
```

# インストールしたい（`hugo`）

```console
$ brew install hugo
```

[Hugo](https://gohugo.io/)はHomebrewでインストールできます。
インストールした後は、``hugo``コマンドが使えるようになります。

```console
$ brew install go
```

[hugo mod](https://gohugo.io/commands/hugo_mod/)を使う場合はGoのインストールが必要です。

```console
// uvを使ってプロジェクトに追加
$ uv add --group docs hugo
```

[（おそらく）個人のボランティア](https://github.com/agriyakhetarpal/hugo-python-distributions)
によって`wheel`ビルドが提供されているおかげで、`uv`でプロジェクトに追加できます。
