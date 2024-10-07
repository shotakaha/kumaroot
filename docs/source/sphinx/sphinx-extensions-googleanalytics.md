```{eval-rst}
.. index::
    single: Sphinx Extensions; Google Analytics

```

# Google Analyticsしたい

```console
$ pip3 install sphinxcontrib-googleanalytics
```

```python
extensions = [
    ...
    "sphinxcontrib.googleanalytics",
    ...
]

googleanalytics_enabled = True
googleanalytics_id = "G-xxxxxxxx"
```

[sphinxcontrib-googleanalytics](https://github.com/sphinx-contrib/googleanalytics)を使うと、どのテーマにもGoogle Analyticsを追加できます。

テーマによってはオプションでGAに対応しているものがあります。
詳しくは[sphinx_book_themeのGA設定](./sphinx-html-theme-book.md)を参照してください。
その他のテーマについては、そのテーマのドキュメントを確認してください。
