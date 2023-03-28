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
    "attrs_block",
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

```{warning}
``linkfy``は別途モジュールが必要なエラーがでたため、コメントアウトしています。
```

## ロールを使いたい

```md
{ロール}`ラベル名`
```

ロール（role）は文章中で単語をマークアップするときに使います。
HTMLタグのインライン要素に近いものだと思っています。
``attrs_inline``を有効にすると、属性（``#id``や``.class``など）を追加できます。

```md
{ロール}`ラベル名`{.クラス名}
```

```html
<span class="クラス名">ラベル名</span>
```

:::{seealso}

reST形式で書くと次のようになります。

```rst
:ロール:`ラベル名`
```

:::

## ディレクティブを使いたい

````md
```{ディレクティブ} 引数
---
オプション1: 値1
オプション2: 値2
---
内容内容内容内容内容内容内容内容
内容内容内容内容内容内容内容内容
内容内容内容内容内容内容
```
````

ディレクティブ（directive）は段落をマークアップするときに使います。
ディレクティブには引数とオプションをとるものもあります。
オプションは``---``で区切った範囲にYAML形式で``キー: 値``を指定します。

HTMLタグのブロック要素に近いものだと思っています。
``attrs_block``を有効にすると、属性（``#id``や``.class``など）を追加できます。

:::{seealso}

reST形式で書くと次のようになります。

```rst
.. ディレクティブ:: 引数
   :オプション1: 値1
   :オプション2: 値2

   内容内容内容内容内容内容内容内容
   内容内容内容内容内容内容内容内容
   内容内容内容内容内容内容
```

:::

:::{hint}
Sphinxドキュメントをマークアップするときに、この``ロール``と``ディレクティブ``の役割と使い分けを理解するのはとても大切だと思います。
:::

## 置換したい（``sub-ref``）

```md
> {sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read
```

> {sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read

``sub-ref``ロールを使うと、あるキーワードを置換できます。

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



## リファレンス

- [MyST Parser Document](https://myst-parser.readthedocs.io/en/latest/index.html)
- [Roles and Directives - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
- [Directives - Sphinx Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
- [Roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)
