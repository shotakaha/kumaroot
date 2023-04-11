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
テーマによってはオプションでGAに対応しているものもあります（例：sphinx_rtd_themeなど）。
``sphinx_book_theme``にはないようなので、このパッケージを使って追加しました。
ソースコードを見た感じだとGA4タグにも対応しているっぽいです。

:::{note}

``sphinx_book_theme``のベースになっている``pydata_sphinx_theme``にはGA設定用のオプションがあります。
ただし、そのバージョンを含んだ``sphinx_book_theme``のバージョンがまだリリースされてないのが問題のようです。

:::
