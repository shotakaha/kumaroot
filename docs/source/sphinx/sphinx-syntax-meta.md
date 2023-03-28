# メタデータをしたい（``meta``）

```python
language = "ja"
myst_html_meta = {
    "description lang=en": "metadata description"
    "description lang=ja": "メタデータの説明"
    "keywords": "Sphinx, MyST"
    "property=og:locale": "en_US"
}
```

ページ全体のメタデータは``conf.py``の``myst_html_meta = {}``に設定します。
HTMLの出力は次ようになります。

```html
<html lang="en">
  <head>
    <meta content="metadata description" lang="en" name="description" xml:lang="en" />
    <meta content="メタデータの説明" lang="ja" name="description" xml:lang="ja" />
    <meta name="keywords" content="Sphinx, MyST">
    <meta content="en_US" property="og:locale" />
    </head>
```

## ページごとにメタデータしたい（``myst.html_meta``）

````md
```yaml
---
myst:
  html_meta:
    "description lang=en": "metadata description"
    "description lang=ja": "メタデータの説明"
    "keywords": "Sphinx, MyST"
    "property=og:locale": "en_US"
---
```
````

メタデータはページごとのfrontmatterでも設定できます。
frontmatterはYAML形式で指定します。

:::{seealso}

reST形式だと次のようになります。

```rst
.. meta::
   :description lang=en: metadata description
   :description lang=ja: メタデータの説明
   :keywords: Sphinx, MyST
   :property=og:locale: en_US
```

:::

## リファレンス

- [HTML Metadata - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#html-metadata)
- [Meta information markup - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#meta-information-markup)
- [Settein HTML metadata - MyST Parser](https://myst-parser.readthedocs.io/en/latest/configuration.html#setting-html-metadata)
- [メタデータ要素 - MDN](https://developer.mozilla.org/ja/docs/Web/HTML/Element/meta)
