# 拡張機能したい（``extensions``）

```python
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_openbutton",
]
```

Sphinxにはさまざまな拡張機能パッケージが存在し、より便利にできます。
``pip``などを使ってインストールしたあと、{file}``conf.py``の``extensions = []``の部分に追加して有効化します。
詳しい設定は、それぞれの拡張機能のドキュメントを参照してください。

拡張機能パッケージの全体設定は``conf.py``に記述しますが、パッケージによっては各ページのフロントマター設定できる場合もあります。

- [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [sphinx.ext.doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
- [sphinx.ext.intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
- [sphinx.ext.todo](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
- [sphinx.ext.coverage](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html)
- [sphinx.ext.mathjax](https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax)
- [sphinx.ext.ifconfig](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html)
- [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
