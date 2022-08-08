# Markdown文書の設定

これまでSphinxを ``reST`` 記法で書いてきましたが、
``Markdown`` 記法で書くことができるように設定を追加します。
{command}`pip` もしくは {command}`poetry` を使って、
[MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest/intro.html)の拡張パッケージを追加します。

```bash
$ poetry add myst-parser
```

パッケージを追加したら``conf.py``の``extensions``に追加します。

```python
extensions = ['myst_parser']
```

さらに次のオプションを有効にします。
``conf.py`` の任意の場所に追記します。


```python
myst_enable_extensions = [
    "amsmath,
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
```

:::{note}
``linkfy``は別途モジュールが必要そうなエラーがでたので、とりあえずコメントアウトしました
:::




```{toctree}
sphinx-myst-syntax
```
