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

googleanalytics_id = "G-xxxxxxxx"
```

[sphinxcontrib-googleanalytics](https://github.com/sphinx-contrib/googleanalytics)を使うとGoogle Analyticsを挿入できるようになります。
テーマによってはオプションでGAに対応しているものあるので、テーマのドキュメントを確認してみましょう。

## sphinx_rtd_themeでGAしたい

```python
html_theme_options = {
    "analytics_id": "G-xxxxxxxx",
    "analytics_anonymize_ip": False,
}
```

``Read the Docs``のドキュメントを参照すると、[Configuration](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)のページにオプションの設定方法が書かれていました。

## sphinx_book_theme / pydata_sphinx_theme

```python
html_theme_options = {
    "analytics": {"google_analytics_id": "G-xxxxxxxx"},
}
```

``Sphinx Book Theme``は``PyData Theme``を継承しているので、``PyData Theme``ドキュメントを参照します。
[Analytics and usage services](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/analytics.html)のページにオプションの設定方法が書かれていました。
