# ハイパーリンクを挿入したい

```md
[外部サイトのタイトル](外部URL)
[ページのタイトル](内部のファイルへの相対パス)
[](内部のファイルへの相対パス)
```

``reST``記法のハイパーリンクの書き方をまったく覚えることができなかったので、
これだけでも``MyST``を有効にしてよかったと思っています。
``ページのタイトル``が空欄の場合は、そのページのタイトルが自動で表示されます。

:::{seealso}
reST形式で書くと次のようになります。

```rst
`外部サイトのタイトル <外部URL>`__
```

内部リンクの場合、``reST``記法だとロール（``:doc:`` / ``:download:`` / ``:any:``など）を意識して使い分ける必要があります。
:::

## リファレンス

- [Cross-references - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
- [Cross-referencing with Sphinx - Read the Docs](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
- [Hyperlinks - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks)
- [Cross-referencing arbitrary locations - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role)
