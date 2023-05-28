```{eval-rst}
.. index::
    single: Sphinx Theme; pydata_sphinx_theme
```

# PyDataしたい（``pydata_sphinx_theme``）

```console
$ pip3 install pydata_sphinx_theme
```

[pydata_sphinx_themeのtheme.conf](https://github.com/pydata/pydata-sphinx-theme/blob/main/src/pydata_sphinx_theme/theme/pydata_sphinx_theme/theme.conf)も眺めてみましょう。
元のテーマは``basic``となっていて、組み込みテーマから作成されたことが分かりました。

## Google Analyticsしたい

```python
html_theme_options = {
    "analytics": {"google_analytics_id": "G-xxxxxxxx"},
}
```

``PyData Theme``ドキュメントの[Analytics and usage services](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/analytics.html)にオプションの設定方法が書かれていました。
