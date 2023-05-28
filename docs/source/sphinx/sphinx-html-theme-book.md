```{eval-rst}
.. index::
    single: Sphinx Theme; sphinx_book_theme
```

# Bookしたい（``sphinx_book_theme``）

```console
$ pip3 install sphinx_book_theme
```

いま一番気に入っているのが[Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/)です。
[Jupyter Book](https://jupyterbook.org/en/stable/)で使われているテーマで、Bootstrap5に対応しています。

[theme.conf](https://github.com/executablebooks/sphinx-book-theme/blob/master/src/sphinx_book_theme/theme/sphinx_book_theme/theme.conf)を確認すると、``pydata_sphinx_theme``をベースにしていて、たくさんの``[options]``が使えることが分かります。

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

``poetry``を使ってプロジェクトに追加する手順を書き出してみました。
ドキュメント関係のパッケージなので``--group=docs``に分類しています。

``sphinx_book_theme``はMySTとABlogと併用できます。
必要はパッケージ（``sphinx`` / ``sphinx_book_theme`` / ``myst_parser`` / ``ablog``）を追加、
``docs``にドキュメント用ディレクトリを作成、{file}`docs/conf.py`を開いて、以下の設定を追記します。

## 設定ファイル

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

## Google Analyticsしたい

```python
html_theme_options = {
    "analytics": {"google_analytics_id": "G-xxxxxxxx"},
}
```

``Sphinx Book Theme``は``PyData Theme``を継承しているので、``PyData Theme``ドキュメントを参照します。
[Analytics and usage services](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/analytics.html)のページにオプションの設定方法が書かれていました。
