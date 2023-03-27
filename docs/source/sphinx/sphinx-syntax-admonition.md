# ふきだししたい（``admonition``）

```python
myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
]
```

文章中にふきだし（コラム？）を挿入するディレクティブです。
``attention`` / ``caution`` / ``danger`` / ``error`` / ``hint`` / ``important`` / ``note`` / ``seealso`` / ``tip`` / ``warning``のキーワードがプリセットされています。
これらのキーワードは引数を取りませんが、``:class:``と``:name:``のオプションが使えます。

:::{tip}
MyST Parserを使う場合、``colon_fence``と``html_admonition``のオプションを有効にしておくとよいです。
:::

## リファレンス

- [Admonitions - MyST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/admonitions.html)
- [HTML Admonitions - MyST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/optional.html#syntax-html-admonition)
