# CSSしたい（``html_css_files``）

```python
# config.py
html_static_path = ["_static"]
html_css_files = [
    # "ファイル名",
    "custom.css",
]
```

カスタム用のCSSファイルを``docs/_static/custom.css``に配置します。
``conf.py``の``html_static_path``には``_static``を、``html_css_files``にCSSファイル名を記述します。

:::{hint}

CSSファイルは複数指定できます。
用途別にファイルを分割してもよいと思います。

```python
html_css_files = [
    "css/heading.css", # 見出し用
    "css/font.css",    # フォント用
]
```

:::

## メディアクエリしたい

```python
html_css_files = [
    # ("ファイル名", {"media": "メディアクエリの種類"}),
    ("print.css", {"media": "print"}),
]
```

``tuple``形式で[メディアクエリー](https://developer.mozilla.org/ja/docs/Learn/CSS/CSS_layout/Media_queries)を指定できます。
メディアクエリの種類は``all``（すべて）、``print``（印刷）、``screen``（画面）、``speech``（音声合成）から選択します。

:::{seealso}

出力される[linkタグ（外部ソースへのリンク要素）](https://developer.mozilla.org/ja/docs/Web/HTML/Element/link)は次のようになります。

```html
<link href="print.css" rel="stylesheet" media="print">
```

:::
