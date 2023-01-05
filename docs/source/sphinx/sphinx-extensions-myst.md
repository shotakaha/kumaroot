# Markdownを使いたい（``myst_parser``）

[MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest/intro.html)の拡張パッケージを追加すると、
``Markdown``記法でドキュメントを記述できます。

すでに``Markdown``記法に慣れている場合は、迷わずこの拡張を追加しましょう。

## インストール

```bash
$ pip3 install myst-parser
```

## 設定

``conf.py``の``extentions``に次のように追記します。

```python
extensions = [...,
              "myst_parser",
              ...,
              ]
```

## オプションを有効にする

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
