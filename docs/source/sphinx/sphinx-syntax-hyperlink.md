# ハイパーリンクしたい

```md
% 外部リンク
[外部サイトのタイトル](外部URL)

% 内部リンク
[ページのタイトル](内部のファイルへの相対パス)
[](内部のファイルへの相対パス)
```

ハイパーリンクは外部リンクと内部リンクがありますが、MySTでは同じように記述できます。
``reST``記法のハイパーリンクの書き方をまったく覚えることができなかったので、
これだけでも``MyST``を有効にしてよかったと思っています。
``ページのタイトル``が空欄の場合は、そのページのタイトルが自動で表示されます。

:::{seealso}

reST形式で書くと次のようになります。

```rst
.. 外部リンク
`外部サイトのタイトル <外部URL>`__

.. 内部リンク
:ref:`ラベル名`
:ref:`リンクラベル <ラベル名>`
:doc:`ページのタイトル <相対パス>`
:doc:`相対パス`
```

内部リンクの場合、``reST``記法だとロール（``:doc:`` / ``:download:`` / ``:any:``など）を意識して使い分ける必要があります。
:::

## リファレンス

- [Cross-references - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
- [Cross-referencing with Sphinx - Read the Docs](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
- [Hyperlinks - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks)
- [ハイパーリンク - Sphinxドキュメント](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html#hyperlinks)
- [Cross-referencing arbitrary locations - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role)
- [任意の場所へのクロスリファレンス - Sphinxドキュメント](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/roles.html#ref-role)
