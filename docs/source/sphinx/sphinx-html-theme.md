# テーマしたい（``html_theme``）

```python
html_theme = "テーマ名"
```

Sphinxを使うときに必ず設定する項目のひとつです。
[html_theme](https://www.sphinx-doc.org/ja/master/usage/configuration.html#confval-html_theme)を使ってHTML出力のテーマ（＝スタイルを集めたもの）を設定できます。


## テーマのオプションを設定したい（``html_theme_options``）

```python
html_theme = "テーマ名"
html_theme_options = {
    "設定キー": "値",
    "設定キー": "値",
    ...,
}
```

[html_theme_options](https://www.sphinx-doc.org/ja/master/usage/configuration.html#confval-html_theme_options)を使って、テーマのオプションを設定できます。
設定できる値はテーマごとに違うので、そのテーマのドキュメントを参照するのが適切です。

[組み込みテーマのオプション](https://www.sphinx-doc.org/ja/master/usage/theming.html#builtin-themes)も設定できます。
ただし、組み込みテーマ自体の見た目が全体的にぱっとしないので、あまり出番はないかもしれません。
他のテーマの中身を確認したり、自作テーマを作成したりするときの参考にはなると思います。

## 既存のテーマを使いたい

デフォルトは[alabaster](https://alabaster.readthedocs.io/en/latest/)ですが、あまり日本語向きではないと感じています。
安定したオススメは[sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)です。
最近は[sphinx_book_theme](https://sphinx-book-theme.readthedocs.io/en/stable/)が気に入っています。
[Sphinx Theme Gallery](https://sphinx-themes.readthedocs.io/en/latest/)から自分の好みのテーマを探すことができます。

```{toctree}
---
maxdepth: 1
---
sphinx-html-theme-rtd
sphinx-html-theme-pydata
sphinx-html-theme-book
```

## 自作テーマしたい（``theme.conf``）

Sphinxのテーマは自作できます。
が、いきなり自分で作るのは大変なので、既存のテーマのソースコードを読むときに、どのファイルを読めばいいのか確認しておきます。

まず設定ファイル{file}`theme.conf`を確認します。
これは``configparser``でパースできる``ini``形式のファイルです。
元となるテーマがある場合は``inherit = 元にするテーマ名``でいろいろ引き継ぐことができます。

CSSファイルは``stylesheet = CSSファイル名,CSSファイル名,...``で設定できます。
カンマで区切って複数のファイルのリストを設定できます。
このファイルはHTMLヘッダーで参照されます。
この値は{file}`conf.py`の``html_style``で上書きできます。

シンタックスハイライトは``pygments_style = スタイル名``で設定できます。
この値は{file}`conf.py`の``pygments_style``で上書きできます。

サイドバーは``sidbar = テンプレート名,...``で設定できます。
この値は{file}`conf.py`の``html_sidebars``で上書きできます。

テーマのオプションは``[options]``セクションに``変数名 = デフォルト値``の、いわゆる``key - value``形式で設定できます。
これらのオプション値は{file}`conf.py`の``html_theme_options``で上書きできます。
また、すべてのテンプレートからは``theme_<名前>``としてこの値にアクセスできます。

### theme.confを鑑賞したい

いくつかのレポジトリを確認し、``theme.conf``がどうなっているかを眺めてみます。





#### sphinx-designを鑑賞したい

さらに、ちょっと気になっている[sphinx-design](https://github.com/executablebooks/sphinx-design)を眺めてみます。
が、ここには``theme.conf``がなく、これはテーマではないようです。
ただの拡張パッケージであることが分かりました。



#### まとめ

いまのところ、``sphinx_book_theme``が気に入っているので、お手軽に作成する場合はこのテーマを``inherit``すればよさそうです。
もし、ゴリゴリ自作したい場合は、``basic``を``inherit``して作り始めればよさそうです。

## 自作テンプレートしたい

テーマの引き継ぎとオプションの設定ができたら、次はテンプレートを追加する必要があります。
Sphinxでは以下の優先度でテンプレートが適用されます。

1. ユーザーテンプレート（＝{file}`conf.py`の``templates_path``ディレクトリのテンプレート）
2. 選択したテーマのテンプレート
3. 引き継いだテーマのテンプレート

Sphinxのテンプレートエンジンは``Jinja2``であるため、読み込まれたファイルは``Jinja2``に食べられます。

### ユーザーテンプレートしたい

```html
{% extends "!layout.html" %}
<!doctype html>
<head>
<meta charset="utf-8">
<link href=".css">
</head>
    <div class="container">
    <main></main>
    <footer></footer>
    </div>
    <script></script>
</html>
```

``layout.html``というテンプレートを作成し、その中のブロック要素をカスタマイズします。

### doctypeしたい

```html
{% extends "!layout.html" %}
{% block doctype %}
<!doctype html>
{% endblock %}

{% block extrahead %}
<meta charset="utf-8">
{% endblock}

{% block footer %}
{% endblock %}
```

- [HTMLテーマ](https://www.sphinx-doc.org/ja/master/development/theming.html)
- [HTMLテンプレート](https://www.sphinx-doc.org/ja/master/development/templating.html)
- [Sphinx Extensions API](https://www.sphinx-doc.org/ja/master/extdev/index.html#dev-extensions)
