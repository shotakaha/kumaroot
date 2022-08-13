# ドキュメントの基本設定（``conf.py``）

Sphinxドキュメントの全体設定は ``source/conf.py`` で行います。
まずはすべての文書に共通した設定をしておきます。

Sphinxは継続的な開発が進んでいるため、ひさしぶりに使ってみると新しい機能が追加されていたり、既存の機能が設定しやすくなっていることがあります。
昔のバージョンで作り始めたドキュメントは、いちど設定を見直してみるといいかもしれません。

## プロジェクトの情報

```python
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KumaROOT'
author = 'Shota TAKAHASHI'
copyright = '2015 - 2022, Shota TAKAHASHI'
version = '0.5.0'
release = '0.5.0'
```

## 拡張パッケージ

```python
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'ja'
root_doc = "index"
```

拡張パッケージで有効にできる機能については、それぞれのドキュメントを参照して、必要な設定を追加します。

- [sphinx_rtd_themeの設定](https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html)
- [myst_parserの設定](https://myst-parser.readthedocs.io/en/latest/intro.html)

## 図表番号の表示設定

```
numfig = True

# 図表番号を表示するときのカスタム設定
# フォーマット文字列を辞書型で指定
# デフォルトの設定を書いた後、カスタム設定で上書き
numfig_format = {
    'figure' : 'Fig. %s',
    'table' : 'Table %s',
    'code-block' : 'Listing %s'
}
numfig_format['figure'] = '図 %s'
numfig_format['table'] = '表 %s'
numfig_format['code-block'] = 'コードサンプル %s'

# 図表番号のスコープ
# 0: 全てのドキュメントで通し番号
# 1: セクション毎に番号を付与（x.1, x.2, x.3, ...）
# 2: サブセクション毎に番号を付与（x.x.1, x.x.2, x.x.3, ...）
# デフォルトは 1
numfig_secnum_depth = 1
```

## 日付の表示設定

```
today_fmt = "%Y-%m-%d"
```
