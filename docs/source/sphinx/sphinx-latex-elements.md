# ドキュメントクラスオプションを設定する（``latex_elements``）

ドキュメントクラス（``\documentclass``）のオプションを設定する部分です。
プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけして、中身はあとで書くことにします。

```python
latex_elements = {
    'papersize' = 'a4paper',
    'pointsize' = '12pt',
    'preamble': '',    # あとで追加するので定義だけしておく
    'figure_align': 'htbp',
#   'fontpkg': '\\usepackage{times}',
}
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}
```

## Polyglossiaパッケージを無効にしたい

LaTeXエンジンに``lualatex``を指定すると、自動で``Polyglossia``パッケージが読み込まれるようになっています。
このままビルドすると、多数の``Package polyglossia Warning: Asking to add empty feature to latin font(Script="CJK" to scripttag "")``が表示されます。
多言語対応したドキュメントであれば、無効にしてしまいましょう。

```python
latex_elements = {
    ...,
    "polyglossia": "",
    ...,
}
```
