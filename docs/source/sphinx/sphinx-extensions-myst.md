# Markdownしたい（``myst_parser``）

Sphinxの文書を``Markdown``形式で書けるようにする拡張パッケージです。
すでに``Markdown``記法に慣れている場合は、迷わずこの拡張を追加しましょう。

```{note}
2023年3月にv0.19がリリースされ、ドキュメントが大幅に書き直され、その直後にv1.0がリリースされました。
新しいドキュメントに従って使い方を書き直しています。
```

## インストールする

```bash
$ pip3 install myst-parser
```

## 設定を有効にする

```python
extensions = [...,
              "myst_parser",
              ...,
              ]
```

``conf.py``の``extentions``に``myst_parser``を追加します。

## オプションを有効にする

```python
# -- Options for MyST Parser -------------------------------------------------

myst_enable_extensions = [
    "amsmath,
    "attrs_inline",
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

``conf.py`` の適当な場所に``myst_enable_extensions = [...]``を定義して、MyST Parserのオプションを有効にします。
オプションは[Syntax Extensions](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html)を参照してください。
基本的に全部有効にして大丈夫だと思いますが、自分の用途にあったものを選択してください。

```{note}
``linkfy``は別途モジュールが必要なエラーがでたため、
とりあえずコメントアウトしました
```

## ロールを使いたい

```md
{ロール}`キーワード`
```

## ディレクティブを使いたい

````md
```{ディレクティブ}
---
オプション
---
内容
```
````

> {sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read

## メタデータを設定したい

```python
language = "ja"
myst_html_meta = {
    "description lang=ja": "サイトの説明",
    "keywords": "Sphinx, KumaROOT",
    "property=og:locale":  "ja_JP"
}
```

サイト全体のメタデータは{file}`conf.py`の``myst_html_meta``で設定できます。

```yaml
---
myst:
  html_meta:
    "description lang=ja": "記事の説明"
    "keywords": "Sphinx, 記事のキーワード"
    "property=og:locale": "ja_JP"
---
```

記事ごとのメタデータはフロントマターで設定できます。

## コメントアウトしたい

```md
% コメントの内容
```

コメントやコメントアウトしたい場合は、行頭に`%`をつけます。

## リファレンス

- [MyST Parser Document](https://myst-parser.readthedocs.io/en/latest/index.html)
