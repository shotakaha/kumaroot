# CSSしたい（`html_css_files`）

```python
# config.py
html_static_path = ["_static"]
html_css_files = [
    # "ファイル名",
    "custom.css",
]
```

`html_css_files`でカスタムCSSを追加できます。
ファイル名は`html_static_path`に設定したディレクトリからの相対パスにします。

```python
html_css_files = [
    "css/heading.css", # 見出し用
    "css/font.css",    # フォント用
]
```

CSSファイルは複数指定できます。
その場合、リストに記述した順番で読み込まれます。
用途別にファイルを分割してもよいと思います。

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

## レイヤーしたい

```python
# conf.py
html_css_files = [
    "custom.css",
]
```

`custom.css`とCSSのレイヤー機能（`@layer`）と組み合わせることで、スタイルを柔軟に制御できます。

```css
/* custom.css */
/* @import は custom.css からの相対パス */
@import url("reset.css") layer(reset);
@import url("base.css") layer(base);
@import url("layout.css") layer(layout);
@import url("theme.css") layer(theme);
@import url("components.css") layer(components);
@import url("overrides.css") layer(overrides);

/* レイヤーの優先度 : 低 -> 高 */
@layer reset, base, layout, theme, components, overrides
```

このサンプルでは、`custom.css`の中でCSSファイル`@import`しています。
それぞれのファイルの内容は[CSSの@layer](../html/css-layer.md)を参照してください。

```console
$ tree
docs/
  |-- conf.py
  |-- _static/
        |-- custom.css
        |-- reset.css
        |-- base.css
        |-- layout.css
        |-- theme.css
        |-- components.css
        |-- overrides.css
```

`_static`ディレクトリの中に、それぞれのCSSを配置しま
す。
CSSファイルの中身は空でも問題ありません。

:::{note}

CSSファイルの中身が空でも問題ありませんが、
ファイルがない場合はエラーになります。

:::
