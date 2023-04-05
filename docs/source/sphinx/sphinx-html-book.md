# Sphinx Book Theme の設定

```bash
$ pip3 install sphinx_book_theme
```

[Jupyter Book](https://jupyterbook.org/en/stable/)で使われているテーマです。
Bootstrap5に対応しています。

## プロジェクトに追加したい

```bash
$ cd プロジェクト名
$ poetry add --group=docs sphinx
$ poetry add --group=docs sphinx-book-theme
$ poetry add --group=docs myst-parser
$ poetry add --group=docs ablog
$ sphinx-quickstart docs
$ code docs/conf.py
```

``sphinx_book_theme``はMySTとABlogと併用できます。
必要はパッケージ（``sphinx`` / ``sphinx_book_theme`` / ``myst_parser`` / ``ablog``）を追加、
``docs``にドキュメント用ディレクトリを作成、
{file}`docs/conf.py`を開いて、以下の設定を追記します。

## テーマを使いたい

```python
extensions = [
    ...
    "sphinx_book_theme",
    "myst_parser",
    "ablog",
    ...
]

html_theme = "sphinx_book_theme"
```

拡張（``extensions``）一覧にパッケージ名を追加します。
また、``html_theme``をパッケージ名に変更します。

## リファレンス

- [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/)
