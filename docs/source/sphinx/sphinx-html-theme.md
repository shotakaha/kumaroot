# テーマしたい（``html_theme``）

```python
html_theme = "テーマ名"
```

Sphinxを使うときに必ず設定する項目のひとつです。
[html_theme](https://www.sphinx-doc.org/ja/master/usage/configuration.html#confval-html_theme)を使ってHTML出力のテーマ（＝スタイルを集めたもの）を設定できます。
デフォルトは[alabaster](https://alabaster.readthedocs.io/en/latest/)に設定されますが、あまり日本語向きではないと感じています。
安定したオススメは[sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)です。
最近は[sphinx_book_theme](https://sphinx-book-theme.readthedocs.io/en/stable/)が気に入っています。
[Sphinx Theme Gallery](https://sphinx-themes.readthedocs.io/en/latest/)から自分の好みのテーマを探すことができます。

## テーマのオプションを設定したい（``html_theme_options``）

```python
html_theme = "テーマ名"
html_theme_options = {
    "設定キー": "値",
    "設定キー": "値",
    ...,
}
```

[html_theme_options](https://www.sphinx-doc.org/ja/master/usage/configuration.html#confval-html_theme_options)を使って、テーマのオプションを設定できます。
設定できる値はテーマごとに違うので、そのテーマのドキュメントを参照するのが適切です。

[組み込みテーマのオプション](https://www.sphinx-doc.org/ja/master/usage/theming.html#builtin-themes)も設定できます。
ただし、組み込みテーマ自体の見た目が全体的にぱっとしないので、あまり出番はないかもしれません。
他のテーマの中身を確認したり、自作テーマを作成したりするときの参考にはなると思います。
