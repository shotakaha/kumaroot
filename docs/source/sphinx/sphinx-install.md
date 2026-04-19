```{eval-rst}
.. index::
    pair: Sphinx; install
```

# インストールしたい

```console
// uv toolを使ってシステム全体にインストール
$ uv tool install sphinx

// uvを使ってプロジェクトに追加
$ uv add --group docs sphinx

// テーマを追加
$ uv add --group docs sphinx_rtd_theme
$ uv add --group docs sphinx_book_theme

// Markdown (MyST) を追加
$ uv add --group docs myst-parser
```

Sphinxは`uv`でインストールできます。
インストールした後は、`sphinx-build`コマンドが使えるようになります。

デフォルトのテーマである`alabaster`は、あまり日本語に向いていないと感じるため、
`sphinx_rtd_theme`や`sphinx_book_theme`などのテーマもインストールしておくとよいでしょう。

:::{seealso}

- [Sphinx Theme Gallery](https://sphinx-themes.readthedocs.io/en/latest/)
- [](./sphinx-html-theme.md)

:::

このドキュメントも[Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html)を使っています。

`myst-parser`を追加すると、MyST記法で記述できるようになります。

MySTは、Markedly Structured Textの略で、Markdownを拡張した記法です。
`Markdown`記法の手軽さに、
`reST（reStructuredText）`記法の構造化を追加できます。

このドキュメントも`MyST`記法で書いています。
