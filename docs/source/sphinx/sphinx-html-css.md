# CSSしたい（``html_css_files``）

```python
# config.py
html_static_path = ["_static"]
html_css_files = [
    # "ファイル名",
    "custom.css",
]
```

カスタマイズしたCSSファイルは``conf.py``の``html_static_path``で指定したディレクトリに配置します。
そして、``conf.py``の``html_css_files``にファイル名を追記します。
ファイルは複数指定できます。

## メディアクエリしたい

```python
html_css_files = [
    "custom.css",
    # ("ファイル名", {"media": "メディアクエリの種類"}),
    ("print.css", {"media": "print"}),
]
```

``tuple``形式でメディアクエリを指定することもできます。
メディアクエリの種類は``all``（すべて）、``print``（印刷）、``screen``（画面）、``speech``（音声合成）から選択します。

:::{seealso}

出力したい``<link>``タグは次のようになります。

```html
<link href="custom.css" rel="stylesheet">
<link href="print.css" rel="stylesheet" media="print">
```

:::

## リファレンス

- [メディアクエリーの初心者向けガイド - mdn web docs](https://developer.mozilla.org/ja/docs/Learn/CSS/CSS_layout/Media_queries)
- [<link>：外部ソースへのリンク要素 - mdn web docs](https://developer.mozilla.org/ja/docs/Web/HTML/Element/link)
