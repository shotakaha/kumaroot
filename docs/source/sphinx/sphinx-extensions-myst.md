# Markdownしたい（``myst_parser``）

[MyST Parser](https://myst-parser.readthedocs.io/en/latest/)は、Sphinx文書を``Markdown``形式で書けるようにする拡張パッケージです。
すでに``Markdown``記法に慣れている場合は、迷わずこの拡張を追加しましょう。

```{note}
このドキュメントのサンプルは``MyST``記法をメインに使用しています。
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
コピペしてすべて有効にして使えばOKだと思いますが、自分の必要にあったオプションを選択してください。

:::{warning}
``linkfy``は別のパッケージが必要なため、コメントアウトしています。
:::

## ディレクティブしたい

````md
```{ディレクティブ名} 引数
---
オプション1: 値1
オプション2: 値2
---
内容内容内容内容内容内容内容内容
内容内容内容内容内容内容内容内容
内容内容内容内容内容内容
```
````

[ディレクティブ（directives）](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#directives-a-block-level-extension-point)は段落などのブロック要素をマークアップするときに使います。

MyST記法の場合、コードブロック記法のように書きます。
また、ディレクティブには引数とオプションをとるものもあります。
オプションは``---``で区切った範囲にYAML形式で``キー: 値``を指定します。

[colon_fence](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#code-fences-using-colons)を有効にすると`` ```{ディレクティブ名} ``の代わりに``:::{ディレクティブ名}``で書けるようになります。

また、[attrs_block](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#block-attributes)を有効にすると、ブロック要素に対して属性（``#id``や``.class``など）を追加できます。
Markdown記法はシンプルでよいのですが、SSG（＝静的サイトジェネレーター）するときはちょっと不便に感じていました。
これは、それを解決するための拡張です。

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

## ロールを使いたい

```md
{ロール}`ラベル名`
```

[ロール（roles）](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#roles-an-in-line-extension-point)は文章中の単語などのインライン要素をマークアップするときに使います。

[attrs_inline](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#inline-attributes)を有効にすると、インライン要素に対して属性（``#id``や``.class``など）を追加できます。

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

## 置換したい（``sub-ref``）

```md
{sub-ref}`today`
{sub-ref}`wordcount-words`
{sub-ref}`wordcount-minutes`
```

:::{seealso}

- 更新日: {sub-ref}`today`
- このページの単語数: {sub-ref}`wordcount-words` 単語
- 読む時間の目安: {sub-ref}`wordcount-minutes` 分

:::

[sub-ref](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#insert-the-date-and-reading-time)ロールを使うと、キーワードを置換できます。

## メタデータしたい

```python
language = "ja"
myst_html_meta = {
    "description lang=ja": "サイトの説明",
    "keywords": "Sphinx, KumaROOT",
    "property=og:locale":  "ja_JP"
}
```

メタデータは、サイト全体と記事ごとのそれぞれに設定できます。
サイト全体のメタデータは{file}`conf.py`の``myst_html_meta``で設定します。

```yaml
---
myst:
  html_meta:
    "description lang=ja": "記事の説明"
    "keywords": "Sphinx, 記事のキーワード"
    "property=og:locale": "ja_JP"
---
```

記事ごとのメタデータはフロントマターで設定します。

## リファレンス

- [MyST Parser Document](https://myst-parser.readthedocs.io/en/latest/index.html)
- [Roles and Directives - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
