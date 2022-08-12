# Markdownを使いたい

[MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest/intro.html)の拡張パッケージを追加すると、
``Markdown``記法でドキュメントを書き進めることができます。

すでに``Markdown``記法に慣れている場合は、
迷わずこの拡張を追加しておきましょう。

```bash
$ pip3 install myst-parser
```

``conf.py``の``extentions``に次のように追記します。

```python
extensions = [...,
              "myst_parser",
              ...,
              ]
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
``linkfy``は別途モジュールが必要そうなエラーがでたため、
とりあえずコメントアウトしました
:::
