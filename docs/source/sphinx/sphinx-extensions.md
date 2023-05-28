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

Sphinxにはさまざまな拡張パッケージが存在し、より便利にできます。
有効にしたい拡張機能は``conf.py``の``extensions = []``に追加します。
詳しい設定は、それぞれの拡張機能のドキュメントを参照してください。

基本的に全体設定は``conf.py``に記述しますが、パッケージによっては各ページのfrontmatterで個別に設定できるものもあります。

- [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [sphinx.ext.doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
- [sphinx.ext.intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
- [sphinx.ext.todo](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
- [sphinx.ext.coverage](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html)
- [sphinx.ext.mathjax](https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax)
- [sphinx.ext.ifconfig](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html)
- [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
