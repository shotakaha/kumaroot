```{eval-rst}
.. index::
    pair: Sphinx; install
```

# インストールしたい

```console
$ pip3 install sphinx
```

``pip3``コマンドで``Sphinx``パッケージをインストールします。

## テーマしたい

```console
$ pip3 install テーマのパッケージ名
```

SphinxのテーマもPythonパッケージとして公開されています。
[Sphinx Theme Gallery](https://sphinx-themes.readthedocs.io/en/latest/)などから、自分の好みのテーマを検索し、インストールしてください。

デフォルトのテーマは``alabaster``ですが、僕は``sphinx_rtd_theme``か``sphinx_book_theme``を使っています。

```console
$ pip3 install sphinx_rtd_theme
$ pip3 install sphinx_book_theme
```

詳しくは[テーマの使い方](./sphinx-html-theme.md)にまとめておきます。

## Markdownしたい

```bash
$ pip3 install myst-parser
```

``myst-parser``パッケージをインストールし、``MyST（Markedly Structured Text）``というMarkdownを拡張した記法でSphinx文書が作成できるようにします。
``reST``記法で書いていたことが、ほぼ``Markdown``記法で書けるようになりとても便利です。

:::{note}

このドキュメントのサンプルも``MyST``で書いています。

:::
