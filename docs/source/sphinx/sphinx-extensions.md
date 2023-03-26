# 拡張機能を設定したい

```python
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinxext.opengraph',
]
```

拡張機能の設定は``extensions``に記述します。
設定方法や設定オプションは、それぞれの拡張機能のドキュメントを参照してください。

- [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [sphinx.ext.doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
- [sphinx.ext.intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
- [sphinx.ext.todo](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
- [sphinx.ext.coverage](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html)
- [sphinx.ext.mathjax](https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax)
- [sphinx.ext.ifconfig](https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html)
- [sphinx.ext.viewcode](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html)
- [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html)
- [MyST Parser](https://myst-parser.readthedocs.io/en/latest/index.html)
- [sphinxext-opengraph](https://sphinxext-opengraph.readthedocs.io/en/latest/)
